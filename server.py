import tornado.ioloop
import tornado.web

from server_kafka import KafkaHandler
from server_mongo import MongoHandler
from server_elastic import ElasticHandler
from server_couchdb import CouchHandler


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, walter')


if __name__ == '__main__':
    routes = [
            (r"/kafka", KafkaHandler),
            (r"/mongo", MongoHandler),
            (r"/elastic", ElasticHandler),
            ("/couch", CouchHandler),
            (r"/", IndexHandler)
            ]
    app = tornado.web.Application(routes)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
