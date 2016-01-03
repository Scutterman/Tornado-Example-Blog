from BaseHandler import BaseHandler;
from Model.PostModel import PostModel;

class PostHandler(BaseHandler):
    
    # Create or update a post
    def post(self, id):
        id = int(id);
        title = self.get_argument('title', '');
        text = self.get_argument('text', '');
        
        if id == -1:
            id = PostModel.createPost(None, title, text);
        else:
            id = PostModel.updatePost(None, id, title, text);
        
        if id is None:
            self.redirect("/");
        else:
            self.redirect("/get/post/{}/".format(id));
    
    # Form to create or update a single post
    def get(self, id):
        thePost = PostModel(None, id);
        if thePost.getId() is -1:
            page_title = 'Create Post';
        else:
            page_title = 'Update Post';
            
        self.render('create-post.html', page_title = page_title, thePost = thePost);