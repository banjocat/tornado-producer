import concurrent

import tornado
from tornado import gen
from tornado.concurrent import run_on_executor
import psycopg2cffi


class BaseHandler(tornado.web.RequestHandler):
    psql = psycopg2cffi.connect(
            database='test', user='test', password='test', host='postgres')

    def json_write(self, msg):
        sql = "INSERT INTO json (data) VALUES (%s)"
        with self.psql:
            with self.psql.cursor() as cursor:
                cursor.execute(sql, (msg,))

    def jsonb_write(self, msg):
        sql = "INSERT INTO jsonb (data) VALUES (%s)"
        with self.psql:
            with self.psql.cursor() as cursor:
                cursor.execute(sql, (msg,))

    def text_write(self, msg):
        sql = "INSERT INTO string (data) VALUES (%s)"
        with self.psql:
            with self.psql.cursor() as cursor:
                cursor.execute(sql, (msg,))


class PostgresJsonSyncHandler(BaseHandler):

    def post(self):
        msg = self.request.body.decode('utf-8')
        self.json_write(msg)


class PostgresJsonAsyncHandler(BaseHandler):
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)

    @run_on_executor
    def async_json_write(self):
        msg = self.request.body.decode('utf-8')
        self.json_write(msg)

    @gen.coroutine
    def post(self):
        yield self.async_json_write()
        self.write('{"result": "success"}')


class PostgresJsonbSyncHandler(BaseHandler):

    def post(self):
        msg = self.request.body.decode('utf-8')
        self.jsonb_write(msg)


class PostgresJsonbAsyncHandler(BaseHandler):
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)

    @run_on_executor
    def async_jsonb_write(self):
        msg = self.request.body.decode('utf-8')
        self.jsonb_write(msg)

    @gen.coroutine
    def post(self):
        yield self.async_jsonb_write()
        self.write('{"result": "success"}')


class PostgresStringSyncHandler(BaseHandler):

    def post(self):
        msg = self.request.body.decode('utf-8')
        self.text_write(msg)


class PostgresStringAsyncHandler(BaseHandler):
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)

    @run_on_executor
    def async_string_write(self):
        msg = self.request.body.decode('utf-8')
        self.text_write(msg)

    @gen.coroutine
    def post(self):
        yield self.async_string_write()
