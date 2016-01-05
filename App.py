import tornado.ioloop
import tornado.web
import os.path
import tornado.httpserver

from Controller.BaseHandler import BaseHandler
from Controller.NotFoundHandler import NotFoundHandler
from Controller.IndexHandler import IndexHandler
from Controller.ViewHandler import ViewHandler
from Controller.PostHandler import PostHandler
from Controller.DeleteHandler import DeleteHandler

from Module.SinglePost.SinglePost import SinglePost

class Application(tornado.web.Application):
    """
        This is the entry point for the app.
        The Tornado docs show initialising it a slightly different way, but I couldn't get the settings to register that way.
        It might have been me mistaking the syntax, but this way definitely works.
        Set up the Handlers (these would be the Controllers in an MVC app) here, as well as app settings.
        An instance of this app is used to start the Tornado web server (see below)
        
        @ivar handlers: These are the request handlers.
        When a URL request comes in, it is compared against this regular expressions in the list and.
        If the url matches a pattern, the specified L{tornado.web.RequestHandler} subclass is used for the request.
        RequestHandlers are selected as first-come, first-served. As soon as a match is found, that handler is used and the app doesn't try to match further RequestHandlers.
        I just used the pattern and handler parts of URLSpec, but there's also kwargs and name paramaters that you might want to check out.
        These are all subclasses of L{BaseHandler}, which is a subclass of L{tornado.web.RequestHandler}
        These subclasses define the methods that the subclass can handle (get, post, etc.).
        This is important if you don't want the app throwing a 405 Method Not Allowed http error.
        @type handlers: [L{tornado.web.URLSpec}]
        
        @ivar settings: These are settings for the Tornado app.
        I've included a few here, but a full list is avaliable at U{http://www.tornadoweb.org/en/stable/web.html#tornado.web.Application.settings}.
        This sets up:
            - The default path for template/view files used to render pages
            - A list of re-usable ui elements (UIModules).
            Each one is a Subclass of U{http://www.tornadoweb.org/en/stable/web.html#tornado.web.UIModule}
            - Cross Site Request Forgery protection (see U{http://www.tornadoweb.org/en/stable/guide/security.html?highlight=xsrf#cross-site-request-forgery-protection})
            - A ridiculously weak cookie secret key, you should change this. See (U{http://www.tornadoweb.org/en/stable/guide/security.html?highlight=xsrf#cookies-and-secure-cookies})
            - Turning debug mode on. This sets several other settings. Turn this off before going into production.
        See U{http://www.tornadoweb.org/en/stable/guide/running.html#debug-mode-and-automatic-reloading}
        @type settings: dict
    """
    
    def __init__(self):
        
        handlers = [
            (r"/", IndexHandler),                               #GET retrieve all posts
            (r"/get/post/([0-9]+)/", ViewHandler),              #GET retrieve single post
            (r"/delete/post/([0-9]+)/", DeleteHandler),         #POST delete single post
            (r"/delete/status/(.*)/([0-9]+)/", DeleteHandler),  #GET retrieve post delete status
            (r"/post/post/(-1)/", PostHandler),                 #GET or POST create single post
            (r"/post/post/([0-9]+)/", PostHandler),             #GET or POST update single post
            (r"/(.*)", NotFoundHandler),                        #404 links and everything else
        ];
        
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "View"),
            ui_modules={"SinglePost": SinglePost},
            xsrf_cookies=True,
            cookie_secret="Swordfish",
            debug=True,
        )
        
        # Initialize the app, passing in the handlers and settings.
        super(Application, self).__init__(handlers, **settings)

"""
    This is how you start the tornado web server.
    Use L{tornado.web.httpserver.HTTPServer(L{tornado.web.Application})<tornado.web.httpserver.HTTPServer>} to get a reference to the server.
    That can be told to listen on a port, which will happen at regular intervals after you call L{tornado.ioloop.IOLoop.instance().start()}
"""
if __name__ == "__main__":
    app = tornado.httpserver.HTTPServer(Application());
    app.listen(8888);
    try:
        tornado.ioloop.IOLoop.instance().start();
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop();