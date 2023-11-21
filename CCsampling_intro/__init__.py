from random import random, seed, choice as random_choice, randint
from otree.api import *
import numpy as np
# import scipy.stats as stats



author = 'Zahra Rahmani'
doc = """
Description Experience Gap with Carbon Externalities
"""


# def truncnorm(lower, upper, mean, std):
#     return stats.truncnorm((lower - mean) / std, (upper - mean) / std, loc=mean, scale=std).rvs()

class C(BaseConstants):
    NAME_IN_URL = 'Sampling_Intro'
    PLAYERS_PER_GROUP = None
    ROUNDS_PER_CONDITION = 1
    NUM_ROUNDS = 1
    GAME_ROUNDS = 15

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
    


class beforeTask(Page):
    form_model='player'
    form_fields = ['range_ccconcern']


page_sequence = [
    Introduction,
    beforeTask
]
