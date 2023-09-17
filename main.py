from chatterbot import ChatBot
from chatterbot.trainers import chatterBotCorpusTrainer

bot = ChatBot("My Bot")

trainer = chatterBotCorpusTrainer(bot)

trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations")

while True:
    user_input = input("user: ")
    if user_input == "exit":
        break
    response = bot.get_response(user_inppiut)
    print ("Bot: ", response)
