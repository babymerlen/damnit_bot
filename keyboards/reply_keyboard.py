from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def generate_reply_keyboard():
    kb = ReplyKeyboardBuilder()
    kb.button(text="О нас")
    kb.button(text="Наши работы")
    kb.button(text="Контакты")
    kb.button(text="Заявка")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
