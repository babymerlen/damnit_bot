from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def generate_inline_keyboard():
    kb = [
        [InlineKeyboardButton(text="О нас", callback_data="about_us")],
        [InlineKeyboardButton(text="Наши примеры", callback_data="our_works")],
        [InlineKeyboardButton(text="Контакты", callback_data="contacts")],
        [InlineKeyboardButton(text="Заявка", callback_data="request")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard


def generate_request_keyboard():
    kb = [
        [InlineKeyboardButton(text="Заявка", callback_data="request")],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard
