class Lexicon:
    Title_affectiveImagery = "有关碳税的关联"
    Instr_affectiveImagery = "在开始我们的任务之前，我们想请您写下当您想到‘碳税’一词时想到的至少一个词或想法"
    Association1 = "1. 关联"
    Association2 = "2. 关联"
    Association3 = "3. 关联"
    Association4 = "4. 关联"

    
     # transition
    #transition_title = '欢迎来到研究的下一个部分'

    #transitions_a = '非常感谢您迄今为止的回答。如果您在继续学习之前需要短暂休息，那么现在是个好时机。 <br> 单击此页面上的下一个按钮后，我们要求您一次性完成此块'
    # we will need to add a counter and then display that variable in the page, not sure how to integrate it in the lexicon 
    #transitions_b = '这是区块号 '
    #transitions_c = '共 4 个区块。 再次感谢您花时间回答所有问题。 <br>一旦你准备好了，请继续。'

    transitions_first_1 = '欢迎参加本研究'
    transitions_first_2= '本学习包括四个部分。您即将开始第一部分。请尽量一次性完成这一部分，不要间断。感谢您抽出时间参与本研究。准备好后，请单击 "下一个"。'
    transition_title = '欢迎来到研究的下一个部分'
    transitions_second_1 =  '您已完成本研究四个部分中的 '
    transitions_second_2 = '部分。第 '
    transitions_second_3 = '部分即将开始。如果你在继续这项研究之前需要短暂休息，现在是个好时机。'
    transitions_second_4 = '请尽量一次性完成下一部分，不要中断。感谢您抽出时间参与本研究。 准备就绪后，请点击 "下一个"。'

    
    # Affective Imagery Rating
    Title_rating = "您关于碳税的关联"
    Instructions_rating = "您可以在下面找到您提到的与'碳税'一词相关的词语和想法。请指出这些关联对于碳税的积极或消极影响。"
    very_negative = "非常消极(1)"
    very_positive = "非常积极(7)"

    # Instructions on Task 
    Title_Instructions = "关于你的任务的说明"
    Text_Instructions = "<p> 二氧化碳 (CO<sub>2</sub>) 等温室气体是全球气候变化的主要来源。<br> </p> <p> 解决这一问题的一种方法是使用‘碳税’。 <br> 碳税是对各种产品的生产和消费以及各种活动所产生的二氧化碳 (CO<sub>2</sub>) 排放征收的费用。这包括但不限于化石燃料、 肉类和奶制品等农产品以及工业流程。它的目标是让人们和企业减少排放。<br>碳税通常是因为某种活动或产品而排放的每吨二氧化碳的固定价格 。<br></p><p>除了减少排放之外，碳税征收的资金还可用于几种目的，例如，应对社会不公正或进一步减少排放。<br><p> 政府设计碳税政策的可能性有多种。因此，想象一下，中国的中央政府宣布开征碳税。<br> 这种碳税可能有不同的要素。这些要素及其示例将在下一页向您解释。<br> <br> 然后，我们请您在 12 个假设的公众投票中投票，表示您是否支持引入碳税。<br></p>"

    # Task Example 
    Title_taskExample = "任务说明 - 任务示例"
    example_taskExample = "这就是我们任务中假设的碳税投票的样子。"
    intro_attributes = "这些政策可能在以下要素上有所不同："
    attributes_sector = "<b>碳定价行业</b><br><b>一般可以对所有由服务、生产过程和能源生产造成的排放每吨二氧化碳</b> 的征税。这意味着将根据与其相关的碳排放量对每种产品和服务征税。或者，可以仅对<b>肉类和乳制品每吨二氧化碳的排放量</b>征税，或仅对<b>能源生产每吨二氧化碳的排放量</b>征税。后者包括比如电力、汽油或取暖油。"
    attributes_price = "<b>每吨二氧化碳排放量的价格</b><br>根据每吨二氧化碳排放量的价格，可以在国家碳中和方面实现不同的结果。碳中和意味着释放到大气中的二氧化碳排放量不会超过可以消除的量。碳税越高，实现碳中和的速度就越快。然而，碳税越高也意味着碳密集型产品和服务的价格上涨。<br><b>每吨二氧化碳 234 元</b>的价格,碳中和可以在本世纪中叶以后实现,即2060年左右。就价格上涨而言,这将导致例如 1 公斤猪肉价格上涨1.65元(肉类和奶制品),1 千瓦时煤电价格上涨0.25元(能源生产),一件普通的T 恤价格上涨 2.60 元（一般对所有排放）。<br> <b>每吨二氧化碳价格为467 元</b>,碳中和可以在本世纪中叶实现,即2050 年左右。这将导致，例如， 1 公斤猪肉的价格上涨 3.30 元（肉类和奶制品/吨),1 千瓦时煤电价格上涨0.45 元（能源生产/吨），一件普通 T 恤价格上涨5.15 元（一般对所有排放/吨）。"
    attributes_revenue = "<b>收入机制</b> <br>通过对碳排放征税而收取的资金（收入）可以<b>作为红利返还</b>给每个公民。这意味着社会 不公正现象可以得到平衡，因为造成高二氧化碳排放的人也必须缴纳更多的税，但所有公民获得的红利都是相同的。这样， 二氧化碳排放量少的人就可以从排放量大的人的税收中受益。另一种选择是，将收入<b>投资于二氧化碳去除技术</b>。这些新技术能够从大气中去除二氧化碳，从而有助于减少二氧化碳。"
    attributes_timing = "<b>实施时间</b><br>一揽子政策的开始时间可能是<b>1年</b>或<b>7年</b>之内。持续时间和效果（收入、 附加税）是指具体实施已决定措施的起点。这意味着,如果一揽子政策在7年内实施,二氧化碳排放量只会从该点开始减少,并同时还将征收额外税款。"
    button_info_CDR = "有关这些技术的更多信息可以在此打开"
    more_info_CDR =   "二氧化碳去除技术是使用各种方法去除大气中二氧化碳并将其长期储存的技术。其中包括，比如重新造林、沼泽加湿以及‘直接空气捕获’等解决方案。在这里，巨大的风机吸入空气并分离其中所含的二氧化碳，然后将其压成坚硬的块。然后，比如，可以将其储存在地下。这样的技术还有很多，如下图所示："
    helpButton_CDR = "这里。"
    helpClose_CDR = "关闭附加信息"
    explain_Example = "<i>也就是说，在上面的例子中，政府提出了一项碳税政策，其中<b>一般对所有排放</b>均以<b>每吨467元</b>的价格征税。 收集到的资金将用于<b>投资二氧化碳去除技术</b>，并且该碳税将在从现在开始<b>7年内</b>开始征收。</i> <br>"
    instr_continue = "现在您将依次看到 <b>12 项假设性政策提案</b>。<br>对于每一项，您都可以投票<b>是</b>或<b>否</b> ，表示您是否支持该政策提案。<br>请仔细查看每个政策提案，并花一些时间做出决定。<br>这 4 个要素的呈现顺序将在 12 个示例中发生变化。"


    example_CT = '/static/global/images/task_designCT_zh_hans.png'
    next = "下一个"


    ## attention check study is about what screenout
    interlude_title = "Brief Interruption"
    interlude_header = "This study has one superordinate topic. Have you paid attention and do you know what this study is about? Please choose the correct answer carefully."
    aboutWhatLabel = "What is this study about?"

    about_a = "City Tourism"
    about_b = "Climate Change"
    about_c = "Washing Machines"
    about_d = "Preference for spicy food"

    
    ## screenouts 
    screenout_title = "Participation not possible."
    screenout_sentence = "Sorry, your previous results indicated that you did not pay enough attention. You therefore cannot participate in this study."

    # comprehension check 
    comp_Title = "Implementation of a carbon tax?"
    compQuestion = "In what way would the CO2 tax be implemented?"
    comp_answerA = "It would be a fixed price that every citizen has to pay every year "
    comp_answerB = "Each citizen pays a voluntary amount each month to compensate for their emissions"
    comp_answerCorrect = "A certain amount of tax would be levied on each product/service based on the emissions emitted by the product/service "

    # Prior Knowledge CT 
    HeardCTbefore = "Have you ever heard of the term 'carbon tax' before?"
    yes = "Yes, I have heard of it before"
    no = "No, I have never of this term"

    # Explanation CT
    short_CT = "A carbon tax is a tax levied on the carbon emissions from producing goods and services intended to reduce carbon emissions."
    CT_title = "Carbon Tax:"
