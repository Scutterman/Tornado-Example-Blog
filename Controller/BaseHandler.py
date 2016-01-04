import tornado.web;
from tornado import gen;
import concurrent.futures;

class BaseHandler(tornado.web.RequestHandler):
    thread_pool = concurrent.futures.ThreadPoolExecutor(4);
    
    # Handle Errors
    def prepare(self):
        pass;