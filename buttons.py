from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import room


def get_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Идентификатор Чата', callback_data='navigation_chat')
    keyboard_builder.button(text='Идентификатор Пользователя', callback_data='navigation_user')

    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()


def get_keyboard_nav(index=0):
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text=room[index - 1], callback_data=f'audience-{(index + 9) % 10}')
    keyboard_builder.button(text=room[(index + 1) % 10], callback_data=f'audience-{(index + 1) % 10}')
    keyboard_builder.adjust(2)
    keyboard_builder.button(text='Главное меню', callback_data=f'main')
    keyboard_builder.button(text='Список всех локаций', callback_data=f'all_audience')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()


def get_keyboard_all_audience(index=0):
    keyboard_builder = InlineKeyboardBuilder()
    for i in range(2):
        keyboard_builder.button(text=room[index], callback_data=f'audience-{index}')
        index += 1
        index %= 10
    keyboard_builder.adjust(2)
    for i in range(2):
        keyboard_builder.button(text=room[index], callback_data=f'audience-{index}')
        index += 1
        index %= 10
    keyboard_builder.adjust(2)

    keyboard_builder.button(text='↩ Назад', callback_data=f'page_aud-{(index + 4) % 10}')
    keyboard_builder.button(text='Вперед ↪', callback_data=f'page_aud-{index % 10}')
    keyboard_builder.button(text='≣ Главное меню', callback_data=f'main')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()


def get_keyboard_main():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Экскурсия по IT-этажу', callback_data=f'all_audience')
    keyboard_builder.button(text='Наши контакты', callback_data=f'contact')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def get_keyboard_contact():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Главное меню', callback_data=f'main')
    keyboard_builder.button(text='Экскурсия по этажу', callback_data=f'all_audience')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
