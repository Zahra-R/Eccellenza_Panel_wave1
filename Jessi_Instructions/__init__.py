import random
import os


from otree.api import *

#from settings import LANGUAGE_CODE
#LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE')

#LANGUAGE_CODE = environ.get('LANGUAGE_CODE')




class C(BaseConstants):
    NAME_IN_URL = 'instructions_carbonTaxtask'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
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
    subsession.session.JessiIntroLexi = Lexicon 

class Group(BaseGroup):
    pass


def aboutWhat_choices(player): 
    Lexicon = player.session.JessiIntroLexi 
    return [
    ['tourism_false', Lexicon.about_a],
    ['true',  Lexicon.about_b],
    ['washingMachine_false', Lexicon.about_c],
    ['spicy_false',  Lexicon.about_d]
]


class Player(BasePlayer):
    # FUNCTIONS
    def make_field_association(label):
        return models.StringField( blank=True )
    
    #Affective Imagery text fields
    Association1 = models.StringField(  )
    Association2 = models.StringField( blank=True )
    Association3 = models.StringField(blank=True )
    Association4 = models.StringField( blank=True )

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
    block_order = models.IntegerField()
    already_counted = models.BooleanField(initial=False)

    aboutWhat = models.StringField()
    screenoutAboutWhat = models.BooleanField(initial= False)


# PAGES
class transition (Page): 
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        if player.already_counted == False:
            try: 
                player.participant.task_counter
            except:   
                player.participant.task_counter = 0
            player.participant.task_counter += 1 
            player.block_order = player.participant.task_counter
            player.already_counted = True
        return dict(Lexicon=player.session.JessiIntroLexi, blocknumber = player.block_order, blockaccomplished = player.block_order -1)
    
    
class instructions_intro(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        return{
            'Lexicon': player.session.JessiIntroLexi
        } 

class task_example(Page):
    form_model = 'player'  
    @staticmethod
    def vars_for_template(player: Player):
        return{
            'Lexicon': player.session.JessiIntroLexi
        } 

class affectiveImagery(Page):
    form_model = 'player'
    form_fields = ['Association1', 'Association2', 'Association3', 'Association4']
    @staticmethod
    def vars_for_template(player: Player):
        return{
            'Lexicon': player.session.JessiIntroLexi
        } 
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.JessiIntroLexi
        return dict(
        form_fields = ['Association1', 'Association2', 'Association3', 'Association4'] ,
        form_field_labels = [Lexicon.Association1, Lexicon.Association2, Lexicon.Association3, Lexicon.Association4 ]
    )

class ratingAffectiveImagery (Page):
    form_model = 'player'
    form_fields = ['AssociationRating1', 'AssociationRating2', 'AssociationRating3', 'AssociationRating4']

    @staticmethod
    def vars_for_template(player: Player):
        return{
            'Lexicon': player.session.JessiIntroLexi
        } 
    @staticmethod
    def js_vars(player):
        Lexicon = player.session.JessiIntroLexi
        return dict(
        form_fields = ['AssociationRating1', 'AssociationRating2', 'AssociationRating3', 'AssociationRating4'] ,
        form_field_labels = [Lexicon.Instructions_rating ]
    )


class slider(Page):
    form_model = 'player'
    form_fields = ['range_party']

class interlude (Page): 
    form_model = 'player'
    form_fields = ['aboutWhat']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(Lexicon=player.session.JessiIntroLexi)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if(player.aboutWhat != "true" ):
               player.screenoutAboutWhat = True
    @staticmethod
    def is_displayed(player: Player):
        return (player.participant.task_counter == 1)
    

class Screenout(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        return{
             'Lexicon': player.session.JessiIntroLexi
        } 
    @staticmethod
    def is_displayed(player: Player):
        return (player.screenoutAboutWhat)
   
    
   


# Page sequence
page_sequence = [ 
    transition,
    affectiveImagery,
    ratingAffectiveImagery,
    instructions_intro,
    task_example, 
    interlude, 
    Screenout
]
