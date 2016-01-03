from BaseHandler import BaseHandler;
from Model.PostModel import PostModel;

class IndexHandler(BaseHandler):
    # Retrieve all posts
    def get(self):
        self.render('index.html', page_title = 'Index', thePosts = PostModel.getAllPosts(None));