import tornado.web;

class BaseHandler(tornado.web.RequestHandler):
    # Handle Errors
    def prepare(self):
        pass;
    
    #def get_template_path(self):
        #return 'View/';