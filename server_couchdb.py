import json

import tornado.ioloop
import tornado.web
import couchdb


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
