import webapp2
import jinja2
import os
import logging

from google.appengine.ext import ndb
from google.appengine.api import users

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

# class User(ndb.Model):
#     user_id = ndb.StringProperty()

class Books(ndb.Model):
    name = ndb.StringProperty()
    description = ndb.StringProperty()
    genre = ndb.StringProperty()
    author = ndb.StringProperty()
    date_published = ndb.DateTimeProperty()
    ISBN = ndb.IntegerProperty()

class Note(ndb.Model):
    quote = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

    def url(self):
        return '/note?key=' + self.key.urlsafe()

class Comment(ndb.Model):
    text = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
    note_key = ndb.KeyProperty(kind=Note)

# class BookList(ndb.Model):
#
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


class NoPdfHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('nopdf.html')
        self.response.out.write(template.render())

class AdventureHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('adventure.html')
        self.response.out.write(template.render())

class SciHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('sci.html')
        self.response.out.write(template.render())

class HomeHandler(webapp2.RequestHandler):

    # myscript = '<script>function blah = </script>'

    def get(self):
        user = users.get_current_user()

        template = jinja_environment.get_template('home.html')
        if user:
            email = user.email()
            logout_url = users.CreateLogoutURL('/')
            template1 = jinja_environment.get_template('sign-out.html')
            template_values = {'email':email, 'logout_url':logout_url}
            self.response.out.write(template.render() + template1.render(template_values))
        else:
            login_url = users.CreateLoginURL('/')
            template1 = jinja_environment.get_template('sign-in.html')
            template_values = {'login_url':login_url}
            self.response.out.write(template.render() + template1.render(template_values))
            # self.redirect(login_url)

class ResultsHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        template = jinja_environment.get_template('results.html')
        if user:
            email = user.email()
            logout_url = users.CreateLogoutURL('/')
            template1 = jinja_environment.get_template('sign-out.html')
            template_values = {'email':email, 'logout_url':logout_url}
            self.response.out.write(template.render() + template1.render(template_values))
        else:
            login_url = users.CreateLoginURL('/')
            template1 = jinja_environment.get_template('sign-in.html')
            template_values = {'login_url':login_url}
            self.response.out.write(template.render() + template1.render(template_values))
            # self.redirect(login_url)

class BookHandler(webapp2.RequestHandler):
    def get(self):
        id = self.request.get('id')
        template_values = {'id':id}
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

class PracticeHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        template= jinja_environment.get_template('practice.html')
        self.response.out.write(template.render())

class MyBooksHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        template = jinja_environment.get_template('mybooks.html')
        if user:
            email = user.email()
            logout_url = users.CreateLogoutURL('/')
            template1 = jinja_environment.get_template('sign-out.html')
            template_values = {'email':email, 'logout_url':logout_url}
            self.response.out.write(template.render() + template1.render(template_values))
        else:
            login_url = users.CreateLoginURL('/')
            template1 = jinja_environment.get_template('sign-in.html')
            template_values = {'login_url':login_url}
            # self.response.out.write(template.render() + template1.render(template_values))
            self.redirect(login_url)

class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        template = jinja_environment.get_template('aboutus.html')
        if user:
            email = user.email()
            logout_url = users.CreateLogoutURL('/')

            template1 = jinja_environment.get_template('sign-out.html')
            template_values = {'email':email, 'logout_url':logout_url}
            self.response.out.write(template.render() + template1.render(template_values))
        else:
            login_url = users.CreateLoginURL('/')
            template1 = jinja_environment.get_template('sign-in.html')
            template_values = {'login_url':login_url}
            self.response.out.write(template.render(template_values) + template1.render(template_values))
            # self.redirect(login_url)

