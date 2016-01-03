import tornado.web;

class SinglePost(tornado.web.UIModule):
    def render(self, thePost):
        #return "<a href=\"/get/post/{}/\"> Post id {}</a> has the title of \"{}\" and the text of \"{}\"<br />".format(
        #    thePost.getId(),
        #    thePost.getId(),
        #    thePost.getTitle(),
        #    thePost.getText()
        #);
        return self.render_string('../Module/SinglePost/single-post.html', thePost=thePost);