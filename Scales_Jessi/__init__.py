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
    subsession.session.scalesJessiLexi = Lexicon

# custom function to automatically make likert type fields with 5 options
# custom function to automatically make 4 option fields
def make_options4(label):
        return models.IntegerField(
            choices=[1,2,3,4],
            label=label,
            widget=widgets.RadioSelect,
            )

def make_no_yes(label):
        return models.IntegerField(
            choices=[0,1],
            label=label,
            widget=widgets.RadioSelect,
            )

def make_likert5(label):
        return models.IntegerField(
            choices=[1,2,3,4,5],
            label=label,
            widget=widgets.RadioSelect,
            )

def make_likert7(label):
        return models.IntegerField(
            choices=[1,2,3,4,5,6,7],
            label=label,
            widget=widgets.RadioSelect,
            )

# 9-point likert scale with scaling for biospheric values
def make_likert9(label):
        return models.IntegerField(
            choices=[-1,0,1,2,3,4,5,6,7],
            label=label,
            widget=widgets.RadioSelect,
            )

def make_likert10(label):
        return models.IntegerField(
            choices=[1,2,3,4,5,6,7,8,9,10],
            label=label,
            widget=widgets.RadioSelect,
            )

#region Choices for demographics

def education_choices(player):
    Lexicon = player.session.scalesJessiLexi
    language_code =  player.session.config['language']
    education_choices = []
    if language_code == 'de':
        education_choices = [    
            Lexicon.no_formal,
            Lexicon.obligatory,
            Lexicon.high_school,
            Lexicon.degree,
            Lexicon.doctoral_degree,
            Lexicon.prefer_not_to_say_education,
        ]

    elif language_code == 'zh_hans':
        education_choices = [ 
            Lexicon.no_formal,
            Lexicon.obligatory,
            Lexicon.high_school,
            Lexicon.degree,
            Lexicon.doctoral_degree,
            Lexicon.prefer_not_to_say_education,
            ]
   
    else:
        education_choices = [
            Lexicon.no_formal,
            Lexicon.obligatory,
            Lexicon.high_school,
            Lexicon.degree,
            Lexicon.doctoral_degree,
            Lexicon.prefer_not_to_say_education,
        ]
    return education_choices

def get_party_choices(player):
    party_choices = []
    Lexicon = player.session.scalesJessiLexi
    language_code =  player.session.config['language']
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

def gender_choices(player):
    gender_choices = []
    Lexicon = player.session.scalesJessiLexi
    language_code = player.session.config['language']
    if language_code == 'zh_hans':
        gender_choices = [
            ["female", Lexicon.female],
            ["male", Lexicon.male],
            ["other", Lexicon.other]
        ]
    else:
        gender_choices = [
            ["female", Lexicon.female],
            ["male", Lexicon.male],
            ["diverse", Lexicon.diverse], 
            ["other", Lexicon.other]
        ]
    return gender_choices

def income_choices(player):
    income_choices = []
    Lexicon = player.session.scalesJessiLexi
    language_code = player.session.config['language']
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


def residential_area_choices(player): # ready and checked
    Lexicon = player.session.scalesJessiLexi
    return  [["metropolitan", Lexicon.metropolitan_area], ["suburb", Lexicon.suburban], ["rural", Lexicon.rural]]

#endregion

