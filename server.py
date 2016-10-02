import os
import tornado.ioloop
import tornado.web
from kafka import KafkaProducer

KAFKA = os.getenv('kafka', 'kafka:9092')


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, walter')


class KafkaHandler(tornado.web.RequestHandler):
    producer = KafkaProducer(bootstrap_servers=KAFKA)

    def post(self):
        self.producer.send('json', self.request.body)
        self.write('{"result": "success"}')

if __name__ == '__main__':
    routes = [
            (r"/kafka", KafkaHandler),
            (r"/", IndexHandler)
            ]
    app = tornado.web.Application(routes)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
