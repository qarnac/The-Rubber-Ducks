#main.py
import webapp2
import jinja2
import os
import logging
from models import *

#this is a test

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.info('in get self')
        mypage = env.get_template('templates/main.html')
        self.response.write(mypage.render())
    def post(self):
        mypage = env.get_template('templates/main.html')
        self.response.write(mypage.render())


class CreateNewAccPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/create_new.html')
        self.response.write(mypage.render())

class LoginAccPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/login.html')
        self.response.write(mypage.render())

class HomePage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/home.html')
        self.response.write(mypage.render())

class NavPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/navigation.html')
        self.response.write(mypage.render())

class SignUpPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/signup.html')
        self.response.write(mypage.render())



app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/create_new', CreateNewAccPage),
    ('/login', LoginAccPage)
    ('/home', HomePage)
    ('/navigation', NavPage)
    ('/signup', SignUpPage)
], debug=True)
