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
         num_demo_participants=30,
     ),
      dict(
         name='Intro_Redirection_ch',
  #      app_sequence=['survey','task'],
         app_sequence=['Intro'],
         consent_form="redirect",
         language = "zh_hans",
         num_demo_participants=10,
     ),
     dict(
         name='NinaFirsttestscreenouts',
  #      app_sequence=['survey','task'],
         app_sequence=[ 'FirstBlock', 'Nina_instructions', 'Jessi_Instructions', 'CCsampling_intro', 'CCsampling'],
         language = "zh_hans",
         num_demo_participants=10,
     ),
      dict(
         name='JessiFirsttestscreenouts',
  #      app_sequence=['survey','task'],
         app_sequence=[ 'Jessi_Instructions',  'CCsampling_intro',  'Nina_instructions',],
         language = "de",
         num_demo_participants=10,
     ),
      dict(
         name='ZahraFirsttestscreenouts',
  #      app_sequence=['survey','task'],
         app_sequence=['CCsampling_intro',  'Nina_instructions', 'Jessi_Instructions'],
         language = "de",
         num_demo_participants=10,
     ),
     dict(
         name='Order_Nina_Jessi_Zahra_zh',
  #      app_sequence=['survey','task'],
         app_sequence=['FirstBlock',  'Nina_instructions', 'Nina_carbontask',  'Jessi_Instructions',  'Jessi_carbonTax','CCsampling_intro', 'CCsampling',  'Scales','CCsampling_Debrief', 'Goodbye'],
         language = "zh_hans",
         num_demo_participants=10,
     ),
      dict(
         name='Order_Jessi_Zahra_Nina_zh',
  #      app_sequence=['survey','task'],
         app_sequence=['FirstBlock', 'Jessi_Instructions',  'Jessi_carbonTax','CCsampling_intro', 'CCsampling', 'Nina_instructions', 'Nina_carbontask', 'Scales','CCsampling_Debrief', 'Goodbye' ],
         language = "zh_hans",
         num_demo_participants=10,
     ),
     dict(
         name='Order_Zahra_Nina_Jessi_zh',
  #      app_sequence=['survey','task'],
         app_sequence=['FirstBlock', 'CCsampling_intro', 'CCsampling', 'Nina_instructions', 'Nina_carbontask',  'Jessi_Instructions',  'Jessi_carbonTax',  'Scales','CCsampling_Debrief', 'Goodbye'],
         language = "zh_hans",
         num_demo_participants=10,
     ),
      
      dict(
         name='Order_Zahra_Nina_Jessi_de',
  #      app_sequence=['survey','task'],
         app_sequence=[ 'FirstBlock', 'CCsampling_intro', 'CCsampling','Nina_instructions', 'Nina_carbontask',  'Jessi_Instructions',  'Jessi_carbonTax', 'Scales','CCsampling_Debrief', 'Goodbye'],
         language = "de",
         num_demo_participants=10,
     ),
      dict(
         name='Order_Jessi_Zahra_Nina_de',
  #      app_sequence=['survey','task'],
         app_sequence=[ 'FirstBlock',  'Jessi_Instructions',  'Jessi_carbonTax', 'CCsampling_intro', 'CCsampling','Nina_instructions', 'Nina_carbontask',  'Scales','CCsampling_Debrief', 'Goodbye'],
         language = "de",
         num_demo_participants=10,
     ),
      dict(
         name='Order_Nina_Jessi_Zahra_de',
  #      app_sequence=['survey','task'],
         app_sequence=['FirstBlock',  'Nina_instructions', 'Nina_carbontask', 'Jessi_Instructions',  'Jessi_carbonTax', 'CCsampling_intro', 'CCsampling',  'Scales','CCsampling_Debrief', 'Goodbye'],
         language = "de",
         num_demo_participants=10,
     ),
     dict(
         name='Order_Zahra_Nina_Jessi_en',
  #      app_sequence=['survey','task'],
         app_sequence=['FirstBlock',  'CCsampling_intro', 'CCsampling','Nina_instructions', 'Nina_carbontask',  'Jessi_Instructions',  'Jessi_carbonTax', 'Scales','CCsampling_Debrief', 'Goodbye'],
         language = "en",
         num_demo_participants=10,
     ),
     dict(
         name='Order_Jessi_Zahra_Nina_en',
  #      app_sequence=['survey','task'],
         app_sequence=[ 'FirstBlock',  'Jessi_Instructions',  'Jessi_carbonTax', 'CCsampling_intro','Nina_instructions', 'Nina_carbontask',  'CCsampling', 'Scales','CCsampling_Debrief', 'Goodbye'],
         language = "en",
         num_demo_participants=10,
     ),
     dict(
         name='Order_Nina_Jessi_Zahra_en',
  #      app_sequence=['survey','task'],
         app_sequence=[ 'FirstBlock', 'Nina_instructions', 'Nina_carbontask',  'Jessi_Instructions',  'Jessi_carbonTax', 'CCsampling_intro', 'CCsampling', 'Scales','CCsampling_Debrief', 'Goodbye'],
         language = "en",
         num_demo_participants=10,
     ),
    dict(
         name='chinese_Panel_scales_pure',
  #      app_sequence=['survey','task'],
         app_sequence=['Scales', 'CCsampling_Debrief'],
         language = "zh_hans",

         num_demo_participants=10,
     ),
      dict(
         name='german_Panel_scales_pure',
  #      app_sequence=['survey','task'],
         app_sequence=['Scales', 'CCsampling_Debrief'],
         language = "de",

         num_demo_participants=10,
     ),
     dict(
         name='english_test_end',
  #      app_sequence=['survey','task'],
         app_sequence=['CCsampling', 'CCsampling_Debrief', 'Goodbye'],
         language = "en",
         consent_form="redirect",

         num_demo_participants=10,
     ),
        dict(
         name='Pretest_Jessi_de',
         app_sequence= [ 'Intro', 'FirstBlock', 'Jessi_Instructions', 'Jessi_carbonTax', 'CCsampling_intro'],
         consent_form = "standalone",
         language = "de",
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
    'task_counter',

     #CC SAMPLING FIELDS
    'randomInfoArray',
    'randomMisinfoArray', 
    'reverseBoxes',
    'seenMisinfo',
    'seenMislInfo',
     #'telling_box_label',

    ## carbon footprint task
    'task_rounds',

    # carbonTaxTask
    'task_rounds_J'
    
    ]
SESSION_FIELDS = [
    'introLexi',
    'firstBlockLexi',
    
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
