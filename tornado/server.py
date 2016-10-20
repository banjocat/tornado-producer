import tornado.ioloop
import tornado.web

import server_kafka
import server_couchdb
import server_rabbitmq
import server_postgres
from server_mongo import MongoHandler
from server_elastic import ElasticHandler


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, walter')


if __name__ == '__main__':
    routes = [
            (r"/kafka/sync", server_kafka.KafkaSyncHandler),
            (r"/kafka/async", server_kafka.KafkaAsyncHandler),
            (r"/mongo", MongoHandler),
            (r"/elastic", ElasticHandler),
            ("/couch/sync", server_couchdb.CouchSyncHandler),
            ("/couch/async", server_couchdb.CouchAsyncHandler),
            ("/rabbitmq/sync", server_rabbitmq.RabbitSyncHandler),
            ("/rabbitmq/async", server_rabbitmq.RabbitAsyncHandler),
            ("/postgjson/sync", server_postgres.PostgresJsonSyncHandler),
            ("/postgjson/async", server_postgres.PostgresJsonAsyncHandler),
            ("/postgjsonb/sync", server_postgres.PostgresJsonbSyncHandler),
            ("/postgjsonb/async", server_postgres.PostgresJsonbAsyncHandler),
            (r"/", IndexHandler)
            ]
    app = tornado.web.Application(routes)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
