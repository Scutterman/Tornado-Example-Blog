from BaseHandler import BaseHandler;
from Model.PostModel import PostModel;
from tornado import gen;
import concurrent.futures;

class PostHandler(BaseHandler):
    """
        Handles requests to create or update a post.
        GET: Display a form to create or update a post, depending on if the id parameter is -1 or not.
        POST: Create or update a post, depending on if the id parameter is -1 or not.
    """
    
    @gen.coroutine
    def post(self, id):
        """
            Create or update a post.
            Happens in another thread.
            Redirects to view the individual post on success, or to the index page if the post isn't found.
            
            @param id: The id of the post. If it's -1, try to create a new post. Otherwise, try to update the post.
            @type id: int
        """
        
        # Cast to int for safety.
        id = int(id);
        
        # Get the post title and post content from the POST request.
        title = self.get_argument('title', '');
        text = self.get_argument('text', '');
        
        # Create a post, using the thread_pool in the BaseHandler.
        if id == -1:
            id = yield BaseHandler.thread_pool.submit(PostModel.createPost, None, title, text);
        # Update a post, using the thread_pool in the BaseHandler.
        else:
            id = yield BaseHandler.thread_pool.submit(PostModel.updatePost, None, id, title, text);
        
        # Fail. Probably the post doesn't exist, so just go back to the index page. No fancy error handling for us
        if id is None:
            self.redirect("/");
        # Success, go to see the fruits of our labour.
        else:
            self.redirect("/get/post/{}/".format(id));
    
    @gen.coroutine
    def get(self, id):
        """
            Display a HTML form that will be used to create or update a post
            
            @param id: The id of the post. If it's -1, we want to create a new post. Otherwise, we want to update a post.
            @type id: int
        """
        
        # Attempt to get a post using the supplied id. This happens in another thread to prevent blocking.
        thePost = yield BaseHandler.thread_pool.submit(PostModel, None, id);
        
        # If the post id is -1, then the post cannot exist yet. Create a new one.
        if thePost.getId() is -1:
            page_title = 'Create Post';
        # Otherwise, the post exists and we want to update it.
        else:
            page_title = 'Update Post';
            
        # Render the html.
        self.render('create-post.html', page_title = page_title, thePost = thePost);