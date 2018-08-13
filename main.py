#main.py
import webapp2
import jinja2
import os
import logging
from models import *

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.info('in get self')
        mypage = env.get_template('templates/index.html')
        self.response.write(mypage.render())
    def post(self):
        mypage = env.get_template('templates/index.html')
        self.response.write(mypage.render())


class CreateNewAccPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('template/create_new.html')
        self.response.write(mypage.render())

class LoginAccPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('template/create_new.html')
        self.response.write(mypage.render())

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/create_new', CreateNewAccPage),
    ('/login', LoginAccPage)
], debug=True)
