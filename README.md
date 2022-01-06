# Webprogrammeren en Databases voor Informatiekunde

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

*Versie: Januari 2022 (versie 1)*

In vier weken leer je hoe je een interactieve website maakt met behulp van het Flask-framework. We focussen op het maken van websites met een database-backend waarin gebruikersgegevens worden opgeslagen. Zo kun je in je verdere studie prototypes bouwen van applicaties en snel data verzamelen voor onderzoek. Er wordt gewerkt in vrij grote teams.

**Let op! Dit vak eindigt na de uitschrijfdeadline voor studietwijfelaars.** Overweeg je je uit te schrijven, dan mag je gewoon starten met het vak, maar zorg dat je je teamgenoten én de docenten vooraf op de hoogte brengt. Je kunt het vak gewoon volgen maar als je je uitschrijft krijg je geen studiepunten meer. Toch kan het vak een hele leuke ervaring zijn!

### Begeleiding

Dit vak is een projectvak. Voor het grootste deel ligt de verantwoordelijkheid bij de teams en de studenten om zelfstandig voortgang te maken. Zelfstandig betekent niet dat er geen hulp is! Begeleiding is er in de vorm van coaching, kritische vragen en simpelweg hulp op aanvraag.

De docenten zijn Robin Langerak en Martijn Stegeman, en je team wordt begeleid door twee mentoren (assistenten). Zij helpen je wegwijs maken, doen voor hoe je het beste de opdrachten kunt aanpakken en kijken je werk na. Elke week zijn er **voortgangsgesprekken** met je hele team en je mentor, op woensdag of donderdag.

Natuurlijk zijn er soms administratieve zaken. Voor uitzonderingen en persoonlijke afspraken moet je altijd een mail sturen naar <progik@mprog.nl>. Alles wat niet of niet duidelijk in deze studiewijzer staat moet schriftelijk worden afgestemd met de examinator Martijn Stegeman.


### Projecteisen

- Het project wordt gedaan in een team van 6-8 personen. Studenten werken afwisselend samen binnen dit team.
- Alle teamleden programmeren een individuele bijdrage die afgestemd is op hun voorkennis en comfort met programmeren.
- De website van je team is gebaseerd op één van de vaste projectstarters (zie onder) en de invulling van het project is voor de start goedgekeurd door de examinator.


### Team en Zulip

Tijdens het vak houd je contact met je teamgenoten en assistenten via Zulip. Op de eerste dag krijg je een uitnodiging voor deze omgeving. Check je spam-folder en zorg dat je direct contact legt met teamgenoten die niet fysiek aanwezig zijn. Dit is jullie gezamenlijke verantwoordelijkheid.

Als je geen contact krijgt met een teamlid moet je dit tijdens deze eerste dag nog laten weten aan de docenten (voor 14:00 uur via Zulip). Als een teamlid voor het eind van de dag geen contact heeft met de groep en/of met de docenten kan deze persoon worden uitgesloten van het vak.


### Elkaar helpen

Bij dit vak ligt er een speciale verantwoordelijkheid voor alle teamleden, ervaren en minder ervaren, om elkaar te helpen het vak tot een goed einde te brengen. Dit komt ook terug in de beoordeling.

- Onervaren studenten moeten een programmeertaak oppakken die uitdagend is voor hun niveau. Ervaren studenten helpen inschatten wat haalbaar is en wat leuk en goed is om te leren.
- Tijdens het project nemen de studenten die enige ervaring hebben het voortouw met het gebruiken van Git en het afstemmen van het werk van de teamleden.
- Ook hebben zij expliciet de taak om medestudenten te helpen om verder te komen en (voor hun niveau) uitdagende projecten aan te pakken.

### Kickoff

Maandag 10 januari ontvang je een eerste mail met meer informatie over wat je die dag moet doen. Zorg met absolute prioriteit dat je die hele dag online beschikbaar bent. Overigens is het essentieel dat je elke werkdag beschikbaar bent voor dit vak!


