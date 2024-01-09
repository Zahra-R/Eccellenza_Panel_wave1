import random
import json

from otree.api import *
from settings import LANGUAGE_CODE

if LANGUAGE_CODE == 'de':
    from .lexicon_de import Lexicon
elif LANGUAGE_CODE == 'zh_hans':
    from .lexicon_zh_hans import Lexicon
else:
    from .lexicon_en import Lexicon

which_language = {'en': False, 'de': False, 'zh_hans': False}  # noqa
which_language[LANGUAGE_CODE[:2]] = True


class C(BaseConstants):
    NAME_IN_URL = 'instructions_task'
    PLAYERS_PER_GROUP = None
    payment_per_correct_answer = .1
    NUM_ROUNDS = 1
    

    if LANGUAGE_CODE == 'de':
        example_pic = '/static/global/images/example_de.png'
    else:
        example_pic = '/static/global/images/example_en.png'
    example_pic = example_pic




class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
   

# FUNCTIONS

# for this all to work, need to add 'task_rounds' as PARTICIPANT_FIELDS in settings.py!!
# PAGES
class instructions(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)
    
class task_example(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)    

# Page sequence
page_sequence = [
  instructions, task_example,  
    ]