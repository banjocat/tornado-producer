import tornado.ioloop
import tornado.web

import server_kafka
import server_couchdb
import server_rabbitmq
import server_postgres
import server_cassandra
from server_mongo import MongoHandler
from server_elastic import ElasticHandler


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, walter')


if __name__ == '__main__':
    routes = [
            (r"/kafka/sync",
                server_kafka.KafkaSyncHandler),
            (r"/kafka/async",
                server_kafka.KafkaAsyncHandler),
            (r"/mongo",
                MongoHandler),
            (r"/elastic",
                ElasticHandler),
            ("/cassandra/async",
                server_cassandra.CassandraSyncHandler),
            ("/cassandra/sync",
                server_cassandra.CassandraSyncHandler),
            ("/couch/sync",
                server_couchdb.CouchSyncHandler),
            ("/couch/async",
                server_couchdb.CouchAsyncHandler),
            ("/rabbitmq/sync",
                server_rabbitmq.RabbitSyncHandler),
            ("/rabbitmq/async",
                server_rabbitmq.RabbitAsyncHandler),
            ("/postgres/json/sync", server_postgres.PostgresJsonSyncHandler),
            ("/postgres/json/async",
                server_postgres.PostgresJsonAsyncHandler),
            ("/postgres/jsonb/sync",
                server_postgres.PostgresJsonbSyncHandler),
            ("/postgres/jsonb/async",
                server_postgres.PostgresJsonbAsyncHandler),
            (r"/", IndexHandler)
            ]
    app = tornado.web.Application(routes)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