## Eindcijfer

Tijdens het vak doe je een aantal persoonlijke opdrachten en je werkt in een team aan een project. De cijfers worden als volgt samengesteld.

**Persoonlijke website** (25%)---jouw eigen kleine website bouw je in de eerste week. Deze wordt beoordeeld op uitgebreidheid van de site en kwaliteit van de code.

Om voor dit onderdeel punten te kunnen krijgen moet er genoeg code zijn om te kunnen beoordelen. Het is de bedoeling dat je mikt op de mimimumeisen zoals in de opdracht vermeld staan.

- Uitgebreidheid
    0. Weinig code of geen JS/CSS
    1. Voldoet niet helemaal precies aan de minimumeisen
    2. Voldoet volledig aan minimumeisen zoals vermeld in de opgave
    3. Richting 2x de minimumeisen
    {: start="0"}

- Kwaliteit
    0. Alleen gekopieerde code is netjes, opmaak code verder niet netjes
    1. Indentatie bijna overal consistent doorgevoerd
    2. Consistente indentatie, in alle files, opdeling code in blokjes door middel van witregels en duidelijke afscheiding grote onderdelen met hulp van comments
    3. Superconsistent, opdelen in files van redelijke omvang, her en der zinvolle comments
    {: start="0"}

**Individueel aandeel project** (50%)---jouw bijdrage aan het groepsproject wordt beoordeeld op uitgebreidheid, kwaliteit van de code, en diepgang van uitleg in je persoonlijk verslag.

Om voor dit onderdeel punten te kunnen krijgen moet je minimaal een redelijke hoeveelheid HTML, CSS en Flask hebben geschreven. Je hoeft niet per se JS te gebruiken.

Je moet tijdens het projectdeel (17--30 januari) minimaal 7 dagen aantoonbaar significant werk hebben gedaan. Uitzoeken, puzzelen en ontwerpen is ook werk! Als je het maar aantoont via het procesboek met screenshots, overwegingen, foto's. Voldoe je hier niet aan dan kun je geen punten krijgen voor het project.

- Hoeveelheid werk tussen 17 januari en 30 januari:
    0. Minimaal 7 dagen aantoonbaar siginificant en leerzaam werk gedaan
    1. Minimaal 8 dagen aantoonbaar siginificant en leerzaam werk gedaan
    2. Minimaal 9 dagen aantoonbaar siginificant en leerzaam werk gedaan
    3. Minimaal 10 dagen aantoonbaar siginificant en leerzaam werk gedaan
    {: start="0"}

- Kwaliteit HTML, CSS, JS
    0. Alleen wat is gecopy-paste is netjes, indentatie niet netjes
    1. Indentatie bijna overal consistent doorgevoerd
    2. Consistente indentatie, alle files op zelfde manier, opdeling in blokjes, visuele afscheiding grote delen
    3. Superconsistent, opdelen in meerdere files waar mogelijk en nodig, her en der zinvolle comments
    {: start="0"}

- Kwaliteit Python-code
    0. Grote delen zijn slordig
    1. Aardige basisstijl, maar functies zijn erg lang en niet opgesplitst, duplicatie van code
    2. Duidelijke onderdelen, prima stijl, redelijk wat comments
    3. Consistent opgemaakt, duidelijk afgescheiden onderdelen, onderdelen zijn kort en eenvoudig en hebben comments die overzicht helpen houden
    {: start="0"}

- Diepgang persoonlijk verslag
    0. Alleen opsommingen van wat gedaan is per dag of per week, geen uitleg van leerproces
    1. Plausibele connectie tussen bronnen en wat per dag gedaan is, maar weinig uitleg
    2. Per gemaakt onderdeel overzichtelijk wat gedaan is en welke bronnen en analyse van wat je hiervan geleerd hebt
    3. Voor enkele gemaakte onderdelen een duidelijke beschrijving van hoe het in elkaar zit, welke bronnen zijn gebruikt en <u>hoe</u> die bronnen hebben geholpen te leren; uitgebreide beschouwing op algemeen leren tijdens het vak.
    {: start="0"}

