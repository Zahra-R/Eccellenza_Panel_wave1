import random

from otree.api import *
from settings import LANGUAGE_CODE


doc = """
How to translate an app to multiple languages (e.g. English and German).

There are 2 ways to define localizable strings:
(1) Put it in a "lexicon" file (see lexicon_en.py, lexicon_de.py).
    This is the easiest technique, and it allows you to easily reuse the same string multiple times.
(2) If the string contains variables, then it should to be defined in the template.
    Use an if-statement, like {{ if de }} Nein {{ else }} No {{ endif }}

When you change the LANGUAGE_CODE in settings.py, the language will automatically be changed.

Note: this technique does not require .po files, which are a more complex technique.    
"""


class C(BaseConstants):
    NAME_IN_URL = 'panel_study'
    NUM_ROUNDS = 1
    PLAYERS_PER_GROUP = None

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
    subsession.session.myLexicon = Lexicon


# custom function to automatically make likert type fields with 5 options
# custom function to automatically make 4 option fields
def make_likert7():
    return models.IntegerField(
        choices=[1,2,3,4,5,6,7],
            widget=widgets.RadioSelect,
    )

def make_likert10():
        return models.IntegerField(
            choices=[1,2,3,4,5,6,7,8,9,10],
            widget=widgets.RadioSelect,
        )
def get_education_choices(language_code):
    education_choices = []
    if language_code == 'de':
        education_choices = [    
            Lexicon.no_formal_education,
            Lexicon.elementary_school,
            Lexicon.secondary_school,
            Lexicon.higher_secondary_school,
            Lexicon.vocational_training,
            Lexicon.high_school,
            Lexicon.college_degree,
            Lexicon.master_degree,
            Lexicon.doctoral_degree,
            Lexicon.prefer_not_to_say_education
        ]
    elif language_code == 'zh_hans':
        education_choices = [
            Lexicon.education_label, 
            Lexicon.high_school,
            Lexicon.vocational_education,
            Lexicon.some_college, 
            Lexicon.bachelors_degree,
            Lexicon.masters_degree,
            Lexicon.doctoral_degree
            Lexicon.education_label, 
            Lexicon.high_school,
            Lexicon.vocational_education,
            Lexicon.some_college, 
            Lexicon.bachelors_degree,
            Lexicon.masters_degree,
            Lexicon.doctoral_degree
        ]
    else:
        education_choices = [
            Lexicon.high_school,
            Lexicon.some_college,
            Lexicon.bachelors_degree,
            Lexicon.masters_degree,
            Lexicon.doctoral_degree,
        ]
    return education_choices


def get_party_choices(language_code):
    party_choices = []
    if language_code == 'de':
        party_choices = [    
            Lexicon.cdcsu,
            Lexicon.spd,
            Lexicon.gruene,
            Lexicon.fdp,
            Lexicon.linke,
            Lexicon.afd,
            Lexicon.other_party
        ]
    elif language_code == 'zh_hans':
        party_choices = [
            # Add choices for Chinese language if needed
        ]
    else:
        party_choices = [
            Lexicon.republicans, 
            Lexicon.democrats, 
            Lexicon.independent_party, 
            Lexicon.other_party
        ]
    return party_choices

def get_gender_choices(language_code):
    gender_choices = []
    if language_code == 'de':
        party_choices = [    
            Lexicon.female,
            Lexicon.male,
            Lexicon.diverse, 
            Lexicon.other
        ]
    elif language_code == 'zh_hans':
        gender_choices = [
            Lexicon.female,
            Lexicon.male,
            Lexicon.other
        ]
    else:
        gender_choices = [
            Lexicon.female,
            Lexicon.male,
            Lexicon.diverse, 
            Lexicon.other
        ]
    return gender_choices

def get_income_choices(language_code, session):
    income_choices = []
    Lexicon = session.myLexicon
    if language_code == 'de':
        income_choices = [    
            Lexicon.income_label,
            Lexicon.income_less_than_A,
            Lexicon.income_A_to_B,
            Lexicon.income_B_to_C,
            Lexicon.income_C_to_D,
            Lexicon.income_more_than_D,
            Lexicon.prefer_not_to_say
        ]
    elif language_code == 'zh_hans':
        income_choices = [
            Lexicon.income_label,
            Lexicon.income_less_than_A,
            Lexicon.income_A_to_B,
            Lexicon.income_B_to_C,
            Lexicon.income_C_to_D,
            Lexicon.income_D_to_E,
            Lexicon.income_more_than_E,
            Lexicon.prefer_not_to_say
        ]
    else:
        income_choices = [
            Lexicon.income_label,
            Lexicon.income_less_than_A,
            Lexicon.income_A_to_B,
            Lexicon.income_B_to_C,
            Lexicon.income_C_to_D,
            Lexicon.income_more_than_D,
            Lexicon.prefer_not_to_say
        ]
    return income_choices


#region
def cknow1_choices(player):
    Lexicon = player.session.myLexicon
    return [
    ['a_false', Lexicon.know_1a],
    ['b_true',  Lexicon.know_1b],
    ['c_false', Lexicon.know_1c],
    ['dk',  Lexicon.dont_know],
]


