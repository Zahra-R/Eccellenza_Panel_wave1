from os import environ

SESSION_CONFIGS = [
     dict(
         name='Intro_Redirection',
  #      app_sequence=['survey','task'],
         app_sequence=['Intro'],
         consent_form="redirect",
         num_demo_participants=10,
     ),
     dict(
         name='Order_Nina_Jessi_Zahra',
  #      app_sequence=['survey','task'],
         app_sequence=['Nina_footprint_calculator', 'Nina_instructions', 'Nina_carbontask', 'Jessi_Instructions',  'Jessi_carbonTax','CCsampling_intro', 'CCsampling',],

         num_demo_participants=10,
     ),
      dict(
         name='Order_Jessi_Zahra_Nina',
  #      app_sequence=['survey','task'],
         app_sequence=['Jessi_Instructions',  'Jessi_carbonTax','CCsampling_intro', 'CCsampling','Nina_footprint_calculator', 'Nina_instructions', 'Nina_carbontask'],

         num_demo_participants=10,
     ),
      dict(
         name='Order_Zahra_Nina_Jessi',
  #      app_sequence=['survey','task'],
         app_sequence=['CCsampling_intro', 'CCsampling','Nina_footprint_calculator', 'Nina_instructions', 'Nina_carbontask', 'Jessi_Instructions',  'Jessi_carbonTax'],
         language = "de",
         num_demo_participants=10,
     ),
    dict(
         name='first_draft_Panel_scales_pure',
  #      app_sequence=['survey','task'],
         app_sequence=['Scales'],

         num_demo_participants=10,
     ),
       dict(
        name='first_draft_Panel_withSampling',
        app_sequence=['Intro','CCsampling_intro', 'CCsampling', 'Scales'],
        num_demo_participants=5,
        consent_form="standalone"
    ),
        dict(
         name='first_draft_NinasPart',
         #app_sequence=[ 'Nina_survey', 'Nina_carbontask', 'Nina_footprint_calculator', 'Nina_questionnaire'],
         app_sequence= ['Nina_footprint_calculator', 'Nina_instructions', 'Nina_carbontask'],
         num_demo_participants=10,
     ),
        dict(
         name='first_draft_JessisPart',
         app_sequence= ['Intro', 'Jessi_Instructions', 'Jessi_carbonTax', 'Scales'],
         consent_form = "standalone",
         num_demo_participants=10,
     )

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = [

    ## Overall Structure
    'order_tasks',

     #CC SAMPLING FIELDS
    'randomInfoArray',
    'randomMisinfoArray', 
    'reverseBoxes',
    'seenMisinfo',
    'seenMislInfo',
    'telling_box_label',

    ## carbon footprint task
    'task_rounds',

    # carbonTaxTask
    'task_rounds_J'
    
    ]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '5553960384234'
