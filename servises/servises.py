from random import choice
from lexicon.lexicon_ru import LEXICON_RU

rps_dict = {
    'rock': LEXICON_RU.rock,
    'paper': LEXICON_RU.paper,
    'scissors': LEXICON_RU.scissors
    }

def get_bot_choice() -> str:
    return choice(list(rps_dict.values()))

#def _normalize_user_answer(user_answer: str) -> str:
#    for key in rps_dict:
#        if rps_dict[key] == user_answer:
#            return key

def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = user_choice
    rules = {LEXICON_RU.rock: LEXICON_RU.scissors,
             LEXICON_RU.scissors: LEXICON_RU.paper,
             LEXICON_RU.paper: LEXICON_RU.rock}
    print(user_choice, bot_choice)
    if user_choice == bot_choice:
        return LEXICON_RU.nobody_won
    elif rules[user_choice] == bot_choice:
        return LEXICON_RU.user_won
    return LEXICON_RU.bot_won