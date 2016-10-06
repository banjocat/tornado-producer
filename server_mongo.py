import os
import json

import tornado.ioloop
import tornado.web
from tornado import gen
import motor


MONGO = os.getenv('mongo', 'mongo')
PORT = os.getenv('port', 27017)


class MongoHandler(tornado.web.RequestHandler):
    client = motor.motor_tornado.MotorClient(MONGO, PORT)

    @gen.coroutine
    def post(self):
        msg = self.request.body.decode('utf-8')
        data = json.loads(msg)
        db = self.client['test']
        collection = db['test']
        yield collection.insert(data)
        self.write('{"result": "success"}')
