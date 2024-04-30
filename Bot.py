//Комментарий
from aiogram import executor, types, Bot, Dispatcher

token = '7066702701:AAFbr0iviTtnLDcFmd4asckiyNc6o9CQxxE'
bot = Bot(token=token)
dp = Dispatcher(bot=bot)
import asyncio

@dp.message_handler(commands=['start'])
async def echo_handler(message: types.Message):
    await message.answer(f'Приветствую, {message.from_user.username}! Это бот от Антона. Вот список команд, которые в данный момент поддерживает бот: /about')

@dp.message_handler(commands=['about'])
async def echo_handler(message: types.Message):
    await message.answer('Данный бот создан для всего, что только можно сюда впихнуть. Спасибо за внимание!')

if __name__ == '__main__':
    executor.start_polling(dp)
