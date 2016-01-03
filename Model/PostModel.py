from collections import defaultdict

class PostModel:
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
        id = int(id);
        
        try:
            thePost = PostModel.posts[id];
            if thePost is None:
                return None;
            
            self.id = id;
            self.title = thePost[0];
            self.text = thePost[1];
        except IndexError:
            return None;
    
    def getId(self):
        return self.id;
    
    def getTitle(self):
        return self.title;
    
    def getText(self):
        return self.text;
        
    @staticmethod
    def getAllPosts(db):
        allPosts = [];
        for key in PostModel.posts:
            post = PostModel(None, key);
            if post.id != -1:
                allPosts.append(post);  
        return allPosts;
    
    @staticmethod
    def createPost(db, title, text):
        postId = PostModel.nextPostId;
        PostModel.posts[postId].extend([title, text]);
        PostModel.nextPostId += 1;
        return postId;
    
    @staticmethod
    def updatePost(db, id, title, text):
        id = int(id);
        
        try:
            thePost = PostModel.posts.get(id, None);
            if thePost is None:
                return None;
            
            thePost[0] = title;
            thePost[1] = text;
            PostModel.posts[id] = thePost;
        except KeyError:
            return None;
        
        return id;
    
    @staticmethod
    def deletePost(db, id):
        id = int(id);
        
        try:
            thePost = PostModel.posts.get(id, None);
            if thePost is not None:
                del PostModel.posts[id];
                return "successful";
        except KeyError:
            pass;
        
        return "not successful";
    