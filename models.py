#classes go here
import logging
from google.appengine.ext import ndb


#this is google's database
#This class is for creating objects of website users
class DuckUser(ndb.Model): #this is my constructor!
    name = ndb.StringProperty(required = False, default="Duck Person")
    username = ndb.StringProperty(required = True)
    password = ndb.StringProperty(required = True)
    friendCount = ndb.IntegerProperty(required = True, default=0)

class Post(ndb.Model): #this is for the feed/home page!
    name = ndb.StringProperty(required = False)
    username = ndb.StringProperty(required = False)
    text = ndb.StringProperty(required = True)
    time = ndb.StringProperty(required = True)

class Friends(ndb.Model):
    friendName = ndb.StringProperty(required = False, default="Scrooge McDuck")
    friendUsername = ndb.StringProperty(required = True)
