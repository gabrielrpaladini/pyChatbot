from chatterbot.trainers import ListTrainer 
from chatterbot import ChatBot

bot = ChatBot('Bot')

bot.set_trainer(ListTrainer)

#Training 
file_trainer = open(r'Trainer.txt', 'r')
chats = file_trainer.readlines()
bot.train(chats)
file_trainer.close()

while True:
    question = input('You: ')
    answer = bot.get_response(question)
    print('Bot: {}'.format(str(answer)))