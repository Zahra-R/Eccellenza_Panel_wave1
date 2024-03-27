import random
from otree.api import *
import numpy as np
import json
# import scipy.stats as stats



author = 'Zahra Rahmani'
doc = """
Debrief for Sampling
"""


# def truncnorm(lower, upper, mean, std):
#     return stats.truncnorm((lower - mean) / std, (upper - mean) / std, loc=mean, scale=std).rvs()

class C(BaseConstants):
    NAME_IN_URL = 'Goodbye'
    PLAYERS_PER_GROUP = None
    ROUNDS_PER_CONDITION = 1
    NUM_ROUNDS = 1
    

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

#PLAYER FUNCTION 


class Player(BasePlayer):
    pass
  # FUNCTIONS
    





# ---------------------------------------------------------------
# ------------------- PAGES--------------------------------------
#----------------------------------------------------------------


    



class goodbye (Page): 
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.debriefLexi)
    def vars_for_template(player: Player):
       return{
            #Lexicon': player.session.introLexi
            'u': player.participant.label,
            'participantlabel':player.participant.label,
            'Lexicon': player.session.debriefLexi

        } 





page_sequence = [

    goodbye
]
