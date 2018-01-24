# -*- coding: utf-8 -*-
# Auto-generated file: do not modify directly
# - altair version info: v1.2.1-28-g231518a
# - date: 2018-01-25 00:15:27

import pandas as pd

from . import jstraitlets as jst
from . import schema
from ...traitlet_utils import parse_shorthand, infer_vegalite_type


class FacetField(schema.FacetFieldDef):
    """Wrapper for Vega-Lite FacetFieldDef definition.
    
    Attributes
    ----------
    shorthand: Unicode
        A shorthand description of the channel
    aggregate : string
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
        __Default value:__ `undefined` (None)
    bin : AnyOf([boolean, BinParams])
        A flag for binning a `quantitative` field, or [an object
        defining binning parameters](bin.html#params).
        If `true`, default [binning parameters](bin.html) will be
        applied.
        __Default value:__ `false`
    field : AnyOf([string, RepeatRef])
        __Required.__ A string defining the name of the field from
        which to pull a data value
        or an object defining iterated values from the
        [`repeat`](repeat.html) operator.
        __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to
        access nested objects (e.g., `"field": "foo.bar"` and
        `"field": "foo['bar']"`).
        If field names contain dots or brackets but are not nested,
        you can use `\\` to escape dots and brackets (e.g., `"a\\.b"`
        and `"a\\[0\\]"`).
        See more details about escaping in the [field
        documentation](field.html).
        __Note:__ `field` is not required if `aggregate` is `count`.
    header : Header
        An object defining properties of a facet's header.
    sort : ['string', 'null']
        Sort order for a facet field.
        This can be `"ascending"`, `"descending"`.
    timeUnit : AnyOf([AnyOf([string, string]), AnyOf([string, string])])
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a
        temporal field.
        or [a temporal field that gets casted as
        ordinal](type.html#cast).
        __Default value:__ `undefined` (None)
    type : string
        The encoded field's type of measurement (`"quantitative"`,
        `"temporal"`, `"ordinal"`, or `"nominal"`).
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    _skip_on_export = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', aggregate=jst.undefined, bin=jst.undefined, field=jst.undefined, header=jst.undefined, sort=jst.undefined, timeUnit=jst.undefined, type=jst.undefined, **kwargs):
        self.shorthand = shorthand
        kwds = dict(aggregate=aggregate, bin=bin, field=field, header=header, sort=sort, timeUnit=timeUnit, type=type)
        kwargs.update({k:v for k, v in kwds.items() if v is not jst.undefined})
        super(FacetField, self).__init__(**kwargs)

    def _finalize(self, **kwargs):
        """Finalize object: this involves inferring types if necessary"""
        # parse the shorthand to extract the field, type, and aggregate
        for key, val in parse_shorthand(self.shorthand).items():
            setattr(self, key, val)

        # infer the type if not already specified
        if self.type is jst.undefined:
            data = kwargs.get('data', jst.undefined)
            if isinstance(data, pd.DataFrame) and self.field in data:
                self.type = infer_vegalite_type(data[self.field])

        super(FacetField, self)._finalize(**kwargs)


class Field(schema.FieldDef):
    """Wrapper for Vega-Lite FieldDef definition.
    Definition object for a data field, its type and transformation of
    an encoding channel.
    Attributes
    ----------
    shorthand: Unicode
        A shorthand description of the channel
    aggregate : string
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
        __Default value:__ `undefined` (None)
    bin : AnyOf([boolean, BinParams])
        A flag for binning a `quantitative` field, or [an object
        defining binning parameters](bin.html#params).
        If `true`, default [binning parameters](bin.html) will be
        applied.
        __Default value:__ `false`
    field : AnyOf([string, RepeatRef])
        __Required.__ A string defining the name of the field from
        which to pull a data value
        or an object defining iterated values from the
        [`repeat`](repeat.html) operator.
        __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to
        access nested objects (e.g., `"field": "foo.bar"` and
        `"field": "foo['bar']"`).
        If field names contain dots or brackets but are not nested,
        you can use `\\` to escape dots and brackets (e.g., `"a\\.b"`
        and `"a\\[0\\]"`).
        See more details about escaping in the [field
        documentation](field.html).
        __Note:__ `field` is not required if `aggregate` is `count`.
    timeUnit : AnyOf([AnyOf([string, string]), AnyOf([string, string])])
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a
        temporal field.
        or [a temporal field that gets casted as
        ordinal](type.html#cast).
        __Default value:__ `undefined` (None)
    type : string
        The encoded field's type of measurement (`"quantitative"`,
        `"temporal"`, `"ordinal"`, or `"nominal"`).
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    _skip_on_export = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', aggregate=jst.undefined, bin=jst.undefined, field=jst.undefined, timeUnit=jst.undefined, type=jst.undefined, **kwargs):
        self.shorthand = shorthand
        kwds = dict(aggregate=aggregate, bin=bin, field=field, timeUnit=timeUnit, type=type)
        kwargs.update({k:v for k, v in kwds.items() if v is not jst.undefined})
        super(Field, self).__init__(**kwargs)

    def _finalize(self, **kwargs):
        """Finalize object: this involves inferring types if necessary"""
        # parse the shorthand to extract the field, type, and aggregate
        for key, val in parse_shorthand(self.shorthand).items():
            setattr(self, key, val)

        # infer the type if not already specified
        if self.type is jst.undefined:
            data = kwargs.get('data', jst.undefined)
            if isinstance(data, pd.DataFrame) and self.field in data:
                self.type = infer_vegalite_type(data[self.field])

        super(Field, self)._finalize(**kwargs)


class MarkPropFieldWithCondition(schema.MarkPropFieldDefWithCondition):
    """Wrapper for Vega-Lite MarkPropFieldDefWithCondition definition.
    A FieldDef with Condition<ValueDef>
    {
       condition: {value: ...},
       field: ...,
       ...
    }
    Attributes
    ----------
    shorthand: Unicode
        A shorthand description of the channel
    aggregate : string
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
        __Default value:__ `undefined` (None)
    bin : AnyOf([boolean, BinParams])
        A flag for binning a `quantitative` field, or [an object
        defining binning parameters](bin.html#params).
        If `true`, default [binning parameters](bin.html) will be
        applied.
        __Default value:__ `false`
    condition : AnyOf([Conditional_ValueDef, Array(Conditional_ValueDef)])
        One or more value definition(s) with a selection predicate.
        __Note:__ A field definition's `condition` property can only
        contain [value definitions](encoding.html#value-def)
        since Vega-Lite only allows at mosty  one encoded field per
        encoding channel.
    field : AnyOf([string, RepeatRef])
        __Required.__ A string defining the name of the field from
        which to pull a data value
        or an object defining iterated values from the
        [`repeat`](repeat.html) operator.
        __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to
        access nested objects (e.g., `"field": "foo.bar"` and
        `"field": "foo['bar']"`).
        If field names contain dots or brackets but are not nested,
        you can use `\\` to escape dots and brackets (e.g., `"a\\.b"`
        and `"a\\[0\\]"`).
        See more details about escaping in the [field
        documentation](field.html).
        __Note:__ `field` is not required if `aggregate` is `count`.
    legend : AnyOf([Legend, null])
        An object defining properties of the legend.
        If `null`, the legend for the encoding channel will be
        removed.
        __Default value:__ If undefined, default [legend
        properties](legend.html) are applied.
    scale : Scale
        An object defining properties of the channel's scale, which is
        the function that transforms values in the data domain
        (numbers, dates, strings, etc) to visual values (pixels,
        colors, sizes) of the encoding channels.
        __Default value:__ If undefined, default [scale
        properties](scale.html) are applied.
    sort : AnyOf([['string', 'null'], SortField, null])
        Sort order for the encoded field.
        Supported `sort` values include `"ascending"`, `"descending"`
        and `null` (no sorting).
        For fields with discrete domains, `sort` can also be a [sort
        field definition object](sort.html#sort-field).
        __Default value:__ `"ascending"`
    timeUnit : AnyOf([AnyOf([string, string]), AnyOf([string, string])])
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a
        temporal field.
        or [a temporal field that gets casted as
        ordinal](type.html#cast).
        __Default value:__ `undefined` (None)
    type : string
        The encoded field's type of measurement (`"quantitative"`,
        `"temporal"`, `"ordinal"`, or `"nominal"`).
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    _skip_on_export = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', aggregate=jst.undefined, bin=jst.undefined, condition=jst.undefined, field=jst.undefined, legend=jst.undefined, scale=jst.undefined, sort=jst.undefined, timeUnit=jst.undefined, type=jst.undefined, **kwargs):
        self.shorthand = shorthand
        kwds = dict(aggregate=aggregate, bin=bin, condition=condition, field=field, legend=legend, scale=scale, sort=sort, timeUnit=timeUnit, type=type)
        kwargs.update({k:v for k, v in kwds.items() if v is not jst.undefined})
        super(MarkPropFieldWithCondition, self).__init__(**kwargs)

    def _finalize(self, **kwargs):
        """Finalize object: this involves inferring types if necessary"""
        # parse the shorthand to extract the field, type, and aggregate
        for key, val in parse_shorthand(self.shorthand).items():
            setattr(self, key, val)

        # infer the type if not already specified
        if self.type is jst.undefined:
            data = kwargs.get('data', jst.undefined)
            if isinstance(data, pd.DataFrame) and self.field in data:
                self.type = infer_vegalite_type(data[self.field])

        super(MarkPropFieldWithCondition, self)._finalize(**kwargs)


class OrderField(schema.OrderFieldDef):
    """Wrapper for Vega-Lite OrderFieldDef definition.
    
    Attributes
    ----------
    shorthand: Unicode
        A shorthand description of the channel
    aggregate : string
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
        __Default value:__ `undefined` (None)
    bin : AnyOf([boolean, BinParams])
        A flag for binning a `quantitative` field, or [an object
        defining binning parameters](bin.html#params).
        If `true`, default [binning parameters](bin.html) will be
        applied.
        __Default value:__ `false`
    field : AnyOf([string, RepeatRef])
        __Required.__ A string defining the name of the field from
        which to pull a data value
        or an object defining iterated values from the
        [`repeat`](repeat.html) operator.
        __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to
        access nested objects (e.g., `"field": "foo.bar"` and
        `"field": "foo['bar']"`).
        If field names contain dots or brackets but are not nested,
        you can use `\\` to escape dots and brackets (e.g., `"a\\.b"`
        and `"a\\[0\\]"`).
        See more details about escaping in the [field
        documentation](field.html).
        __Note:__ `field` is not required if `aggregate` is `count`.
    sort : ['string', 'null']
        The sort order. One of `"ascending"` (default) or
        `"descending"`.
    timeUnit : AnyOf([AnyOf([string, string]), AnyOf([string, string])])
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a
        temporal field.
        or [a temporal field that gets casted as
        ordinal](type.html#cast).
        __Default value:__ `undefined` (None)
    type : string
        The encoded field's type of measurement (`"quantitative"`,
        `"temporal"`, `"ordinal"`, or `"nominal"`).
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    _skip_on_export = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', aggregate=jst.undefined, bin=jst.undefined, field=jst.undefined, sort=jst.undefined, timeUnit=jst.undefined, type=jst.undefined, **kwargs):
        self.shorthand = shorthand
        kwds = dict(aggregate=aggregate, bin=bin, field=field, sort=sort, timeUnit=timeUnit, type=type)
        kwargs.update({k:v for k, v in kwds.items() if v is not jst.undefined})
        super(OrderField, self).__init__(**kwargs)

    def _finalize(self, **kwargs):
        """Finalize object: this involves inferring types if necessary"""
        # parse the shorthand to extract the field, type, and aggregate
        for key, val in parse_shorthand(self.shorthand).items():
            setattr(self, key, val)

        # infer the type if not already specified
        if self.type is jst.undefined:
            data = kwargs.get('data', jst.undefined)
            if isinstance(data, pd.DataFrame) and self.field in data:
                self.type = infer_vegalite_type(data[self.field])

        super(OrderField, self)._finalize(**kwargs)


class PositionField(schema.PositionFieldDef):
    """Wrapper for Vega-Lite PositionFieldDef definition.
    
    Attributes
    ----------
    shorthand: Unicode
        A shorthand description of the channel
    aggregate : string
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
        __Default value:__ `undefined` (None)
    axis : AnyOf([Axis, null])
        An object defining properties of axis's gridlines, ticks and
        labels.
        If `null`, the axis for the encoding channel will be removed.
        __Default value:__ If undefined, default [axis
        properties](axis.html) are applied.
    bin : AnyOf([boolean, BinParams])
        A flag for binning a `quantitative` field, or [an object
        defining binning parameters](bin.html#params).
        If `true`, default [binning parameters](bin.html) will be
        applied.
        __Default value:__ `false`
    field : AnyOf([string, RepeatRef])
        __Required.__ A string defining the name of the field from
        which to pull a data value
        or an object defining iterated values from the
        [`repeat`](repeat.html) operator.
        __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to
        access nested objects (e.g., `"field": "foo.bar"` and
        `"field": "foo['bar']"`).
        If field names contain dots or brackets but are not nested,
        you can use `\\` to escape dots and brackets (e.g., `"a\\.b"`
        and `"a\\[0\\]"`).
        See more details about escaping in the [field
        documentation](field.html).
        __Note:__ `field` is not required if `aggregate` is `count`.
    scale : Scale
        An object defining properties of the channel's scale, which is
        the function that transforms values in the data domain
        (numbers, dates, strings, etc) to visual values (pixels,
        colors, sizes) of the encoding channels.
        __Default value:__ If undefined, default [scale
        properties](scale.html) are applied.
    sort : AnyOf([['string', 'null'], SortField, null])
        Sort order for the encoded field.
        Supported `sort` values include `"ascending"`, `"descending"`
        and `null` (no sorting).
        For fields with discrete domains, `sort` can also be a [sort
        field definition object](sort.html#sort-field).
        __Default value:__ `"ascending"`
    stack : AnyOf([string, null])
        Type of stacking offset if the field should be stacked.
        `stack` is only applicable for `x` and `y` channels with
        continuous domains.
        For example, `stack` of `y` can be used to customize stacking
        for a vertical bar chart.
        `stack` can be one of the following values:
        - `"zero"`: stacking with baseline offset at zero value of
          the scale (for creating typical stacked
          [bar](stack.html#bar) and [area](stack.html#area) chart).
        - `"normalize"` - stacking with normalized domain (for
          creating [normalized stacked bar and area
          charts](stack.html#normalized). <br/>
        -`"center"` - stacking with center baseline (for
          [streamgraph](stack.html#streamgraph)).
        - `null` - No-stacking. This will produce layered
          [bar](stack.html#layered-bar-chart) and area chart.
        __Default value:__ `zero` for plots with all of the following
        conditions are true:
        (1) the mark is `bar` or `area`;
        (2) the stacked measure channel (x or y) has a linear scale;
        (3) At least one of non-position channels mapped to an
        unaggregated field that is different from x and y.  Otherwise,
        `null` by default.
    timeUnit : AnyOf([AnyOf([string, string]), AnyOf([string, string])])
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a
        temporal field.
        or [a temporal field that gets casted as
        ordinal](type.html#cast).
        __Default value:__ `undefined` (None)
    type : string
        The encoded field's type of measurement (`"quantitative"`,
        `"temporal"`, `"ordinal"`, or `"nominal"`).
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    _skip_on_export = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', aggregate=jst.undefined, axis=jst.undefined, bin=jst.undefined, field=jst.undefined, scale=jst.undefined, sort=jst.undefined, stack=jst.undefined, timeUnit=jst.undefined, type=jst.undefined, **kwargs):
        self.shorthand = shorthand
        kwds = dict(aggregate=aggregate, axis=axis, bin=bin, field=field, scale=scale, sort=sort, stack=stack, timeUnit=timeUnit, type=type)
        kwargs.update({k:v for k, v in kwds.items() if v is not jst.undefined})
        super(PositionField, self).__init__(**kwargs)

    def _finalize(self, **kwargs):
        """Finalize object: this involves inferring types if necessary"""
        # parse the shorthand to extract the field, type, and aggregate
        for key, val in parse_shorthand(self.shorthand).items():
            setattr(self, key, val)

        # infer the type if not already specified
        if self.type is jst.undefined:
            data = kwargs.get('data', jst.undefined)
            if isinstance(data, pd.DataFrame) and self.field in data:
                self.type = infer_vegalite_type(data[self.field])

        super(PositionField, self)._finalize(**kwargs)


class TextFieldWithCondition(schema.TextFieldDefWithCondition):
    """Wrapper for Vega-Lite TextFieldDefWithCondition definition.
    A FieldDef with Condition<ValueDef>
    {
       condition: {value: ...},
       field: ...,
       ...
    }
    Attributes
    ----------
    shorthand: Unicode
        A shorthand description of the channel
    aggregate : string
        Aggregation function for the field
        (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).
        __Default value:__ `undefined` (None)
    bin : AnyOf([boolean, BinParams])
        A flag for binning a `quantitative` field, or [an object
        defining binning parameters](bin.html#params).
        If `true`, default [binning parameters](bin.html) will be
        applied.
        __Default value:__ `false`
    condition : AnyOf([Conditional_ValueDef, Array(Conditional_ValueDef)])
        One or more value definition(s) with a selection predicate.
        __Note:__ A field definition's `condition` property can only
        contain [value definitions](encoding.html#value-def)
        since Vega-Lite only allows at mosty  one encoded field per
        encoding channel.
    field : AnyOf([string, RepeatRef])
        __Required.__ A string defining the name of the field from
        which to pull a data value
        or an object defining iterated values from the
        [`repeat`](repeat.html) operator.
        __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to
        access nested objects (e.g., `"field": "foo.bar"` and
        `"field": "foo['bar']"`).
        If field names contain dots or brackets but are not nested,
        you can use `\\` to escape dots and brackets (e.g., `"a\\.b"`
        and `"a\\[0\\]"`).
        See more details about escaping in the [field
        documentation](field.html).
        __Note:__ `field` is not required if `aggregate` is `count`.
    format : string
        The [formatting pattern](format.html) for a text field. If not
        defined, this will be determined automatically.
    timeUnit : AnyOf([AnyOf([string, string]), AnyOf([string, string])])
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a
        temporal field.
        or [a temporal field that gets casted as
        ordinal](type.html#cast).
        __Default value:__ `undefined` (None)
    type : string
        The encoded field's type of measurement (`"quantitative"`,
        `"temporal"`, `"ordinal"`, or `"nominal"`).
    """
    # Traitlets
    shorthand = jst.JSONString(default_value='', help="Shorthand specification of field, optionally including the aggregate and type (see :ref:`shorthand-description`)")
    _skip_on_export = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', aggregate=jst.undefined, bin=jst.undefined, condition=jst.undefined, field=jst.undefined, format=jst.undefined, timeUnit=jst.undefined, type=jst.undefined, **kwargs):
        self.shorthand = shorthand
        kwds = dict(aggregate=aggregate, bin=bin, condition=condition, field=field, format=format, timeUnit=timeUnit, type=type)
        kwargs.update({k:v for k, v in kwds.items() if v is not jst.undefined})
        super(TextFieldWithCondition, self).__init__(**kwargs)

    def _finalize(self, **kwargs):
        """Finalize object: this involves inferring types if necessary"""
        # parse the shorthand to extract the field, type, and aggregate
        for key, val in parse_shorthand(self.shorthand).items():
            setattr(self, key, val)

        # infer the type if not already specified
        if self.type is jst.undefined:
            data = kwargs.get('data', jst.undefined)
            if isinstance(data, pd.DataFrame) and self.field in data:
                self.type = infer_vegalite_type(data[self.field])

        super(TextFieldWithCondition, self)._finalize(**kwargs)


