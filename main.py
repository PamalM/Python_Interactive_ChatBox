import random
import re
import string
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
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



my_bot = ChatBot(name='PyBot', read_only=True,
                 logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'])

trainer = ChatterBotCorpusTrainer(my_bot)
trainer.train(
    "chatterbot.corpus.english",
     "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)
small_talk = ['hi there!',
              'hi!',
              'how do you do?',
              'how are you?',
              'i\'m cool.',
              'fine, you?',
              'always cool.',
              'i\'m ok',
              'glad to hear that.',
              'i\'m fine',
              'glad to hear that.',
              'i feel awesome',
              'excellent, glad to hear that.',
              'not so good',
              'sorry to hear that.',
              'what\'s your name?',
              'i\'m pybot. ask me a math question, please.']
math_talk_1 = ['pythagorean theorem',
               'a squared plus b squared equals c squared.']
math_talk_2 = ['law of cosines',
               'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']

list_trainer = ListTrainer(my_bot)


for item in (small_talk, math_talk_1, math_talk_2):
          list_trainer.train(item)

#Keep chatroom running until user says farewell to bot.
while True:

    #User inputs their message.
    message = input("You: ")
    if message == "farewell":
       break
    else:
        print(my_bot.get_response(message))
