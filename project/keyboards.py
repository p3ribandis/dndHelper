from aiogram import types, utils


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

    sheets_kb = [
        [types.KeyboardButton(text="Главное меню 🔙")],
        [types.KeyboardButton(text="Цвет")],
        [types.KeyboardButton(text="Таблица2")],
        [types.KeyboardButton(text="Таблица3")],
        [types.KeyboardButton(text="Таблица4")],
        [types.KeyboardButton(text="Таблица5")]
    ]

    sheets_kb_style = types.ReplyKeyboardMarkup(
        keyboard=sheets_kb,
        resize_keyboard=True,
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
    