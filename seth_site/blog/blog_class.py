from ..models import Post

def get_pages(posts):
    pages = []
    for i in range(4, len(posts), 5):
        pages.append(posts[i-4:i+1])
    r = len(posts) % 5
    if r > 0:
        pages.append(posts[len(posts) - r:])
    return pages

class Blog():
    def __init__(self):
        self.posts = Post.query.all()
        self.posts.sort(key = lambda i: i.date, reverse = True)
        self.pages = get_pages(self.posts)
