import json
import concurrent

import tornado
import couchdb
from tornado import gen
from tornado.concurrent import run_on_executor


class BaseHandler(tornado.web.RequestHandler):
    couch = couchdb.Server('http://couchdb:5984')
    if 'test' not in couch:
        couch.create('test')

    def write_couch(self):
        msg = self.request.body.decode('utf-8')
        data = json.loads(msg)
        db = self.couch['test']
        db.save(data)


class CouchSyncHandler(BaseHandler):

    def post(self):
        self.write_couch()
        self.write('{"result": "success"}')


class CouchAsyncHandler(BaseHandler):
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)

    @run_on_executor
    def async_write_couch(self):
        self.write_couch()

    @gen.coroutine
    def post(self):
        yield self.async_write_couch()
        self.write('{"result": "success"}')
