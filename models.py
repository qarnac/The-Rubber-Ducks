#classes go here
import logging
from google.appengine.ext import ndb #this is google's database
current_user = ""
#This class is for creating objects of website users
class DuckUser(ndb.Model): #this is my constructor!
    name = ndb.StringProperty(required = False, default="Duck Person")
    username = ndb.StringProperty(required = True)
    password = ndb.StringProperty(required = True)

class Post(ndb.Model): #this is for the feed/home page!
    username = ndb.StringProperty(required = False)
    text = ndb.StringProperty(required = True)
    time = ndb.StringProperty(required = True)

class Friends(ndb.Model):
    friendName = ndb.StringProperty(required = False, default="Duck Person")
# might want to include username & profile icon and picture thing

# #This class is for creating....?
# class Duck(ndb.Model): #this is my constructor!
#     #duck info here
def set_user(username):
    current_user = username
    logging.info("set user to " + current_user)

def get_current_user():
    logging.info("get user as " + current_user)
    return current_user
