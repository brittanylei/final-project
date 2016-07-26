import webapp2
import jinja2
import os
import logging

from google.appengine.ext import ndb
from google.appengine.api import users

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

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

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('home.html')
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

        #url = "https://www.googleapis.com/books/v1/volumes?q=" + API_KEY
        #results = urlfetch.fetch(url)

        #result_dic = json.parse(result.content)
        #logging.info(results_info(items))

        #template_values = {}
        template= jinja_environment.get_template('apistuff.html')
        self.response.out.write(template.render())

class SignInHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        template= jinja_environment.get_template('sign-in.html')
        self.response.out.write(template.render())

class PracticeHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        template= jinja_environment.get_template('practice.html')
        self.response.out.write(template.render())

class MyBooksHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        template= jinja_environment.get_template('mybooks.html')
        self.response.out.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/home', HomeHandler),
    ('/results', ResultsHandler),
    ('/apistuff', ApiStuffHandler),
    ('/signin', SignInHandler),
    ('/mybooks', MyBooksHandler),
    ('/practice', PracticeHandler),
], debug=True)
