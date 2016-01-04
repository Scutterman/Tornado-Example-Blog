import tornado.web;

class SinglePost(tornado.web.UIModule):
    def render(self, thePost):
        return self.render_string('../Module/SinglePost/single-post.html', thePost=thePost);