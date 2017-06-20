'''
Created on May 22, 2017

@author: nyga
'''

from dnutils import out, stop, trace
from dnutils.console import get_terminal_size, ProgressBar, StatusMsg
from dnutils.tools import allnone, allnot
from colored import stylize
import colored
import time
import random


def print_globals():
    out('here come the locals:', tb=2)
    for var, val in globals().items():
        print(var, val, sep='=')
    trace('give me a stack trace!')


if __name__ == '__main__':

    for i in range(100):
        status = StatusMsg(message='  * Operation #%d:' % (i + 1))
        time.sleep(.2)
        status.status = StatusMsg.OK if random.random() > .3 else StatusMsg.ERROR
        status.finish()
