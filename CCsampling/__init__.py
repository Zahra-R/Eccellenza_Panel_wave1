import random

from otree.api import *
import numpy as np
import json


author = 'Zahra Rahmani'
doc = """
Sampling Paradigma
"""

# this is the dict you should pass to each page in vars_for_template,
# enabling you to do if-statements like {{ if de }} Nein {{ else }} No {{ endif }}


class C(BaseConstants):
    NAME_IN_URL = 'SAMPLING'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10
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

class Player(BasePlayer):
    boxChoice = models.StringField( choices = ['i', 'm'])
    range_agree = models.IntegerField( min=-100, max=100)
    # range_likelyTrue = models.IntegerField( min=-100, max=100)
    range_ccconcern = models.IntegerField( min=-100, max=100)
    statementText =models.StringField()
    statementID = models.StringField()
    boxlikingInfo = models.IntegerField(choices=[1,2,3,4,5,6,7,8,9],label='How much do you like Box<b> A</b>?', widget = widgets.RadioSelect )
    boxrecommendationInfo = models.IntegerField(choices=[1,2,3,4,5,6,7,8,9],label='Would you follow Box A if it were its own social media channel?',widget = widgets.RadioSelect )
    boxlikingMisinfo = models.IntegerField(choices=[1,2,3,4,5,6,7,8,9],label='How much do you like Box B?' , widget = widgets.RadioSelect)
    boxrecommendationMisinfo = models.IntegerField(choices=[1,2,3,4,5,6,7,8,9],label='Would you follow Box B if it were its own social media channel?',widget = widgets.RadioSelect )
    boxpoliticsMisinfo = models.IntegerField(choices=[1,2,3,4,5,6,7,8,9], widget = widgets.RadioSelect)
    boxpoliticsInfo = models.IntegerField(choices=[1,2,3,4,5,6,7,8,9], widget = widgets.RadioSelect )
    InfohasDebrief = models.BooleanField()
   
    reverseBoxes = models.BooleanField()


    attention_agree = models.IntegerField( min=-100, max=100)
    attention_ccconcern = models.IntegerField( min=-100, max=100)
    attention_boxChoice = models.StringField(choices= ['i', 'm'])


def creating_session(subsession:Subsession):

    if subsession.session.config['language'] == 'de':
        from .lexicon_de import Lexicon       

    elif subsession.session.config['language'] == 'zh_hans':
        from .lexicon_zh_hans import Lexicon
    else:
        from .lexicon_en import Lexicon  
    subsession.session.samplingLexi = Lexicon
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



#----------------------------------------------------------------
#------------------Custum Functions------------------------------------
#----------------------------------------------------------------

def allocateBoxNames(player: Player):
    reversed = player.participant.reverseBoxes
    # if player.round_number % C.ROUNDS_PER_CONDITION == 0:
    likingA = player.boxlikingInfo
    likingB = player.boxlikingMisinfo
    recomA = player.boxrecommendationInfo
    recomB = player.boxrecommendationMisinfo
    if reversed == True:
        player.boxlikingInfo = likingB
        player.boxlikingMisinfo = likingA
        player.boxrecommendationInfo = recomB
        player.boxrecommendationMisinfo = recomA
    print('in make choice again')

def saveParticipantVarsToPlayer(player: Player): 
    player.reverseBoxes = player.participant.reverseBoxes


# ---------------------------------------------------------------
# ------------------- PAGES--------------------------------------
#----------------------------------------------------------------

class sampling(Page):
    form_model = 'player'
    form_fields = ['boxChoice','statementText', 'statementID', 'range_ccconcern', 'range_agree']
    @staticmethod
    def vars_for_template(player: Player):
        round_number = player.round_number
        if player.session.config['language'] == "de":
            misinfofile = C.misinfofile_de
            infofile = C.infofile_de
        elif player.session.config['language'] == "en":
            misinfofile = C.misinfofile_en
            infofile = C.infofile_en
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------are we talking?")
        print(round_number-1)
        print(player.participant.randomMisinfoArray)
        print(misinfofile[player.participant.randomMisinfoArray[round_number-1]])
        MisinfoText = misinfofile[player.participant.randomMisinfoArray[round_number-1]]['finalStatement']
        InfoText = infofile[player.participant.randomInfoArray[round_number-1]]['finalStatement']
        player.InfohasDebrief = True if "correctedStatement" in  infofile[player.participant.randomInfoArray[round_number-1]] else False
        # these are tweetids, we are not submitting them. We only submit the index of the statement in the json file (internal statementID)
        #MisinfoID = misinfo[player.participant.randomMisinfoArray[round_number-1]]['tweetid']
        #InfoID = info[player.participant.randomInfoArray[round_number-1]]['tweetid']
        return {
            'round_number': round_number,
            'randomInfo': player.participant.randomInfoArray[round_number-1],
            'randomMisinfo': player.participant.randomMisinfoArray[round_number-1],
            'reverseBoxes': player.participant.reverseBoxes,
            'MisinfoText': MisinfoText,
            'InfoText': InfoText, 
            'Lexicon': player.session.samplingLexi
        } 
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if(player.boxChoice == "m"):
            player.participant.seenMisinfo.append(player.participant.randomMisinfoArray[player.round_number-1])
        else:
            if(player.InfohasDebrief == True ):
               player.participant.seenMislInfo.append(player.participant.randomInfoArray[player.round_number-1]) 


class sampling_a(Page):
    form_model = 'player'
    form_fields = ['attention_boxChoice', 'attention_ccconcern', 'attention_agree']
    @staticmethod
    def vars_for_template(player: Player):
        round_number = player.round_number
        return {
            'round_number': round_number,
            'reverseBoxes': player.participant.reverseBoxes,
            'Lexicon': player.session.samplingLexi
        } 
    @staticmethod
    def is_displayed(player: Player):
        return (player.round_number == 3)
   


class boxrating(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        if player.round_number == C.NUM_ROUNDS:
            return ['boxlikingInfo', 'boxrecommendationInfo', 'boxlikingMisinfo', 'boxrecommendationMisinfo', 'boxpoliticsInfo', 'boxpoliticsMisinfo' ]
        else:
            return ['boxlikingInfo', 'boxrecommendationInfo', 'boxlikingMisinfo', 'boxrecommendationMisinfo' ]
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'round_number': player.round_number,
            'Lexicon': player.session.samplingLexi
        }
    @staticmethod
    def is_displayed(player: Player):
        return (player.round_number % 5 == 0)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        print('in before next page function', player.boxlikingInfo, player.boxlikingMisinfo, player.boxrecommendationInfo, player.boxrecommendationMisinfo )
        allocateBoxNames(player)
        if (player.round_number % C.NUM_ROUNDS == 0):
            saveParticipantVarsToPlayer(player)




page_sequence = [
    sampling, sampling_a, boxrating
]
