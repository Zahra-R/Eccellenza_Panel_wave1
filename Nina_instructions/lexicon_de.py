class Lexicon:
    next = "Weiter"

     # transition
    transition_title = 'Willkommen beim nächsten Block der Studie'
    transitions_a = 'Vielen Dank für Ihre bisherigen Antworten. Wenn Sie eine kurze Pause benötigen, bevor Sie mit der Studie fortfahren, wäre jetzt ein guter Zeitpunkt. <br> Sobald Sie auf den weiter-Knopf auf dieser Seite klicken, bitten wir Sie, diesen Block in einem Rutsch auszufüllen.'
    # we will need to add a counter and then display that variable in the page, not sure how to integrate it in the lexicon 
    transitions_b ='Dies ist Block Nummer '
    transitions_c = ' von insgesamt 4 Blöcken. Vielen Dank, dass Sie sich die Zeit genommen haben, alle Fragen zu beantworten. Wenn Sie bereit sind, fahren Sie bitte fort.'
   

    # instructions
    instructions_title = "Anweisungen zur nächsten Aufgabe"
    instructions_pa = "Im Folgenden werden wir Sie bitten, <b>die Klimafreundlichkeit verschiedener CO2-Fußabdrücke zu beurteilen</b>. <br> Das bedeutet, wir bitten Sie, Ihre beste Einschätzung <b>über die Größe des persönlichen CO2-Fußabdrucks einer Reihe von Personen mit unterschiedlichen Lebensstilen zu geben.</b> Die vorgestellten Personen werden sich hinsichtlich <b>ihrer Ernährung, ihres Pendel- und Reiseverhaltens sowie ihrer Stromversorgung und Recycling-Verhaltens</b> unterscheiden. <br> "
    instructions_pb = "Ein persönlicher CO2-Fußabdruck bezieht sich auf die Gesamtmenge an Treibhausgasen (einschließlich CO2 und Methan), die aufgrund des Verhaltens einer Person in die Atmosphäre ausgestoßen wird. <br> Der CO2-Fußabdruck umfasst somit Emissionen aus dem Fahren, Fliegen, dem Verbrauch von Strom, der Kühlung oder Heizung Ihres Zuhauses, dem Kauf von Waren und anderen Quellen. <br> Er wird in CO2-Äquivalenten gemessen, sodass andere Treibhausgase zusätzlich zu CO2 (z. B. Methan) ebenfalls einbezogen werden. <br> <br> Mit anderen Worten, <b>ein persönlicher CO2-Fußabdruck spiegelt die gesamte Auswirkung einer Person auf das Klimasystem wider</b>."
    instructions_pc = "Bitte beachten Sie, dass die individuellen CO2-Fußabdrücke, die Sie bewerten werden, <b>vereinfacht</b> sind und nur auf 6 Verhaltensweisen basieren, daher berücksichtigen sie nicht den gesamten CO2-Fußabdruck einer Person. <br> Sie werden gebeten, diese Einschätzung auf einer <b>Skala von 1 (geringer CO2-Fußabdruck) bis 10 (hoher CO2-Fußabdruck)</b> vorzunehmen. <br> Das bedeutet, Sie müssen keine konkreten Zahlen schätzen. Basierend auf den 6 Verhaltensweisen würde ein geringer CO2-Fußabdruck (für eine Person in Deutschland) etwa 0,7 Tonnen CO2 pro Jahr und ein hoher CO2-Fußabdruck etwa 5,3 Tonnen CO2 entsprechen.  <br> Auf der Skala von 1 bis 10 entspricht jeder Anstieg um 1 (z. B. von 2 auf 3 oder von 7 auf 8) einem Anstieg von etwa 500 kg Kohlendioxid. <br>"

    instructions_pd = "Als Nächstes werden Sie sehen, wie die Aufgabe aussehen wird. <br> Dann bitten wir Sie, <b>den CO2-Fußabdruck von 16 Personen mit unterschiedlichen Lebensstilen zu schätzen</b>."
    # task_example
    example_pa = 'So sieht der CO2-Fußabdruck einer Person in unserer Aufgabe aus. <br>'

    example_pb = 'Die unterschiedlichen Lebensstile dieser Personen beziehen sich auf: <ul> <li> <b>Ernährungsverhalten:</b> Die betreffende Person folgt entweder einer <b>Fleisch-basierten Ernährung </b> oder einer <b>Pflanzen-basierten Ernährung (vegetarisch)</b> </li> <li> <b>Recycling Verhalten:</b> Die betreffende Person <b>recycelt alles</b> oder <b>recycelt nicht</b> </li>  <li> <b>Regionalität der Lebensmittel:</b> Die betreffende Person kauft und konsumiert entweder <b>hauptsächlich regionale Lebensmittel </b> oder <b>auch importierte</b> Lebensmittel </li><li> <b>Stromvertrag basierend auf 7000 kWh Stromverbrauch einer Person:</b> Die betreffende Person hat entweder einen Stromvertrag abgeschlossen der <b>gemischt ist, also fossile Quellen und 40% erneuerbare Quelen beinhaltet</b> oder <b> 100% erneuerbare Quellen beinhaltet</b> </li> <li> <b>Arbeitsweg:</b> Die betreffende Person fährt jeden Tag die 20km zur und von der Arbeit, 5 Tage die Woche für 48 Wochen in Jahr <b>mit dem Fahrrad</b> oder <b>mit dem Bus</b> </li> <li> <b>Urlaubsreisen:</b> Die betreffende Person nimmt entweder <b>2 Mittelstreckenflüge pro Jahr (=3-6 Stunden)</b> oder <b>nimmt den Zug(z.B. London-Basel oder London-Amsterdam)</b> </li>'
    example_pc = ' <i>Das heißt, im obigen Beispiel ernährt sich die Person vegetarisch, recycelt nicht, isst regionale und importierte Lebensmittel, hat einen gemischten Stromvertrag abgeschlossen, pendelt jeden Wochentag mit dem Bus zur Arbeit und fährt mit dem Zug in den Urlaub.</i>  <br> '
    example_pd = 'Als Nächstes werden Sie den CO2-Fußabdruck von <b>16</b> Personen mit unterschiedlichen Lebensstilen einschätzen. <br> Bitte betrachten Sie jeden einzelnen CO2-Fußabdruck genau und nehmen Sie sich etwas Zeit, um Ihre Schätzung abzugeben. <br> Die Reihenfolge, in der die 6 Verhaltensweisen dargestellt werden, wird sich innerhalb der 16 gezeigten Beispielen, ändern.'
    example_pic = '/static/global/images/example_de.png '


