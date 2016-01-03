from BaseHandler import BaseHandler;
from Model.PostModel import PostModel;

class DeleteHandler(BaseHandler):
    
    #Status of delete
    def get(self, status, id):
        self.render('delete.html', page_title = "delete {}".format(status), status = status, id = id);
        
    # Delete a single post
    def post(self, id):
        status = PostModel.deletePost(None, id);
        self.redirect("/delete/status/{}/{}/".format(status, id));