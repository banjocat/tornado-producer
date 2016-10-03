import tornado.ioloop
import tornado.web

from server_kafka import KafkaHandler


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, walter')


if __name__ == '__main__':
    routes = [
            (r"/kafka", KafkaHandler),
            (r"/", IndexHandler)
            ]
    app = tornado.web.Application(routes)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
