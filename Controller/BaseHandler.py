import tornado.web;
from tornado import gen;
import concurrent.futures;

class BaseHandler(tornado.web.RequestHandler):
    """
        This is the base class for all of the L{Request Handlers<tornado.web.RequestHandler>} used by the app.
        It supplies a L{concurrent.futures.ThreadPoolExecutor} and handles http errors in L{write_error}
        
        @cvar thread_pool: To be used by subclasses when they need to execute synchronous code during a co-routine.
        @type thread_pool: L{concurrent.futures.ThreadPoolExecutor}
        
        @cvar status_messages_4xx: A dictionary of status messages to use for when a http status error is raised.
        @type status_messages_4xx: L{dict}
        
        @cvar status_messages_5xx: A dictionary of status messages to use for when a http status error is raised.
        @type status_messages_5xx: L{dict}
    """

    thread_pool = concurrent.futures.ThreadPoolExecutor(4);
    
    status_messages_4xx = {
        401: 'Please log in and try again.',
        403: 'You don\'t have access to that.',
        404: 'We can\'t find that, sorry.',
        408: 'This is taking too long, but feel free to try again',
        410: 'That isn\'t there any more.',
        418: 'This kingdom runs on tea.',
        426: 'You\'re old fashioned,',
        429: 'Slow Down!',
        451: 'Somebody doesn\'t want you to see this...',
    };
    
    status_messages_5xx = {
        500: 'It\'s broken, bear with us',
        503: 'We\'re a bit overwhelmed at the moment, try again soon.',
    }
    
    def write_error(self, status_code, **kwargs):
        """
            Handles http status errors that get raised by the application.
            
            Overrides L{RequestHandler.write_error}
            
            @param status_code: The http status code that was raised.
            @type status_code: integer
            
            @param kwargs: other arguments (see U{http://www.tornadoweb.org/en/stable/web.html#tornado.web.RequestHandler.write_error} for details)
            @type kwargs: dict
        """
        
        # A message to pass to the view template
        message = "";
        
        # Get the first digit of the status code. This will determine the type of code that's been raised.
        firstDigit = int(str(status_code)[0]);
        
        # Set the correct message based on the first digit of the code
        
        # 1xx - Informational
        if firstDigit is 1:
            message = "As you were.";
        # 2xx - Request successful
        elif firstDigit is 2:
            message = "We did it!";
        # 3xx - Redirect
        elif firstDigit is 3:
            message = "Time to go...";
        # 4xx - Request error
        elif firstDigit is 4:
            message = BaseHandler.status_messages_4xx.get(status_code, 'Something went wrong.');
        # 5xx - Server error
        elif firstDigit is 5:
            message = BaseHandler.status_messages_5xx.get(status_code, 'it\'s brokeded.');
        # Everything else
        else:
            message = "Well that's strange.";
        
        # Set response header
        self.set_header('Content-Type', 'text/html');
        
        # Render the template view for errors, pass in the page title and message to display.
        self.render('error.html', page_title=message, message=message);