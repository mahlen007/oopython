class Error(Exception):
   """User defined class for custom exceptions"""
   pass

class MissingIndex(Error):
   """Raised when the index is missing. """
   pass

class MissingValue(Error):
   """Raised when the value is missing. """
   pass