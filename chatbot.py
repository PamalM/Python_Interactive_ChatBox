from chatterbot.trainers import ListTrainer
from datetime import datetime
from chatterbot import ChatBot
import logging

#Method fetches and displays the current date and time for chat start/stop points.
def displayDateTime():

    #Fetch current month.
    month = datetime.now().month

    #Fetch current day.
    day = datetime.now().day

    #Fetch current year.
    year = datetime.now().year

    #Fetch current hour.
    hour = datetime.now().hour

    #Fetch current minute.
    minute = datetime.now().minute

    #Utilizing a python dictionary to hold month according to their digit key. 
    months = {1: "Jan",
                2: "Feb",
                3: "March",
                4: "April",
                5: "May",
                6: "June",
                7: "July",
                8: "Aug",
                9: "Sep",
                10: "Oct",
                11: "Nov",
                12: "Dec"}

    #Utilizing a python dictionary to hold hours according to their 24 - Format. 
    formatTime = {0 : 12,
                  1 : 1,
                  2 : 2,
                  3 : 3,
                  4 : 4,
                  5 : 5,
                  6 : 6,
                  7 : 7,
                  8 : 8,
                  9 : 9,
                  10 : 10,
                  11 : 11,
                  12 : 12,
                  13 : 1,
                  14 : 2,
                  15 : 3,
                  16 : 4,
                  17 : 5,
                  18 : 6,
                  19: 7,
                  20 : 8,
                  21 : 9,
                  22 : 10,
                  23 : 11}
    
    #Determine AM/PM indicator; depending on hour.
    timeOfDay = ""
    if (hour >= 0 and hour <= 11):
        timeOfDay = "AM"
    else:
        timeOfDay = "PM"
        
    
    #Output the current data and time.
    print("Chat Started on " + months[month] + "/" + str(day) + "/" + str(year) +
          " @ " + str(formatTime[hour]) + ":" + str(minute) + " " + timeOfDay + "\n")

#Method literally just prints a dividor to make output look cleaner.
def displayLineSeperator():
    print("-----------------------------------------")
    
#Set logging level to 'CRITICAL'.
#To remove excessive console output to terminal.
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

print("\nChatBox Initializing... ")
print("Please allow Chatbot training to perform.")
displayLineSeperator()

#Open .txt file to populate/train the bot.
with open('Chats.txt') as file:
    conv = file.readlines()

#Create instance of ChatBot.
bot = ChatBot('Kevin Hart')

#Set the trainer for the bot.
trainer = ListTrainer(bot)
trainer.train(conv)

displayLineSeperator()

#Output the chat start time/date. 
displayDateTime()

while True:
    #Get user message.
    request = input("You: ")

    #Get response from bot
    response = bot.get_response(request)

    #Print bot's response.
    print("Bot: ", response)
    print("")
    
