import tornado.web
import tornado.ioloop
import asyncio


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("this is from backend dude")


class movieHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class numberHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if (num.isdigit()):
            r = "odd" if int(num) % 2 else "even"
            self.write(num + "is" + r)
        else:
            self.write(num + "is not a digit bae")


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/movielist", movieHandler),
        (r"/numbercheck", numberHandler)
    ])

    app.listen(2345)
    print("application is running siva! go ahead")
    tornado.ioloop.IOLoop.current().start()
