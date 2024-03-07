from aiogram.fsm.state import StatesGroup, State


class User(StatesGroup):
    email = State()
    email_sender = State(state=True)
    telegram_sender = State(state=True)
    excursions_view_count = State(state=0)
    correct_answer_count = State(state=0)
    views = State()


class Quiz(StatesGroup):
    q1 = State()
    q2 = State()
    q3 = State()
    q4 = State()
    q5 = State()
