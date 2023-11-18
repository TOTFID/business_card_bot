from aiogram import Bot
from bot.settings import settings


async def start_bot(bot: Bot):
	await bot.send_message(settings.bots.admin_id, text='Bot already start')


async def stop_bot(bot: Bot):
	await bot.send_message(settings.bots.admin_id, text='Bot already stop')
