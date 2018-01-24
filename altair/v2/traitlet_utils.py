"""
Helpers for working with traitlet-based classes.

In particular, these helpers help with instantiation of HasTraits object
hierarchies from dictionaries and lists of trait names.
"""
import re
import warnings
import six

import pandas as pd
import numpy as np

try:
    from pandas.api.types import infer_dtype
except ImportError: # Pandas before 0.20.0
    from pandas.lib import infer_dtype

import traitlets as T

from ..utils import infer_vegalite_type

TYPECODE_MAP = {'ordinal': 'O',
                'nominal': 'N',
                'quantitative': 'Q',
                'temporal': 'T'}

INV_TYPECODE_MAP = {v: k for k, v in TYPECODE_MAP.items()}


def channel_type_dict(cls):
    """Create a dict of trait names to channel type"""

    traits = cls.class_traits()

    def is_union_of_trait_and_list(trait):
        return (isinstance(trait, T.Union) and
                len(trait.trait_types) == 2 and
                isinstance(trait.trait_types[0], T.Instance) and
                isinstance(trait.trait_types[1], T.List) and
                trait.trait_types[0].klass == trait.trait_types[1]._trait.klass)

    def get_class(trait):
        if isinstance(trait, T.Instance):
            return trait.klass
        elif is_union_of_trait_and_list(trait):
            return trait.trait_types[0].klass
        else:
            return None

    classes = {n: get_class(t) for n, t in traits.items()}
    return {n:t for n, t in classes.items() if t is not None}


def infer_keywords(cls, *args, **kwargs):
    """Utility to initialize a HasTraits object from args and kwargs

    Arguments are converted to keyword arguments by inferring the keyword
    from their type.
    Keyword arguments are converted to the correct Instance class
    if required.
    """
    # Import here to avoid circular imports
    from .schema import jstraitlets as jst

    # For all traits, extract the channel type.
    traits = cls.class_traits()
    trait_classes = channel_type_dict(cls)

    # Turn all keyword arguments to the appropriate class
    for name, arg in kwargs.items():
        Trait = trait_classes.get(name, None)
        if Trait is not None and not isinstance(arg, Trait):
            try:
                kwargs[name] = Trait(arg)
            except (TypeError, T.TraitError):
                pass  # errors will handled by traitlets below

    # find forward/backward mapping among unique classes
    name_to_trait = {}
    while trait_classes:
        name, trait = trait_classes.popitem()
        if trait is jst.undefined:
            continue
        if trait not in set.union(set(trait_classes.values()),
                                  set(name_to_trait.values())):
            name_to_trait[name] = trait
    trait_to_name = {t: n for n, t in name_to_trait.items()}

    # Update all arguments
    for arg in args:
        # find highest-level class in the method resolution order that appears
        # in the dict:
        names = (trait_to_name.get(cls, None) for cls in arg.__class__.__mro__)
        name = next((n for n in names if n), None)
        if name is None:
            raise ValueError("{0}: Unable to infer argument name for {1}"
                             "".format(cls, arg))
        elif name in kwargs:
            raise ValueError("{0}: {1} specified both by arg and kwarg"
                             "".format(cls, name))

        else:
            kwargs[name] = arg
    return kwargs


def update_traits(obj, **kwargs):
    """Convenience routine to call set_trait() with a dictionary of values"""
    for key, val in kwargs.items():
        obj.set_trait(key, val)
    return obj


def update_inferred_traits(obj, *args, **kwargs):
    """Infer types from positional arguments and update traits of obj"""
    kwargs = infer_keywords(obj, *args, **kwargs)
    return update_traits(obj, **kwargs)


def update_subtraits(obj, attrs, *args, **kwargs):
    """Recursively update sub-traits without overwriting other traits"""
    # Import here to avoid circular imports
    from .schema import jstraitlets as jst

    if not (args or kwargs):
        return obj
    if isinstance(attrs, six.string_types):
        attrs = (attrs,)
    if len(attrs) == 0:
        update_inferred_traits(obj, *args, **kwargs)
    else:
        attr = attrs[0]
        trait = getattr(obj, attr)  # error here if attr is not present
        if trait is jst.undefined:
            trait = obj.traits()[attr].klass()
        setattr(obj, attr, update_subtraits(trait, attrs[1:], *args, **kwargs))
    return obj


def construct_shorthand(field=None, aggregate=None, type=None):
    """Construct a shorthand representation.

    See also: parse_shorthand"""
    # Import here to avoid circular imports
    from .schema import jstraitlets as jst

    if field is jst.undefined or field is None:
        return ''

    sh = field

    if aggregate is not jst.undefined and aggregate is not None:
        sh = '{0}({1})'.format(aggregate, sh)

    if type is not jst.undefined and type is not None:
        type = TYPECODE_MAP.get(type, type)
        if type not in INV_TYPECODE_MAP:
            raise ValueError('Unrecognized Type: {0}'.format(type))
        sh = '{0}:{1}'.format(sh, type)

    return sh


def parse_shorthand(shorthand):
    """
    Parse the shorthand expression for aggregation, field, and type.

    These are of the form:

    - "col_name"
    - "col_name:O"
    - "average(col_name)"
    - "average(col_name):O"

    Parameters
    ----------
    shorthand: str
        Shorthand string

    Returns
    -------
    D : dict
        Dictionary containing the field, aggregate, and typecode
    """
    if not shorthand:
        return {}

    # Must import this here to avoid circular imports
    from .schema import AggregateOp
    valid_aggregates = AggregateOp().values
    valid_typecodes = list(TYPECODE_MAP) + list(INV_TYPECODE_MAP)

    # build regular expressions
    units = dict(field='(?P<field>.*)',
                 type='(?P<type>{0})'.format('|'.join(valid_typecodes)),
                 aggregate='(?P<aggregate>{0})'.format('|'.join(valid_aggregates)))
    patterns = [r'{field}',
                r'{field}:{type}',
                r'{aggregate}\({field}\)',
                r'{aggregate}\({field}\):{type}']
    regexps = (re.compile('\A' + p.format(**units) + '\Z', re.DOTALL)
               for p in patterns[::-1])

    # find matches depending on valid fields passed
    match = next(exp.match(shorthand).groupdict() for exp in regexps
                 if exp.match(shorthand))

    # Use short form of the type expression
    typ = match.get('type', None)
    if typ:
        match['type'] = INV_TYPECODE_MAP.get(typ, typ)
    return match