def cknow2_choices(player):
    Lexicon = player.session.myLexicon
    return [
    ['a_false', Lexicon.know_2a],
    ['b_false',  Lexicon.know_2b],
    ['c_true', Lexicon.know_2c],
    ['dk',  Lexicon.dont_know],
]


def cknow3_choices(player):
    Lexicon = player.session.myLexicon
    return [
    ['a_true', Lexicon.know_3a],
    ['b_false',  Lexicon.know_3b],
    ['c_false', Lexicon.know_3c],
    ['dk',  Lexicon.dont_know],
]

def cknow4_choices(player):
    Lexicon = player.session.myLexicon
    return [
    ['a_false', Lexicon.know_4a],
    ['b_true',  Lexicon.know_4b],
    ['c_false', Lexicon.know_4c],
    ['dk',  Lexicon.dont_know],
]

def cknow5_choices(player):
    Lexicon = player.session.myLexicon
    return [
    ['a_false', Lexicon.know_5a],
    ['b_true',  Lexicon.know_5b],
    ['c_false', Lexicon.know_5c],
    ['dk',  Lexicon.dont_know],
]

def cknow6_choices(player):
    Lexicon = player.session.myLexicon
    return [
    ['a_false', Lexicon.know_6a],
    ['b_false',  Lexicon.know_6b],
    ['c_true', Lexicon.know_6c],
    ['dk',  Lexicon.dont_know],
]

def cknow8_choices(player):
    Lexicon = player.session.myLexicon
    return [
    ['a_true', Lexicon.know_8a],
    ['b_false',  Lexicon.know_8b],
    ['c_false', Lexicon.know_8c],
    ['dk',  Lexicon.dont_know],
]

def cknow9_choices(player):
    Lexicon = player.session.myLexicon
    return [
    ['a_true', Lexicon.know_9a],
    ['b_false',  Lexicon.know_9b],
    ['c_false', Lexicon.know_9c],
    ['d_false',  Lexicon.know_9d],
    ['dk',  Lexicon.dont_know],
]

def cknow10_choices(player):
    Lexicon = player.session.myLexicon
    return [
    ['a_false', Lexicon.know_10a],
    ['b_true',  Lexicon.know_10b],
    ['c_false', Lexicon.know_10c],
    ['d_false',  Lexicon.know_10d],
    ['dk',  Lexicon.dont_know],
]

#endregion

class Player(BasePlayer):
    ### Climate Change Concern Scale by Tobler et al. 2012
  
    ### Climate Change Emotions Scale based on Knauf 2022 and Truelove 2012
    emoAng1 = make_likert10() ## Anger
    emoAng2 = make_likert10() ## Anger
    emoAng3 = make_likert10() ## Anger
    emoSad1 = make_likert10() ## Sadness
    emoSad2 = make_likert10() ## Sadness
    emoSad3 = make_likert10() ## Sadness
    emoFear1 = make_likert10() ## Fear/Worry
    emoFear2 = make_likert10() ## Fear/Worry
    emoFear3 = make_likert10() ## Fear/Worry
    emoHope1 = make_likert10() ## Hope
    emoHope2 = make_likert10() ## Hope
    emoHope3 = make_likert10() ## Hope
    emoGuilt1 = make_likert10() ## guilt
    emoGuilt2 = make_likert10() ## guilt
    emoGuilt3 = make_likert10() ## guilt

    # new knowledge questions Allianz
    cknow1 = models.StringField( choices=["a_false", "b_true", "c_false", "dk"], widget=widgets.RadioSelect)
    cknow2 = models.StringField(choices=["a_false", "b_false", "c_true", "dk"], widget=widgets.RadioSelect)
    cknow3 = models.StringField(choices=["a_true", "b_false", "c_false", "dk"], widget=widgets.RadioSelect,)
    cknow4 = models.StringField(choices=["a_false", "b_true", "c_false", "dk"], widget=widgets.RadioSelect,)  
    cknow5 = models.StringField(choices=["a_false", "b_true", "c_false", "dk"], widget=widgets.RadioSelect,)     
    cknow6 = models.StringField(choices=["a_false", "b_false", "c_true", "dk"], widget=widgets.RadioSelect,) 
    cknow8 = models.StringField(choices=["a_true", "b_false", "c_false", "dk"], widget=widgets.RadioSelect,)     
    cknow9 = models.StringField(choices=["a_true", "b_false", "c_false", "d_false", "dk"], widget=widgets.RadioSelect,)     
    cknow10 = models.StringField(choices=["a_false", "b_true", "c_false", "d_false", "dk"], widget=widgets.RadioSelect,)

    # Worldviews and values - Hierarchy-Egalitarianism & Individualism-Communitarianism  
    hie1 = make_likert10()
    hie2 = make_likert10()
    hie3 = make_likert10()
    ind1 = make_likert10()
    ind2 = make_likert10()
    ind3 = make_likert10()

    ### Demographics
    age = models.IntegerField(min=18,max = 99)
    income = models.StringField(    )
    #education = models.StringField(choices=get_education_choices(LANGUAGE_CODE, Lexicon) )
    #residential_area = models.StringField(choices=[Lexicon.metropolitan_area, Lexicon.suburban, Lexicon.rural] )
    #zip_code = models.StringField( blank=True)
    #party_affiliation = models.StringField(choices=get_party_choices(LANGUAGE_CODE, Lexicon) )


