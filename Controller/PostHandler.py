from BaseHandler import BaseHandler;
from Model.PostModel import PostModel;
from tornado import gen;
import concurrent.futures;

class PostHandler(BaseHandler):
    
    # Create or update a post
    @gen.coroutine
    def post(self, id):
        id = int(id);
        title = self.get_argument('title', '');
        text = self.get_argument('text', '');
        
        if id == -1:
            id = yield BaseHandler.thread_pool.submit(PostModel.createPost, None, title, text);
        else:
            id = yield BaseHandler.thread_pool.submit(PostModel.updatePost, None, id, title, text);
        
        if id is None:
            self.redirect("/");
        else:
            self.redirect("/get/post/{}/".format(id));
    
    # Form to create or update a single post
    @gen.coroutine
    def get(self, id):
        thePost = yield BaseHandler.thread_pool.submit(PostModel, None, id);
        if thePost.getId() is -1:
            page_title = 'Create Post';
        else:
            page_title = 'Update Post';
            
        self.render('create-post.html', page_title = page_title, thePost = thePost);