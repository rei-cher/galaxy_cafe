"""
Decorators modulo

Defines decoration
"""
import os
import sys

def path_exists(func):
    """
    Decorator that checks if the provided path exists in the system
    """
    def wrapper(*args, **kwargs):
        if os.path.exists(args[0]):
            return func(*args, **kwargs)
        else:
            print(f"Path {args[0]} does not exist")
            sys.exit(1)
            return
            
    return wrapper
