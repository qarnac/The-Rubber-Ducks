import webapp2
import os
import jinja2
import random

def get_random_image():
    image_list=['RDPlain.png','RDZilla.png']

    return(random.choice(image_list))

def get_random_first_name():
    first_name_list=['']

    return(random.choice(first_name_list))

def get_random_last_name():
    last_name_list=['']

    return random(choice(last_name_list))

#if  return(random.choice(image_list)) doesnt work, try below
#    randNum = random.randint(0,10);
#    return(fortune[random.randint(0,len(fortune)-1)])