**Groepscijfer** (25%)---jullie groepsproject krijgt als geheel ook een cijfer voor consistentie in de werking van de site en in hoeverre <u>alle</u> studenten een passende, uitdagende bijdrage hebben gedaan en aantoonbaar van elkaar geleerd hebben. Aantonen kan met hulp van het procesboek dat elk teamlid bijhoudt.

- Algemene consistentie
    0. Website bestaat vrijwel geheel uit losse onderdelen bovenop de template
    1. Topnavigatie verbindt duidelijk alle onderdelen, wel aardig verschillend in werking/opmaak
    2. Navigatie is consistent, functionaliteit is wat losjes verbonden
    3. Navigatie is consistent, functionaliteit coherent, wel altijd ruimte voor "eigenheid" individuele bijdragen
    {: start="0"}

- Samenwerking en bijdrage
    0. Er zijn niet veel tekenen van samenwerken gevonden en/of diverse teamleden hebben niet genoeg uitdagend werk gedaan met hulp van anderen
    1. Voor sommige onderdelen is duidelijk op een zinvolle manier samengewerkt tussen teamleden maar enkele teamleden hebben vooral individueel gewerkt en/of niet uitdagend werk gedaan
    2. Vrijwel alle teamleden hebben aantoonbaar werk op hun niveau gedaan, samenwerking tussen verschillende leden is ook duidelijk uit dagelijks bijgehouden procesboek
    3. Alle teamleden hebben aantoonbaar werk op hun niveau gedaan, zijn gecoacht door ervaren medestudenten en groep heeft als geheel iedereen erbij gehouden
    {: start="0"}

Voor het groepscijfer is het essentieel dat teamgenoten elkaar uitgebreid helpen tijdens de projectfase, zelfs al doet iedereen een individuele bijdrage aan het project. Dit wordt onder andere gecontroleerd tijdens de voortgangsgesprekken, en via het procesboek dat elke student moet bijhouden.

Let op dat bovenstaande beschrijvingen **indicaties** zijn. Uiteindelijk vind er een weloverwogen oordeel plaats in samenspraak tussen mentoren, docenten en examinator op basis van het ingeleverde werk. Gebruik de indicaties om te begrijpen wat de bedoeling is, maar onthou dat als je specifiek op het randje gaat mikken, je kunt verwachten dat naar beneden wordt afgerond.

De opdrachten Profile, Movies en Fiftyville moeten vóór de respectievelijke deadlines (zie onder) perfect klaar zijn en ingeleverd worden om het vak te kunnen halen. Ze mogen niet blijven hangen.

## Projectidee

Tijdens het project kun je een geheel eigen idee kan uitwerken. Het is wel een kort vak met veel nieuwe stof, en dat maakt het lastig in te schatten wat er zoal kan in twee weken. Daarom zijn projecten gebaseerd op één van onderstaande projectstarters. Deze starters zijn uitdagend, maar tegelijk weten we dat ze haalbaar zijn in korte tijd. Het is, in goed overleg met het hele team en de mentoren, toegestaan om af te wijken van de projectstarters, als daar een goede reden voor is. Maar veel websites zijn simpelweg een variatie van één van onderstaande ideeën!

##### Keuze 1. Photo Sharing

Gebruikers kunnen publiekelijk foto's posten met of zonder begeleidende tekst. Alle gebruikers kunnen elkaar "volgen" en zo de foto's bekijken en liken 💕. Gebruikers kunnen in plaats van een eigen foto ook een gif zoeken uit een online API zoals die van <http://api.giphy.com>

Voorbeelden van functionaliteit:

