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


class C(BaseConstants):
    NAME_IN_URL = 'panel_study'
    NUM_ROUNDS = 1
    PLAYERS_PER_GROUP = None


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


# custom function to automatically make likert type fields with 5 options
def make_likert5(label):
        return models.IntegerField(
            choices=[1,2,3,4,5],
            label=label,
            widget=widgets.RadioSelect,
            )

# custom function to automatically make 4 option fields
def make_options4(label):
        return models.IntegerField(
            choices=[1,2,3,4],
            label=label,
            widget=widgets.RadioSelect,
            )


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

    ### Climate Change Emotions Scale based on Knauf 2022 and Truelove 2012
    cce1 = make_likert5(Lexicon.cce1Label) ## Anger
    cce2 = make_likert5(Lexicon.cce2Label) ## Fear/Worry
    cce3 = make_likert5(Lexicon.cce3Label) ## Sadness
    cce4 = make_likert5(Lexicon.cce4Label) ## Joy
    cce5 = make_likert5(Lexicon.cce5Label) ## Curiosity
    cce6 = make_likert5(Lexicon.cce6Label) ## Hope

    ### Injunctive /descriptive norms for global warming generally (Goldberg et al, 2021)
    gwn1 = make_likert5(Lexicon.gwn1Label) ## injunctive
    gwn2 = make_likert5(Lexicon.gwn2Label) ## descriptive

    ### Climate Change Knowledge by van der Linden 2015
    cck1  = make_options4(Lexicon.cck1Label)
    cck2  = make_options4(Lexicon.cck2Label)
    cck3  = make_options4(Lexicon.cck3Label)
    cck4  = make_options4(Lexicon.cck4Label)
    cck5  = make_options4(Lexicon.cck5Label)
    cck6  = make_options4(Lexicon.cck6Label)
    cck7  = make_options4(Lexicon.cck7Label)
    cck8  = make_options4(Lexicon.cck8Label)
    cck9  = make_options4(Lexicon.cck9Label)
    cck10 = make_options4(Lexicon.cck10Label)
    cck11 = make_options4(Lexicon.cck11Label)
    cck12 = make_options4(Lexicon.cck12Label)
    cck13 = make_options4(Lexicon.cck13Label)
   

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
    
class GWNorms(Page):
    form_model = 'player'
    form_fields= ['gwn1', 'gwn2']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)
    
class CCKnowledge(Page):
    form_model = 'player'
    form_fields= ['cck1', 'cck2', 'cck3', 'cck4',  'cck5', 'cck6', 'cck7', 'cck8', 'cck9', 'cck10', 'cck11', 'cck12', 'cck13']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)


page_sequence = [CCKnowledge, CCConcern, CCEmotion]