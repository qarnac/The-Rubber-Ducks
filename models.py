#classes go here
from google.appengine.ext import ndb #this is google's database

#This class is for creating objects of website users
class DuckUser(ndb.Model): #this is my constructor!
    name = ndb.StringProperty(required = False, default="Duck Person")
    username = ndb.StringProperty(required = True)
    password = ndb.StringProperty(required = True)

class Post(ndb.Model): #this is for the feed/home page!
    username = ndb.StringProperty(required = False)
    text = ndb.StringProperty(required = True)
    time = ndb.StringProperty(required = True)
# might want to include username & profile icon and picture thing

# #This class is for creating....?
# class Duck(ndb.Model): #this is my constructor!
#     #duck info here
