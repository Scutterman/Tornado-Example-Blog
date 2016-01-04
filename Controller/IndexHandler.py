from BaseHandler import BaseHandler;
from Model.PostModel import PostModel;
from tornado import gen;
import concurrent.futures;

class IndexHandler(BaseHandler):
    
    # Retrieve all posts
    @gen.coroutine
    def get(self):
        thePosts = yield BaseHandler.thread_pool.submit(PostModel.getAllPosts, None);
        self.render('index.html', page_title = 'Index', thePosts = thePosts);