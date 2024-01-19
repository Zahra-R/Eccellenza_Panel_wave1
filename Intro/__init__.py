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
    NAME_IN_URL = 'intro'
    NUM_ROUNDS = 1
    PLAYERS_PER_GROUP = None


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ### Climate Change Concern Scale by Tobler et al. 2012
    dataScience = models.BooleanField(initial=False)
    dataTeach = models.BooleanField(initial=False)
    mobileDevice= models.BooleanField(initial=False, blank=True)

def creating_session(subsession:Subsession):
    import itertools
    order_tasks = itertools.cycle([1,2,3])
    for player in subsession.get_players():
        if subsession.round_number == 1: 
            player.participant.order_tasks = next(order_tasks)
   
   


class Consent(Page):
    form_model = 'player'
    form_fields = ['dataScience', 'dataTeach', 'mobileDevice']
    @staticmethod
    def vars_for_template(player: Player):
        if(player.participant.order_tasks == 1):
            #insert session link for Order_Nina_Jessi_Zahra
            stringOrder = "http://localhost:8888/join/popevapa"
        elif(player.participant.order_tasks == 2):
            #insert session link for Order_Jessi_Zahra_Zahra
            stringOrder = "http://localhost:8888/join/mapedugo"
        else:
            #insert session link for Order_Jessi_Zahra_Nina
            stringOrder = "http://localhost:8888/join/didubahe"

        return {
            'stringOrder': stringOrder,
            'Lexicon': Lexicon,
            'which_language': which_language
        }



page_sequence = [Consent]
