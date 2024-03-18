from random import random, seed, choice as random_choice, randint
from otree.api import *
import numpy as np
# import scipy.stats as stats



author = 'Zahra Rahmani'
doc = """
Description Experience Gap with Carbon Externalities
"""


# this is the dict you should pass to each page in vars_for_template,
# enabling you to do if-statements like {{ if de }} Nein {{ else }} No {{ endif }}


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
    if subsession.session.config['language'] == 'de':
        from .lexicon_de import Lexicon        

    elif subsession.session.config['language'] == 'zh_hans':
        from .lexicon_zh_hans import Lexicon
    else:
        from .lexicon_en import Lexicon  
    subsession.session.samplingIntroLexi = Lexicon



def make_likert_n(n):
    nchoices = list(range(1, n+1))
    return models.IntegerField(
        choices=nchoices,
        widget=widgets.RadioSelect,
)



#PLAYER FUNCTION 
class Player(BasePlayer):
    range_ccconcern = models.IntegerField( min=-100, max=100)
    ### Belief
    belief1Happening= make_likert_n(6)

    beliefHuman1 = make_likert_n(7)
    beliefHuman2 = make_likert_n(7)
    beliefHuman3 = make_likert_n(7)

    beliefConseqences1 = make_likert_n(7)
    beliefConseqences2 = make_likert_n(7)
    beliefConseqences3 = make_likert_n(7)
    beliefConseqences4 = make_likert_n(7)
    block_order = models.IntegerField()
    already_counted = models.BooleanField(initial=False)
   

# ---------------------------------------------------------------
# ------------------- PAGES--------------------------------------
#----------------------------------------------------------------


    
class Introduction(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        return dict(Lexicon = player.session.samplingIntroLexi)


class beforeTask(Page):
    form_model='player'
    form_fields = ['range_ccconcern', 'beliefHuman1', 'beliefHuman2', 'beliefHuman3',
                  'beliefConseqences1', 'beliefConseqences2', 'beliefConseqences3']
    def vars_for_template(player: Player):
        return dict(Lexicon = player.session.samplingIntroLexi)
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.samplingIntroLexi
        return dict(
        form_fields= [ 'beliefHuman1','beliefHuman2', 'beliefHuman3',
                  'beliefConseqences1', 'beliefConseqences2', 'beliefConseqences3'],
        form_field_labels = [ Lexicon.beliefHuman1Label, Lexicon.beliefHuman2Label, Lexicon.beliefHuman3Label, 
                             Lexicon.beliefConseqences1Label, Lexicon.beliefConseqences2Label, Lexicon.beliefConseqences3Label ]
    )
    
class transition (Page): 
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        if player.already_counted == False:
            try: 
                player.participant.task_counter
            except:   
                player.participant.task_counter = 0
            player.participant.task_counter += 1 
            player.block_order = player.participant.task_counter
            player.already_counted = True
        return dict(Lexicon=player.session.samplingIntroLexi,blocknumber = player.block_order, blockaccomplished = player.block_order -1)
    
   

page_sequence = [
    transition,
    Introduction,
    beforeTask
]
