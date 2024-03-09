import random
import os


from otree.api import *

#from settings import LANGUAGE_CODE
LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE')

#LANGUAGE_CODE = environ.get('LANGUAGE_CODE')

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


if LANGUAGE_CODE == 'de':
    from .lexicon_de import Lexicon
elif LANGUAGE_CODE == 'zh_hans':
    from .lexicon_zh_hans import Lexicon
else:
    from .lexicon_en import Lexicon


# this is the dict you should pass to each page in vars_for_template,
# enabling you to do if-statements like {{ if de }} Nein {{ else }} No {{ endif }}
#which_language = {'en': False, 'de': False, 'zh_hans': False}  # noqa
#which_language[LANGUAGE_CODE[:2]] = True


class C(BaseConstants):
    NAME_IN_URL = 'intro'
    NUM_ROUNDS = 1
    PLAYERS_PER_GROUP = None


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
    subsession.session.introLexi = Lexicon 

    import itertools
    order_tasks = itertools.cycle([1,2,3])
    for player in subsession.get_players():
        if subsession.round_number == 1: 
            player.participant.order_tasks = next(order_tasks)
    

        #region Choices for demographics
# Nina: added gender german at beginning
def education_choices(player):
    Lexicon = player.session.introLexi
    language_code =  player.session.config['language']
    education_choices = []
    if language_code == 'de':
        education_choices = [    
            ["noFormalEducation", Lexicon.no_formal],
            ["obligatory", Lexicon.obligatory],
            ["high_school", Lexicon.high_school],
            ["degree", Lexicon.degree],
            ["doctoral_degree", Lexicon.doctoral_degree]
        ]

    elif language_code == 'zh_hans':
        education_choices = [    
            ["noFormalEducation", Lexicon.no_formal],
            ["obligatory", Lexicon.obligatory],
            ["high_school", Lexicon.high_school],
            ["degree", Lexicon.degree],
            ["doctoral_degree", Lexicon.doctoral_degree]
        ]
   
    else:
        education_choices = [    
            ["noFormalEducation", Lexicon.no_formal],
            ["obligatory", Lexicon.obligatory],
            ["high_school", Lexicon.high_school],
            ["degree", Lexicon.degree],
            ["doctoral_degree", Lexicon.doctoral_degree]
        ]
    return education_choices

def get_party_choices(player):
    party_choices = []
    Lexicon = player.session.introLexi
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
    Lexicon = player.session.introLexi
    language_code = player.session.config['language']
    if language_code == 'de':
        gender_choices = [
            ["female", Lexicon.female],
            ["male", Lexicon.male],
            ["diverse", Lexicon.diverse], 
            ["other", Lexicon.other]
        ]
    elif language_code == 'zh_hans':
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
    Lexicon = player.session.introLexi
    language_code = player.session.config['language']
    if language_code == 'de':
        income_choices = [    
            ["quintile1", Lexicon.income_quintile1],
            ["quintile2", Lexicon.income_quintile2],
            ["quintile3", Lexicon.income_quintile3],
            ["quintile4", Lexicon.income_quintile4],
            ["quintile5", Lexicon.income_quintile5],
            ["NoAnswer", Lexicon.prefer_not_to_say],
        ]
    elif language_code == 'zh_hans':
        income_choices = [    
            ["quintile1", Lexicon.income_quintile1],
            ["quintile2", Lexicon.income_quintile2],
            ["quintile3", Lexicon.income_quintile3],
            ["quintile4", Lexicon.income_quintile4],
            ["quintile5", Lexicon.income_quintile5],
            ["NoAnswer", Lexicon.prefer_not_to_say],
        ]
    else:
        income_choices = [    
            ["quintile1", Lexicon.income_quintile1],
            ["quintile2", Lexicon.income_quintile2],
            ["quintile3", Lexicon.income_quintile3],
            ["quintile4", Lexicon.income_quintile4],
            ["quintile5", Lexicon.income_quintile5],
            ["NoAnswer", Lexicon.prefer_not_to_say],
        ]
    return income_choices


#endregion


