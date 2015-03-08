#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .data_structures import Lookup, Structure, CaseInsensitiveMapping
from .common import (
    handle_numpy_errors,
    ignore_numpy_errors,
    raise_numpy_errors,
    print_numpy_errors,
    warn_numpy_errors,
    batch,
    is_scipy_installed,
    is_iterable,
    is_string,
    is_numeric,
    is_integer)
from .array import (
    as_numeric,
    closest,
    normalise,
    steps,
    is_uniform,
    row_as_diagonal)
from .verbose import message_box, warning

__all__ = ['handle_numpy_errors',
           'ignore_numpy_errors',
           'raise_numpy_errors',
           'print_numpy_errors',
           'warn_numpy_errors',
           'batch',
           'is_scipy_installed',
           'is_iterable',
           'is_string',
           'is_numeric',
           'is_integer']
__all__ += ['as_numeric',
            'closest',
            'normalise',
            'steps',
            'is_uniform',
            'row_as_diagonal']
__all__ += ['Lookup', 'Structure', 'CaseInsensitiveMapping']
__all__ += ['message_box', 'warning']

