#classes go here

from google.appengine.ext import ndb #this is google's database

#This class is for creating objects of website users
class DuckUser(ndb.Model): #this is my constructor!
    name = ndb.StringProperty(required = False, default="Duck Person")
    username = ndb.StringProperty(required = True)
    password = ndb.StringProperty(required = True)

# #This class is for creating....?
# class Duck(ndb.Model): #this is my constructor!
#     #duck info here
