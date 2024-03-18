class Lexicon:
    instructions = "Instructions"
    next = "Next"
    no = "No"
    results = 'Results'
    round_number = "Round no."
    start = "Start"
    stop = "Stop"
    yes = "Yes"
    your_decision = "Your decision"
    not_at_all = "not at all"
    very_much = "very much"
    
    completely_agree = "completely agree"
    completely_disagree = "completely disagree"

    do_not_believe = "I do not believe that climate change is happening"
    
    dont_know = "Don't know"
    opposed_to_values = "opposed to my values"
    not_important = "not <br> important"
    not_at_all_important = "not at all important"
    extremely_important = "extremely <br>  important"

   
    somewhat_liberal = "Somewhat Liberal"
    moderate = "Moderate"
    somewhat_conservative = "Somewhat Conservative"
    no_trust_at_all = "Totally distrust"
    full_trust = "Totally trust"
    completely_false = "Completeley False"
    completely_true = "Completely True"

    
    ## belief in climate change 
    beliefCC_intro = "Climate change refers to the idea that the world’s average temperature has been increasing over the past 150 years, will increase more in the future, and that the world’s climate will change as a result. What do you think: Do you think climate change is happening?"
    belief1HappeningLabel = "I believe that climate change is real."

    ### belief in (human) causes taken from  Valkengoed
    beliefHuman_title = "What do you believe?"
    beliefHuman_header = "How much do you agree with the following statements?"
    beliefHuman1Label = "Human activities are <b> not </b> a major cause of climate change." # reversed (originally not)
    beliefHuman2Label = "Climate change is mostly caused by human activity."
    beliefHuman3Label = "The main causes of climate change are human activities." 

    beliefConseqences1Label = "Overall, climate change will bring more negative than positive consequences to the world."
    beliefConseqences2Label = "Climate change will bring about serious negative consequences."
    beliefConseqences3Label = "The consequences of climate change will <b> not </b> be very serious." # reversed (originally not)

    beliefConsensLabel = "Which percentage of climate scientists agree that climate change is real and caused by human activity?"

    ##belief in solutions

    beliefSolutions1Label = "Transforming to a sustainable and climate-friendly society would reduce our national standards of living."  # reversed
    beliefSolutions2Label = " Sustainable technologies and solutions are in their infancy, and a phase-out of fossil fuels is not yet feasible." # reversed
    beliefSolutions3Label = "I think High-income countries have a greater responsibility to reduce greenhouse gas emissions than low and middle-income countries." #responsibility national
    beliefSolutions4Label = "Industry has a greater responsibility to reduce greenhouse gas emissions than individuals."  #responsibility systemic
    beliefSolutions5Label = " I would rather prepare to live with climate change than to fight climate change." # adaptation


    #Climate Change Emotion Knauf/Truelove
    cce_title = "Attitudes about Climate Change"
    cce_header = "When I think of Climate Change I feel..."
    emoAng1Label = "angry"
    emoAng2Label = "mad"
    emoAng3Label = "irritated"
    emoFear1Label = "fearful"
    emoFear2Label = "afraid"
    emoFear3Label = "scared"
    emoSad1Label = "sad"
    emoSad2Label = "sorrowful"
    emoSad3Label = "unhappy"
    emoHope1Label = "hopeful"
    emoHope2Label = "optimistic"
    emoHope3Label = "upbeat"
    emoGuilt1Label = "guilty"
    emoGuilt2Label = "regretful"
    emoGuilt3Label = "remorseful"
    
    emoConcern1Label = "worried"
    emoConcern2Label = "concerned"
    emoConcern3Label = "upset"


    # Worldviews and values - Hierarchy-Egalitarianism & Individualism-Communitarianism  
    ## TBD kevin tam
    wvv_title = "How do you see the world?"
    wvv_header = "How much do you agree with the following statements?"
    hie1Label = "Our society would be better off if the distribution of wealth was more equal."
    hie2Label = "A lot of problems in our society come from the decline in the traditional family, where the man works and the woman stays home."
    hie3Label = "Discrimination against minorities is still a very serious problem in our country."
    ind1Label = "The government interferes far too much in our everyday lives."
    ind2Label = "I feel that people who are successful in business have a right to enjoy their wealth as they see fit."
    ind3Label = "Too many people expect society to do things for them that they should be doing for themselves."

   # Importance of biospheric values van der Linden, 2015   
    ibv_title = "Guiding principles in enviromental issues"
    ibv_header = "How important are the following values to you as guiding principles of your life?"
    ibv1Label = "Respecting the Earth (harmony with other species)"
    ibv2Label = "Protecting the Environment (preserving nature)"
    ibv3Label = "Preventing Pollution (protecting natural resources)"
    ibv4Label = "Unity with Nature (fitting into nature)"

    # Political Orientation Pennycook et al 2020
    polOrientationLabel = "How do you see your general stance in political issues?."
    strongly_liberal = "strongly liberal/left-wing"
    strongly_conservative = "strongly conservative/right-wing"


    # Trust  in institutions in terms of cc Based on (Pan et al., 2023)
    pit_title = "Trust in regards to climate change"
    pit_header = "How much do you trust these actors in climate change?"
    pit1Label = "the local government"
    pit2Label = "the national government"


    # Knowledge Question from Allianz Climate Literacy Report
    cck_title = 'What do you know about climate change?'
    cck_header = 'Please answer all these questions to the best of your knowledge, without looking up any information. You may choose the "I do not know" option if you are unsure or do not know'
    know_dontknow = "I don't know."

    know_1qu = "What is the COP?" ## This is maybe too easy given that the whole study is about CC???
    know_1a = "UN initiative for distributing funds to reduce the impact of climate change on poverty."
    know_1b = "An annual formal meeting to discuss climate change and establish mitigation actions."
    know_1c = "An EU initiative for multinational cooperation against organized crime." 
    
    know_2qu = "What does Net-Zero mean?"
    know_2a = "Monetary strategy of increasing interest rate to fight inflation."
    know_2b = "No greenhouse gas emission by a specific date, typically 2050."
    know_2c = "Carbon emission neutrality, stabilization of greenhouse gas concentrations in the atmosphere."
    
    know_3qu = "The Intergovernmental Panel on Climate Change (IPCC) plays an important role in global climate policy. Which one?"
    know_3a = "Providing objective scientific information relevant to understanding climate change."
    know_3b = "Deciding on global climate policies, particularly setting the global carbon price."
    know_3c = "Host of the UN climate justice court which arbitrates climate disputes between states."
    
    know_4qu = "What is the carbon market?"
    know_4a = "The supply channel of the EU backed gas-buying cartel that aims to supply affordable natural gas to EU countries struggling to get supply because of the war in Ukraine."
    know_4b = "A trading system through which emitters may buy or sell units of greenhouse-gas emission allowances to meet national restrictions on total emissions."
    know_4c = "An online marketplace where you can buy recycled carbon fiber and carbon black."
    

    ## I suggest a modification of tis question:
    #Rising temperatures pose no existential threat. Even if the rise exceeds 3°C, humans and nature can adapt. Do you agree with this statement?"
    know_5qu = "How long does CO2 stay in the atmosphere?"
    know_5a = "10 years"
    know_5b = "up to 1000 years"
    know_5c = "more than 5000 years"

    
    ## I suggest a modification of this question
    know_6qu = "Which of the following options describes the greenhouse gas effect"
    # old was Climate change cannot be stopped. Average temperatures will continue to increase in the near future. The only thing we can possible do is to limit the increase to 1.5°C."
    know_6a = "Deforestation and plastic pollution cause a collapse of many ecosystems. The increasing loss of biodiversity and the loss of flora and fauna in the wild is called the greenhouse gas effect."
    know_6b = "Greenhouse gasses cause air pollution. They lead to more fine particulars and more fine dust which in turn decreases the ventilation. Without the circulation of fresh air, the earth gets increasingly warmer. "
    know_6c = "Excess greenhouse gases accumulate in the atmosphere. Because of their molecular structure, the infrared radiation from the earth is reflected and is re-radiated to the earth. This way, heat is trapped."
    
    
    know_7qu = "At current rates, after how many years we will have burnt our CO2-budget to limit the temperature rise to 1.5C?" # this will be September 2026 (Stand 2023)
    know_7a = "less than 1 year"
    know_7b = "1-2 years"
    know_7c = "2-4 years"
    know_7d = "More than 4 years"
    

    know_8qu = "Which country/region causes the highest absolute CO2-emissions per year?"
    know_8a = "China"
    know_8b = "USA"
    know_8c = "EU"
    know_8d = "India"

    know_9qu = "Which country/region causes the highest per-capita CO2-emissions per year?"
    know_9a = "China"
    know_9b = "USA"
    know_9c = "EU"
    know_9d = "India"
    
    ### Behaviors ###
    behaviors_title = ' Behavior '
    intro_a = ' In this next part, we are collecting information about some of your actual behavior. <br>Please answer as accurately as possible. Thank you in advance!'
    regional_label = ' What percentage of your food is regional (from within your country or region, not imported) ? '
    regional_less_than = 'Less than a quarter'
    regional_quarter= 'About a quarter' 
    regional_half = 'About half' 
    regional_3_quarter = 'About three quarters'
    regional_more_than = 'the largest part is regional'

    electricity_label = 'This question is about your electricity supply. What does your electricity supply look like?'
    electricity_D = 'I have green electricity entirely '
    electricity_C = 'I partly have green electricity (mixed)' 
    electricity_B = ' I have a conventional (fossil) supply'
    electricity_A = 'I don,t know'

    food_overall_text = ' In the last month, how many times did you eat the following food items...'
    food_overall_label1 = 'Beef'
    food_overall_label2 = 'Lamb or mutton'
    food_overall_label3 = 'Pork'
    food_overall_label4 = 'Poultry (e.g. chicken)'
    food_overall_label5 = 'Fish'
    food_overall_label6 = 'Dairy products (e.g milk or cheese)'

    food_overall_A = 'Never'
    food_overall_B = 'Once a month'
    food_overall_C= '2-3 times per month'
    food_overall_D = 'Once a week'
    food_overall_E = '2-3 times per week'
    food_overall_F = '4-6 times per week'
    food_overall_G = 'Once a day'
    food_overall_H = '2 or more times per day'



    commute_pt_label = 'How many kilometers do you <b> commute weekly in public transport </b> (train, bus, etc.)or an e-bike? Please calculate all private journeys including the work commute, but not business travels.'
    commute_pt_never = 'I never use public transport'
    commute_pt_less_than_A = '1 - 39 miles'
    commute_pt_A_to_B= '40 - 50 miles'
    commute_pt_B_to_C = '50 -149 miles'
    commute_pt_C_to_D = '150 - 224 miles'
    commute_pt_D_to_E = '225 - 370 miles'
    commute_pt_more_than_E = 'more than 370 miles'

    commute_car_label = 'How many kilometers do you <b> annually drive in a car </b> or on a motorcycle (outside of work times, both driving and as a passenger)?'
    commute_car_never = 'I never use a car or motorcycle'
    commute_car_less_than_A = '1 - 1,244 miles'
    commute_car_A_to_B= '1,245 - 4,659 miles'
    commute_car_B_to_C = '4,660 - 7,769 miles'
    commute_car_C_to_D = '7,770 - 18,640 miles'
    commute_car_more_than_D = 'more than 18,640 miles'

    commute_car_type_label = 'Which kind of fuel does your car operate on?'
    commute_car_type_none = 'I do not have a car'
    commute_car_type_E = 'Gasoline/Diesel/Hybrid'
    commute_car_type_D = 'Natural gas'
    commute_car_type_C = 'Biogas'
    commute_car_type_B = 'Electric (conventional energy) '
    commute_car_type_A = 'Electric (green energy)'

    flying_short_label = 'How many <b>short-distance flights (<3 hours)</b> did you take on average in the past two years? <i> i: one round-trip flight counts as two flights. So if you flew from San Francisco to Los Angeles and back this counts as 2 flights. </i> '
    # for chinese version example:  from Shanghai to Beijing and back
    flying_mid_label ='How many <b>mid-distance flights (3-6 hours) </b> did you take on average in the past two years? <i> i: one round-trip flight counts as two flights. So if you flew from New York to San Francisco and back this counts as 2 flights. </i> '
    #for chinese version example:  from Guangzhou to Beijing and back
    flying_long_label = 'How many <b>long-distance flights (>6 hours) </b> did you take on average in the past two years? <i> i: one round-trip flight counts as two flights. So if you flew from Miami to London and back this counts as 2 flights. </i> '
    # for  chinese version example: from Beijing to Jakarta (Indonesia) and back

 


    ### Demographics
    demographics_title = "Personal data"
    demographics_header = "Please enter the following information about yourself."
    
    ageYear_label = "In which year were you born?"

    residential_area_label = "What describes your residential area best?"
    metropolitan_area = "Metropolitan Area"
    suburban = "Suburban Area"
    rural = "Rural Area"

    zip_code_label = "What is your Zip Code? (Answering this question is optional.)"
    
    party_affiliation_label = "Which party would you be most likely to vote for?"
    republicans = "Republicans"
    democrats = "Democrats"
    independent_party = "Independent Party"
    other_party = "Other"

    # Transition page
    transition_title = 'Welcome to the last block of the study'
    
    # these are the exact same 4 things as in the lexicon 'Nina instructions' => we will copy the translations here
    transitions_a = 'Thank you very much for your answers so far. If you need a short break before continuing with the study, now would be a good time. <br> Once you click on the next button on this page, we ask you to please complete this block in one go.'
    # add counter (Zahra)
    transitions_b =' This is the last  '
    transitions_c = 'out of 4 blocks. Thank you for taking the time to complete everything so far. <br> Once you are ready, please click "next".'

    

