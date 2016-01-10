import tornado.web;

class SinglePost(tornado.web.UIModule):
    """
        A re-usable module (UIModule) for displaying a single post, usually called from a template (view) file.
        This can be used on its own, to show one post, or inside a for loop, to show a list of posts.
    """
    
    def render(self, thePost):
        """
            Automatically called by the UIModule.
            
            @param thePost: An instance of PostModel that will be used to render the post html.
            @type thePost: L{PostModel}
            
            @return: the html that represents the output of the module.
            @rtype: string
        """
        
        # Render a template (view) that contains the required html.
        return self.render_string('../Module/SinglePost/single-post.html', thePost=thePost);