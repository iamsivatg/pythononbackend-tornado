import tornado.web
import tornado.ioloop
import asyncio
import json

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
            self.write(num+ " " + "is"+" " +r)
        else:
            self.write(num + " " + "is not a digit bae")
            
class resourcesHandler(tornado.web.RequestHandler):
    def get(self,studentName,courseId):
        self.write("hello" + " " + studentName + " " + "you are currently viewing"+" " +courseId + " " + "in this page")

class listHandler(tornado.web.RequestHandler):
    def get(self):
        f = open("list.txt", "r")
        movie = f.read().splitlines()
        f.close()
        self.write(json.dumps(movie))
    def post(self):
        movie = self.get_argument("movie")
        f = open("list.txt", "a")
        f.write(movie)
        f.write("\n")
        f.close()
        self.write(json.dumps("Its success da"))
        
        

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/movielist", movieHandler),
        (r"/numbercheck", numberHandler),
        (r"/list", listHandler),
        (r"/students/([a-zA-Z]+)/([0-9]+)", resourcesHandler),
        
    ])

    app.listen(2345)
    print("application is running siva! go ahead")
    tornado.ioloop.IOLoop.current().start()
