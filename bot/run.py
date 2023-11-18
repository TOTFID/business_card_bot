from handlers import rt, start_bot, stop_bot
from aiogram import Bot, Dispatcher
from bot.settings import settings
import logging
import asyncio


async def main():
   bot = Bot(token=settings.bots.bot_token, parse_mode='html')
   dp = Dispatcher()
   dp.include_router(rt)
   
   dp.startup.register(start_bot)
   dp.shutdown.register(stop_bot)
   
   try:
      await dp.start_polling(bot)
   finally:
      await bot.session.close()

if __name__=='__main__':
   try:
      asyncio.run(main())
   except ConnectionError:
      print('Code has no bot token')