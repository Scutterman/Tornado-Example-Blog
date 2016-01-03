import tornado.ioloop
import tornado.web
import os.path
import tornado.httpserver

from Controller.IndexHandler import IndexHandler
from Controller.ViewHandler import ViewHandler
from Controller.PostHandler import PostHandler
from Controller.DeleteHandler import DeleteHandler

from Module.SinglePost.SinglePost import SinglePost

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),                               #GET retrieve all posts
            (r"/get/post/([0-9]+)/", ViewHandler),              #GET retrieve single post
            (r"/delete/post/([0-9]+)/", DeleteHandler),         #POST delete single post
            (r"/delete/status/(.*)/([0-9]+)/", DeleteHandler),  #GET retrieve post delete status
            (r"/post/post/(-1)/", PostHandler),                 #GET or POST create single post
            (r"/post/post/([0-9]+)/", PostHandler),             #GET or POST update single post
        ];
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "View"),
            ui_modules={"SinglePost": SinglePost},
            xsrf_cookies=True,
            cookie_secret="Swordfish",
            debug=True,
        )
        super(Application, self).__init__(handlers, **settings)

if __name__ == "__main__":
    app = tornado.httpserver.HTTPServer(Application());
    app.listen(8888);
    try:
        tornado.ioloop.IOLoop.instance().start();
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop();