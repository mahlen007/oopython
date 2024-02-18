#!/usr/bin/env python3
"""
Class for Errors
"""
class Error(Exception):
    """User defined class for custom exceptions"""

class MissingIndex(Error):
    """Raised when the index is missing. """

class MissingValue(Error):
    """Raised when the value is missing. """
