class Lexicon:
    next = "Weiter"
    small = "small (1)"
    large = "large (10)"


    # instructions
    instructions_title = "Instructions on the next task"
    instructions_pa = "In the following we will ask you to <b>judge the climate friendliness of different carbon footprints</b>.  <br> This means we ask you to give your best estimation of <b>the size of the personal carbon footprint of a series of people with different lifestyles.</b>  The presented persons will differ with respect to <b>their diets, commuting and travel behavior as well as their electricity supply and recycling behavior</b>. <br> "
    instructions_pb = "A personal carbon footprint refers to the total amount of greenhouse gases (including CO2 and methane) that are emitted into the atmosphere as a result of an individual,s behavior. <br> The carbon footprint thus includes emissions from driving, flying, using electricity, cooling or heating your home, purchasing goods and other sources. <br> It is measured in CO2 equivalents, so that other greenhouse gases additional to CO2 (e.g., methane) are also included. <br> <br> In other words, <b>a personal carbon footprint reflects an individual,s total impact on the climate system</b>. "
    instructions_pc = "Please note that the individual carbon footprints you will assess are <b>simplified</b>, based on only 6 behaviors, so they do not account for a person,s entire carbon footprint.  <br>     You will be asked to make this judgment on a <b>scale from 1 (low carbon footprint) to 10 (large carbon footprint).</b>   <br> This means you do not have to estimate any numbers. Based on the 6 behaviors, a small carbon footprint (for a person in the United States) would equal about 1 ton of CO2 per year and a large carbon footprint about 5.5 tons of CO2. <br> "
    instructions_pd = "Next you will see how the task will look like.<br> Then we ask you to <b>estimate the carbon footprints of 16 persons with different lifestyles </b> ."
    
    # task_example
    example_pa = 'This is how a carbon footprint of an individual looks like in our task. <br>'
    example_pb = 'The different lifestyles of these individuals refer to: <ul> <li> <b>Dietary behavior:</b> The respective person either follows a <b>meat-based diet (omnivorous)</b> or a <b>plant-based diet (vegetarian)</b> </li> <li> <b>Recycling behavior:</b> The respective person either <b>recycles comprehensively</b> or <b>does not recycle</b> </li>  <li> <b>Regionality of food purchases:</b> The respective person either buys and consumes <b>mainly regional food </b> or <b>also imported</b> food items </li><li> <b>Electricity supply:</b> The respective person either subscribed to an electricity supply that is <b>mixed, so includes fossil and some renewable sources</b> or <b>based 100% on renewable energy sources</b> </li> <li> <b>Commuting to work:</b> The respective person either commutes a total of 20km to and from work everyday, 5 days a week for 48 weeks per year <b>by bike</b>  or <b>by bus</b> </li> <li> <b>Traveling on vacation:</b> The respective person either <b>takes two medium distance flights a year (=3-6hours)</b> or <b>or takes the train (e.g. Boston-New York or LA-San Francisco)</b> </li>'
    example_pc = ' <i>That is, in the example above, the person follow a vegetarian diet, does not recycle, eats regional and imported food,subscribed to a mixed electricity supply, commutes every weekday to work by bus, and takes the train to go on vacation.</i>  <br> '
    example_pd = 'Next, you will estimate the carbon footprint of <b>16</b> persons with different lifestyles. <br> Please look at each individual carbon footprint carefully and take some time to provide your estimation. <br> The order in which the 6 behaviors are presented will change across the 16 examples you will see.'

    # task_page
     
    title = 'Please rate these carbon footprints'
    BEHAVIORTYPES =  '["Diet", "Electricity", "Recycling", "Food", "Commute", "Vacation"]'
    instruction_task ='<b> Think about a person with the lifestyle below. How large do you think the carbon footprint of this person is? </b>'
    task_info = 'Please note that a small footprint refers to a person that has a lifestyle that is accompanied by little greenhouse gas emissions (for a person in the United States) and a large footprint to a person that has a lifestyle that is accompanied by a lot of greenhouse gas emissions. <br> Please make your rating from 1– small carbon footprint to 10– large carbon footprint based on the 6 behaviors presented'
