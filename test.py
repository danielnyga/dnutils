#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

import colored
from pymongo import MongoClient

from dnutils import out, stop, trace, logs
from dnutils.console import bf, ProgressBar, StatusMsg
from dnutils.logs import getlogger

db = MongoClient()

logs.setup({
    'default': logs.newlogger(logs.console),
    'results': logs.newlogger(logs.console, logs.FileHandler('dnutils-test.log'))
})


def wait():
    time.sleep(1)

bfctnames = {
    'out': colored.stylize('out()', colored.attr('bold')),
    'stop': colored.stylize('stop()', colored.attr('bold')),
    'trace': colored.stylize('trace()', colored.attr('bold'))
}

if __name__ == '__main__':
    logger = getlogger('results', logs.DEBUG)
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

    logger.level = logs.ERROR
    logger.info('If you see this message, something went wrong with the log levels.')
    logger.level = logs.DEBUG

    logger.info('Testing the debug functions.')
    wait()
    out('the %s function always prints the code location where it is called so it can be found again later swiftly.' %
        bfctnames['out'])
    wait()
    out('it', 'also', 'accepts', 'multiple', 'arguments', 'which', 'are', 'being', 'concatenated')
    stop('the %s function is equivalent to %s except for it stops until you hit return:' % (bfctnames['stop'],
                                                                                            bfctnames['out']))

    trace('the %s function gives you a stack trace of the current position' % bfctnames['trace'])

    logger.info('testing the', bf('ProgressBar'), 'and', bf('StatusMsg'), '...')
    bar = ProgressBar(steps=10, color='deep_sky_blue_4c')
    for i in range(11):
        bar.update(value=i/10., label='step %d' % (i+1))
        time.sleep(.5)
    bar.finish()

    for i in range(20):
        bar = StatusMsg('this is a Linux-style status bar (%.2d)...' % (i+1))
        bar.status = StatusMsg.OK
        wait()
        bar.finish()


