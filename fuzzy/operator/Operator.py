"""
    Calculate value for fuzzy rule.
    
    Used to build fuzzy rules.
""" 
import fuzzy.Exception

class Operator:
    """Abstract base class for any kind of operator."""
    
    def __init__(self):
        """Dummy initialization, so it is safe to call it
	   from any sub class."""  
        pass
 
    def __call__(self):
	"""Return current value."""
        raise fuzzy.Exception.Exception("abtract class %s can't be called" % self.__class__.__name__)