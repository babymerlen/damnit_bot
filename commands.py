from aiogram import Bot
from aiogram.types import BotCommand


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Вернуться в начало"),
        BotCommand(command="/help", description="Узнать список команд")
    ]
    await bot.set_my_commands(commands)
