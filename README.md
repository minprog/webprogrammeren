# Inleiding Dataverwerking<br> en Webtechnieken<br><small>Tools voor Data Science</small>

<style>
    h2
    {
        break-before: page;
    }
    h1, h2, h3, h4, h5
    {
        break-after: avoid-page;
    }
</style>

*Versie: Januari 2024 (versie 1)*

In vier weken ga je aan de slag met diverse platforms voor dataverwerking en webtechnieken. Elke module staat in principe op zich, maar bouwt wel enigszins op je eerder opgedane programmeerervaring. Dat betekent **niet** dat je het vak Programmeren IK gehaald moet hebben om dit vak goed te kunnen doen! Maar je moet wél een begin hebben gemaakt met programmeren en wat handigheid gekregen.

**Let op! Dit vak eindigt na de uitschrijfdeadline voor studietwijfelaars.** Overweeg je je uit te schrijven, dan mag je gewoon starten met het vak. Als je je uitschrijft krijg je geen studiepunten meer, omdat de uitslag wordt vastgelegd op de laatste vrijdag van het vak (en dan is het al 2 februari).


## Rooster

- Zie [Datanose voor het rooster](https://datanose.nl/#course[121180]).
- Niet alle groepen hebben tegelijk les. Je moet altijd naar je eigen groep.
- Alle bijeenkomsten zijn verplicht, tenzij je alle opdrachten van het hele vak af hebt.
- Het hertentamen van Programmeren IK is gepland op 30 januari in de avond.
- Het tentamen van dit vak is gepland op 2 februari in de vroege middag.


## Docenten en assistenten

De docenten bij dit vak zijn Martijn Stegeman en Imane Tarrahi. Zij geven het vak vorm en verzorgen de organisatie. Je kunt ze bereiken via e-mail op <python@proglab.nl>. Daarnaast zijn er veel student-assistenten, die de cursus goed kennen en jou gaan helpen op de momenten dat het nodig is: Pim Dijkhuizen, Moad Matoug, Melih Metin, Floor van Steijn en Floor Verkade.


## Onderwerpen

We behandelen uiteenlopende onderwerpen in modules:

1. **Homepage (basisvaardigheid).** Leren schrijven van HTML en begrijpen hoe dit in de browser wordt ingeladen als DOM. Kennis maken met CSS en Javascript.
2. **UNIX (essentieel).** Kennismaken met de onderdelen van besturingsystemen. Een uitgebreide verkenning van de UNIX shell.
3. **Databases (basisvaardigheid).** Kennismaken met de relationele manier om data vast te leggen. Oefenen met het schrijven van SQL-queries om interessante data uit een database te halen.
4. **Reguliere expressies (basisvaardigheid).** Leren hoe je teksten kunt filteren en selecteren met hulp van reguliere expressies en het commando `grep`.
5. **Pandas (basisvaardigheid).** Data modelleren in Pandas zodat je Python kunt gebruiken om grote datasets te analyseren. Je gaat oefenen met allerlei commando's die je hiervoor kunt gebruiken.
6. **Scraping (basisvaardigheid).** Oefenen met het geautomatiseerd scrapen van informatie van websites, om deze informatie verder te kunnen verwerken in eigen programma's.
7. **Flask (geavanceerd).** Kennis maken met Flask als platform om webapplicaties mee te bouwen. Een webapplicatie bouwen als opdracht en ruimte om zelf uitbreidingen te maken.

Alle modules bestaan uit individuele opdrachten die helpen oefenen voor toetsjes en tentamen. De opdrachten zelf tellen niet mee.


## Kalender en deadlines

De activiteiten zijn in de weken als volgt **ingepland**. Elke week zijn er twee onderwerpen. Je kunt voor een deel zelf schuiven met activiteiten binnen de week, maar je kunt verwachten de volle werkweek bezig te zijn met het vak.

De **workshops** vinden plaats tijdens de les op dinsdag, en hebben als doel om te zorgen dat je goed op weg bent en geen installatie- of configuratieproblemen hebt.

Het kan goed zijn dat je het moeilijk vindt en wat moet **schuiven** met de modules. Het is akkoord om dit te doen, maar je moet wel elke week voortgang maken en inleveren. In de derde week is het handig om advies te vragen aan Imane of Martijn welke onderwerpen je het beste aandacht kunt geven.

De opdrachten Homepage en Finance worden na de hieronder genoemde **deadlines** nagekeken en kunnen daarna niet meer worden ingeleverd om welke reden dan ook.

**Week 1**

| ma                  | di                        | wo         | do                         | vr                                                |
|---------------------|---------------------------|------------|----------------------------|---------------------------------------------------|
| homepage<br>lecture | **carpentry<br>workshop** | unix       | homepage                   | **toetsje<br>unix**                               |
| homepage            | unix                      | unix       | homepage                   | homepage                                          |

Deadline Homepage: vrijdag 12 januari 17:15 uur

**Week 2**

| ma                  | di                        | wo         | do                         | vr                                                |
|---------------------|---------------------------|------------|----------------------------|---------------------------------------------------|
| database<br>lecture | **database<br>workshop**  | fiftyville | regex                      | **toetsje<br>databases, regex**                   |
| movies              | movies                    | regex      | regex                      | regex                                             |

**Week 3**

| ma                  | di                        | wo         | do                         | vr                                                |
|---------------------|---------------------------|------------|----------------------------|---------------------------------------------------|
| scraping            | **pandas<br>workshop**    | pandas     | scraping                   | **toetsje<br>pandas, scraping**                   |
| scraping            | pandas                    | pandas     | scraping                   | scraping                                          |

**Week 4**

| flask<br>lecture    | finance                   | finance    | tentamen-<br>voorbereiding | tentamen-<br>voorbereiding                        |
| finance             | finance                   | finance    | **13:00<br>q&a sessie**    | **tentamen<br>unix,db,regex,<br>pandas,scraping** |

Deadline Finance: woensdag 31 januari 17:15 uur


## Cijfers

Hieronder vind je per module de punten die je kunt verdienen.

- **Homepage** (2 punten)
    - 2 punten voor een prettig werkende en informatieve persoonlijke website, voldoende en volgens de eisen ingeleverd

- **UNIX** (4 punten)
    - 1 punt door op het wekelijkse toetsje te laten zien dat je op dat moment de basis beheerst, inclusief het uit je hoofd kennen van diverse UNIX-commando's
    - 3 punten mits voldaan aan:
        - de twee schrijfopdrachten voldoende en volgens de eisen ingeleverd
        - op tentamen aangetoonde basiskennis middels schrijven van one-liners

- **Databases** (4 punten)
    - 1 punt door op het wekelijkse toetsje te laten zien dat je op dat moment de basis beheerst, zoals het schrijven van eenvoudige select-queries
    - 3 punten door op het tentamen aangetoonde kennis van sql-operaties en manieren om gegevens uit meerdere tabellen te combineren, middels het schrijven van diverse sql-queries

- **Reguliere expressies** (3 punten)
    - 1 punt door op het wekelijkse toetsje te laten zien dat je op dat moment de basis beheerst, door het schrijven van eenvoudige reguliere expressies
    - 2 punten door op het tentamen aangetoonde kennis van de elementaire symbolen in reguliere expressies en hun werking, middels schrijven van grep-commando's

- **Pandas** (4 punten)
    - 1 punt door op het wekelijkse toetsje te laten zien dat je op dat moment de basis beheerst, door het schrijven van eenvoudige Pandas-operaties
    - 3 punten door op het tentamen aangetoonde kennis van Pandas-operaties en manieren om data in Dataframes te manipuleren, middels het schrijven van codefragmenten in Python met Pandas

- **Scraping** (3 punten)
    - 1 punt door op het wekelijkse toetsje te laten zien dat je op dat moment de basis beheerst, door het schrijven van eenvoudige commando's om informatie te scrapen uit een HTML-bestand
    - 2 punten door op het tentamen aangetoonde kennis van CSS selectors en toepassing om informatie te scrapen uit HTML-bestanden, middels het schrijven van scraping-oneliners

- **Flask** (3 punten)
    - 2 punten te verkrijgen mits opdracht voldoende en volgens de eisen ingeleverd
    - 1 punt voor een extra zelfbedachte feature van de website

Over het algemeen worden geen deelpunten gegeven.

Het maximumaantal punten is 23 en daarmee is de formule voor een eindcijfer `punten / 23 * 9 + 1`.


## Aanwezigheidsplicht

Er geldt een aanwezigheidsplicht voor alle activiteiten in het vak.

De ochtendsessies lopen van 9:00 tot 12:30 en de middagsessies van 13:30 tot 17:00 uur.

Als je minimaal 5 van de 7 bijeenkomsten volledig bijwoont (maximaal 15 minuten te laat en maximaal 15 minuten eerder vertrekken), dan mag je het hertentamen maken. Ben je niet voldoende aanwezig dan mag je geen hertentamen maken.

Als je heel erg goed gaat dan kun je de ruimte nemen om de opdrachten versneld af te maken. Zodra je *alle* opdrachten af hebt en ingeleverd, moet je nog één keer langskomen om ze te bespreken met Imane of Martijn. Dan kun je ontheffing van de aanwezigheidsplicht krijgen.

Studenten die in het tweede jaar van de opleiding Informatiekunde zitten en dit vak al een keer gevolgd hebben zijn uitgezonderd van de aanwezigheidsplicht, op voorwaarde dat opdrachten en oefeningen zijn ingeleverd op de laatste dag van het betreffende onderwerp in bovenstaande kalender. Je mag sowieso gewoon komen, maar altijd alleen in de ingedeelde groep.


## Toetsing en eindcijfer

Elk onderwerp wordt op een eigen manier getoetst. In de meeste gevallen is er sprake van zelfstandig uitwerken van open vragen op het tentamen.

Je moet voor de meeste opdrachten bijhouden welke dingen je hebt geleerd die jou opvielen, maar ook welke bronnen je hebt gebruikt en wat voor soort hulp je hebt gevraagd. Bij de meeste opdrachten wordt gevraagd om dit in te vullen. Deze opmerkingen zijn belangrijk om aan te tonen dat je productief aan de cursus hebt gewerkt. Je kunt dit deel van de opdrachten dus niet overslaan, anders kun je geen punten krijgen.

Je eindcijfer is een optelling van de punten die je met de goede uitgewerkte opdrachten kunt halen. De meeste onderdelen komen ook terug op het tentamen. Daar moet je van de geleerde talen en technieken laten zien dat je ze voldoende (dus niet per se perfect) beheerst. Alleen als je dat laat zien krijg je de punten voor de betreffende onderdelen.


## Samenwerken

Je mag met je medestudenten (en anderen) communiceren in het Nederlands of Engels over je werk in deze cursus, maar niet in de vorm van meer dan een paar regels Python, JavaScript, HTML en dergelijke talen. Als je twijfelt of je manier van werken in deze correct is, neem gerust contact op met de docenten.


### Citeren en hulpbronnen

Je mag gerust op het web zoeken naar uitleg die verder gaat dan de colleges en andere materialen die in de cursus bijgeleverd zijn, en je mag op zoek naar oplossingen voor technische problemen waar je tegenaan loopt, maar je mag zeker geen oplossingen voor onderdelen van de opdrachten overnemen om aan de eisen te voldoen. Daarnaast moet je bij het geheel of gedeeltelijk overnemen van codefragmenten of werken via tutorials en dergelijke altijd een precieze bronvermelding doen. Voor de meeste opdrachten geldt dat je zélf een antwoord of uitwerking moet formuleren.


### Officiële regels

Wat betreft fraude en plagiaat volgen we in deze cursus de richtlijnen van de Universiteit van Amsterdam en de werkwijze van de bachelor Informatiekunde. De richtlijnen kun je [hier vinden](https://student.uva.nl/onderwerpen/plagiaat-en-fraude).
