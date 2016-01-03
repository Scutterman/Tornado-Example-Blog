from BaseHandler import BaseHandler;
from Model.PostModel import PostModel;

class ViewHandler(BaseHandler):
    
    # Retrieve a single post
    def get(self, id):
        thePost = PostModel(None, id);
        
        if (thePost.id is -1):
            self.setStatus(404);
        else:
            self.render('view-post.html', page_title = 'Index', thePost = thePost);