import concurrent
import uuid

import tornado
from tornado import gen
from tornado.concurrent import run_on_executor
from cassandra.cqlengine import columns, connection
from cassandra.cqlengine.management import sync_table, create_keyspace_simple
from cassandra.cqlengine.models import Model


class JsonModel(Model):
    example_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    data = columns.Text()

connection.setup(['cassandra'], 'json')
create_keyspace_simple('json', replication_factor=1)
sync_table(JsonModel)


class BaseHandler(tornado.web.RequestHandler):

    def write_cassandra(self):
        msg = tornado.escape.native_str(self.request.body)
        JsonModel.create(data=msg)


class CassandraSyncHandler(BaseHandler):

    def post(self):
        self.write_cassandra()
        self.write('{"result": "success"}')


class CassandraAsyncHandler(BaseHandler):
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)

    @run_on_executor
    def async_write_cassandra(self):
        self.write_cassandra()

    @gen.coroutine
    def post(self):
        yield self.async_write_cassandra()
        self.write('{"result": "success"}')
