# Oefeningen

Deze vragen zijn goede oefeningen voor het tentamen. De verwachting is dat je alle vragen op het tentamen correct beantwoordt, foutjes daargelaten. Je hebt dus parate kennis nodig van reguliere expressies. Als je merkt dat je deze kennis nog niet echt paraat hebt, dan kun je extra studeren met hulp van het materiaal in deze module.

Je kunt onderstaande oefeningen niet inleveren en ze horen dus ook niet bij de deadline voor de regex-module.

Onderstaande vragen zijn *grotendeels* representatief voor de vragen die je op het tentamen tegen zou kunnen komen. De vraagstelling kan wat anders zijn maar je zult sowieso `grep`-commando's op basis van reguliere expressies moeten schrijven (in feite gewoon alle stof uit het boek). Alle vormen van reguliere expressies van [de opdrachten op deze pagina](/regex/opdrachten) kunnen voorkomen.

## Tekst

Gebruik de volgende tekst (door Robin Langerak) als context voor de opgaven hieronder. De tekst op het tentamen zal korter zijn zodat je makkelijker je antwoorden kan nalopen.

     1    Where the world ends
     2
     3    The wall was high, but no one knew its length. We had tried to go underneath but no luck:
     4    even a tunnel thirty feet long didn't bring us to the other side.
     5
     6    The previous night you vandalised the wall by throwing rocks at it with all the
     7    strength you had in you. Did you really think you could breach it that way? Only
     8    when we saw you make handholds out of the chips and cracks you caused the night
     9    before we understood. At first you climbed hesitantly, so concentrated that there
    10    was no room for your usual dry humour, But soon we saw you move with more
    11    confidence. The higher you reached, the more people came to watch. I am still not
    12    sure if they came to see you labour against gravity or to see you fall.
    13
    14    The long trip through the mountains had gone at the cost of your weight but you
    15    still had the trained muscles you have always had because you had carried grandma.
    16
    17    Halfway up the wall you looked down as if to vocalise the thought: "See... it's
    18    not that hard!" But the sweat stains that colourised your shirt told us something
    19    different. We all held our breath when you climbed the wall with what must have
    20    been the last of your strength. When you finally managed to swing a leg over the
    21    edge a deafening cheer rose up from the crowd that stood watching and everyone weighed in.
    22
    23    For a moment you lay panting on top of the wall. Then you stood and waved at us.
    24    Was it a greeting or a goodbye? You disappeared from sight and for a moment the crowd
    25    continued to cheer. Immediately others ran to the wall as well to try to repeat your
    26    success. But one by one people gave up or fell down. Us, the ones with too little
    27    left to even attempt the climb, stood watching the spot where we had last seen you.
    28
    29    After a long time of waiting the first people started to return to what they called home
    30    here. For a moment you had given me hope, but most of us had lost too much to still
    31    know what hope is. Now only grandma and me are left. We've been waiting here a while
    32    now, even though I don't recall when it was that we have last seen you.
    33    Why don't you give us a sign of life...

## Vragen

Schrijf voor alle opgaven een complete oneliner die het gevraagde resultaat geeft. Gebruik een vorm van `grep`, `egrep` of `fgrep`, en als invoer de bijgeleverde tekst 'Where the world ends.txt'. Geef ook expliciet aan welke regels matchen.

1. Vind alle voorkomens van de tekst `length`, `strength` of `weight`
2. Vind alle regels met zinnen die beginnen met het woord `But`
3. Vind alle regels met zinnen die eindigen op `...`. Let op dat voorkomens van `...` die niet aan het eind van de zin staan niet meetellen.
4. Vind alle voorkomens van woorden die eindigen op `ise`
5. Vind alle voorkomens van woorden die eindigen op `our`, uitgezonderd de woorden `our` en `your`. Let op! Je mag meerdere commando's gebruiken
