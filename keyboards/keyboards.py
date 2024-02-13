from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU


# Клавиатура с ответами согласия или отказа
yes_btn = KeyboardButton(text=LEXICON_RU.yes_button)
no_btn = KeyboardButton(text=LEXICON_RU.no_button)

yes_no_kb_builder = ReplyKeyboardBuilder()

yes_no_kb_builder.row(yes_btn, no_btn, width=2)

yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# Клавиатура для с кнопками камень/ножницы/бумага
rock_btn = KeyboardButton(text=LEXICON_RU.rock)
paper_btn = KeyboardButton(text=LEXICON_RU.paper)
scissors_btn = KeyboardButton(text=LEXICON_RU.scissors)

game_kb_builder = ReplyKeyboardBuilder()

game_kb_builder.row(rock_btn, paper_btn, scissors_btn, width=1)

game_kb: ReplyKeyboardMarkup = game_kb_builder.as_markup(
    resize_keyboard=True
)