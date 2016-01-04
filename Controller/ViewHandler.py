from BaseHandler import BaseHandler;
from Model.PostModel import PostModel;
from tornado import gen;
import concurrent.futures;

class ViewHandler(BaseHandler):
    
    # Retrieve a single post
    @gen.coroutine
    def get(self, id):
        thePost = yield BaseHandler.thread_pool.submit(PostModel, None, id);
        
        if (thePost.id is -1):
            self.setStatus(404);
        else:
            self.render('view-post.html', page_title = 'Index', thePost = thePost);