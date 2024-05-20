import asyncio

from aiogram import Bot, Dispatcher
from handlers import start_handler, request_handler
from config_reader import config
from commands import set_commands

bot = Bot(token=config.TOKEN_API.get_secret_value())
dp = Dispatcher()


async def main():
    await set_commands(bot)
    dp.include_router(start_handler.router)
    dp.include_router(request_handler.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
