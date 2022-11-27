# Здесь переменные и методы, для их чтения и установки (аля работа классами)

from aiogram import types
from bot import bot
import view
import random
import commands

candies = 200
max_turn = 30
candiesPl1 = 0
candiesBot = 0
count = 0


async def game(message: types.Message):
    global candies
    global max_turn
    global candiesPl1
    global candiesBot
    global count
    if candies > 0:
        while True:
            if count %2 == 0:
                await view.turn_pl(message) 
                
                player = int(message.text)
                
                if 0 < int(player) < max_turn:
                    candiesPl1 += player
                    candies -= player
                    count+=1
                    if candies<=0:
                        if count%2!=0:
                            await view.wins_pl(message)
                            
                            break
                        else:
                            await view.wins_bot(message)
                            
                            break
                else:
                    await view.fat(message)
                
            else:
                await view.turn_bot(message) 
                
                player = int(random.randint(1,20)) 
                
                await bot.send_message(message.from_user.id,f"Bot взял - {player} конфет\n\n")
                
                candiesBot += player
                candies -= player
                count+=1
                if candies<=0:
                    if count%2!=0:
                        await view.wins_pl(message)
                        
                        break
                    else:
                        await view.wins_bot(message)
                        
                        break
                        
            await view.result(message)
            
# async def start_game(message: types.Message):
#     await bot.send_message(message.from_user.id,f'Введите /candies и' 
#         f'начальное количество конфет в корзине, сладкоежки: ')
#     global total_count
#     if 100 < int(total_count) < 1000:
#         await bot.send_message(message.from_user.id,f'Количество конфет на столе: {total_count}\n'
#             f'Конфеты первого игрока {candiesPl1}\n'
#             f'Конфеты Bot {candiesBot}')
#     else:
#         await bot.send_message(message.from_user.id,f'Попробуй от 100 до 1000')
        