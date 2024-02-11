from random import random, seed, choice as random_choice, randint
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
    NAME_IN_URL = 'Debrief'
    PLAYERS_PER_GROUP = None
    ROUNDS_PER_CONDITION = 1
    NUM_ROUNDS = 1
    ### German Tweets
    misinfo_path_de = "CCsampling/ClimateMisinfo_de.json"
    with open(misinfo_path_de, 'r') as j:
        misinfofile_de = json.loads(j.read())
    info_path_de = "CCsampling/ClimateInfo_de.json"
    with open(info_path_de, 'r') as j:
        infofile_de = json.loads(j.read())
    ### English Tweets
    misinfo_path_en = "CCsampling/ClimateMisinfo_en.json"
    with open(misinfo_path_en, 'r') as j:
        misinfofile_en = json.loads(j.read())    
    info_path_en = "CCsampling/ClimateInfo_en.json"
    with open(info_path_en, 'r') as j:
        infofile_en = json.loads(j.read())

    ## all tweets
    infofile_de= infofile_de['CCInfo']
    misinfofile_de= misinfofile_de['CCMisinfo']
    infofile_en= infofile_en['CCInfo']
    misinfofile_en= misinfofile_en['CCMisinfo']

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

#PLAYER FUNCTION 


class Player(BasePlayer):
    click_debunk = models.BooleanField()
    click_mechanism = models.BooleanField()
    click_ipcc = models.BooleanField()
    click_consequences = models.BooleanField()
  # FUNCTIONS
    

def creating_session(subsession:Subsession):

    if subsession.session.config['language'] == 'de':
        from .lexicon_de import Lexicon       

    elif subsession.session.config['language'] == 'zh_hans':
        from .lexicon_zh_hans import Lexicon
    else:
        from .lexicon_en import Lexicon  
    subsession.session.debriefLexi = Lexicon
    subsession.session.myLangCode = subsession.session.config['language'] 

    import itertools
    reverse_display = itertools.cycle([True, False])
    for player in subsession.get_players():
        if subsession.round_number == 1: 
            player.participant.randomInfoArray = random.sample(range(1,147),C.NUM_ROUNDS)
            player.participant.randomMisinfoArray = random.sample(range(1,79),C.NUM_ROUNDS)
            player.participant.reverseBoxes = next(reverse_display)
            player.participant.seenMisinfo = []
            player.participant.seenMislInfo = []



        



# ---------------------------------------------------------------
# ------------------- PAGES--------------------------------------
#----------------------------------------------------------------


    




    

class Debrief(Page):
    form_model = 'player'
    form_fields = ['click_consequences', 'click_debunk', 'click_ipcc', 'click_mechanism']
    @staticmethod
    def vars_for_template(player: Player):
        import string
        seenM = player.participant.seenMisinfo
        seenMlI = player.participant.seenMislInfo
        if player.session.config['language'] == "de":
            misinfofile = open('CCsampling/ClimateMisinfo_de.json')
            infofile = open('CCsampling/ClimateInfo_de.json')
        elif player.session.config['language'] == "zh_hans":
            misinfofile = open('CCsampling/ClimateMisinfo_en.json')
            infofile = open('CCsampling/ClimateInfo_en.json')
        else:
            misinfofile = open('CCsampling/ClimateMisinfo_en.json')
            infofile = open('CCsampling/ClimateInfo_en.json')
        misinfofile = open('CCsampling/ClimateMisinfo.json')
        infofile = open('CCsampling/ClimateInfo.json')
        misinfo = json.load(misinfofile)['CCMisinfo']
        info = json.load(infofile)['CCInfo']
        seenMstatements = []
        seenMcorrections = []
        for x in seenM:
            #string.replace(old, new, count)
            statementstring = misinfo[x]['finalStatement']
            statementstring =statementstring.replace("'", "´")
            seenMstatements.append(statementstring)
            correctedstring = misinfo[x]['correctedStatement']
            correctedstring = correctedstring.replace("'", "´")
            seenMcorrections.append(correctedstring)
        for x in seenMlI: 
            statementstring = info[x]['finalStatement']
            statementstring =statementstring.replace("'", "´")
            seenMstatements.append(statementstring)
            correctedstring = info[x]['correctedStatement']
            correctedstring = correctedstring.replace("'", "´")
            seenMcorrections.append(correctedstring)
            
        return {
            'seenM': seenM,
            'seenMlI': seenMlI,
            'seenMstatements': seenMstatements,
            'seenMcorrections': seenMcorrections,
            'Lexicon': player.session.debriefLexi
        }

    

class Feedback(Page):
    form_model = 'player'
    form_fields = ["faithful", "use_data", "generalFeedback"]




page_sequence = [
    Feedback,
    Debrief
]
