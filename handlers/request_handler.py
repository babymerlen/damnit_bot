from aiogram import types, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from config_reader import config

router = Router()


class Form(StatesGroup):
    waiting_for_application = State()


@router.callback_query(F.data == "request")
async def answer_request(call: CallbackQuery, state: FSMContext):
    await call.message.answer(
        text=(
            "Готовы сотрудничать с нами? Для обратной связи заполните простую форму заявки! Это займет не больше минуты! За оставленную заявку Вас ждет бонус.\n\n"
            "Этапы заполнения заявки:\n\n"
            "1. ФИО: Введите ваше полное имя, чтобы мы могли обращаться к вам лично и корректно обрабатывать Ваш запрос.\n\n"
            "2. Номер телефона: Укажите ваш контактный номер, чтобы мы могли оперативно связаться с вами по Вашему вопросу или заявке.\n\n"
            "3. Цель обращения: Опишите кратко цель или содержание обращения, чтобы мы могли быстро понять суть проблемы или задачи, с которой Вы обратились к нам."
        )
    )
    await state.set_state(Form.waiting_for_application)


@router.message(Form.waiting_for_application)
async def process_application(message: Message, state: FSMContext):
    admin_message = f"Новая заявка:\n\n{message.text}"
    await message.bot.send_message(chat_id=config.ADMIN_USER_ID.get_secret_value(), text=admin_message)
    await message.answer(
        "Спасибо! Запрос передан в разработку. На первый заказ Вам доступен персональный промокод: DAMN15\n\nДостигайте новых высот с командой «DamnIt»!")
    await state.clear()
