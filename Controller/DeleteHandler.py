from BaseHandler import BaseHandler;
from Model.PostModel import PostModel;
from tornado import gen;
import concurrent.futures;

class DeleteHandler(BaseHandler):
    """
        Handles requests involved in deleting a blog post.
    """
    
    @gen.coroutine
    def post(self, id):
        """
            Request to delete a post.
            The attempt at deleting a post will happen in another thread, and the user will be re-directed to a status page once the delete attempt has completed.
            
            @param id: The id of the post that you want to delete.
            @type id: int
        """
        
        # Attempt to delete the post using the PostModel deletePost method.
        # This happens inside a new thread thanks to the BaseHandler thread_pool.
        status = yield BaseHandler.thread_pool.submit(PostModel.deletePost, None, id);
        
        # Re-direct to the status page and let the user know what the result was.
        self.redirect("/delete/status/{}/{}/".format(status, id));
        
    def get(self, status, id):
        """
            Display a page showing off the status of the attempted post deletion.
            
            @param status: The status message showing the result of the delete.
            @type status: string
            
            @param id: The id of the post that was to be deleted.
            @type id: int
        """
        self.render('delete.html', page_title = "delete {}".format(status), status = status, id = id);