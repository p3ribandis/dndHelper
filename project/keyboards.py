from aiogram import types, utils
import keyboard_creator as kc

class keyboards:
    main_kb = [
        [types.KeyboardButton(text="Дайсы 🎲")],
        [types.KeyboardButton(text="Таблички 🎰")]
    ]

    main_kb_style = types.ReplyKeyboardMarkup(
        keyboard=main_kb,
        resize_keyboard=True,
        input_field_placeholder='Выберите подраздел'
    )

    sheets_names = kc.keyboard_creator.get_sheets_names()

    sheets_kb = [
        [types.KeyboardButton(text="Главное меню 🔙")]
    ]
    for name in sheets_names:
        sheets_kb.append([types.KeyboardButton(text = name)])

    sheets_kb_style = types.ReplyKeyboardMarkup(
        keyboard=sheets_kb,
        resize_keyboard=False,
        input_field_placeholder='Выберите таблицу'
    )

    dice_kb = [
        [types.KeyboardButton(text="Главное меню 🔙")],
        [types.KeyboardButton(text="d4")],
        [types.KeyboardButton(text="d6")],
        [types.KeyboardButton(text="d8")],
        [types.KeyboardButton(text="d10")],
        [types.KeyboardButton(text="d12")],
        [types.KeyboardButton(text="d20")],
        [types.KeyboardButton(text="d100")]
    ]

    dice_kb_style = types.ReplyKeyboardMarkup(
        keyboard=dice_kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите дайс для броска"
    )
    