import webapp2
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

from google.appengine.ext import ndb
from google.appengine.api import users

class Books(ndb.Model):
    name = ndb.StringProperty()
    description = ndb.StringProperty()
    genre = ndb.StringProperty()
    author = ndb.StringProperty()
    date_published = ndb.DateTimeProperty()
    ISBN = ndb.IntegerProperty()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('new.html')
        self.response.out.write(template.render())

class ResultsHandler(webapp2.RequestHandler):
    def get(self):
        template= jinja_environment.get_template('results.html')
        self.response.out.write(template.render())

class BookHandler(webapp2.RequestHandler):
    def get(self):
        template= jinja_environment.get_template('book.html')
        self.response.out.write(template.render())

class ApiStuffHandler(webapp2.RequestHandler):
    def get(self):
        template= jinja_environment.get_template('apistuff.html')
        self.response.out.write(template.render())

class SignInHandler(webapp2.RequestHandler):
    def get(self):
        template= jinja_environment.get_template('book.html')
        self.response.out.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/results', ResultsHandler),
    ('/apistuff', ApiStuffHandler),
    ('/signin', SignInHandler),
], debug=True)
