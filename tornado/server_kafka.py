import concurrent

import tornado
from tornado import gen
from tornado.concurrent import run_on_executor
from kafka import KafkaProducer


class BaseHandler(tornado.web.RequestHandler):
    producer = KafkaProducer(bootstrap_servers='kafka:9092')

    def kafka_write(self, msg):
        self.producer.send('json', msg)


class KafkaSyncHandler(BaseHandler):

    def post(self):
        self.kafka_write(self.request.body)
        self.write('{"result": "success"}')


class KafkaAsyncHandler(BaseHandler):
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)

    @run_on_executor
    def async_kafka_write(self, msg):
        self.kafka_write(msg)

    @gen.coroutine
    def post(self):
        yield self.async_kafka_write(self.request.body)
        self.write('{"result": "success"}')
