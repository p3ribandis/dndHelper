"""

This is a echo bot.

It echoes any incoming text messages.

"""


import logging


from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '5724628929:AAFwpDIs93caCBxxa50DorFq_YptQX3d8Yc'


# Configure logging

logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    kb = [
        [types.KeyboardButton(text="Персонаж")],
        [types.KeyboardButton(text="Таблички")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("", reply_markup=keyboard)

    #await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")




@dp.message_handler()
async def echo(message: types.Message):

    # old style:

    # await bot.send_message(message.chat.id, message.text)


    await message.answer(message.text)




if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)

