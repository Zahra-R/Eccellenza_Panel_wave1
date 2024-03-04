from os import environ

SESSION_CONFIGS = [
     dict(
         name='Intro_Redirection_de',
  #      app_sequence=['survey','task'],
         app_sequence=['Intro'],
         consent_form="redirect",
         language = "de",
         num_demo_participants=10,
     ),
      dict(
         name='Intro_Redirection_en',
  #      app_sequence=['survey','task'],
         app_sequence=['Intro'],
         consent_form="redirect",
         language = "en",
         num_demo_participants=10,
     ),
      dict(
         name='Intro_Redirection_ch',
  #      app_sequence=['survey','task'],
         app_sequence=['Intro'],
         consent_form="redirect",
         language = "de",
         num_demo_participants=10,
     ),
     dict(
         name='Order_Nina_Jessi_Zahra_zh',
  #      app_sequence=['survey','task'],
         app_sequence=[ 'Nina_instructions', 'Nina_carbontask',  'Jessi_Instructions',  'Jessi_carbonTax','CCsampling_intro', 'CCsampling'],
         language = "zh_hans",
         num_demo_participants=10,
     ),
      dict(
         name='Order_Jessi_Zahra_Nina_zh',
  #      app_sequence=['survey','task'],
         app_sequence=['Jessi_Instructions',  'Jessi_carbonTax','CCsampling_intro', 'CCsampling', 'Nina_instructions', 'Nina_carbontask' ],
         language = "zh_hans",
         num_demo_participants=10,
     ),
      dict(
         name='Order_Zahra_Nina_Jessi_de',
  #      app_sequence=['survey','task'],
         app_sequence=['CCsampling_intro', 'CCsampling','Scales'],
         language = "de",
         num_demo_participants=10,
     ),
     dict(
         name='Order_Zahra_Nina_Jessi_en',
  #      app_sequence=['survey','task'],
         app_sequence=['CCsampling_intro', 'CCsampling','Scales'],
         language = "en",
         num_demo_participants=10,
     ),
    dict(
         name='first_draft_Panel_scales_pure',
  #      app_sequence=['survey','task'],
         app_sequence=['Scales'],
         language = "de",

         num_demo_participants=10,
     ),
        dict(
         name='NinasPart_de',
         #app_sequence=[ 'Nina_survey', 'Nina_carbontask', 'Nina_footprint_calculator', 'Nina_questionnaire'],
        app_sequence= ['Nina_instructions', 'Nina_carbontask'],
        language = "de",
         num_demo_participants=10,
     ),
        dict(
         name='Pretest_Jessi_de',
         app_sequence= [ 'Intro', 'Jessi_Instructions', 'Jessi_carbonTax', 'CCsampling_intro'],
         consent_form = "standalone",
         #language = "de",
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
    'pLangCode',

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
SESSION_FIELDS = [
    'introLexi',
    'samplingLexi',
    'samplingIntroLexi',

    'introNinaLexi',
    'carbonTaskLexi',

    'JessiTaskLexicon',
    'JessiIntroLexi',
    
    'scalesLexi',
    'debriefLexi',

    'myLangCode'
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '5553960384234'
