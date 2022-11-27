# Отправления сообщений

from aiogram import types
from bot import bot
import model


async def greetings(message: types.Message):
  
    await bot.send_message(message.from_user.id,
        f'{message.from_user.first_name}, привет!\n'
        f'Это игра в конфетки\n'
        f'набери /candies если хочешь сыграть в игру')


# async def nachalo(message: types.Message):
#     await bot.send_message(message.from_user.id,f'введите число от 1 до 29\n\n')
#     await model.game(message)

async def turn_pl(message: types.Message):
    await bot.send_message(message.from_user.id,f'Ходит {message.from_user.first_name}\n\n')

async def turn_bot(message: types.Message):
    await bot.send_message(message.from_user.id,f'Ходит Bot\n\n')

async def fat(message: types.Message):
    await bot.send_message(message.from_user.id,f'Слишком много конфет, жадина')
    
async def wins_pl(message: types.Message):
    await bot.send_message(message.from_user.id,f'Победил {message.from_user.first_name}')

async def wins_bot(message: types.Message):
    await bot.send_message(message.from_user.id,f'Победил Bot')
    
    
async def result (message: types.Message):
    await bot.send_message(message.from_user.id,f"Конфеты первого игрока {model.candiesPl1}\n")
    await bot.send_message(message.from_user.id,f"Конфеты Bot {model.candiesBot}\n")
    await bot.send_message(message.from_user.id,f"Остаток конфет {model.candies}\n\n")
