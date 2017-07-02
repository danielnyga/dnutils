#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

import colored
import sys
from pymongo import MongoClient

import dnlog
from dnlog import getlogger
from dnutils import out, stop, trace
from dnutils.console import bf, ProgressBar, StatusMsg, barstr

db = MongoClient()

dnlog.setup({
    'default': dnlog.newlogger(dnlog.console),
    'results': dnlog.newlogger(dnlog.console, dnlog.FileHandler('dnutils-test.log'))
})


def wait():
    time.sleep(1)


if __name__ == '__main__':
    logger = getlogger('results', dnlog.DEBUG)
    logger.info('Initialized. Running all tests...')
    wait()
    logger.info('Testing log levels...')
    logger.debug('this is the debug level')
    logger.info('this is the info level')
    logger.warning('this is the warning level')
    logger.error('this is the error level')
    logger.critical('this is the critical level')

    logger.critical('wait a second...')
    wait()
    logger.debug('This debug message spreads over\nmultiple lines and should be\naligned with appropriate indentation.')
    wait()

    logger.level = dnlog.ERROR
    logger.info('If you see this message, something went wrong with the log levels.')
    logger.level = dnlog.DEBUG

    logger.info('Testing the debug functions.')
    wait()
    out('the', bf('out()'), 'function always prints the code location where it is called so it can be found again later swiftly.')
    wait()
    out('it', 'also', 'accepts', 'multiple', 'arguments', 'which', 'are', 'being', 'concatenated')
    stop('the', bf('stop()'), 'function is equivalent to', bf('out()'), 'except for it stops until you hit return:')

    trace('the', bf('trace()'), 'function gives you a stack trace of the current position')

    logger.info('testing the', bf('ProgressBar'), '...')
    bar = ProgressBar(steps=10, color='deep_sky_blue_4c')
    for i in range(11):
        bar.update(value=i/10., label='step %d' % (i+1))
        time.sleep(.5)
    bar.finish()

    logger.info('testing the', bf(StatusMsg), '(you should see 5 "OK" and 5 "ERROR" messages)')
    wait()
    for i in range(10):
        bar = StatusMsg('this is a Linux-style status bar (%.2d)...' % (i+1))
        bar.status = StatusMsg.OK if i <= 4 else StatusMsg.ERROR
        wait()
        bar.finish()