class NoteListHandler(webapp2.RequestHandler):
    # def get(self):
    #     # 1. Get the info from the request.
    #     # 2. Logic (interact w database)
    #     notes = Note.query().fetch()
    #
    #     # 3. Render response
    #     template = jinja_environment.get_template('notelist.html')
    #     template_values = {'notes':notes}
    #     self.response.write(template.render(template_values))
    def get(self):
        user = users.get_current_user()

        notes = Note.query().fetch()
        # 3. Render response
        template = jinja_environment.get_template('notelist.html')
        template_values = {'notes':notes}

        if user:
            email = user.email()
            logout_url = users.CreateLogoutURL('/')
            template1 = jinja_environment.get_template('sign-out.html')
            template_values1 = {'email':email, 'logout_url':logout_url}
            self.response.out.write(template.render(template_values) + template1.render(template_values1))
        else:
            login_url = users.CreateLoginURL('/')
            template1 = jinja_environment.get_template('sign-in.html')
            template_values1 = {'login_url':login_url}
            # self.response.out.write(template.render(template_values) + template1.render(template_values1))
            self.redirect(login_url)

    def post(self):
        # 1. Get the info from the request.
        quote = self.request.get('quote')

        # 2. Logic (interact w database)
        note = Note(quote=quote)
        note.put()

        # 3. Render response
        self.redirect('/notes')


class NotesHandler(webapp2.RequestHandler):
    # def get(self):
    #     user = users.get_current_user()
    #     # 1. Get the info from the request.
    #     urlsafe_key = self.request.get('key')
    #
    #     # 2. Logic (interact w database)
    #     key = ndb.Key(urlsafe=urlsafe_key)
    #     note = key.get()
    #     comments = Comment.query(Comment.note_key == note.key).order(-Comment.date).fetch()
    #
    #     # 3. Render response
    #     template_values = {'note':note, 'comments':comments}
    #     template = jinja_environment.get_template('note.html')
    #     self.response.write(template.render(template_values))

    def get(self):
        user = users.get_current_user()
        # 1. Get the info from the request.
        urlsafe_key = self.request.get('key')

        # 2. Logic (interact w database)
        key = ndb.Key(urlsafe=urlsafe_key)
        note = key.get()
        comments = Comment.query(Comment.note_key == note.key).order(-Comment.date).fetch()

        # 3. Render response
        template_values = {'note':note, 'comments':comments}
        template = jinja_environment.get_template('note.html')

        if user:
            email = user.email()
            logout_url = users.CreateLogoutURL('/')
            template1 = jinja_environment.get_template('sign-out.html')
            template_values1 = {'email':email, 'logout_url':logout_url}
            self.response.out.write(template.render(template_values) + template1.render(template_values1))
        else:
            login_url = users.CreateLoginURL('/')
            template1 = jinja_environment.get_template('sign-in.html')
            template_values1 = {'login_url':login_url}
            # self.response.out.write(template.render(template_values) + template1.render(template_values1))
            self.redirect(login_url)


    def post(self):
        # 1. Get the info from the request.
        text = self.request.get('comment')
        note_key_urlsafe = self.request.get('key')
        # 2. Logic (interact w database)
        note_key = ndb.Key(urlsafe=note_key_urlsafe)
        note = note_key.get()

        comment = Comment(text=text, note_key=note.key)
        comment.put()
        # 3. Render response
        self.redirect(note.url())






class BreakOutHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        template = jinja_environment.get_template('breakout.html')
        if user:
            email = user.email()
            logout_url = users.CreateLogoutURL('/')
            template1 = jinja_environment.get_template('sign-out.html')
            template_values = {'email':email, 'logout_url':logout_url}
            self.response.out.write(template.render() + template1.render(template_values))
        else:
            login_url = users.CreateLoginURL('/')
            template1 = jinja_environment.get_template('sign-in.html')
            template_values = {'login_url':login_url}
            self.response.out.write(template.render(template_values) + template1.render(template_values))
            # self.redirect(login_url)

        # users = User.query().fetch()
        # user_email = self.request.get('email')
        # if (user not in users):
        #     new_user = User(user_id=user_email)
        #     new_user.put()
        #     print "New user alert!!"
        # else:
        #     print "This is a user already"




app = webapp2.WSGIApplication([
    ('/new', MainHandler),
    ('/', HomeHandler),
    ('/results', ResultsHandler),
    ('/apistuff', ApiStuffHandler),
    ('/adventure', AdventureHandler),
    ('/sci', SciHandler),
    ('/mybooks', MyBooksHandler),
    ('/aboutus', AboutUsHandler),
    ('/notes', NoteListHandler),
    ('/note', NotesHandler),
    ('/practice', PracticeHandler),
    ('/book', BookHandler),
    ('/nopdf', NoPdfHandler),
    ('/breakout', BreakOutHandler),
], debug=True)
