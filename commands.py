# Здесь что-то типо контроллера, связывающего хэндлеры и вью


from aiogram import types
from bot import bot
import view




async def start(message: types.Message):
    await view.greetings(message)

async def finish(message: types.Message):
    await bot.send_message(message.from_user.id,f'{message.from_user.first_name}, '
        f'Чао!')

# async def candies(message: types.Message):
#     await view.nachalo(message)
    

