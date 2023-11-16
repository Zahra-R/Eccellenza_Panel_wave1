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



def make_likert5(label):
        return models.IntegerField(
            choices=[1,2,3,4,5],
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
   

class CCConcern(Page):
    form_model = 'player'
    form_fields= ['ccc1', 'ccc2', 'ccc3', 'ccc4',  'ccc10', 'ccc11', 'ccc12', 'ccc13', 'ccc14', 'ccc15', 'ccc16'  ]
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)

page_sequence = [CCConcern]
