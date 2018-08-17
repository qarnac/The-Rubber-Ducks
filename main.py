#main.py
import webapp2
import jinja2
import os
import logging
from models import *
from google.appengine.api import users
from game import *
import time

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
        name = self.request.get('name')
        username = self.request.get('username')
        password = self.request.get('password')
        #this is michael 1 testing cookies
        self.response.set_cookie('current_name', name)
        logging.info('users actual name is ' + name + ', username is ' + username + ", password is " + password)
        userInfo = DuckUser(name = name,
                    username = username,
                    password = password)
        userInfo.put()
        jinja_values = {'name': name, 'username': username, 'password': password}
        mypage = env.get_template('templates/login.html')
        self.response.write(mypage.render(jinja_values))

#DONT TOUCH THIS UNLESS COMPLETLY NECESSARY
class LoginAccPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/login.html')
        self.response.write(mypage.render())
    def post(self):
        name = self.request.get('name')
        username = self.request.get('username')
        password = self.request.get('password')
        logging.info('user is ' + username + ', password is' + password)
        userVer = DuckUser.query(DuckUser.username==username, DuckUser.password==password).fetch()
        logging.info(userVer)
        if len(userVer)>0:
            logging.info("user found")
            logging.info("current user in login is: " + username)
            mypage = env.get_template('templates/navigation.html')
            self.response.set_cookie('current_username', username)
            self.response.write(mypage.render())
        else:
            logging.info("user not found")
            mypage = env.get_template('templates/login.html')
            self.response.write(mypage.render())

###################################################
class HomePage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/home.html')
        #test by Kristian
        all_posts = Post.query().fetch()
        logging.info(all_posts)
        dict = {"posts": all_posts}
        self.response.write(mypage.render())
        #end test
    def post(self):
        new_post = self.request.get('new_post')
#        username = current_user
        logging.info("new post is:" + new_post)
        current_username = self.request.cookies.get('current_username')
        current_name = self.request.cookies.get('current_name')
        logging.info("Cookies show:")
        logging.info(current_username)
        user_post = Post(text = new_post, username = current_username, name = current_name, time = time.asctime( time.localtime(time.time()) ))
        user_post.put()
        #username = self.request.get()
        #test by Kris
        mypage = env.get_template('templates/home.html')
        #self.response.write(mypage.render())
        time.sleep(1)
        all_posts = Post.query(Post.username == current_username).fetch()

        logging.info(all_posts)
        dict = {"posts": all_posts,
                "name": current_name,
                "username": current_username}
        self.response.write(mypage.render(dict))
        #end test


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
        dict = {"friend_count": 0}
        self.response.write(mypage.render(dict))
    def post(self):
        current_user = self.request.cookies.get('current_username')
        logging.info("check1")
        logging.info(current_user)

        user = DuckUser.query(DuckUser.username == current_user).fetch()
        logging.info("check2")
        logging.info(user)

        user[0].friendCount = user[0].friendCount + 1
        logging.info("check3")
        logging.info(user[0].friendCount)

        user[0].put()
        logging.info("check4")

        dict = {"friend_count": user[0].friendCount}
        logging.info("check5")
        mypage = env.get_template('templates/profile.html')
        self.response.write(mypage.render(dict))


class GamePage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/gamestart.html')
        self.response.write(mypage.render())

    def post(self):
#        random_image = get_random_image()random_image =
#        random_first_name = get_random_first_name()
#        random_last_name = get_random_last_name()
#        duckVars = { "random_image": random_image,
#        "random_first_name": random_first_name,
#        "random_last_name": random_last_name}
        mypage = env.get_template('templates/gamestart.html')
        self.response.write(mypage.render(duckVars))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/create_new', CreateNewAccPage),
    ('/login', LoginAccPage),
    ('/home', HomePage),
    ('/navigation', NavPage),
    ('/signup', SignUpPage),
    ('/profile', ProfilePage),
    ('/game', GamePage)
], debug=True)
