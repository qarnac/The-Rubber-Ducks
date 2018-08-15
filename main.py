#main.py
import webapp2
import jinja2
import os
import logging
from models import *
from google.appengine.api import users
from game import *

#this is a test

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
#DONT TOUCH THIS UNLESS COMPLETLY NECESSARY
class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.info('in get self')
        mypage = env.get_template('templates/main.html')
        self.response.write(mypage.render())
    def post(self):
        mypage = env.get_template('templates/main.html')
        self.response.write(mypage.render())
#DONT TOUCH THIS UNLESS COMPLETLY NECESSARY
class CreateNewAccPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/create_new.html')
        self.response.write(mypage.render())
        logging.info('in create new account page')
    def post(self):
        user = self.request.get('user')
        username = self.request.get('username')
        password = self.request.get('password')
        logging.info('user is ' + user + ', username is ' + username + ", password is " + password)
        userInfo = DuckUser(name = user,
                    username = username,
                    password = password)
        userInfo.put()
        jinja_values = {'name': user, 'username': username, 'password': password}
        mypage = env.get_template('templates/login.html')
        self.response.write(mypage.render(jinja_values))

#DONT TOUCH THIS UNLESS COMPLETLY NECESSARY
class LoginAccPage(webapp2.RequestHandler):
    def get(self):

        mypage = env.get_template('templates/login.html')
        self.response.write(mypage.render())

    def post(self):
        user = self.request.get('username')
        password = self.request.get('password')
        logging.info('user is ' + user + ', password is' + password)
        userVer = DuckUser.query(DuckUser.username==user, DuckUser.password==password).fetch()
        logging.info(userVer)
        if len(userVer)>0:
            logging.info("user found")
            mypage = env.get_template('templates/navigation.html')
            self.response.write(mypage.render())
        else:
            logging.info("user not found")
            mypage = env.get_template('templates/login.html')
            self.response.write(mypage.render())

###################################################
class HomePage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/home.html')
        self.response.write(mypage.render())
    def post(self):
        mypage = env.get_template('templates/navigation.html')
        self.response.write(mypage.render())

#class CreateNewAccPage(webapp2.RequestHandler):
#    def get(self):
#        mypage = env.get_template('templates/create_new.html')
#        self.response.write(mypage.render())
#        logging.info('in create new account page')
#    def post(self):
#        user = self.request.get('user')
#        username = self.request.get('username')
#        password = self.request.get('password')
#        logging.info('user is ' + user + ', username is ' + username + ", password is " + password)
#        userInfo = DuckUser(name = user,
#                    username = username,
#                    password = password)
#        userInfo.put()
#        jinja_values = {'name': user, 'username': username, 'password': password}
#        mypage = env.get_template('templates/login.html')
#        self.response.write(mypage.render(jinja_values))
class NavPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/navigation.html')
        self.response.write(mypage.render())
    def post(self):
        mypage = env.get_template('templates/navigation.html')
        self.response.write(mypage.render())

class SignUpPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/signup.html')
        self.response.write(mypage.render())

class ProfilePage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/profile.html')
        self.response.write(mypage.render())

class GameStartPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/gamestart.html')
        self.response.write(mypage.render())

    def post(self):
        #random_image = get_random_image()random_image =
#        random_first_name = get_random_first_name()
        random_last_name = get_random_last_name()
        duckVars = { #"random_image": random_image,
        "random_first_name": random_first_name,
        "random_last_name": random_last_name}
        mypage = env.get_template('templates/gameresults.html')
        self.response.write(mypage.render(duckVars))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/create_new', CreateNewAccPage),
    ('/login', LoginAccPage),
    ('/home', HomePage),
    ('/navigation', NavPage),
    ('/signup', SignUpPage),
    ('/profile', ProfilePage),
    ('/gamestart', GameStartPage)
], debug=True)
