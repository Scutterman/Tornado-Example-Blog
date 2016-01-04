import tornado.web;
from tornado import gen;
import concurrent.futures;

class BaseHandler(tornado.web.RequestHandler):
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
    
    # Handle Errors
    def write_error(self, status_code, **kwargs):
        massage = "";
        firstDigit = int(str(status_code)[0]);
        
        if firstDigit is 1:
            message = "As you were.";
        elif firstDigit is 2:
            message = "We did it!";
        elif firstDigit is 3:
            message = "Time to go...";
        elif firstDigit is 4:
            message = BaseHandler.status_messages_4xx.get(status_code, 'Something went wrong.');
        elif firstDigit is 5:
            message = BaseHandler.status_messages_5xx.get(status_code, 'it\'s brokeded.');
        else:
            message = "Well that's strange.";
        
        self.set_header('Content-Type', 'text/html');
        self.render('error.html', page_title=message, message=message);