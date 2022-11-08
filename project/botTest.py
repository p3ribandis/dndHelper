import logging
import random
from keyboards import keyboards
from sheets import pygsheetsExt

from aiogram import *
from aiogram.dispatcher.filters import Text


API_TOKEN = '5724628929:AAFwpDIs93caCBxxa50DorFq_YptQX3d8Yc'


# Configure logging

logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)


#What user see after start command
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Добро пожаловать в Dnd Helper!\nВыберите раздел", reply_markup=keyboards.main_kb_style)

#Base buttons
@dp.message_handler(Text("Таблички 🎰"))
async def choose_section(message: types.Message):
    await message.answer("Выберите табличку", reply_markup=keyboards.sheets_kb_style)

@dp.message_handler(Text("Дайсы 🎲"))
async def choose_section(message: types.Message):
    await message.answer("Выберите дайс для броска", reply_markup=keyboards.dice_kb_style)

@dp.message_handler(Text('Главное меню 🔙'))
async def main_menu(message: types.Message):
    await message.answer('Выберите раздел', reply_markup=keyboards.main_kb_style)
#---------

#Дайсы
@dp.message_handler(filters.Regexp(regexp='d([0-9]*)'))
async def roll_dice(message: types.Message, regexp):
    val = (int)(regexp.group(1))
    r = random.randint(1, val)
    await message.reply(f"Результат броска d{val}: {str(r)}")
#-----

#Таблички
@dp.message_handler(Text("Цвет"))
async def get_character(message: types.Message):
    m = pygsheetsExt.getColor()
    await message.answer(m)
#----

if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)

