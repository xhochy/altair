# -*- coding: utf-8 -*-
# Auto-generated file: do not modify directly
# - altair version info: v1.2.1-28-g231518a
# - date: 2018-01-25 00:15:27

import traitlets as T
from . import jstraitlets as jst
from . import schema


def _localname(name):
    return '.'.join(__name__.split('.')[:-1] + ['named_channels', name])


class Encoding(schema.Encoding):
    """Object for storing channel encodings

    Attributes
    ----------
    color: AnyOf([Color, MarkPropValueDefWithCondition])
        Color of the marks – either fill or stroke color based on mark
        type.
        By default, `color` represents fill color for `"area"`,
        `"bar"`, `"tick"`,
        `"text"`, `"circle"`, and `"square"` / stroke color for
        `"line"` and `"point"`.
        __Default value:__ If undefined, the default color depends on
        [mark config](config.html#mark)'s `color` property.
        _Note:_ See the scale documentation for more information about
        customizing [color scheme](scale.html#scheme).
    detail: AnyOf([Detail, Array(Detail)])
        Additional levels of detail for grouping data in aggregate
        views and
        in line and area marks without mapping data to a specific
        visual channel.
    opacity: AnyOf([Opacity, MarkPropValueDefWithCondition])
        Opacity of the marks – either can be a value or a range.
        __Default value:__ If undefined, the default opacity depends
        on [mark config](config.html#mark)'s `opacity` property.
    order: AnyOf([Order, Array(Order)])
        Stack order for stacked marks or order of data points in line
        marks for connected scatter plots.
        __Note__: In aggregate plots, `order` field should be
        `aggregate`d to avoid creating additional aggregation
        grouping.
    shape: AnyOf([Shape, MarkPropValueDefWithCondition])
        The symbol's shape (only for `point` marks). The supported
        values are
        `"circle"` (default), `"square"`, `"cross"`, `"diamond"`,
        `"triangle-up"`,
        or `"triangle-down"`, or else a custom SVG path string.
        __Default value:__ If undefined, the default shape depends on
        [mark config](config.html#point-config)'s `shape` property.
    size: AnyOf([Size, MarkPropValueDefWithCondition])
        Size of the mark.
        - For `"point"`, `"square"` and `"circle"`, – the symbol
          size, or pixel area of the mark.
        - For `"bar"` and `"tick"` – the bar and tick's size.
        - For `"text"` – the text's font size.
        - Size is currently unsupported for `"line"`, `"area"`, and
          `"rect"`.
    text: AnyOf([Text, TextValueDefWithCondition])
        Text of the `text` mark.
    tooltip: AnyOf([Tooltip, TextValueDefWithCondition])
        The tooltip text to show upon mouse hover.
    x: AnyOf([X, ValueDef])
        X coordinates of the marks, or width of horizontal `"bar"` and
        `"area"`.
    x2: AnyOf([X2, ValueDef])
        X2 coordinates for ranged  `"area"`, `"bar"`, `"rect"`, and
        `"rule"`.
    y: AnyOf([Y, ValueDef])
        Y coordinates of the marks, or height of vertical `"bar"` and
        `"area"`.
    y2: AnyOf([Y2, ValueDef])
        Y2 coordinates for ranged  `"area"`, `"bar"`, `"rect"`, and
        `"rule"`.
    """
    _skip_on_export = ['channel_names']
    channel_names = ['color', 'detail', 'opacity', 'order', 'shape', 'size', 'text', 'tooltip', 'x', 'x2', 'y', 'y2']
    
    color = jst.JSONAnyOf([jst.JSONInstance(_localname('Color')), jst.JSONInstance(_localname('MarkPropValueDefWithCondition'))], help='Color of the marks – either fill or stroke color based on mark [...]')
    detail = jst.JSONAnyOf([jst.JSONInstance(_localname('Detail')), jst.JSONArray(jst.JSONInstance(_localname('Detail')))], help='Additional levels of detail for grouping data in aggregate views [...]')
    opacity = jst.JSONAnyOf([jst.JSONInstance(_localname('Opacity')), jst.JSONInstance(_localname('MarkPropValueDefWithCondition'))], help='Opacity of the marks – either can be a value or a range. [...]')
    order = jst.JSONAnyOf([jst.JSONInstance(_localname('Order')), jst.JSONArray(jst.JSONInstance(_localname('Order')))], help='Stack order for stacked marks or order of data points in line [...]')
    shape = jst.JSONAnyOf([jst.JSONInstance(_localname('Shape')), jst.JSONInstance(_localname('MarkPropValueDefWithCondition'))], help="The symbol's shape (only for `point` marks). The supported [...]")
    size = jst.JSONAnyOf([jst.JSONInstance(_localname('Size')), jst.JSONInstance(_localname('MarkPropValueDefWithCondition'))], help='Size of the mark. - For `"point"`, `"square"` and `"circle"`, – [...]')
    text = jst.JSONAnyOf([jst.JSONInstance(_localname('Text')), jst.JSONInstance(_localname('TextValueDefWithCondition'))], help='Text of the `text` mark.')
    tooltip = jst.JSONAnyOf([jst.JSONInstance(_localname('Tooltip')), jst.JSONInstance(_localname('TextValueDefWithCondition'))], help='The tooltip text to show upon mouse hover.')
    x = jst.JSONAnyOf([jst.JSONInstance(_localname('X')), jst.JSONInstance(_localname('ValueDef'))], help='X coordinates of the marks, or width of horizontal `"bar"` and [...]')
    x2 = jst.JSONAnyOf([jst.JSONInstance(_localname('X2')), jst.JSONInstance(_localname('ValueDef'))], help='X2 coordinates for ranged `"area"`, `"bar"`, `"rect"`, and `"rule"`.')
    y = jst.JSONAnyOf([jst.JSONInstance(_localname('Y')), jst.JSONInstance(_localname('ValueDef'))], help='Y coordinates of the marks, or height of vertical `"bar"` and [...]')
    y2 = jst.JSONAnyOf([jst.JSONInstance(_localname('Y2')), jst.JSONInstance(_localname('ValueDef'))], help='Y2 coordinates for ranged `"area"`, `"bar"`, `"rect"`, and `"rule"`.')


