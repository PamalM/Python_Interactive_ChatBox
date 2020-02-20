import random
import re
import string

#Class to represent our celebrity chat agent.
class Celebrity:

    #Constructor method; Some attributes to describe our celebrity.
    def __init__(self, name, age, birthday, height, career):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.height = height
        self.career = career

#Create a celebrity object for Kevin Hart.
kevinHart = Celebrity("Kevin Hart", 40, "07-06-1979", "1.63m", "standup comedian & actor")

#Keep chatroom running until user says farewell to bot.
while True:

    #User inputs their message.
    message = input("You: ")
