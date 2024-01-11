class Lexicon:
    instructions = "Instructions"
    no = "No"
    results = 'Results'
    round_number = "Round no."
    start = "Start"
    stop = "Stop"
    yes = "Yes"
    your_decision = "Your decision"
    not_at_all = "not at all"
    very_much = "very much"
    no_effort = "no effort"
    great_deal_of_effort = "a great deal of effort"
    not_important = "not important"
    not_at_all_important = "not at all important"
    extremely_important = "extremely important"
    likely_increase = "Likely to Increase"
    no_change = "No Change"
    likely_decrease = "Likely to Decrease"
    dont_know = "Don't know"
    opposed_to_values = "opposed to my values"
    strongly_liberal = "Strongly Liberal"
    somewhat_liberal = "Somewhat Liberal"
    moderate = "Moderate"
    somewhat_conservative = "Somewhat Conservative"
    strongly_conservative = "Strongly Conservative"
    no_trust_at_all = "No trust at all"
    full_trust = "Full trust"
    completely_false = "Completeley False"
    completely_true = "Completely True"


    #Climate Change Concern Tobler
    ccc_title = "Attitudes about Climate Change"
    ccc_header = "How much do you agree with the following statements?"
    ccc1Label = "We must protect the climate’s delicate equilibrium."
    ccc2Label = "Climate protection is important for our future."
    ccc3Label = "I worry about the climate’s state."
    ccc4Label = "Climate change has severe consequences for humans and nature."
    ccc10Label = "Climate change and its consequences are being exaggerated in the media."
    ccc11Label = "Climate change is a racket."
    ccc12Label = "As long as meteorologists are not even able to accurately forecast weather, climate cannot be reliably predicted either."
    ccc13Label = "There are larger problems than climate protection."
    ccc14Label = "I do not feel threatened by climate change."
    ccc15Label = "The impacts of climate change are unpredictable; thus, my climate-friendly behavior is futile."
    ccc16Label = "Climate protection needlessly impedes economic growth."


    #Climate Change Emotion Knauf/Truelove
    cce_title = "Attitudes about Climate Change"
    cce_header = "When I think of Climate Change I feel..."
    cce1Label = "Anger"
    cce2Label = "Fear"
    cce3Label = "Sadness"
    cce4Label = "Joy"
    cce5Label = "Curiosity"
    cce6Label = "Hope"


    
    # Personal efficacy Leiserowitz et al, 2010
    #Only item 1
    pe_title = "Attitudes about Climate Change"
    pe_header = "How much do you agree with the following statements?"
    pe1Label = "The actions of a single individual won't make any difference in climate change."
  
    
    # Worldviews and values - Hierarchy-Egalitarianism & Individualism-Communitarianism  
    ## TBD kevin tam
    wvv_title = "How do you see the world?"
    wvv_header = "How much do you agree with the following statements?"
    wvv1Label = "Our society would be better off if the distribution of wealth was more equal."
    wvv2Label = "A lot of problems in our society come from the decline in the traditional family, where the man works and the woman stays home."
    wvv3Label = "Discrimination against minorities is still a very serious problem in our country."
    wvv4Label = "The government interferes far too much in our everyday lives."
    wvv5Label = "I feel that people who are successful in business have a right to enjoy their wealth as they see fit."
    wvv6Label = "Too many people expect society to do things for them that they should be doing for themselves."

   # Importance of biospheric values van der Linden, 2015   
    ibv_title = "Guiding principles in enviromental issues"
    ibv_header = "How important are the following values to you as guiding principles of your life?"
    ibv1Label = "Respecting the Earth (harmony with other species)"
    ibv2Label = "Protecting the Environment (preserving nature)"
    ibv3Label = "Preventing Pollution (protecting natural resources)"
    ibv4Label = "Unity with Nature (fitting into nature)"

    # Political Orientation Pennycook et al 2020
    po_title = "Political Orientation"
    po_header = "What's your general stance in political issues?"
    po1Label = "On social issues I am..."
    po2Label = "On economic issues I am..."

    # Trust in political institutions from Eurobarometer / Lantian et al 2016  
    pit_title = "How much trust do you have in certain institutions?"
    pit_header = "For each of the following institutions, do you tend to trust it or tend not to trust it?"
    pit1Label = "The government"
    pit2Label = "Regional or local public authorities"
    pit3Label = "Justice and the legal system"
    pit4Label = "The media"


    # Knowledge Question from Allianz Climate Literacy Report
    know_dontknow = "I don't know."

    know_1qu = "What is the COP?" ## This is maybe too easy given that the whole study is about CC???
    know_1a = "UN initiative for distributing funds to reduce the impact of climate change on poverty."
    know_1b = "An annual formal meeting to discuss climate change and establish mitigation actions"
    know_1c = "An EU initiative against organized and war crimes" ## a potent Greenhouse Gas 
    
    know_2qu = "What does Net-Zero mean?"
    know_2a = "Monetary strategy of increasing interest rate to fight inflation."
    know_2b = "No greenhouse gas emission by a specific date, typically 2050"
    know_2c = "Carbon emission neutrality, stabilization of greenhouse gas concentrations in the atmosphere"
    
    know_3qu = "The Intergovernmental Panel on Climate Change (IPCC) plays an important role in global climate policy. Which one?"
    know_3a = "Providing objective scientific information relevant to understanding climate change"
    know_3b = "Deciding on global climate policies, particularly setting the global carbon prize"
    know_3c = "Host of the UN climate justice court which arbitrates climate disputes between states"
    
    know_4qu = "What is the carbon market?"
    know_4a = "The supply channel of the EU backed gas-buying cartel that aims to supply affordable natural gas to EU countries struggling to get supply because of the war in Ukraine."
    know_4b = "A trading system through which emitters may buy or sell units of greenhouse-gas emission allowances to meet national restrictions on total emissions."
    know_4c = "An online marketplace where you can buy recycled carbon fiber and carbon black."
    

    ## I suggest a modification of tis question:
    # "How long does CO2 stay in the atmosphere"
    # a) 10 years
    # b) up to 1000 years
    # c) more than 5000 years 
    know_5qu = "Rising temperatures pose no existential threat. Even if the rise exceeds 3°C, humans and nature can adapt. Do you agree with this statement?"
    know_5a = "yes, change is the only constant - this applies to climate as well."
    know_5b = "no, even at a temperature rise of more than 1.5°C irreparable damages loom, with unforeseen economic and social consequences."

    
    ## I suggest a modification of this question
    know_6qu = "Climate change cannot be stopped. Average temperatures will continue to increase in the near future. The only thing we can possible do is to limit the increase to 1.5°C."
    # Which of the following describes the greenhouse gas effect?
    know_6a = "Deforestation and plastic pollution cause a collapse of many ecosystems. The increasing loss of biodiversity and the loss of flora and fauna in the wild is called the greenhouse gas effect."
    know_6b = "Greenhouse gasses cause air pollution. They lead to more fine particulars and more fine dust which in turn decreases the ventilation. Without the circulation of fresh air, the earth gets increasingly warmer. "
    know_6c = "Excess greenhouse gases accumulate in the atmosphere. Because of their molecular structure, the infrared radiation from the earth is reflected and is re-radiated to the earth. This way, heat is trapped."
    

    know_7qu = "If the world manages to stabilize CO2-emissions levels, damaging consequences of climate change can be avoided."
    # I propose to change it to "Yes, it is enough to break the past trend of continuous increases of annual emissions"
    know_7a = "Yes, key is to break the past trend of continuous increases of annual emissions"
    know_7b = "No, we must reduce annual emissions drastically below zero, thus actively extracting and storing CO2 from the atmosphere."
    know_7c = ""
    

    know_8qu = "At current rates, after how many years we will have burnt our CO2-budget to limit the temperature rise to 1.5C?" ### double check if still true in 2024!!!!
    know_8a = "6 years"
    know_8b = "11 years"
    know_8c = "24 years"
    

    know_9qu = "Which country/region causes the highest absolute CO2-emissions per year?"
    know_9a = "China"
    know_9b = "USA"
    know_9c = "India"

    know_10qu = "Which of the four countries causes the highest per-capita CO2-emissions per year?"
    know_10a = "China"
    know_10b = "USA"
    know_10c = "EU"
    


    ### Demographics
    demographics_title = "Personal data"
    demographics_header = "Please enter the following information about yourself."

    age_label = "How old are you?"
    gender_label = "What gender do you identify as?"
    female = "Female"
    male = "Male"
    diverse = "Diverse"
    other = "Other"

    income_label = "What is your yearly income?"
    income_less_than_A = "Less than $25,000"
    income_A_to_B = "$25,000 - $50,000"
    income_B_to_C = "$50,001 - $75,000"
    income_C_to_D = "$75,001 - $100,000"
    income_more_than_D = "More than $100,000"
    prefer_not_to_say = "Prefer not to say"

    education_label = "What is your highest level of education?"
    high_school = "High School"
    some_college = "Some College"
    bachelors_degree = "Bachelor's Degree"
    masters_degree = "Master's Degree"
    doctoral_degree = "Doctoral Degree"

    residential_area_label = "What describes your residential area best?"
    metropolitan_area = "Metropolitan Area"
    suburban = "Suburban Area"
    rural = "Rural Area"

    zip_code_label = "Zip Code (voluntarily)"
    
    party_affiliation_label = "Which party would you be most likely to vote for?"
    republicans = "Republicans"
    democrats = "Democrats"
    independent_party = "Independent Party"
    other_party = "Other"
