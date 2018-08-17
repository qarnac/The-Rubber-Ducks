import webapp2
import os
import jinja2
import random






###################################################################################
#def get_random_image():
#    image_list=['RDPlain.png','RDZilla.png','RDBow.png','RDBubbles.png','RDCowboy.png','RDGun.png','RDInfinity.png','RDKing.png','RDMustache.png','RDSailor.png','RDShades.png','RDTop.png']
#    return (random.choice(image_list))

def get_random_image():
    image_list=['/images/IDCard_User.png']
    return (image_list)

#def get_random_first_name():
#    first_name_list=['Nutquacker','Quackmire','Eggbert','Quackzilla','Dr.','Locklear','Wisequack','Kevin','Firequacker','Quackerjack','Mallory','Duckleberry','Ducktape','Ducktor','Spuck','Canardinal','Quackatoa','Aqueduckt','Clusterduck']
#    return(random.choice(first_name_list))

#def get_random_last_name():
#    last_name_list=['Waddles','Werbenjaegermanjensen','XIV','Von Drake','Vanderflock','McMallard','The Swan','Webber','Quackers n Milk','The Quacken','The Quack','Afroduck','The Featherweight','The Ponderer','Darwing','The Fowl-Wench','Quacktail','Canarda','The Quack Death','Quackberry','Adiduck','Francis Beakon','Earthquack','Duck Matter']
#    return (random.choice(last_name_list))

#if  return(random.choice(image_list)) doesnt work, try below
#    randNum = random.randint(0,10);
#    return(fortune[random.randint(0,len(fortune)-1)])
