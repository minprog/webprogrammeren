# Oefeningen

Deze vragen zijn goede oefeningen voor het tentamen. De verwachting is dat je alle vragen op het tentamen correct beantwoordt, foutjes daargelaten. Je hebt dus parate kennis nodig van de regels die je nodig hebt om via `pup` informatie uit een HTML-pagina te extraheren.

Je kunt onderstaande oefeningen niet inleveren en ze horen dus ook niet bij de deadline voor de Scraping-module.

## HTML

Gegeven is dit HTML-document in een bestand `about.html`:

    <html>
      <head>
        <title>Sample Document</title>
      </head>
      <body>
        <div id="header">
          <h1>Welcome to my website</h1>
          <nav>
            <ul>
              <li><a href="/home">Home</a></li>
              <li><a href="/about">About</a></li>
              <li><a href="/contact">Contact</a></li>
            </ul>
          </nav>
        </div>
        <div id="main-content">
          <h2>About Us</h2>
          <p>We are a company that specializes in web development.</p>
          <p>We have been in business for 10 years.</p>
        </div>
        <div id="footer">
          <p>Copyright © 2022 Sample Company</p>
        </div>
      </body>
    </html>

## Opdrachten

Geef complete `pup`-oneliners's om het antwoord te geven op de volgende vragen. Start met `cat about.html`. Geef ook de uitkomst!

1. What is the text of the h1 element in the #header div?
1. What is the href of the first a element within the nav element?
1. What is the text of the second p element within the #main-content div?
1. How many a elements are within the nav element? (deze kun je beantwoorden door te combineren met een ander UNIX-commando, want pup kan niet tellen)
1. What is the text of the p element in the #footer div?

(Deze oefening is gegenereerd met ChatGPT.)
