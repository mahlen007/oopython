#!/usr/bin/env python3
"""
Class for Errors
"""
class Error(Exception):
    """User defined class for custom exceptions"""

class SearchMiss(Error):
    """Raised when word is missing. """