class Player(BasePlayer):
    ### Climate Change Concern Scale by Tobler et al. 2012
    ccc1 = make_likert5(Lexicon.ccc1Label) ## concern 4 items
    ccc2 = make_likert5(Lexicon.ccc2Label)
    ccc3 = make_likert5(Lexicon.ccc3Label)
    ccc4 = make_likert5(Lexicon.ccc4Label)
    ccc10 = make_likert5(Lexicon.ccc10Label) ## skepticism 7 items
    ccc11 = make_likert5(Lexicon.ccc11Label)
    ccc12 = make_likert5(Lexicon.ccc12Label)
    ccc13 = make_likert5(Lexicon.ccc13Label)
    ccc14 = make_likert5(Lexicon.ccc14Label)
    ccc15 = make_likert5(Lexicon.ccc15Label)
    ccc16 = make_likert5(Lexicon.ccc16Label)

    ### Climate Change Emotions Scale only for jessi pretest
    cce1 = make_likert5(Lexicon.cce1Label) ## Anger
    cce2 = make_likert5(Lexicon.cce2Label) ## Fear/Worry
    cce3 = make_likert5(Lexicon.cce3Label) ## Sadness
    cce4 = make_likert5(Lexicon.cce4Label) ## Joy
    cce5 = make_likert5(Lexicon.cce5Label) ## Curiosity
    cce6 = make_likert5(Lexicon.cce6Label) ## Hope

   

    # Importance of biospheric values van der Linden, 2015  
    ibv1 = make_likert9(Lexicon.ibv1Label)
    ibv2 = make_likert9(Lexicon.ibv2Label)
    ibv3 = make_likert9(Lexicon.ibv3Label)
    ibv4 = make_likert9(Lexicon.ibv4Label)

    # Political Orientation Pennycook et al 2020
    po1 = make_likert5(Lexicon.po1Label)
    po2 = make_likert5(Lexicon.po2Label)

    # Trust in institutions in terms of cc Based on (Pan et al., 2023)
    pit1 = make_likert7(Lexicon.pit1Label)
    pit2 = make_likert7(Lexicon.pit2Label)
    pit3 = make_likert7(Lexicon.pit3Label)
    pit4 = make_likert7(Lexicon.pit4Label)
    pit5 = make_likert7(Lexicon.pit5Label)

    # new knowledge questions Allianz
    cknow1 = models.StringField(
        label = Lexicon.know_1qu,
        choices=[
            Lexicon.know_1a, Lexicon.know_1b,
            Lexicon.know_1c, Lexicon.know_dontknow,
        ], 
        widget=widgets.RadioSelect,
    )
    cknow2 = models.StringField(
        label = Lexicon.know_2qu,
        choices=[
            Lexicon.know_2a, Lexicon.know_2b,
            Lexicon.know_2c, Lexicon.know_dontknow,
        ],
        widget=widgets.RadioSelect,
    )
    cknow3 = models.StringField(
        label = Lexicon.know_3qu,
        choices=[
            Lexicon.know_3a, Lexicon.know_3b,
            Lexicon.know_3c, Lexicon.know_dontknow,
        ],
    )
    cknow4 = models.StringField(
        label = Lexicon.know_4qu,
        choices=[
            Lexicon.know_4a, Lexicon.know_4b,
            Lexicon.know_4c, Lexicon.know_dontknow,
        ],
    )


    cknow5 = models.StringField(
        label = Lexicon.know_5qu,
        choices=[
            Lexicon.know_5a, Lexicon.know_5b,
            Lexicon.know_5c, Lexicon.know_dontknow,
        ],
    )
    cknow6 = models.StringField(
        label = Lexicon.know_6qu,
        choices=[
            Lexicon.know_6a, Lexicon.know_6b,
            Lexicon.know_6c, Lexicon.know_dontknow,
        ],
    )

    cknow8 = models.StringField(
        label = Lexicon.know_8qu,
        choices=[
            Lexicon.know_8a, Lexicon.know_8b,
            Lexicon.know_8c, Lexicon.know_dontknow,
        ],
    )
    cknow9 = models.StringField(
        label = Lexicon.know_3qu,
        choices=[
            Lexicon.know_9a, Lexicon.know_9b,
            Lexicon.know_9c, Lexicon.know_9d , Lexicon.know_dontknow,
        ],
    )
    cknow10 = models.StringField(
        label = Lexicon.know_10qu,
        choices=[
            Lexicon.know_10a, Lexicon.know_10b,
            Lexicon.know_10c, Lexicon.know_10d, Lexicon.know_dontknow,
        ],
    )

    ## Familiar  only pretest Jessi. Ninas quesitons
    fam1 = make_likert7(Lexicon.familiar_label1) 
    fam2 = make_likert7(Lexicon.familiar_label2)
    fam3 = make_likert7(Lexicon.familiar_label3)
    fam4 = make_likert7(Lexicon.familiar_label4)
    fam5 = make_likert7(Lexicon.familiar_label5) 
    fam6 = make_likert7(Lexicon.familiar_label6)
    fam7 = make_likert7(Lexicon.familiar_label7)
    fam8 = make_likert7(Lexicon.familiar_label8)
    fam9 = make_likert7(Lexicon.familiar_label9)

    ## Difficult only pretest Jessi. Ninas quesitons
    diff1 = make_likert7(Lexicon.difficult_label1) 
    diff2 = make_likert7(Lexicon.difficult_label2)
    diff3 = make_likert7(Lexicon.difficult_label3)
    diff4 = make_likert7(Lexicon.difficult_label4)
    diff5 = make_likert7(Lexicon.difficult_label5) 
    diff6 = make_likert7(Lexicon.difficult_label6)
    diff7 = make_likert7(Lexicon.difficult_label7)
    diff8 = make_likert7(Lexicon.difficult_label8)
    diff9 = make_likert7(Lexicon.difficult_label9)

  
  
    ### Demographics
    age = models.IntegerField(
        label=Lexicon.age_label,
        min=18,
    )

    gender = models.StringField(
    label=Lexicon.gender_label,
    choices=get_gender_choices(LANGUAGE_CODE),
    )

    income = models.StringField(
        label=Lexicon.income_label,
        choices=get_income_choices(LANGUAGE_CODE),
    )

    education = models.StringField(
        label=Lexicon.education_label,
        choices=get_education_choices(LANGUAGE_CODE),
    )

    residential_area = models.StringField(
        label=Lexicon.residential_area_label,
        choices=[Lexicon.metropolitan_area, Lexicon.suburban, Lexicon.rural],
    )

    zip_code = models.StringField(
        label=Lexicon.zip_code_label,
        blank=True,
    )

    party_affiliation = models.StringField(
        label=Lexicon.party_affiliation_label,
        choices=get_party_choices(LANGUAGE_CODE),
    )


