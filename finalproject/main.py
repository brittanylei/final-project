import webapp2
import jinja2
import os
import logging

from google.appengine.ext import ndb
from google.appengine.api import users

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('new.html')
        self.response.out.write(template.render())

    def post(self):
        #
        # country = self.response.get('country')
        # title = self.response.get('title')
        # publishedDate = self.response.get('publishedDate')
        # language = self.response.get('language')
        # authors = self.response.get('authors')
        #
        # template_values = {'country':country, 'title':title, 'publishedDate':publishedDate, 'language':language,
        # 'authors':authors}

        book_id = self.response.get('')
        template = jinja_environment.get_template('book.html')
        self.response.out.write(template.render(template_values))
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
        id = self.request.get('id')
        logging.info("the id is " + id)
        template_values = {'info':id}
        template= jinja_environment.get_template('book.html')
        self.response.out.write(template.render(template_values))

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

        email = user.email()

        if user:
            logout_url = users.CreateLogoutURL('/')
            template = jinja_environment.get_template('sign-in.html')
            template_values = {'email':email, 'logout_url':logout_url}

            self.response.out.write(template.render(template_values))

        else:
            login_url = users.CreateLoginURL('/')
            self.response.write('Logging Out')

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

class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        template= jinja_environment.get_template('aboutus.html')
        self.response.out.write(template.render())

class NotesHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        template= jinja_environment.get_template('notes.html')
        self.response.out.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/home', HomeHandler),
    ('/results', ResultsHandler),
    ('/apistuff', ApiStuffHandler),
    ('/signin', SignInHandler),
    ('/mybooks', MyBooksHandler),
    ('/aboutus', AboutUsHandler),
    ('/notes', NotesHandler),
    ('/practice', PracticeHandler),
    ('/book', BookHandler)
], debug=True)
