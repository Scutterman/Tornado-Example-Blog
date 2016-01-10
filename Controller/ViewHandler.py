from BaseHandler import BaseHandler;
from Model.PostModel import PostModel;
from tornado import gen;

import concurrent.futures;
import tornado.web;

class ViewHandler(BaseHandler):
    """
        View a single post.
    """
    
    @gen.coroutine
    def get(self, id):
        """
            View the post.
            The attempt at fetching the post will happen in another thread, and the page will be rendered once the results have been returned.
        """
        
        # Attempt to fetch the PostModel that will contain the post details.
        # This happens inside a new thread thanks to the BaseHandler thread_pool.
        thePost = yield BaseHandler.thread_pool.submit(PostModel, None, id);
        
        # Post does not exist. Raise a 404 error so the BaseHandler can respond accorddingly.
        if (thePost.id is -1):
            self.set_status(404);
            raise tornado.web.HTTPError(404, "Page Not Found");
        # Render the post.
        else:
            self.render('view-post.html', page_title = 'Index', thePost = thePost);