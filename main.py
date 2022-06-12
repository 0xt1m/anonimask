import logging

from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = "5507739970:AAERQFAy3OzBBvd8oAtCGfBmRS2QQD-BaDA"

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def hello(message):
	await message.answer("<b>Надішліть мені своє анонімне питання 🤫</b>", parse_mode="HTML")


@dp.message_handler(content_types=['text'])
async def question_handler(message):
	await bot.send_message(721070739, f"<b>Нове питання</b>\n{message.text}", parse_mode="HTML")
	await message.answer("<b>Питання надіслано 🤐</b>", parse_mode="HTML")





if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)