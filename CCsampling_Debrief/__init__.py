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

    ### chinese Tweets
    misinfo_path_zh_hans = "CCsampling/ClimateMisinfo_zh_hans.json"
    with open(misinfo_path_zh_hans, 'r') as j:
        misinfofile_zh_hans = json.loads(j.read())    
    info_path_zh_hans = "CCsampling/ClimateInfo_zh_hans.json"
    with open(info_path_zh_hans, 'r') as j:
        infofile_zh_hans = json.loads(j.read())

    ## all tweets
    infofile_de= infofile_de['CCInfo']
    misinfofile_de= misinfofile_de['CCMisinfo']
    infofile_en= infofile_en['CCInfo']
    misinfofile_en= misinfofile_en['CCMisinfo']
    infofile_zh_hans= infofile_zh_hans['CCInfo']
    misinfofile_zh_hans= misinfofile_zh_hans['CCMisinfo']

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

#PLAYER FUNCTION 


class Player(BasePlayer):
    generalFeedback = models.StringField(max_length=3000, blank=True)
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
            misinfofile = open('CCsampling/ClimateMisinfo_zh_hans.json')
            infofile = open('CCsampling/ClimateInfo_zh_hans.json')
        else:
            misinfofile = open('CCsampling/ClimateMisinfo_en.json')
            infofile = open('CCsampling/ClimateInfo_en.json')
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
    form_fields = ["generalFeedback"]
    @staticmethod
    def vars_for_template(player: Player):
        print("this should be the lixicon")
        return dict(Lexicon=player.session.debriefLexi)



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
    Feedback,
    Debrief, 
    goodbye
]
