class Lexicon:
    next = "下一个"
    instructions = "Instructions"
    no = "No"
    results = 'Results'
    round_number = "Round no."
    start = "Start"
    stop = "Stop"
    yes = "Yes"
    your_decision = "Your decision"
    not_at_all = "一点也不"
    very_much = "非常"
    
    completely_agree = "completely agree"
    completely_disagree = "completely disagree"

    do_not_believe = "I do not believe that climate change is happening"
    
    dont_know = "Don't know"
    
    completely_false = "Completeley False"
    completely_true = "Completely True"
  
    #Scale anchors 
    strongly_liberal = "非常开明"
    somewhat_liberal = "有点开明"
    moderate = "不偏不倚"
    somewhat_conservative = "有点保守"
    strongly_conservative = "非常保守"

    opposed_to_values = "违背我的价值观"
    not_important = "不重要"
    extremely_important = "极其重要"
    
    no_trust_at_all = "Totally distrust"
    full_trust = "Totally trust"



     ## belief in climate change 
    beliefCC_intro = "Climate change refers to the idea that the world’s average temperature has been increasing over the past 150 years, will increase more in the future, and that the world’s climate will change as a result. What do you think: Do you think climate change is happening?"
    belief1Happening = "I believe that climate change is real"

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

    beliefSolutions1Label = "Transforming to a sustainable and climate-friendly society would reduce our national standards of living." 
    beliefSolutions2Label = " Sustainable technologies and solutions are in their infancy, and a phase-out of fossil fuels is not yet feasible."
    beliefSolutions3Label = "I think High-income countries have a greater responsibilty to reduce greenhouse gas emissions than low and middle-income countries." 
    beliefSolutions4Label = "Industry has a greater responsibilty to reduce greenhouse gas emissions than individuals."
    beliefSolutions5Label = " I would rather prepare to live with climate change than to fight climate change."




    #Climate Change Concern Tobler
    ccc_title = "对气候变化的态度"
    ccc_header = "您对以下说法的同意程度如何？"
    ccc1Label = "我们必须保护气候的微妙平衡。"
    ccc2Label = "气候保护对我们的未来很重要。"
    ccc3Label = "我担心气候状况。"
    ccc4Label = "气候变化对人类和自然造成严重后果。"
    ccc10Label = "媒体夸大了气候变化及其后果。"
    ccc11Label = "气候变化是一场闹剧。"
    ccc12Label = "只要气象学家无法准确预测天气，气候也无法可靠预测。"
    ccc13Label = "还有比气候保护更大的问题。"
    ccc14Label = "我没有感受到气候变化的威胁。"
    ccc15Label = "气候变化的影响是不可预测的；因此，我对气候有益的行为是徒劳的。"
    ccc16Label = "气候保护不必要地阻碍了经济增长。"


        # new emotions
    #Climate Change Emotion

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
    wvv1Label = "Our society would be better off if the distribution of wealth was more equal."
    wvv2Label = "A lot of problems in our society come from the decline in the traditional family, where the man works and the woman stays home."
    wvv3Label = "Discrimination against minorities is still a very serious problem in our country."
    wvv4Label = "The government interferes far too much in our everyday lives."
    wvv5Label = "I feel that people who are successful in business have a right to enjoy their wealth as they see fit."
    wvv6Label = "Too many people expect society to do things for them that they should be doing for themselves."

   # Importance of biospheric values van der Linden, 2015   
    ibv_title = "环境问题的指导原则"
    ibv_header = "以下价值作为你生活的指导原则对你来说有多重要？"
    ibv1Label = "尊重地球（与其他物种和谐相处"
    ibv2Label = "保护环境（保全自然"
    ibv3Label = "防止污染（保护自然资源"
    ibv4Label = "与自然合一（融入自然"

    # Political Orientation Pennycook et al 2020
    po_title = "Political Orientation"
    po_header = "What's your general stance in political issues?"
    po1Label = "On social issues I am..."
    po2Label = "On economic issues I am..."

    # Trust  in institutions in terms of cc Based on (Pan et al., 2023)
    pit_title = "Trust in regards to climate change"
    pit_header = "How much do you trust these actors in climate change?"
    pit1Label = "the US government"
  #  pit2Label = "US scientists"
    pit2Label = "foreign governments"
  #  pit4Label = "foreign scientists"
   # pit5Label = "the Intergovernmental Panel on Climate Change (IPCC)"

    # Knowledge Question from Allianz Climate Literacy Report
    cck_title = 'What do you know about climate change?'
    cck_header = 'Please answer all these questions to the best of your knowledge, without looking up any information. You may choose the "I do not know" option if you are unsure or do not know'
    know_dontknow = "I don't know."

    know_1qu = "What is the COP?" ## This is maybe too easy given that the whole study is about CC???
    know_1a = "UN initiative for distributing funds to reduce the impact of climate change on poverty."
    know_1b = "An annual formal meeting to discuss climate change and establish mitigation actions."
    know_1c = "An EU initiative against organized and war crimes." 
    
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
    
    

    know_8qu = "At current rates, after how many years we will have burnt our CO2-budget to limit the temperature rise to 1.5C?" # this will be 2029 (Stand 2023)
    know_8a = "less than 1 year"
    know_8b = "1-2 years"
    know_8c = "2-4 years"
    know_8d = "More than 4 years"
    

    know_9qu = "Which country/region causes the highest absolute CO2-emissions per year?"
    know_9a = "China"
    know_9b = "USA"
    know_9c = "EU"
    know_9d = "India"

    know_10qu = "Which of the four countries/regions causes the highest per-capita CO2-emissions per year?"
    know_10a = "China"
    know_10b = "USA"
    know_10c = "EU"
    know_10d = "India"
    
    ### Demographics
    demographics_title = "个人数据" 
    demographics_header = "请输入以下有关您自己的信息。"

    ageYear_label = "In which year were you born?"


    residential_area_label = "什么最能描述您的居住区？"
    metropolitan_area = "大都市区"
    suburban = "郊区"
    rural = "农村"
    
    #not relevant for China 
    party_affiliation_label = "Which party would you be most likely to vote for?"
    republicans = "Republicans"
    democrats = "Democrats"
    independent_party = "Independent Party"
    other_party = "Other"

    zip_code_label = "邮政编码（自愿）"


    # Transition page
    Transition_text = "感谢您迄今为止的参与！<br>您现在已经完成了政策任务，并将继续回答一些有关您的态度和看法的问题。" 
    # goodbye page 
    goodbye_text = "感谢您参与我们的研究！<br>您现在已完成研究，将被重新导引以获取酬金。"  

 


    
    

