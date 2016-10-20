import concurrent

import tornado
from tornado import gen
from tornado.concurrent import run_on_executor
import pika


class BaseHandler(tornado.web.RequestHandler):
    params = pika.ConnectionParameters('rabbitmq')
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='json')

    def rabbit_write(self):
        msg = self.request.body
        self.channel.basic_publish(exchange='', routing_key='json', body=msg)


class RabbitSyncHandler(BaseHandler):

    def post(self):
        self.rabbit_write()
        self.write('{"result": "success"}')


class RabbitAsyncHandler(BaseHandler):
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)

    @run_on_executor
    def async_rabbit_write(self):
        self.rabbit_write()

    @gen.coroutine
    def post(self):
        yield self.async_rabbit_write()
        self.write('{"result": "success"}')
