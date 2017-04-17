import webapp2
from google.appengine.ext import db
from google.appengine.ext.webapp import template

class Employee(db.Model):
    name = db.StringProperty()
    salary = db.FloatProperty()
    mobile = db.StringProperty()
    profile = db.StringProperty()

class MainPage(webapp2.RequestHandler):
    def get(self):  
        employees = Employee.all().ancestor(employee_key()).order('name') 
        Employees = employees.fetch(10)
        employees_dir = {'Employees': Employees}
        self.response.out.write(template.render('index.html',employees_dir))

def employee_key():
    return db.Key.from_path('comments_dir','default_comments_dir')

class Add(webapp2.RequestHandler):
    def post(self):
        employee= Employee(parent=employee_key())
        employee.name = self.request.get('name')
        employee.mobile = self.request.get('mobile')
        employee.profile = self.request.get('position')
        employee.salary = float(self.request.get('salary'))
        employee.put()
        self.redirect('/')
        
app = webapp2.WSGIApplication([('/',MainPage),('/add',Add)],debug=True)
        
if __name__ == '__main__':
    app.run()