from BaseHandler import BaseHandler;
from Model.PostModel import PostModel;
from tornado import gen;
import concurrent.futures;

class IndexHandler(BaseHandler):
    """
        Handles requests to the index page of the blog. Typically displays a list of all posts.
    """
    
    @gen.coroutine
    def get(self):
        """
            View all posts.
            The attempt at fetching the posts will happen in another thread, and the page will be rendered once the results have been returned.
        """
        
        # Attempt to fetch the posts using the PostModel getAllPosts method.
        # This happens inside a new thread thanks to the BaseHandler thread_pool.
        thePosts = yield BaseHandler.thread_pool.submit(PostModel.getAllPosts, None);
        
        # Render the posts using the template (view) file.
        self.render('index.html', page_title = 'Index', thePosts = thePosts);