#!/usr/bin/env python
'''
example.py - A short example of using the command line wrapper.

Author:
    Martin Norbury (martin.norbury@gmail.com)

January 2014
'''
from scriptutil.command_line import command_line

def myexample(name, repeat=1):
    ''' A simple example function.

        This doesn't do much except print a message.
    '''
    print 'Hello %s' % (name*repeat)


if __name__ == '__main__':
    wrapped = command_line(myexample)
    wrapped()
