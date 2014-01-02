'''
command_line.py
    Utility functions for reading command line arguments.

Author:
    Martin Norbury

Novemeber 2013
'''
import inspect
import argparse

def command_line(fn):
    '''
    A decorator for functions intented to be run from the command line.

    This decorator introspects the method signature of the wrapped function
    to configures and parses command line arguments. Positional arguments
    translate to required command line arguments. Arguments with defaults
    supplied are assumed to be optional e.g.

    def myfunction(a,b=1):
        ...

    Can be called from the command line as:-

    > myfunction <a> [--b=value]

    All arguments are assumed to be strings at this point.
    '''
    def wrapper_fn(*args, **kwargs):

        # Get the original function's method signature
        arguments, varargs, kwargs, defaults = inspect.getargspec(fn)

        # Get required and optional arguments
        required_length    = -len(defaults) if defaults else len(arguments)
        required_arguments = arguments[:required_length]
        optional_arguments = arguments[required_length:]

        # Create a list of optional arguments of the form (name, value)
        optional_arguments_with_defaults = []
        if optional_arguments:
            optional_arguments_with_defaults = zip(optional_arguments, defaults)

        # Create a command line parser
        parser = argparse.ArgumentParser()

        # Configure required arguments
        for argument in required_arguments:
            parser.add_argument('{0}'.format(argument))

        # Configure optional arguments, setting defaults appropriately.
        for argument, default in optional_arguments_with_defaults:
            parser.add_argument('--{0}'.format(argument), type=type(default), default=default)

        # Parse the command line arguments
        args = parser.parse_args()

        # Call the original function with command line supplied arguments
        result = fn(**dict(args._get_kwargs()))

        return result
    return wrapper_fn

