from aiogram import Dispatcher

import commands
import model

def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start, commands=['start'])
    dp.register_message_handler(commands.finish, commands=['finish'])
    #dp.register_message_handler(commands.candies, commands=['candies'])
    dp.register_message_handler(model.game)
    
