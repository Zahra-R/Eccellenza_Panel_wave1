class Lexicon:
    next = "Weiter"
    small = "klein (1)"
    large = "gross (10)"


    # instructions
    instructions_title = "Anweisungen zur nächsten Aufgabe"
    instructions_pa = "Im Folgenden werden wir Sie bitten, <b>die Klimafreundlichkeit verschiedener CO2-Fußabdrücke zu beurteilen</b>. <br> Das bedeutet, wir bitten Sie, Ihre beste Einschätzung <b>über die Größe des persönlichen CO2-Fußabdrucks einer Reihe von Personen mit unterschiedlichen Lebensstilen zu geben.</b> Die vorgestellten Personen werden sich hinsichtlich <b>ihrer Ernährung, ihres Pendel- und Reiseverhaltens sowie ihrer Stromversorgung und Recycling-Verhaltens</b> unterscheiden. <br> "
    instructions_pb = "Ein persönlicher CO2-Fußabdruck bezieht sich auf die Gesamtmenge an Treibhausgasen (einschließlich CO2 und Methan), die aufgrund des Verhaltens einer Person in die Atmosphäre ausgestoßen wird. <br> Der CO2-Fußabdruck umfasst somit Emissionen aus dem Fahren, Fliegen, dem Verbrauch von Strom, der Kühlung oder Heizung Ihres Zuhauses, dem Kauf von Waren und anderen Quellen. <br> Er wird in CO2-Äquivalenten gemessen, sodass andere Treibhausgase zusätzlich zu CO2 (z. B. Methan) ebenfalls einbezogen werden. <br> <br> Mit anderen Worten, <b>ein persönlicher CO2-Fußabdruck spiegelt die gesamte Auswirkung einer Person auf das Klimasystem wider</b>."
    instructions_pc = "Bitte beachten Sie, dass die individuellen CO2-Fußabdrücke, die Sie bewerten werden, <b>vereinfacht</b> sind und nur auf 6 Verhaltensweisen basieren, daher berücksichtigen sie nicht den gesamten CO2-Fußabdruck einer Person. <br> Sie werden gebeten, diese Einschätzung auf einer <b>Skala von 1 (geringer CO2-Fußabdruck) bis 10 (hoher CO2-Fußabdruck)</b> vorzunehmen. <br> Das bedeutet, Sie müssen keine konkreten Zahlen schätzen. Basierend auf den 6 Verhaltensweisen würde ein geringer CO2-Fußabdruck (für eine Person in Deutschland) etwa 1 Tonne CO2 pro Jahr und ein hoher CO2-Fußabdruck etwa 5,5 Tonnen CO2 entsprechen. <br> <br> "
    instructions_pd = "Als Nächstes werden Sie sehen, wie die Aufgabe aussehen wird. <br> Dann bitten wir Sie, <b>den CO2-Fußabdruck von 16 Personen mit unterschiedlichen Lebensstilen zu schätzen</b>."
    # task_example
    example_pa = 'So sieht der CO2-Fußabdruck einer Person in unserer Aufgabe aus. <br>'

    example_pb = 'Die unterschiedlichen Lebensstile dieser Personen beziehen sich auf: <ul> <li> <b>Ernährungsverhalten:</b> Die betreffende Person folgt entweder einer <b>Fleisch-basierten Ernährung </b> oder einer <b>Pflanzen-basierten Ernährung (vegetarisch)</b> </li> <li> <b>Recycling Verhalten:</b> Die betreffende Person <b>recycelt alles</b> oder <b>recycelt nicht</b> </li>  <li> <b>Regionalität der Lebensmittel:</b> Die betreffende Person kauft und konsumiert entweder <b>hauptsächlich regionale Lebensmittel </b> oder <b>auch importierte</b> Lebensmittel </li><li> <b>Stromvertrag:</b> Die betreffende Person hat entweder einen Stromvertrag abgeschlossen der <b>gemischt ist, also fossile und teilweise erneuerbare Quelen beinhaltet</b> oder <b> 100% erneuerbare Quellen beinhaltet</b> </li> <li> <b>Arbeitsweg:</b> Die betreffende Person fährt jeden Tag die 20km zur und von der Arbeit, 5 Tage die Woche für 48 Wochen in Jahr <b>mit dem Fahrrad</b> oder <b>mit dem Bus</b> </li> <li> <b>Urlaubsreisen:</b> Die betreffende Person nimmt entweder <b>2 Mittelstreckenflüge pro Jahr (=3-6 Stunden)</b> oder <b>nimmt den Zug(z.B. London-Basel oder London-Amsterdam)</b> </li>'
    example_pc = ' <i>Das heißt, im obigen Beispiel ernährt sich die Person vegetarisch, recycelt nicht, isst regionale und importierte Lebensmittel, hat einen gemischten Stromvertrag abgeschlossen, pendelt jeden Wochentag mit dem Bus zur Arbeit und fährt mit dem Zug in den Urlaub.</i>  <br> '
    example_pd = 'Als Nächstes werden Sie den CO2-Fußabdruck von <b>16</b> Personen mit unterschiedlichen Lebensstilen einschätzen. <br> Bitte betrachten Sie jeden einzelnen CO2-Fußabdruck genau und nehmen Sie sich etwas Zeit, um Ihre Schätzung abzugeben. <br> Die Reihenfolge, in der die 6 Verhaltensweisen dargestellt werden, wird sich innerhalb der 16 gezeigten Beispielen, ändern.'




   

    # task_page
    
    title = 'Bitte bewerten Sie diese CO2-Fußabdrücke'

    BEHAVIORTYPES =  '["Ernährung", "Elektrizität", "Recycling", "Lebensmittel", "Arbeitsweg", "Urlaub"]'
    instruction_task ='Stellen Sie sich eine Person mit dem folgenden Lebensstil vor. Wie groß ist Ihrer Meinung nach der CO2-Fußabdruck dieser Person?'
    task_info = 'Bitte beachten Sie, dass ein kleiner Fußabdruck sich auf eine Person bezieht, deren Lebensstil mit geringen Treibhausgasemissionen einhergeht (für eine Person in Deutschland) und ein großer Fußabdruck auf eine Person, deren Lebensstil mit vielen Treibhausgasemissionen einhergeht. <br> Bitte machen Sie Ihre Bewertung von 1 - kleiner CO2-Fußabdruck bis 10 - großer CO2-Fußabdruck basierend auf den 6 vorgestellten Verhaltensweisen'
    # 
     