class EncodingWithFacet(schema.EncodingWithFacet):
    """Object for storing channel encodings

    Attributes
    ----------
    color: AnyOf([Color, MarkPropValueDefWithCondition])
        Color of the marks – either fill or stroke color based on mark
        type.
        By default, `color` represents fill color for `"area"`,
        `"bar"`, `"tick"`,
        `"text"`, `"circle"`, and `"square"` / stroke color for
        `"line"` and `"point"`.
        __Default value:__ If undefined, the default color depends on
        [mark config](config.html#mark)'s `color` property.
        _Note:_ See the scale documentation for more information about
        customizing [color scheme](scale.html#scheme).
    column: Column
        Horizontal facets for trellis plots.
    detail: AnyOf([Detail, Array(Detail)])
        Additional levels of detail for grouping data in aggregate
        views and
        in line and area marks without mapping data to a specific
        visual channel.
    opacity: AnyOf([Opacity, MarkPropValueDefWithCondition])
        Opacity of the marks – either can be a value or a range.
        __Default value:__ If undefined, the default opacity depends
        on [mark config](config.html#mark)'s `opacity` property.
    order: AnyOf([Order, Array(Order)])
        Stack order for stacked marks or order of data points in line
        marks for connected scatter plots.
        __Note__: In aggregate plots, `order` field should be
        `aggregate`d to avoid creating additional aggregation
        grouping.
    row: Row
        Vertical facets for trellis plots.
    shape: AnyOf([Shape, MarkPropValueDefWithCondition])
        The symbol's shape (only for `point` marks). The supported
        values are
        `"circle"` (default), `"square"`, `"cross"`, `"diamond"`,
        `"triangle-up"`,
        or `"triangle-down"`, or else a custom SVG path string.
        __Default value:__ If undefined, the default shape depends on
        [mark config](config.html#point-config)'s `shape` property.
    size: AnyOf([Size, MarkPropValueDefWithCondition])
        Size of the mark.
        - For `"point"`, `"square"` and `"circle"`, – the symbol
          size, or pixel area of the mark.
        - For `"bar"` and `"tick"` – the bar and tick's size.
        - For `"text"` – the text's font size.
        - Size is currently unsupported for `"line"`, `"area"`, and
          `"rect"`.
    text: AnyOf([Text, TextValueDefWithCondition])
        Text of the `text` mark.
    tooltip: AnyOf([Tooltip, TextValueDefWithCondition])
        The tooltip text to show upon mouse hover.
    x: AnyOf([X, ValueDef])
        X coordinates of the marks, or width of horizontal `"bar"` and
        `"area"`.
    x2: AnyOf([X2, ValueDef])
        X2 coordinates for ranged  `"area"`, `"bar"`, `"rect"`, and
        `"rule"`.
    y: AnyOf([Y, ValueDef])
        Y coordinates of the marks, or height of vertical `"bar"` and
        `"area"`.
    y2: AnyOf([Y2, ValueDef])
        Y2 coordinates for ranged  `"area"`, `"bar"`, `"rect"`, and
        `"rule"`.
    """
    _skip_on_export = ['channel_names']
    channel_names = ['color', 'column', 'detail', 'opacity', 'order', 'row', 'shape', 'size', 'text', 'tooltip', 'x', 'x2', 'y', 'y2']
    
    color = jst.JSONAnyOf([jst.JSONInstance(_localname('Color')), jst.JSONInstance(_localname('MarkPropValueDefWithCondition'))], help='Color of the marks – either fill or stroke color based on mark [...]')
    column = jst.JSONInstance(_localname('Column'), help='Horizontal facets for trellis plots.')
    detail = jst.JSONAnyOf([jst.JSONInstance(_localname('Detail')), jst.JSONArray(jst.JSONInstance(_localname('Detail')))], help='Additional levels of detail for grouping data in aggregate views [...]')
    opacity = jst.JSONAnyOf([jst.JSONInstance(_localname('Opacity')), jst.JSONInstance(_localname('MarkPropValueDefWithCondition'))], help='Opacity of the marks – either can be a value or a range. [...]')
    order = jst.JSONAnyOf([jst.JSONInstance(_localname('Order')), jst.JSONArray(jst.JSONInstance(_localname('Order')))], help='Stack order for stacked marks or order of data points in line [...]')
    row = jst.JSONInstance(_localname('Row'), help='Vertical facets for trellis plots.')
    shape = jst.JSONAnyOf([jst.JSONInstance(_localname('Shape')), jst.JSONInstance(_localname('MarkPropValueDefWithCondition'))], help="The symbol's shape (only for `point` marks). The supported [...]")
    size = jst.JSONAnyOf([jst.JSONInstance(_localname('Size')), jst.JSONInstance(_localname('MarkPropValueDefWithCondition'))], help='Size of the mark. - For `"point"`, `"square"` and `"circle"`, – [...]')
    text = jst.JSONAnyOf([jst.JSONInstance(_localname('Text')), jst.JSONInstance(_localname('TextValueDefWithCondition'))], help='Text of the `text` mark.')
    tooltip = jst.JSONAnyOf([jst.JSONInstance(_localname('Tooltip')), jst.JSONInstance(_localname('TextValueDefWithCondition'))], help='The tooltip text to show upon mouse hover.')
    x = jst.JSONAnyOf([jst.JSONInstance(_localname('X')), jst.JSONInstance(_localname('ValueDef'))], help='X coordinates of the marks, or width of horizontal `"bar"` and [...]')
    x2 = jst.JSONAnyOf([jst.JSONInstance(_localname('X2')), jst.JSONInstance(_localname('ValueDef'))], help='X2 coordinates for ranged `"area"`, `"bar"`, `"rect"`, and `"rule"`.')
    y = jst.JSONAnyOf([jst.JSONInstance(_localname('Y')), jst.JSONInstance(_localname('ValueDef'))], help='Y coordinates of the marks, or height of vertical `"bar"` and [...]')
    y2 = jst.JSONAnyOf([jst.JSONInstance(_localname('Y2')), jst.JSONInstance(_localname('ValueDef'))], help='Y2 coordinates for ranged `"area"`, `"bar"`, `"rect"`, and `"rule"`.')


