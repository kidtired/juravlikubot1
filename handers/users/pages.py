from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.filters import Command

from loader import dp

import logging
import random

from keyboard.inline.choice_buttons import miliy_menu #info_keyboard, more_keyboard, miliy_menu, polezniy_menu, kakoi

#Для кнопок милого бота
from handers.users.kompliment import compliment
from annekdot import anekdot
from podkat import podkat
from pohvala import pohvala



#@dp.callback_query_handler(text_contains="info")
#async def buying_info(call: CallbackQuery):
#    await call.answer(cache_time=60)
#    callback_data = call.data
#    logging.info(f"{callback_data=}")

#    await call.message.answer("основы... куда же без них :D",
#                              reply_markup=info_keyboard)


#@dp.callback_query_handler(text_contains="more")
#async def buying_more(call: CallbackQuery):
#    await call.answer(cache_time=60)
#    callback_data = call.data
#    logging.info(f"{callback_data=}")

#    await call.message.answer("про метроном не забывай...",
#                              reply_markup=more_keyboard)




# Боты первого меню

#Милый бот запуск кнопок
#@dp.callback_query_handler(text_contains="miliy_bot")
#async def miliy_start(call: CallbackQuery):
#    await call.answer(cache_time=60)
#    callback_data = call.data
#    logging.info(f"{callback_data=}")

@dp.message_handler(Command("start"))
async def miliy_start(message: Message):

    await message.answer('Привет. Я был создан для того, чтобы ты улыбалась.)')

    await message.answer('Создательница научила меня делать комплименты и подкаты, хвалить и рассказывать анекдоты.')

    await message.answer("Что выберешь?",
                              reply_markup=miliy_menu)

# Спец по хобби запуск кнопок
#@dp.callback_query_handler(text_contains="spec_bot")
#async def polezniy_start(call: CallbackQuery):
#    await call.answer(cache_time=60)
#    callback_data = call.data
#    logging.info(f"{callback_data=}")

#    await call.message.answer('Я был создан для того, чтобы ты узнала что-то новое. )',
#                              reply_markup=polezniy_menu)




#Отклик на кнопки милого бота
@dp.message_handler(commands=['Комплимент'])
async def do_compliment(message: Message):
    await message.answer(text=random.choice(compliment))

@dp.message_handler(commands=['Подкат'])
async def do_compliment(message: Message):
    await message.answer(text=random.choice(podkat))

#@dp.message_handler(commands=['Похвала'])
#async def do_compliment(message: Message):
#   await message.answer(text=random.choice(pohvala))

@dp.message_handler(commands=['Анекдот'])
async def do_compliment(message: Message):
    await message.answer(text=random.choice(anekdot))

