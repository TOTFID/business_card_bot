from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery


rt = Router()


@rt.message(F.text == '/start')
async def start_com(message: Message):
	await message.answer(
		f'[USER ID]: {message.from_user.id}\n'
		f'[CHAT ID]: {message.chat.id}'
	)
   

@rt.message()
async def none_command(message: Message):
   await message.answer('none')
   
   
@rt.message(F.text == '/go')
async def go_com(message: Message, bot: Bot):
   await bot.send_message(chat_id=-4096618624, text='Hello')


