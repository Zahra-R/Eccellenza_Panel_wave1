class Lexicon:
    #Scale anchors 
    strongly_liberal = "非常开明"
    somewhat_liberal = "有点开明"
    moderate = "不偏不倚"
    somewhat_conservative = "有点保守"
    strongly_conservative = "非常保守"

    opposed_to_values = "违背我的价值观"
    not_important = "不重要"
    extremely_important = "极其重要"

    not_at_all = "一点也不"
    very_much = "非常"

    next = "下一个"

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

    #Climate Change Emotion Knauf/Truelove
    cce_title = "对气候变化的态度"
    cce_header = "当我想到气候变化时，我感觉…"
    cce1Label = "愤怒"
    cce2Label = "害怕"
    cce3Label = "悲伤"
    cce4Label = "喜悦"
    cce5Label = "好奇"
    cce6Label = "希望"

        # new emotions
    #Climate Change Emotion

    cceA1Label = "angry"
    cceA2Label = "mad"
    cceA3Label = "irritated"
    cceF1Label = "fearful"
    cceF2Label = "afraid"
    cceF3Label = "scared"
    cceS1Label = "sad"
    cceS2Label = "sorrowful"
    cceS3Label = "unhappy"
    cceH1Label = "hopeful"
    cceH2Label = "optimistic"
    cceH3Label = "upbeat"
    cceG1Label = "guilty"
    cceG2Label = "regretful"
    cceG3Label = "remorseful"

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
    pit2Label = "US scientists"
    pit3Label = "foreign governments"
    pit4Label = "foreign scientists"
    pit5Label = "the Intergovernmental Panel on Climate Change (IPCC)"

  
  
    
    ### Demographics
    demographics_title = "个人数据" 
    demographics_header = "请输入以下有关您自己的信息。"

    age_label = "你今年多大？"
    gender_label = "您的性别是什么？" 
    female = "女性"
    male = "男性"
    other = "其他"

    income_label = "你的年收入是多少？"
    income_less_than_A = "3万元人民币以下"
    income_A_to_B = "30,000 - 60,000元人民币"
    income_B_to_C = "60,001 - 120,000元人民币"
    income_C_to_D = "120,001 - 300,000元人民币"
    income_D_to_E = "300,001 - 500,000元人民币"
    income_more_than_E = "超过50万元人民币"
    prefer_not_to_say = "不愿意说"

    education_label = "你的最高学历是什么？"
    high_school = "初中"
    vocational_education = "职业教育"
    some_college = "高等教育（职业）"
    bachelors_degree =  "学士学位"
    masters_degree = "硕士学位"
    doctoral_degree = "博士学位"



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
    link = 'https://www.innofact-umfrage.de/sample_only/ub3/cn/danke_f.php'

    Additional_title = "一些额外的问题"
    Additional_intro = "最后我们想问你一些额外的问题。"

    familiar_header = "对于每项操作，请表明您对它们的熟悉程度："
    familiar_label1 = "选择自己的电力合同或改用其他更具可再生性的合同"
    familiar_label2 = "遵循素食（即不吃肉，包括鱼）"
    familiar_label3 = "骑自行车上班"
    familiar_label4 = "购买和食用进口食品（即来自其他国家）"
    familiar_label5 = "购买和消费区域食品（来自您所在的地区/国家）"
    familiar_label6 = "回收（即纸张、玻璃或金属）"
    familiar_label7 = "乘火车去度假"
    familiar_label8 = "乘公共汽车去度假"
    familiar_label9 = "乘飞机去度假"
    familiar_A = "非常陌生"
    familiar_B = "陌生"
    familiar_C = "有点陌生"
    familiar_D = "不陌生也不熟悉"
    familiar_E = "有点熟悉"
    familiar_F = "熟悉的"
    familiar_G = "非常熟悉"

    Difficult_header = "请说明对于您所在国家/地区的普通人来说执行以下操作有多容易或多困难"
    difficult_label1 = "选择或转换他们的电力合同（例如，获得更高比例的可再生能源电力）"
    difficult_label2 = "遵循素食（即不吃肉或鱼）"
    difficult_label3 = "骑自行车上班"
    difficult_label4 = "购买和消费进口食品（即来自其他国家）"
    difficult_label5 = "主要购买和消费区域食品（来自您所在的地区/国家）"
    difficult_label6 = "回收（即纸张、玻璃或金属）"
    difficult_label7 = "坐火车去度假"
    difficult_label8 = "坐公交车去度假"
    difficult_label9 = "坐飞机去度假"

    difficult_A = "非常困难"
    difficult_B = "难的"
    difficult_C = "有点困难"
    difficult_D = "既不困难也不容易"
    difficult_E = "有点容易"
    difficult_F = "简单的"
    difficult_G = "非常简单"




    
    

