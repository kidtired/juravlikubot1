from main import bot, dp
from aiogram.types import Message, CallbackQuery
from config import admin_id
from loader import dp

from aiogram import types
import keyboard as kb

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")

from aiogram.dispatcher.filters import Command


#@dp.message_handler(Command("start"))
#async def echo(message: Message):
#        text = "привет, журавлик. )"
#        await message.answer (text=text)

#        text = "я сделала кое-что инетересное для тебя"
#        await message.answer (text=text)
#        await message.answer ("выбери бота ^^",
#                              reply_markup=kakoi) #Бот барабаны или Бот по преколу

#async def echo2(message: Message):
#        text = "бота со всевозможной инфой, касающейся игры на барабанах.\n" \
#               " \n" \
#               "ну... и еще кое-что здесь есть ))"
#        await message.answer (text=text)

#        text = "воспользуйся командой /menu"
#        await message.answer(text=text)




