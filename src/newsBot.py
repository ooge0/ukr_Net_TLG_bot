import json

from aiogram import Bot, Dispatcher, executor, types
from src.auth.auth_data import token
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
import time


bot = Bot(token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start (message: types.Message):
    start_buttons = ['🐉 1+1', 'шоТоТам.Net']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer('Чого душа бажає? Тицни сюди >>>', reply_markup=keyboard)

@dp.message_handler(Text(equals='🐉 1+1'))
async def get_info(message: types.Message):
    await message.answer('Searching, please wait ....')
    with open("dataSource/result.json", encoding="utf-8") as file:
        data = json.load(file)
    await message.answer('Data file was found....')
    for index,  item in enumerate(data):
        card = f'{hlink(item.get("article_Title"), item.get("url"))}\n' \
               f'{hbold("#")}{item.get("#")}\n'
        if index%20 == 0:
            time.sleep(3)
        await message.answer(card)
    await message.answer('Data processing completed.')

@dp.message_handler(Text(equals='шоТоТам.Net'))
async def get_info(message: types.Message):
    await message.answer('Далі буде....')

def main():
    executor.start_polling(dp)

if __name__ == '__main__':
    main()