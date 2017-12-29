#!/usr/bin/python

import commands
import webbrowser #webbrowser library open default browser

# print normal message

print "hello world"

# taking input from user
# raw_input always give you string type data
'''
user_input=raw_input("plz enter your name:")

print "welcome to python"+user_input
print "type of data is",type(user_input)
'''


x=raw_input("type any number:")

if int(x) > 20 :nd int(x) <30
	print commands.getoutput('cal')
else :
	print "plz wait youtube is about to open"
	webbrowser.open_new_tab('https://www.youtube.com')
