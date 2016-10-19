import os
import concurrent

import tornado.ioloop
import tornado.web
from tornado import gen
from tornado.concurrent import run_on_executor
from kafka import KafkaProducer


KAFKA = os.getenv('kafka', 'kafka:9092')


class KafkaHandler(tornado.web.RequestHandler):
    producer = KafkaProducer(bootstrap_servers=KAFKA)

    def post(self):
        self.producer.send('json', self.request.body)
        self.write('{"result": "success"}')


class KafkaAsyncHandler(tornado.web.RequestHandler):
    producer = KafkaProducer(bootstrap_servers=KAFKA)
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)

    @run_on_executor
    def kafka_write(self, msg):
        self.producer.send('json_async', msg)

    @gen.coroutine
    def post(self):
        yield self.kafka_write(self.request.body)
        self.write('{"result": "success"}')
