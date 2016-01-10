from collections import defaultdict

class PostModel:
    """
        This is the data model that handles the static methods used for CRUD of blog posts.
        It also can be initialised with a post id and acts as a container for the blog post, allowing the user to get the post id, title, and text
        
        @ivar id: The blog post id
        @type id: int
        
        @ivar title: The blog post title
        @type title: string
        
        @ivar text: The main content of the blog post
        @type text: string
        
        @cvar posts: A dictionary of the blog posts. Each post is represented by a list containing the title in index 0 and the text in index 1. The dictionary key represents the post id.
        @type posts: defaultdic(list)
        
        @cvar nextPostId: Represents the id that will be used the next time a post is created. This just makes it easier to manage the blog when posts start getting created / deleted. This is automatically incremented when a new post is created, so it's always accurate.
        @type nextPostId: int
    """
    id = -1;
    title = '';
    text = '';
    
    posts = defaultdict(list);
    posts[1].extend(['Post 1', 'Text 1']);
    posts[2].extend(['Post 2', 'Text 2']);
    posts[3].extend(['Post 3', 'Text 3']);
    posts[4].extend(['Post 4', 'Text 4']);
    
    nextPostId = 5;
    
    def __init__(self, db, id):
        """
            Populate the instance variables with the values connected with the post id that is passed in.
            
            @param db: Not currently used. Was intended to point to a database that held the posts, but I got lazy and stored the posts in a class variable instead.
            @type db: None
            
            @param id: The id of the post to fetch the values for.
            @type id: int
        """
        
        id = int(id);
        
        try:
            # Get the post
            thePost = PostModel.posts.get(id, None);
            
            # No post found for that id
            if thePost is None:
                return None;
            
            # Set the instance variables
            self.id = id;
            self.title = thePost[0];
            self.text = thePost[1];
        
        # Something went wrong
        except IndexError:
            return None;
    
    def getId(self):
        """
            @return: The id of the instanced post. Will always be >= 1 if the class initialized properly.
            @rtype: int
        """
        return self.id;
    
    def getTitle(self):
        """
            @return: The title of the instanced post.
            @rtype: string
        """
        return self.title;
    
    def getText(self):
        """
            @return: The main content of the instanced post.
            @rtype: string
        """
        return self.text;
        
    @staticmethod
    def getAllPosts(db):
        """
            Fetch all of the posts.
            
            @param db: Not currently used.
            @type db: None
            
            @return: A list of PostModel objects representing the individual blog posts.
            @rtype: list[PostModel]
        """
        
        # To be returned
        allPosts = [];
        
        # Iterate over the post ids
        for key in PostModel.posts:
            # Instantiate the PostModel
            post = PostModel(None, key);
            
            # It's a valid post, add it to the list
            if post.id != -1:
                allPosts.append(post);
                
        # Return the list
        return allPosts;
    
    @staticmethod
    def createPost(db, title, text):
        """
            Create a new blog post.
            
            @param db: Not currently used.
            @type db: None
            
            @param title: The post title.
            @type title: string
            
            @param text: The main content of the blog post.
            @type text: string
            
            @return: The post id of the new post.
            @rtype: int
        """
        
        # Get the next post id, this will become the id of the post we're attempting to create.
        postId = PostModel.nextPostId;
        
        # Add the title and text to the list of blog posts. This creates the new post.
        PostModel.posts[postId].extend([title, text]);
        
        # Increment the next post id, so it's ready to create a new post next time.
        PostModel.nextPostId += 1;
        
        # Return the id of the new post.
        return postId;
    
    @staticmethod
    def updatePost(db, id, title, text):
        """
            Update a blog post.
            
            @param db: Not currently used.
            @type db: None
            
            @param id: The id of the post that will be updated.
            @type id: int
            
            @param title: The new post title.
            @type title: string
            
            @param text: The new content of the blog post.
            @type text: string
            
            @return: Either the post id (successful update), or None (unsuccessful update)
            @rtype: int | None
        """
        
        # Cast to int, for safety
        id = int(id);
        
        try:
            # Get the current values of the post, or None if the post id doesn't exist
            thePost = PostModel.posts.get(id, None);
            
            # The post doesn't exist, return
            if thePost is None:
                return None;
            
            # Update the post values
            thePost[0] = title;
            thePost[1] = text;
            
            # Set the post to have the new values
            PostModel.posts[id] = thePost;
            
        # Something went wrong
        except KeyError:
            return None;
        
        # Success! Return the id to show it went well 
        return id;
    
    @staticmethod
    def deletePost(db, id):
        """
            Delete a blog post.
            
            @param db: Not currently used.
            @type db: None
            
            @param id: The id of the post that will be deleted.
            @type id: int
            
            @return: A string relating to the status of the delete, either "successful", "not successful", or "keyerror".
            @rtype: string
        """
        
        # Cast to int, for safety
        id = int(id);
        
        try:
            # Get the post. An easy way to ensure it exists
            thePost = PostModel.posts.get(id, None);
            
            # It exists if it is not None
            if thePost is not None:
                # Delete it
                del PostModel.posts[id];
                
                # Return status message
                return "successful";
        # Something went wrong 
        except KeyError:
            return "keyerror";
        
        # Post doesn't exist, or something unknown happened.
        return "not successful";
    