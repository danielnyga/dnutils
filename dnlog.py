import logging
import re
import traceback

import sys

import colored

import datetime

from dnutils.debug import _caller

DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL

FileHandler = logging.FileHandler
StreamHandler = logging.StreamHandler


class _LoggerAdapter(object):
    def __init__(self, logger):
        self._logger = logger
        self._logger.findCaller = self._caller

    def _caller(self, *_):
        return _caller(4)

    def critical(self, *args, **kwargs):
        self._logger.critical(' '.join(map(str, args)), extra=kwargs)

    def exception(self, *args, **kwargs):
        self._logger.exception(' '.join(map(str, args)), extra=kwargs)

    def error(self, *args, **kwargs):
        self._logger.error(' '.join(map(str, args)), extra=kwargs)

    def warning(self, *args, **kwargs):
        self._logger.warning(' '.join(map(str, args)), extra=kwargs)

    def info(self, *args, **kwargs):
        self._logger.info(' '.join(map(str, args)), extra=kwargs)

    def debug(self, *args, **kwargs):
        self._logger.debug(' '.join(map(str, args)), extra=kwargs)

    def __getattr__(self, attr):
        return getattr(self._logger, attr)

    @property
    def level(self):
        return self._logger.level

    @level.setter
    def level(self, l):
        self._logger.setLevel(l)

    def add_handler(self, h):
        self._logger.addHandler(h)

    def rm_handler(self, h):
        self._logger.removeHandler(h)

    @property
    def handlers(self):
        return self._logger.handlers

    def new(self, name, level=None):
        '''
        Spawn a new logger with the given name and return it.

        The new logger will be a child logger of this logger, i.e. it will inherit all of its handlers and,
        if not specified by the level parameter, also the log level.

        :param name:
        :param level:
        :return:
        '''
        if level is None:
            level = self.level
        logger = logging.getLogger(name)
        logger.parent = self._logger
        logger._initialized = True
        logger.setLevel(level)
        return _LoggerAdapter(logger)


def loglevel(level, name=None):
    if name is None:
        name = ''
    getlogger(name).level = level


ansi_escape = re.compile(r'\x1b[^m]*m')


def cleanstr(s):
    return ansi_escape.sub('', s)


class ColoredStreamHandler(logging.StreamHandler):
    def emit(self, record):
        self.stream.write(self.format(record))


colored_console = ColoredStreamHandler()


class ColoredFormatter(logging.Formatter):
    fmap = {
        logging.DEBUG: colored.fg('cyan') + colored.attr('bold'),
        logging.INFO: colored.fg('white') + colored.attr('bold'),
        logging.WARNING: colored.fg('yellow') + colored.attr('bold'),
        logging.ERROR: colored.fg('red') + colored.attr('bold'),
        logging.CRITICAL: colored.bg('dark_red_2') + colored.fg('white') + colored.attr('underlined') + colored.attr(
            'bold')
    }
    msgmap = {
        logging.DEBUG: colored.fg('cyan'),
        logging.INFO: colored.fg('white'),
        logging.WARNING: colored.fg('yellow'),
        logging.ERROR: colored.fg('red'),
        logging.CRITICAL: colored.fg('dark_red_2')
    }

    def __init__(self, formatstr=None):
        self.formatstr = formatstr

    def format(self, record):
        levelstr = colored.attr('reset')
        levelstr += ColoredFormatter.fmap[record.levelno]
        maxlen = max(map(len, [n for n in logging._levelNames if type(n) == str]))
        header = '%s - %s - ' % (datetime.datetime.fromtimestamp(record.created).strftime('%Y-%m-%d %H:%M:%S'),
                                 colored.stylize(record.levelname.center(maxlen, ' '), levelstr))
        return header + colored.stylize(('\n' + ' ' * len(cleanstr(header))).join(record.msg.split('\n')) + '\n',
                                        ColoredFormatter.msgmap[record.levelno])


colored_console.setFormatter(ColoredFormatter())

try:
    import pymongo
except ImportError:
    pass
else:
    class MongoHandler(logging.Handler):
        '''
        Log handler for logging into a MongoDB database.
        '''
        def __init__(self, collection):
            '''
            Create the handler.

            :param collection:  An accessible collection in a pymongo database.
            '''
            logging.Handler.__init__(self)
            self.coll = collection
            self.setFormatter(MongoFormatter())

        def emit(self, record):
            self.coll.insert(self.format(record))


    class MongoFormatter(logging.Formatter):

        def format(self, record):
            return {'message': record.msg , 'timestamp': datetime.datetime.utcfromtimestamp(record.created),
                    'module': record.module, 'lineno': record.lineno, 'name': record.name, 'level': record.levelname}


class LoggerConfig(object):
    '''
    Data structure for storing a configuration of a particular
    logger, such as its name and the handlers to be used.
    '''
    def __init__(self, level, *handlers):
        self.handlers = handlers
        self.level = level


def newlogger(*handlers, **kwargs):
    '''
    Create a new logger configuration.

    Takes a list of handlers and optionally a level specification.

    Example:
    >>> dnlog.newlogger(logging.StreamHandler(), level=logging.ERROR)

    :param handlers:
    :param kwargs:
    :return:
    '''
    return LoggerConfig(kwargs.get('level', logging.INFO), *handlers)


def setup(loggers=None):
    '''
    Initial setup for the logging of the current process.

    The root logger is identified equivalently by None or 'default'. If no specification for the root logger
    is provided, a standard console handler will be automatically appended.

    :param loggers: a dictionary mapping the names of loggers to :class:`dnlog.LoggerConfig` instances.
    :return:
    '''
    if loggers is None:
        loggers = {}
    if not {None, 'default'} & set(loggers.keys()):
        loggers['default'] = newlogger(console)
    for name, config in loggers.items():
        logger = getlogger(name)
        for h in logger.handlers:
            logger.removeHandler(h)
        logger.level = config.level
        for handler in config.handlers:
            logger.add_handler(handler)
            logger._logger._initialized = True


def getlogger(name=None, level=None):
    '''
    Get the logger with the associated name.

    If name is None, the root logger is returned. Optionally, a level can be specified that the logger is autmatically
    set to.

    :param name:    the name of the desired logger
    :param level:   the log level
    :return:
    '''
    if name == 'default':
        name = None
    logger = logging.getLogger(name)
    adapter = _LoggerAdapter(logger)
    if not hasattr(logger, '_initialized') or not logger._initialized:
        logger.parent = None
        roothandlers = list(logging.getLogger().handlers)
        # clear all loggers first
        for h in logger.handlers:
            logger.removeHandler(h)
        # take default handlers from the root logger
        for h in roothandlers:
            adapter.add_handler(h)
        logger._initialized = True
    if level is not None:
        adapter.level = level
    return adapter


console = colored_console
setup()