import random
import json

from otree.api import *
from settings import LANGUAGE_CODE


class C(BaseConstants):
    NAME_IN_URL = 'instructions_task'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

def creating_session(subsession:Subsession):
    
    if subsession.session.config['language'] == 'de':
        from .lexicon_de import Lexicon
        subsession.session.myLangCode = "_de"
    elif subsession.session.config['language'] == 'zh_hans':
        from .lexicon_zh_hans import Lexicon
        subsession.session.myLangCode = "_ch"
    else:
        from .lexicon_en import Lexicon
        subsession.session.myLangCode = "_en"
    subsession.session.introNinaLexi = Lexicon 


    import itertools
    order_tasks = itertools.cycle([1,2,3])
    for player in subsession.get_players():
        if subsession.round_number == 1: 
            player.participant.order_tasks = next(order_tasks)

class Player(BasePlayer):
    pass
   

# FUNCTIONS

# for this all to work, need to add 'task_rounds' as PARTICIPANT_FIELDS in settings.py!!
# PAGES
class transition(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.introNinaLexi) 
   
    
class instructions(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.introNinaLexi)
   
    
class task_example(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.introNinaLexi)
        

# Page sequence
page_sequence = [ transition,
                  instructions, 
                  task_example]