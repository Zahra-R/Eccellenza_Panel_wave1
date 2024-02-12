from otree.api import *
from os import environ
#from settings import LANGUAGE_CODE
LANGUAGE_CODE = environ.get('LANGUAGE_CODE')

if LANGUAGE_CODE == 'de':
    from .lexicon_de import Lexicon
elif LANGUAGE_CODE == 'zh-hans':
    from .lexicon_zh_hans import Lexicon
else:
    from .lexicon_en import Lexicon

which_language = {'en': False, 'de': False, 'zh_hans': False}  # noqa
which_language[LANGUAGE_CODE[:2]] = True


class C(BaseConstants):
    NAME_IN_URL = 'instructions_carbonTaxtask'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    

    if LANGUAGE_CODE == 'de':
        example_CT = '/static/global/images/task_designCT_de.png'
    elif LANGUAGE_CODE == 'zh-hans':
        example_CT = '/static/global/images/task_designCT_zh_hans.png'
    else:
        example_CT = '/static/global/images/task_designCT_en.png'
    example_CT = example_CT

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # FUNCTIONS
    def make_field_association(label):
        return models.StringField(label=label, blank=True )
    
    #Affective Imagery text fields
    Association1 = models.StringField(label=Lexicon.Association1 )
    Association2 = make_field_association(Lexicon.Association2)
    Association3 = make_field_association(Lexicon.Association3)
    Association4 = make_field_association(Lexicon.Association4)

    def make_field_associationRating(label):
        return models.IntegerField(
        choices = [['1', 'Very negative (1)'],['2', '2'] , ['3', '3'], ['4', '4'] ,
                 ['5', '5'], ['6', '6'] , ['7', 'Very positive (7)']],
        label=label,
        widget=widgets.RadioSelectHorizontal, 
        blank = True
    )
    #Affective Imagery Rating fields
    AssociationRating1 = make_field_associationRating('Here should be the association')
    AssociationRating2 = make_field_associationRating('Here should be the association')
    AssociationRating3 = make_field_associationRating('Here should be the association')
    AssociationRating4 = make_field_associationRating('Here should be the association')
    
    range_party = models.IntegerField( min=-100, max=100)


# PAGES
class instructions_intro(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)

class task_example(Page):
    form_model = 'player'  
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)

class affectiveImagery(Page):
    form_model = 'player'
    form_fields = ['Association1', 'Association2', 'Association3', 'Association4']
    def vars_for_template(player: Player):
        return dict(Lexicon=Lexicon, **which_language)

class ratingAffectiveImagery (Page):
    form_model = 'player'
    form_fields = ['AssociationRating1', 'AssociationRating2', 'AssociationRating3', 'AssociationRating4']
    def vars_for_template(player: Player):
        return{
            'Lexicon': Lexicon,
            'which_language': which_language,
            'ass1': player.Association1,
            'ass2': player.Association2,
            'ass3': player.Association3,
            'ass4': player.Association4,   
        } 

class slider(Page):
    form_model = 'player'
    form_fields = ['range_party']


# Page sequence
page_sequence = [ 
    affectiveImagery,
    ratingAffectiveImagery,
    instructions_intro,
    task_example
]
