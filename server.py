import tornado.ioloop
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, walter')


if __name__ == '__main__':
    routes = [
            (r"/", IndexHandler)
            ]
    app = tornado.web.Application(routes)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
