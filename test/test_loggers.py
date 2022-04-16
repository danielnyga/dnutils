from unittest import TestCase

from dnutils import getlogger, logs, err

try:
    import pymongo
    import mongomock
except ModuleNotFoundError:
    err('You must have "pymongo" and "mongomock" installed to run the tests.')
    raise


from dnutils.logs import MongoHandler


class MongoHandlerTest(TestCase):

    def test_mongo_handler_insert(self):
        handler = MongoHandler(mongomock.MongoClient(), 'db', 'log')
        coll = handler.coll
        logger = getlogger('/dnutils/test', level=logs.DEBUG)
        logger.add_handler(handler)
        logger.info('Test1')
        logger.debug('Test2')
        self.assertEqual(2, coll.count_documents({}))
        messages = {tuple(doc['message']) for doc in coll.find({})}
        self.assertSetEqual(messages, {('Test1',), ('Test2',)})


class LoggerTest(TestCase):

    def test_logger(self):
        logger = getlogger('test', level=logs.DEBUG)
        logger.debug('This is the DEBUG message.')
        logger.info('This is the INFO message.')
        logger.warning('This is the WARNING message.')
        logger.error('This is the ERROR message.')
        logger.exception('This is the EXCEPTION message.')
        self.assertTrue(True)