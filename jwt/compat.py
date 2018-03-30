# -*- coding: utf-8 -*-
"""
The `compat` module provides support for backwards compatibility with older
versions of python, and compatibility wrappers around optional packages.
"""
import sys


PY3 = sys.version_info[0] == 3


if PY3:
    text_type = str
    binary_type = bytes
else:
    text_type = unicode
    binary_type = str

string_types = (text_type, binary_type)
