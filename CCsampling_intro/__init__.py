from random import random, seed, choice as random_choice, randint
from otree.api import *
import numpy as np
from settings import LANGUAGE_CODE

# import scipy.stats as stats



author = 'Zahra Rahmani'
doc = """
Description Experience Gap with Carbon Externalities
"""

if LANGUAGE_CODE == 'de':
    from .lexicon_de import Lexicon
elif LANGUAGE_CODE == 'zh_hans':
    from .lexicon_zh_hans import Lexicon
else:
    from .lexicon_en import Lexicon


# this is the dict you should pass to each page in vars_for_template,
# enabling you to do if-statements like {{ if de }} Nein {{ else }} No {{ endif }}
which_language = {'en': False, 'de': False, 'zh_hans': False}  # noqa
which_language[LANGUAGE_CODE[:2]] = True

# def truncnorm(lower, upper, mean, std):
#     return stats.truncnorm((lower - mean) / std, (upper - mean) / std, loc=mean, scale=std).rvs()

class C(BaseConstants):
    NAME_IN_URL = 'Sampling_Intro'
    PLAYERS_PER_GROUP = None
    ROUNDS_PER_CONDITION = 1
    NUM_ROUNDS = 1
    GAME_ROUNDS = 10

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass



def creating_session(subsession:Subsession):
    import itertools
    box_labels = itertools.cycle([True, True, False, False])
    for player in subsession.get_players():
        if subsession.round_number == 1: 
            player.participant.telling_box_label = next(box_labels)



#PLAYER FUNCTION 
class Player(BasePlayer):
    range_ccconcern = models.IntegerField( min=-100, max=100)
   



        



# ---------------------------------------------------------------
# ------------------- PAGES--------------------------------------
#----------------------------------------------------------------


    
class Introduction(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)


class beforeTask(Page):
    form_model='player'
    form_fields = ['range_ccconcern']
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)

page_sequence = [
    Introduction,
    beforeTask
]
