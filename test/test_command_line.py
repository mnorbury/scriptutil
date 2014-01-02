'''
test_command_line.py
    Test cases for the command_line module.

Author:
    Martin Norbury

Novemeber 2013
'''
import sys

from nose.tools import eq_

from scriptutil.command_line import command_line

def _positional_arg_function(a, b):
    return locals()

def _optional_arg_function(a='11',b='12'):
    return locals()

def _optional_arg_function_as_int(a=11):
    return locals()

def test_reading_positional_arguments():
    wrapped_function = command_line(_positional_arg_function)

    sys.argv = ['','1','2']

    result = wrapped_function()

    eq_(result, dict(a='1',b='2'))

def test_optional_arguments_assume_defaults():
    wrapped_function = command_line(_optional_arg_function)

    sys.argv = ['']

    result = wrapped_function()

    eq_(result, dict(a='11',b='12'))

def test_optional_arguments_can_be_supplied():
    wrapped_function = command_line(_optional_arg_function)

    sys.argv = ['','--a=21','--b=22']

    result = wrapped_function()

    eq_(result, dict(a='21',b='22'))

def test_optional_arguments_preserve_type():
    wrapped_function = command_line(_optional_arg_function_as_int)

    sys.argv = ['','--a=21']

    result = wrapped_function()

    eq_(result, dict(a=21))