class CCConcern(Page):
    form_model = 'player'
    form_fields= ['ccc1', 'ccc2', 'ccc3', 'ccc4',  'ccc10', 'ccc11', 'ccc12', 'ccc13', 'ccc14', 'ccc15', 'ccc16'  ]
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)
    
class CCEmotion(Page):
    form_model = 'player'
    form_fields= ['cce1', 'cce2', 'cce3', 'cce4', 'cce5', 'cce6']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)
    
    
    
class CCKnowledge(Page):
    form_model = 'player'
    form_fields= ['cknow1', 'cknow2', 'cknow3', 'cknow4', 'cknow5', 'cknow6','cknow8','cknow9', 'cknow10']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)
    


class IBValues(Page):
    form_model = 'player'
    form_fields= ['ibv1', 'ibv2', 'ibv3', 'ibv4']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)
    
class PolOrientation(Page):
    form_model = 'player'
    form_fields= ['po1', 'po2']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)
    
class PITrust(Page):
    form_model = 'player'
    form_fields= ['pit1', 'pit2', 'pit3', 'pit4', 'pit5']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)
    


    
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'income', 'education', 'residential_area', 'zip_code']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)

class transition (Page): 
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)

class goodbye (Page): 
    form_model = 'player'
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)
    
class Familiar (Page): 
    form_model = 'player'
    form_fields = ['fam1', 'fam2', 'fam3', 'fam4', 'fam5', 'fam6', 'fam7', 'fam8', 'fam9' ]
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)
    
class Difficult (Page): 
    form_model = 'player'
    form_fields = ['diff1', 'diff2', 'diff3', 'diff4', 'diff5', 'diff6', 'diff7', 'diff8', 'diff9' ]
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)
    



# for easier visual adjustments, all scales with long anchors are moved to the beginning of the app. for the original order of scales, see copy below. 
#page_sequence = [IBValues, CCConcern, WVValues, CCConcern, CCEmotionNew, PEfficacy, PolOrientation, PITrust, CCKnowledge ,Demographics]
# copy pf page_sequence with original order of scales 
# page_sequence = [CCConcern, CCEmotionNew, GWNorms, CCKnowledge, CSTrust, PEfficacy, WVValues, IBValues, PolOrientation, PITrust, OVTrust, CRTask, EffCompletion, Demographics]
page_sequence = [ transition, Demographics, CCConcern, IBValues, CCEmotion, Familiar, Difficult, goodbye]