import os

import tornado.ioloop
import tornado.web
from kafka import KafkaProducer


KAFKA = os.getenv('kafka', 'kafka:9092')


class KafkaHandler(tornado.web.RequestHandler):
    producer = KafkaProducer(bootstrap_servers=KAFKA)

    def post(self):
        self.producer.send('json', self.request.body)
        self.write('{"result": "success"}')
