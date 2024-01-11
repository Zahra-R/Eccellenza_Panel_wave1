import random
import json

from otree.api import *
from settings import LANGUAGE_CODE


author = 'Zahra Rahmani'


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
    NAME_IN_URL = 'carbon_taxtask'
    PLAYERS_PER_GROUP = None
    payment_per_correct_answer = .1
    NUM_ROUNDS = 12
    if LANGUAGE_CODE == 'de':
        POLICY_COMBINATIONS_TABLE = open('Jessi_carbonTax/Policy_Combinations_Table_de.json')
    else:
        POLICY_COMBINATIONS_TABLE = open('Jessi_carbonTax/Policy_Combinations_Table_en.json')
    PolicyTable = json.load(POLICY_COMBINATIONS_TABLE)['PolicyTable']

    def get_attributes():
        if LANGUAGE_CODE == 'de':
            return ["Sektor", "Preis", "Einnahmenverwendung", "Inkrafttreten"]
        else:
            return ["Sector", "Price", "Revenue mechanism", "Implementation timing"]

    Attributes = get_attributes()


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


#()

class Player(BasePlayer):
    accept = models.IntegerField(choices = [['1', 'yes'], ['2', 'no']])
    vignetteNumber = models.IntegerField(initial= 0)
    order_behavior_types = models.StringField()
    filler_ITI = models.StringField()
   

# FUNCTIONS
# for random order of tasks
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(0, C.NUM_ROUNDS))
            random.shuffle(round_numbers)
            p.participant.task_rounds_J = round_numbers
                
# for this all to work, need to add 'task_rounds' as PARTICIPANT_FIELDS in settings.py!!
# PAGES

class task_page00(Page):

    # 0 is diet, 1 is electricity, 2 is recycling, 3 is regional food, 4 is commute, 5 vacation
    form_model = 'player'
    form_fields = ['accept']
    @staticmethod
    def vars_for_template(player: Player):
        # this determines which vignette
        task_in_round = player.participant.task_rounds_J[player.round_number - 2]
        player.vignetteNumber = task_in_round
        my_vignette_table = C.PolicyTable[task_in_round]
        
        
        # this determines which order within vignette
        random_attribute_order = list(range(0,4))
        random.shuffle(random_attribute_order)
        current_policy_table_shuffled = []
        attributes = C.Attributes
        order_attributes = []
        for i in random_attribute_order:
            current_policy_table_shuffled.append(my_vignette_table[i])
            order_attributes.append(attributes[i])
        player.order_behavior_types = str(order_attributes)
        return {
            "current_policy_table": current_policy_table_shuffled,
            "random_attribute_order": random_attribute_order,
            'Lexicon': Lexicon,
            'which_language': which_language,
            'LANGUAGE_CODE': LANGUAGE_CODE,
            'Attributes' : C.Attributes
        }

class inter_trial(Page):
    form_model = 'player'
    form_fields = ['filler_ITI']
    timeout_seconds = 0.4
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'Lexicon': Lexicon,
            'which_language': which_language,
        }

# Page sequence
page_sequence = [
    task_page00,
    inter_trial 
    ]