class Player(BasePlayer):
    ### Climate Change Concern Scale by Tobler et al. 2012
    dataScience = models.BooleanField(initial=False)
    dataTeach = models.BooleanField(initial=False)
    mobileDevice= models.BooleanField(initial=False, blank=True)


    ### Demographics
    age = models.IntegerField(min=18,max = 99)
    income = models.StringField()
    education = models.StringField()
    gender = models.StringField()
    #party_affiliation = models.StringField(choices=get_party_choices(LANGUAGE_CODE, Lexicon) )


   
   
class Consent(Page):
    form_model = 'player'
    form_fields = ['dataScience', 'dataTeach', 'mobileDevice']
    @staticmethod
    def vars_for_template(player: Player):
        if (player.participant.label == None):
            player.participant.label ="missing"
        
         #insert session links for English
        if(player.session.config['language']=="en"):   
            if(player.participant.order_tasks == 1):
                #insert session link for Order_Nina_Jessi_Zahra
                stringOrder = "http://localhost:8088/join/radobite?participant_label=" + player.participant.label + player.session.myLangCode
            elif(player.participant.order_tasks == 2):
                #insert session link for Order_Jessi_Zahra_Zahra
                stringOrder = "http://localhost:8088/join/radobite?participant_label=" + player.participant.label +  player.session.myLangCode
            else:
                #insert session link for Order_Jessi_Zahra_Nina
                stringOrder = "http://localhost:8088/join/radobite?participant_label=" + player.participant.label + player.session.myLangCode

        #insert session links for German
        if(player.session.config['language']=="de"):   
            if(player.participant.order_tasks == 1):
                #insert session link for Order_Nina_Jessi_Zahra
                stringOrder = "http://localhost:8088/join/venegoza?participant_label=" + player.participant.label + player.session.myLangCode
            elif(player.participant.order_tasks == 2):
                #insert session link for Order_Jessi_Zahra_Zahra
                stringOrder = "http://localhost:8088/join/venegoza?participant_label=" + player.participant.label +  player.session.myLangCode
            else:
                #insert session link for Order_Jessi_Zahra_Nina
                stringOrder = "http://localhost:8088/join/venegoza?participant_label=" + player.participant.label + player.session.myLangCode

        
         #insert session links for Chinese
        if(player.session.config['language']=="zh_hans"):   
            if(player.participant.order_tasks == 1):
                #insert session link for Order_Nina_Jessi_Zahra
                stringOrder = "http://localhost:8888/join/mirutebu?participant_label=" + player.participant.label + player.session.myLangCode
            elif(player.participant.order_tasks == 2):
                #insert session link for Order_Jessi_Zahra_Zahra
                stringOrder = "http://localhost:8888/join/mapedugo?participant_label=" + player.participant.label +  player.session.myLangCode
            else:
                #insert session link for Order_Jessi_Zahra_Nina
                stringOrder = "http://localhost:8888/join/didubahe?participant_label=" + player.participant.label + player.session.myLangCode

        return {
            'stringOrder': stringOrder,
            'Lexicon': player.session.introLexi
        }
    @staticmethod
    def is_displayed(player:Player):
        return (player.session.config['consent_form'] =="redirect")
    

class Consent_Standalone(Page):
    form_model = 'player'
    form_fields = ['dataScience', 'dataTeach', 'mobileDevice']
    @staticmethod
    def vars_for_template(player: Player):
       return{
            #Lexicon': player.session.introLexi
             'Lexicon': Lexicon
        } 
    @staticmethod
    def is_displayed(player:Player):
        return (player.session.config['consent_form'] =="standalone")
    
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'income', 'education']

    @staticmethod
    def vars_for_template(player: Player):
        return{
            #Lexicon': player.session.introLexi
             'Lexicon': Lexicon
        
        } 
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.introLexi
        return dict(
        form_fields = ['age', 'gender', 'income', 'education'],
        form_field_labels = [Lexicon.age_label, Lexicon.gender_label , Lexicon.income_label, Lexicon.education_label]
    )




page_sequence = [Consent, Consent_Standalone, Demographics]
