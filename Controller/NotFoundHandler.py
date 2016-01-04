import tornado.web;
from BaseHandler import BaseHandler;

class NotFoundHandler(BaseHandler):
    def prepare(self):
        raise tornado.web.HTTPError(404, "Page Not Found");
    
    def get(self, url):
        pass;
    
    def post(self, url):
        pass