1. Een **tijdlijn** of **gallerij** waarop meerdere foto's te bekijken zijn.
2. Een **foto-beheer** mogelijkheid, waarbij foto's kunnen worden toegevoegd en ook worden verwijderd.
3. Een **publiek gebruikersprofiel** waarop gebruikers elkaars foto's kunnen zien, en de ingelogde gebruiker de mogelijkheid heeft haar profiel aan te passen.
4. Een **comments-systeem** waarmee ingelogde gebruikers d.m.v. tekst en gif-jes vanuit een online API kunnen reageren op elkaars foto's.
5. Een **like-systeem en/of volg-systeem** waarbij gebruikers de mogelijkheid hebben foto's en andere gebruikers te "liken".

##### Keuze 2. Collectioneur

Gebruikers kunnen op basis van diverse eigenschappen zoeken naar items die afkomstig zijn uit een online database van *fijne dingen* zoals [recepten](http://developer.edamam.com) of [kunstwerken](http://rijksmuseum.github.io). Ze kunnen favorites opslaan op een publieke pagina en ze kunnen andere gebruikers tippen.

Voorbeelden van functionaliteit:

1. Een **overzichtspagina** waarop de verschillende items te zien zijn.
2. Een **zoekfunctie** waarmee een gebruiker de items kan doorzoeken.
3. Een **publieke verzameling** waarop een gebruiker items kan bijhouden.
4. Een **tip-functie** waarmee gebruikers elkaar kunnen tippen van zowel items als verzamelingen.
5. Een **upload-mogelijkheid** waarmee gebruikers hun eigen items kunnen toevoegen aan de verzameling.

##### Keuze 3. Trivia

Gebruikers kunnen triviavragen beantwoorden en op die manier punten scoren. Er is een interessant systeem om van andere gebruikers te winnen. De vragen komen uit een online triviadatabase zoals <http://jservice.io>.

Voorbeelden van functionaliteit:

1. Een **vraagpagina** waarop een gebruiker een triviavraag kan beantwoorden.
2. Een **quizpagina** waarop een gebruiker een quiz kan samenstellen.
3. Een **highscore-pagina** waarop de scores zowel per quiz als per gebruiker zichtbaar zijn.
4. Een **eigen-vraag-pagina** waarmee er een vraag kan worden toegevoegd aan de database.
5. Een **competitie-pagina** dezelfde quiz kunnen maken met een eigen highscore-pagina.


## Week 1

Deze week werk je aan een **persoonlijke website** tijdens de opdracht Profile, leer je over databases en **SQL**, en maak je **plannen** met je projectgroep om aan de gezamenlijke website te werken. Het is aan jou om het groepswerk en individueel werk goed te plannen.

| Belangrijke momenten week 1        |                               |
| ---------------------------------- | ----------------------------- |
| Registratie Zulip                  | maandag 10 januari 11:00      |
| Groepsmeeting                      | maandag 10 januari middag     |
| Projectidee [deadline]             | maandag 10 januari 18:00      |
| Groepsmeeting                      | dinsdag 11 januari ochtend    |
| Projectvoorstel [deadline]         | dinsdag 11 januari 18:00      |
| Mentorgesprek                      | woensdag of donderdag         |
| Opdracht: Movies [deadline]        | woensdag 12 januari 18:00     |
| Opdracht: Fiftyville [deadline]    | woensdag 12 januari 18:00     |
| Opdracht: Profile [deadline]       | vrijdag 14 januari 18:00      |

##### Projectidee

Op maandag ga je als team meteen beslissen welke richting jullie project op gaat. Jullie spreken in de middag met z'n allen af om richting te bepalen. Elke student gaat vervolgens in een paar punten opsommen wat ze zouden willen maken voor het project. Jullie maken hier een document van dat jullie aan het eind van de middag inleveren.

##### Projectmeeting

Op dinsdagochtend hebben jullie als compleet team een meeting waarin je de basis voor het officiële projectplan gaat leggen. Je doet nog een keer een rondje ideeën langs alle teamleden. Jullie komen tot een mondelinge afspraak voor een website waar je gezamenlijk naartoe wil werken. Op basis van deze afspraak werkt iedereen nogmaals de individuele bijdrage uit. Dit gaat als input naar het schriftelijke projectvoorstel.

##### Projectvoorstel

Dinsdagmiddag maken jullie een schriftelijk projectvoorstel waarin jullie gezamenlijk de website beschrijven die je gaat maken.

- Jullie geven de globale richting aan van wat je gaat maken
- Per teamlid:
    - Welke individuele onderdelen ze gaan maken
    - Hoe dit past bij de voorkennis van de student
    - Wat er geleerd gaat worden
- Alle teamleden worden geacht iets aan te pakken dat voor hen leerzaam is, afgestemd op hun voorkennis en comfort met programmeren
- Individuele plannen moeten bijna niet overlappen, óf elkaar juist zorgvuldig aanvullen (dan kan er op een zinvolle manier samengewerkt worden)
- Geef aan wie met wie (eventueel) gaat samenwerken en waaraan precies
- De ervaren studenten hebben een extra rol: geef aan welke studenten voortouw gaan nemen met gebruik van Git en consistent maken project

##### Projectpresentatie

Op basis van het voorstel maken jullie een projectpresentatie voor het mentorgesprek. Zie hieronder welke punten je daar moet benoemen.

##### Mentorgesprek week 1

Elke woensdag of donderdag spreekt het team uitgebreid met minstens 2 **mentoren**. Deze week ga je het plan presenteren.

Je krijgt dan mondelinge feedback van je mentoren, op basis waarvan je het plan kunt finetunen. Ook na bijstellen is je plan niet *automatisch* goedgekeurd. Jullie kunnen nog punten krijgen om te verwerken. Maar je kunt gewoon beginnen!

##### Individuele opdrachten

Let op de individuele opdrachten die je moet doen om SQL en HTML, CSS en Javascript onder de knie te krijgen.


## Week 2

Om te starten met de website heeft het team een **projectstarter** gekregen, die jullie gezamenlijk uitpluizen. Elke student heeft een werkende versie van de projectstarter draaien waarmee ze aan de slag kunnen. Je gaat je daarnaast verdiepen in de **technieken** die je nodig hebt om jouw aandeel in het project te volbrengen.

| Belangrijke momenten week 2       |                               |
| --------------------------------- | ----------------------------- |
| Project: Bootstrap [deadline]     | dinsdag 18 januari 18:00      |
| Project: Prototype [deadline]     | vrijdag 21 januari 18:00      |
| Mentorgesprek                     | woensdag of donderdag         |

##### Opstarten projecten

Volg de instructies voor het Bootstrappen van het project op de website. Eén teamlid maakt een groep aan op Github en de andere studenten komen erbij. Zorg dat je dit niet doet vóór de start van week 2. Je project moet namelijk aan onze cursus gekoppeld worden. Instructies worden rondgestuurd.

##### Prototype

Elke student zorg dat vrijdag een prototype klaarstaat van de functionaliteit van hun deelproject. Dat betekent licht opgemaakte pagina's met de juiste knoppen, invoervelden en dummy-content zoals teksten en plaatjes. Waarschijnlijk zijn de pagina's niet automatisch gegenereerd, maar de HTML en inhoud heeft hiermee een "vorm" gekregen.

##### Mentorgesprek week 2

Deze week draait het om het begrijpen van je projectstarter en opstarten van de individuele deelprojecten.

- Enkele teamleden **presenteren** hoe de projectstarter in elkaar zit, en wat er globaal moet gebeuren om jullie website te maken.
- Daarna vertelt elke individuele student wat ze tot nu toe gedaan hebben aan hun **individuele bijdrage**, en hoe ze aan de slag gaan.
- Iedereen vertelt daarbij ook wat ze verwachten dat moeilijk zal worden en hoe ze hierbij hulp gaan krijgen (van andere teamleden, of op een andere manier).


##  Week 3

Je kent nu de basis van de technieken die je gaat toepassen en je bent deze week keihard aan de slag om jouw **aandeel** in het project uit te werken. Dit is de week waarin het gaat gebeuren!

| Belangrijke momenten week 3       |                               |
| --------------------------------- | ----------------------------- |
| Mentorgesprek                     | woensdag of donderdag         |
| Project: Betaversie [deadline]    | vrijdag 28 januari 18:00      |

##### Betaversie

Elke student heeft individueel of in samenwerking met anderen een voorlopige versie klaar van de afgesproken functionaliteit: een onderdeel van de functionaliteit die <u>werkt</u>. De studenten die "pech" hebben gehad en nog niet klaar zijn worden verder geholpen door alle teamleden en de ervaren teamleden in het bijzonder. Dit gaat boven het perfectioneren van de eigen bijdrage. Hulp moet worden vastgelegd in de procesboeken van alle betrokkenen.

##### Mentorgesprek week 3

Bij deze bijeenkomst maak je met je mentoren plannen voor de afronding van het project.

- Alle teamleden geven een **persoonlijke update** waarin ook wordt doorgevraagd op details. Hiermee toetsen we al of elke student de eigen bijdrage goed onder controle heeft en voldoende leert.

- Er wordt een voorzichtig **plan** gemaakt voor het samenvoegen van al het werk. In sommige gevallen is dit al regelmatig gedaan en werkt iedereen in feite aan één site. In andere gevallen zal er nog flink tijd gestoken moeten worden om alles samen te voegen. De studenten met ervaring nemen hier het voortouw in.


## Week 4

Deze week gaan jullie als groep **afronden**. Maandag worden alle individuele bijdragen definitief samengevoegd. Dan maakt de groep een plan om nog kleine verbeteringen te doen. Deze verbeteringen zijn uiterlijk dinsdag verwerkt in het eindproject, dat dan definitief ingeleverd wordt.

| Belangrijke momenten week 4       |                               |
| --------------------------------- | ----------------------------- |
| Project: Samenvoegen [deadline]   | maandag 31 januari 18:00      |
| Definitieve versie [deadline]     | dinsdag 1 februari 18:00      |
| Mentorgesprek                     | woensdag of donderdag         |
| Virtuele presentatie [deadline]   | donderdag 3 februari 18:00    |

##### Definitieve versie

Voor de definitieve versie zijn alle individuele bijdragen goed samengevoegd tot één enkele Flask-applicatie. De ervaren studenten helpen bij technische problemen op dit vlak (en de assistenten natuurlijk ook!). Daarna is het een kwestie van zorgen dat alles nog netjes werkt, straktrekken van inconsistenties, en elkaar helpen de code zo netjes mogelijk te maken.

##### Virtuele presentaties

Bij de afloop van het vak verzamelen we alle gemaakte websites. Alle studenten, docenten en familie en vrienden kunnen deze sites dan bekijken. Bij de site staat optioneel een screencast met uitleg en een korte demo. De websites blijven na afloop een tijdje beschikbaar.

##### Mentorgesprek week 4

Bij deze laatste bespreking zijn mentoren en docenten aanwezig voor de eindbeoordeling van de projecten. Na de presentaties gaan zij ook naar de ingeleverde code kijken.

- Enkele studenten presenteren eerst het **globale idee** van de website.

- Daarna presenteren alle groepsleden hun eigen bijdrage: eerst demo'en wat je hebt gemaakt en daarbij kort uitleggen hoe het technisch in elkaar zit (met een blik op de code). Je beschrijft ook wat de belangrijkste dingen zijn die je geleerd hebt. Hiermee vindt de definitieve toetsing plaats of je persoonlijk voldoende hebt geleerd.


## Meer informatie

### Procesboek

Alle studenten houden een procesboek bij. Hierin schrijf je elke dag wat je nieuw bent tegengekomen, waar je vragen over hebt op dat moment, wie je heeft geholpen (teamgenoten en assistenten, met naam erbij), wat de oplossing voor je vraag was, welke blokkades je had bij het programmeren en hoe je daar uit bent gekomen, en je ideeën voor de komende dagen of voor de mentorgesprekken. Het procesboek is een essentieel onderdeel van de beoordeling van het groepsproject. Als één van de teamleden het niet goed bijhoudt leidt dit mogelijk tot een lager cijfer voor het groepsdeel.


### Aanwezigheid

Je moet **dagelijks** contact hebben met meerdere groepsgenoten, op locatie of via Zoom. Maar: als de universiteit gesloten is voor bijeenkomsten dan mag je ook niet ergens anders fysiek afspreken. Is de universiteit "normaal" open dan verwachten we je daar aanwezig voor de wekelijkse voortgangsgesprekken, maar niet per se voor de andere activiteiten. Hou er rekening mee dat sommige teamleden niet zo comfy zullen zijn met naar de universiteit komen. Dat is prima. Als er maar goed contact onderhouden wordt via Zulip, Zoom en Wonder. Jouw team kan alleen een hoog cijfer halen als er goede onderlinge begeleiding en hulp is. Alle teamleden moeten **altijd** aanwezig zijn bij alle mentorgesprekken.


### Groepsdynamiek

Voor het groepcijfer is het essentieel dat teamgenoten elkaar <u>aantoonbaar</u> helpen om een uitdagende bijdrage aan het project te doen. Hiervoor is afstemming en vorming van subgroepen noodzakelijk. Mocht je in goed overleg uit de groep moeten stappen, dan kun je geen punten krijgen voor het groepsdeel van het project. Als er *vooraf* geen goed overleg is met de vakcoördinator kun je niet uit de groep stappen of gezet worden. Zorg dus dat je contact opneemt bij problemen.


### Voorkennis

We verwachten dat je bekend bent met de beginselen van programmeren in Python. Als je al bij een andere opleiding een vak hebt gevolgd over webprogrammeren is dit vak niet voor jou, en moet je vrijstelling aanvragen bij de examencommissie. Heb je voorkennis op een andere manier, dan is dit geen probleem: je moet dan je teamgenoten helpen om goed te presteren (en zeker niet al het werk in je eentje doen want dan kan het project niet beoordeeld worden).


### Vragen stellen

Tijdens dit vak zul je vaak de hulp inroepen van de assistenten en medestudenten. Er zijn diverse opties voor het stellen van vragen. De beste optie hangt af van het soort vraag dat je wil stellen.

**Zulip en Wonder:** direct contact met je team en studenten.

- onderlinge support
- snelle vragen over deadlines, contact met samenwerkpartner
- mentor is niet doorlopend beschikbaar!
- voor alle uitzonderingen of bijzondere situaties een mailtje sturen

**Programmeerbalie via Wonder:** direct contact met een assistent.

- hulp <u>alleen</u> via een videogesprek waar je je scherm kunt delen
- je weet niet waar te beginnen of een onvindbare bug
- dagelijks 13-17 uur, wachttijd kan oplopen
- vooraf een afspraak maken via de website

**Helpdesk:** voor technische problemen.

- problemen met je computer
- problemen met de werking van je online IDE of git
- hele nare bugs
- vooraf een afspraak maken via de website

**Mail:** contact met de vakcoördinatoren via <progik@mprog.nl>.

- maken van persoonlijke planningsafspraken
- meedenken over grote problemen met het vak
- andere officiële zaken
- administratie na afloop van het vak


### Herkansingen

Een projectvak als dit kent geen herkansingsmogelijkheden. Mocht je onverhoopt langdurig ziek worden (>4 werkdagen) dan ligt het voor de hand om het vak in het volgende jaar nogmaals te doen. Mocht je je zorgen maken over de consequenties, bespreek het dan zeker!

Afhankelijk van de situatie is het misschien toch mogelijk het vak af te ronden vóór 5 februari, bijvoorbeeld door in het weekend in te halen. Maar dit is natuurlijk niet altijd de gezondste keuze. Overleg dus goed met de studieadviseur over je opties.

Als je te laat contact opneemt met de docenten kan er helaas niets meer geregeld worden, omdat de volgende vakken snel gaan beginnen en er geen inhaalmogelijkheid is.
