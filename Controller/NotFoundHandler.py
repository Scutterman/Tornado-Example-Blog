import tornado.web;
from BaseHandler import BaseHandler;

class NotFoundHandler(BaseHandler):
    """
        Handles requests to parameters that haven't been programmed into the App (404 errors).
    """
    
    def prepare(self):
        """
            This is called before any of the HTTP Method methods.
            It's supposed to be used to prepare the Handler for dealing with the requests, but we'll use it to raise the HTTP 404 Status.
            The 404 is then dealt with in the L{BaseHandler} that this class extends.
        """
        raise tornado.web.HTTPError(404, "Page Not Found");
    
    def get(self, url):
        """
            This must be implemented, otherwise the error will be changed to 405 (method unavailable) for 404 GET requests.
            
            @param url: The url that wasn't successfully matched.
            @type url: string
        """
        pass;
    
    def post(self, url):
        """
            This must be implemented, otherwise the error will be changed to 405 (method unavailable) for 404 POST requests.
            
            @param url: The url that wasn't successfully matched.
            @type url: string
        """
        pass;