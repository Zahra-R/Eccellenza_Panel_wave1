
import random

from otree.api import *

from settings import LANGUAGE_CODE

if LANGUAGE_CODE == 'de':
    from .lexicon_de import Lexicon
elif LANGUAGE_CODE == 'zh_hans':
    from .lexicon_zh_hans import Lexicon
else:
    from .lexicon_en import Lexicon

which_language = {'en': False, 'de': False, 'zh_hans': False}  # noqa
which_language[LANGUAGE_CODE[:2]] = True


class C(BaseConstants):
    NAME_IN_URL = 'carbon_footprint_assessment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

 # functions to generate education and party choices based on language
def make_options8(label):
        return models.StringField(
            choices=[    
            Lexicon.food_overall_A,
            Lexicon.food_overall_B,
            Lexicon.food_overall_C,
            Lexicon.food_overall_D,
            Lexicon.food_overall_E,
            Lexicon.food_overall_F,
            Lexicon.food_overall_G,
            Lexicon.food_overall_H],
            label=label,
            widget=widgets.RadioSelect,
            )

    
class Player(BasePlayer):


    footprint_food_overall1 = make_options8(Lexicon.food_overall_label1)
    footprint_food_overall2 = make_options8(Lexicon.food_overall_label2)
    footprint_food_overall3 = make_options8(Lexicon.food_overall_label3)
    footprint_food_overall4 = make_options8(Lexicon.food_overall_label4)
    footprint_food_overall5 = make_options8(Lexicon.food_overall_label5)


    footprint_regional = models.StringField(
        label = Lexicon.regional_label,
        choices=[
            Lexicon.regional_less_than ,
            Lexicon.regional_quarter,
            Lexicon.regional_half ,
            Lexicon.regional_3_quarter ,
            Lexicon.regional_more_than ,
        ],
    )
    
    footprint_food_dairy = models.StringField(
        label = Lexicon.food_dairy_label,
        choices=[ 
            Lexicon.food_dairy_less_than_A ,Lexicon.food_dairy_A_to_B,
            Lexicon.food_dairy_B_to_C ,Lexicon.food_dairy_C_to_D ,
            Lexicon.food_dairy_D_to_E ,Lexicon.food_dairy_more_than_E,
        ],
    )

    footprint_food_meat = models.StringField(
        label = Lexicon.food_meat_label,
        choices=[ 
            Lexicon.food_meat_less_than_A ,Lexicon.food_meat_A_to_B,
            Lexicon.food_meat_B_to_C ,Lexicon.food_meat_C_to_D ,
            Lexicon.food_meat_D_to_E ,Lexicon.food_meat_more_than_E,
        ],
    )
    
    footprint_flying_short = models.IntegerField(
        label= Lexicon.flying_short_label,
        min=0, max= 300
    )
    footprint_flying_mid = models.IntegerField(
        label= Lexicon.flying_mid_label,
        min=0, max= 300
    )
    footprint_flying_long = models.IntegerField(
        label= Lexicon.flying_long_label,
        min=0, max= 300
    )

    
    footprint_electricity = models.StringField(
        label = Lexicon.electricity_label,
        choices=[
            Lexicon.electricity_D, Lexicon.electricity_C,
            Lexicon.electricity_B, Lexicon.electricity_A  ,
        ],
    )
    footprint_commute_car = models.StringField(
        label = Lexicon.commute_car_label,
        choices=[
            Lexicon.commute_car_never, Lexicon.commute_car_less_than_A,
            Lexicon.commute_car_A_to_B, Lexicon.commute_car_B_to_C  ,
            Lexicon.commute_car_C_to_D  ,Lexicon.commute_car_more_than_D ,
        ],
    )

    footprint_commute_car_type = models.StringField(
        label = Lexicon.commute_car_type_label,
        choices=[
            Lexicon.commute_car_type_none, Lexicon.commute_car_type_A,
            Lexicon.commute_car_type_B, Lexicon.commute_car_type_C  ,
            Lexicon.commute_car_type_D  ,Lexicon.commute_car_type_E ,
        ],
    )

    
    footprint_commute_pt = models.StringField(
        label = Lexicon.commute_pt_label,
        choices=[
            Lexicon.commute_pt_less_than_A, Lexicon.commute_pt_A_to_B,
            Lexicon.commute_pt_B_to_C, Lexicon.commute_pt_C_to_D  ,
            Lexicon.commute_pt_D_to_E  ,Lexicon.commute_pt_more_than_E,
        ],
    )

# FUNCTIONS



# PAGES

class questions_footprint_1(Page):
    form_model = 'player'
    form_fields = [ 'footprint_commute_car' ,'footprint_commute_car_type', 'footprint_commute_pt', 
                    'footprint_regional'
                #  , 'footprint_food_dairy', 'footprint_food_meat'
                  ]
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)
    
class questions_footprint_food(Page):
    form_model = 'player'
    form_fields = [ 'footprint_food_overall1' ,'footprint_food_overall2', 'footprint_food_overall3', 
                   'footprint_food_overall4',  'footprint_food_overall5'
              
                  ]
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)

class questions_footprint_2(Page):
    form_model = 'player'
    form_fields = ['footprint_electricity',
                    'footprint_flying_short', 'footprint_flying_mid', 'footprint_flying_long', 
                  ]
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)

# Page sequence
page_sequence = [
    questions_footprint_food, questions_footprint_1, questions_footprint_2
    
]




