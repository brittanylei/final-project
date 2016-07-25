#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
<<<<<<< HEAD

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))
=======
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
>>>>>>> f5d7ebc81686d71a7a591f913d836aa7e1b4d2e1

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





app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/results', ResultsHandler)
], debug=True)