class CCConcern(Page):
    form_model = 'player'
    form_fields= ['ccc1', 'ccc2', 'ccc3', 'ccc4',  'ccc10', 'ccc11', 'ccc12', 'ccc13', 'ccc14', 'ccc15', 'ccc16'  ]
    print(form_fields[0])
    @staticmethod
    def vars_for_template(player: Player):
        #player.formfields.ccc1.label="test"
        return dict(Lexicon=player.session.myLexicon)
    

class CCEmotionNew(Page):
    form_model = 'player'
    form_fields= ['emoAng1', 'emoAng2', 'emoAng3', 'emoSad1','emoSad2', 'emoSad3', 'emoFear1', 'emoFear2', 'emoFear3', 'emoHope1', 'emoHope2', 'emoHope3', 'emoGuilt1', 'emoGuilt2', 'emoGuilt3']
    @staticmethod
    def vars_for_template(player: Player):
        return{
            'Lexicon': player.session.myLexicon
        } 
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.myLexicon
        return dict(
        form_fields = ['emoAng1', 'emoAng2', 'emoAng3', 'emoSad1','emoSad2', 'emoSad3', 'emoFear1', 'emoFear2', 'emoFear3', 'emoHope1', 'emoHope2', 'emoHope3', 'emoGuilt1', 'emoGuilt2', 'emoGuilt3'],
        form_field_labels = [Lexicon.emoAng1Label, Lexicon.emoAng2Label , Lexicon.emoAng3Label, Lexicon.emoSad1Label,Lexicon.emoSad2Label, Lexicon.emoSad3Label,  Lexicon.emoFear1Label , Lexicon.emoFear2Label , Lexicon.emoFear3Label, Lexicon.emoHope1Label , Lexicon.emoHope2Label , Lexicon.emoHope3Label , Lexicon.emoGuilt1Label, Lexicon.emoGuilt2Label, Lexicon.emoGuilt3Label]
    )
    
    
class CCKnowledge(Page):
    form_model = 'player'
    form_fields= ['cknow1', 'cknow2', 'cknow3', 'cknow4', 'cknow5', 'cknow6','cknow8','cknow9', 'cknow10']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.myLexicon)
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.myLexicon
        return dict(
        form_fields= ['cknow1', 'cknow2', 'cknow3', 'cknow4', 'cknow5', 'cknow6','cknow8','cknow9', 'cknow10'],
        form_field_labels = [Lexicon.know_1qu, Lexicon.know_2qu, Lexicon.know_3qu, Lexicon.know_4qu, Lexicon.know_5qu, Lexicon.know_6qu,  Lexicon.know_8qu, Lexicon.know_9qu, Lexicon.know_10qu]
    )
    

class PEfficacy(Page):
    form_model = 'player'
    form_fields= ['pe1' ]
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.myLexicon)
    
class WVValues(Page):
    form_model = 'player'
    form_fields= ['hie1', 'hie2', 'hie3', 'ind1', 'ind2', 'ind3']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.myLexicon)
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.myLexicon
        return dict(
        form_fields= ['hie1', 'hie2', 'hie3', 'ind1', 'ind2', 'ind3'],
        form_field_labels = [Lexicon.hie1Label, Lexicon.hie2Label , Lexicon.hie3Label, Lexicon.ind1Label,Lexicon.ind2Label, Lexicon.ind3Label]
    )

class IBValues(Page):
    form_model = 'player'
    form_fields= ['ibv1', 'ibv2', 'ibv3', 'ibv4']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.myLexicon)
    
class PolOrientation(Page):
    form_model = 'player'
    form_fields= ['po1', 'po2']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.myLexicon)
    
class PITrust(Page):
    form_model = 'player'
    form_fields= ['pit1', 'pit2', 'pit3', 'pit4', 'pit5']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.myLexicon)
        
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'income', 'education', 'residential_area', 'zip_code']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.myLexicon)

class transition (Page): 
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.myLexicon)

class goodbye (Page): 
    form_model = 'player'
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.myLexicon)


# for easier visual adjustments, all scales with long anchors are moved to the beginning of the app. for the original order of scales, see copy below. 
#page_sequence = [IBValues, CCConcern, WVValues, CCConcern, CCEmotionNew, PEfficacy, PolOrientation, PITrust, CCKnowledge ,Demographics]
# copy pf page_sequence with original order of scales 
# page_sequence = [CCConcern, CCEmotion, GWNorms, CCKnowledge, CSTrust, PEfficacy, WVValues, IBValues, PolOrientation, PITrust, OVTrust, CRTask, EffCompletion, Demographics]
#page_sequence = [transition, CCConcern, IBValues, CCEmotion, Demographics, goodbye]
page_sequence = [CCKnowledge, WVValues, CCEmotion]