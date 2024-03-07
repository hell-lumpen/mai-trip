import asyncio
import re

import aiofiles
from aiogram import types, Router
from aiogram.enums import ParseMode, ContentType
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import Command

import buttons
from aiogram.types import KeyboardButton

import config
from fsm_util import User

router = Router()

main_kb = [
    [
        KeyboardButton(text='Экскурсия по аудиториям'),
        KeyboardButton(text='Ссылки')
    ]
]
main_keyboard = types.ReplyKeyboardMarkup(keyboard=main_kb, resize_keyboard=True)

welcome_message = """
Привет! 👋 <b>Добро пожаловать в бот Института №8 Московского авиационного института!</b> 
Сегодня у нас день открытых дверей, так что держи расписание на сегодняшний день. Не забудь заглянуть на какие-нибудь классные мероприятия, которые тебе нравятся. И, конечно же, зацени <a href=\"https://t.me/pk8mai\">наш телеграм-чат абитуриентов 2024 года</a> - там точно найдешь крутых ребят и всю нужную инфу! 💬✨
"""


async def append_to_file(filename, text):
    try:
        async with aiofiles.open(filename, mode='a') as file:
            await file.write(text + '\n')
    except OSError as e:
        print(f"Error writing to file: {e}")


@router.message(User.email)
async def process_email(message: types.Message, state: FSMContext):
    email = message.text

    if message.from_user.username in config.admin:
        await state.update_data(email='admin@adm.in')
        await message.reply("Вход администратора.")
        await send_welcome_msg(message)
        user_data = str(message.from_user) + ' email=admin@adm.in'
        await append_to_file('users.txt', user_data)
        await state.set_state(User.views)

    elif validate_email(email):
        await state.update_data(email=email)
        await message.reply("Спасибо! Ваша почта успешно сохранена.")
        await send_welcome_msg(message)
        user_data = str(message.from_user) + ' email=' + email
        await append_to_file('users.txt', user_data)

        await state.set_state(User.views)
    else:
        await message.reply("Пожалуйста, введите корректный адрес электронной почты.")


def validate_email(email):
    email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    return re.match(email_regex, email)


@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    config.VIEW_DATA[msg.from_user.username] = {'audience-0': False,
                                                'audience-1': False,
                                                'audience-2': False,
                                                'audience-3': False,
                                                'audience-4': False,
                                                'audience-5': False,
                                                'audience-6': False,
                                                'audience-7': False,
                                                'audience-8': False,
                                                'audience-9': False}

    await state.set_state(User.email_sender)
    await state.update_data(email_sender=True)

    await state.set_state(User.telegram_sender)
    await state.update_data(telegram_sender=True)

    is_admin = 'Введи любой символ.' if msg.from_user.username in config.admin else 'Введите свою почту:'

    await msg.answer(text="""
    Привет! 👋 <b>Добро пожаловать в бот Института №8 Московского авиационного института!</b>
""" + is_admin)
    await state.set_state(User.email)


async def send_welcome_msg(msg):
    await msg.answer_photo(
        caption=welcome_message,
        photo=config.TG_ID_SCHEDULE,
        reply_markup=buttons.get_keyboard_main()
    )


@router.message(Command('result'))
async def get_result(msg: Message, state: FSMContext):
    current_view = config.VIEW_DATA[msg.from_user.username]
    isSuc = True
    for el in current_view.values():
        isSuc = isSuc & el
    if isSuc:
        await msg.answer(
            text='Поздравляю! Ты прошел все локации. Надеюсь тебе понравилось. Можешь подойти за призом к стенду приемной комиссии (рядом с IT-12).',
            parse_mode=None)
    else:
        await msg.answer(text='Ты прошел не все локации!', parse_mode=None)


@router.message(Command('status'))
async def get_status(msg: Message):
    str_status = ''
    if msg.from_user.username in config.admin:
        for user in config.VIEW_DATA:
            str_status += user + "\t" + str(config.VIEW_DATA[user]) + '\n'
    else:
        str_status = 'Недостаточно прав для просмотра'
    await msg.answer(
        text=str_status
    )


@router.callback_query(User.views)
async def set_views(call: CallbackQuery, state: FSMContext):
    views_state = await state.get_data()
    # views_state['views'][call.data] = True
    await state.update_data(views=views_state)

# @router.message(Command('quiz'))
# async def start_quiz(msg: Message, state: FSMContext):
#     await msg.answer_poll(question='question 1', options=['ответ 1', 'ответ 2'], correct_option_id=1, type='quiz')
