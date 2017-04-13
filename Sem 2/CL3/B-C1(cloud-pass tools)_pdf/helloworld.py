import webapp2
import os
from google.appengine.ext import db
from google.appengine.ext.webapp import template

class Comment(db.Model):
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)
    
def comment_key():
    return db.Key.from_path('comments_dir','default_comments_dir')

class MainPage(webapp2.RequestHandler):
    def get(self):
        comments_query = Comment.all().ancestor(comment_key()).order('-date')
        comments = comments_query.fetch(10)
        template_values = {'Comments':comments}
        path = os.path.join(os.path.dirname(__file__),'index.html')
        self.response.out.write(template.render(path, template_values))
        
class AddComment(webapp2.RequestHandler):
    def post(self):
        comment = Comment(parent=comment_key())
        comment.content = self.request.get('content')
        comment.put()
        self.redirect('/')
        
app = webapp2.WSGIApplication([
('/',MainPage),
('/add',AddComment)
], debug=True)
    
if __name__=='__main__':
    app.run()