# This Python file uses the following encoding: utf-8
import os, sys

# Problem Set 0
# Name: Josh Haines
# Collaborators: None
# Time Spent: 15 min


# Write a program that does the following in order: 
# 	Asks the user to enter his/her date of birth. 
# 	Asks the user to enter his/her last name. 
# 	Prints out the user’s last name and date of birth, in that order.

print "Welcome to the first problem set for MIT OpenCourseware class 600."
print "For the first problem we would like to ask you some questions..."

print "Please enter your date of birth in the format 'mm/dd/yyyy'."
dateOfBirth = raw_input(">")
print "Thanks!"

print "Please enter your last name."
lastName = raw_input(">")
print "Got it...doing some calculations, aligning telemetry, adjusting rotation...all set!"
print "Your last name is %s and your date of birth is %s." % (lastName, dateOfBirth)