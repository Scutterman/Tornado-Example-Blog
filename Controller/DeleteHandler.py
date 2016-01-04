from BaseHandler import BaseHandler;
from Model.PostModel import PostModel;
from tornado import gen;
import concurrent.futures;

class DeleteHandler(BaseHandler):
    
    #Status of delete
    def get(self, status, id):
        self.render('delete.html', page_title = "delete {}".format(status), status = status, id = id);
        
    # Delete a single post
    @gen.coroutine
    def post(self, id):
        status = yield BaseHandler.thread_pool.submit(PostModel.deletePost, None, id);
        self.redirect("/delete/status/{}/{}/".format(status, id));