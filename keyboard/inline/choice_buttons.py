from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, \
                            ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

#Первое меню

#kakoi = InlineKeyboardMarkup(inline_keyboard=[
#    [
#        InlineKeyboardButton(text="Милый", callback_data="miliy_bot"),
#        InlineKeyboardButton(text="Полезный", callback_data="spec_bot")
#    ]
#])


#Барабанное меню
#polezniy_menu = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(text="Общая инфа", callback_data="info"),
#         InlineKeyboardButton(text="Ритмы, координация", callback_data="more")
#     ],
#     [
#         InlineKeyboardButton(text="Дальше", callback_data="next"),
#     ]
# ])

#Меню общей инфы по барабанам
#info_keyboard= InlineKeyboardMarkup(inline_keyboard=[
#    [
#        InlineKeyboardButton(text="Ударная установка", callback_data="info")
#    ],
#
#    [
#        InlineKeyboardButton(text="Приёмы игры и звукоизвлечение", callback_data="info")
#    ],
#
#   [
#        InlineKeyboardButton(text="Постановка рук", callback_data="info")
#    ],

#    [
#        InlineKeyboardButton(text="Баланс палочек", callback_data="info")
#    ],

#    [
#        InlineKeyboardButton(text="Одиночные и двойки руками", callback_data="info")
#    ],

#    [
#        InlineKeyboardButton(text="Посадка", callback_data="more")
#    ],

 #   [
 #       InlineKeyboardButton(text="Игра ногой на басу", callback_data="more")
 #   ],

 #   [
 #       InlineKeyboardButton(text="Расстановка элементов", callback_data="more")
 #   ],

 #   [
 #       InlineKeyboardButton(text="Настройка барабанов", callback_data="more")
 #   ]
#])

#Меню ритма по барабанам
#more_keyboard= InlineKeyboardMarkup(inline_keyboard=[
#    [
#        InlineKeyboardButton(text="Ритмы восьмыми и шестнадцатыми (хай хэт)", callback_data="more")
#    ],

#    [
#        InlineKeyboardButton(text="Вариации на координацию", callback_data="more")
#    ],
#
#    [
#        InlineKeyboardButton(text="Популярные ритмы", callback_data="more")
#    ]
#])

#Милый бот меню
miliy_menu= ReplyKeyboardMarkup(resize_keyboard=True,
                                keyboard=[

    [
        KeyboardButton(text="/Комплимент"),
        KeyboardButton(text="/Анекдот"),
    ],

    [
        KeyboardButton(text="/Подкат"),
        #KeyboardButton(text="/Похвала"),
    ]
])
