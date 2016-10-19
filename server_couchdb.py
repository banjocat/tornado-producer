import json
import concurrent

import tornado.ioloop
import tornado.web
import couchdb
from tornado import gen
from tornado.concurrent import run_on_executor


class CouchHandler(tornado.web.RequestHandler):
    couch = couchdb.Server('http://couchdb:5984')

    def post(self):
        msg = self.request.body.decode('utf-8')
        data = json.loads(msg)
        if 'test' not in self.couch:
            self.couch.create('test')
        db = self.couch['test']
        db.save(data)
        self.write('{"result": "success"}')


class CouchAsyncHandler(tornado.web.RequestHandler):
    couch = couchdb.Server('http://couchdb:5984')
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)

    @run_on_executor
    def write_couch(self):
        msg = self.request.body.decode('utf-8')
        data = json.loads(msg)
        if 'test' not in self.couch:
            self.couch.create('test')
        db = self.couch['test']
        db.save(data)

    @gen.coroutine
    def post(self):
        yield self.write_couch()
        self.write('{"result": "success"}')
