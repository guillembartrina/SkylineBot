# SkylineBot

Chatbot de Telegram per a la manipulació i visualització d'**skylines**, mitjançant un intèrpret

## Getting Started

Per posar el bot en marxa heu de seguir les següents instruccions

### Prerequisits

Necessiteu tenir `python3` instal·lat. A continuació podeu instal·lar totes les dependencies necessaries utilitzant el fitxer `requirements.txt` i la següent comanda:
```
pip install -r requirements.txt
```

### Execució

Per iniciar el bot simplement executeu:
```
python3 bot.py
```

## Utilització del bot

Assegureu-vos que el bot està en funcionament, seguint les instruccions de l'apartat *Getting Started*.
A continuació l'heu d'afegir al vostre **Telegram**, agregant un nou contacte i posant el seu username: `@GBM_SkylineBot`.
Per començar la conversa pulsar `start`.

### Edifici

Què és un *edifici*?
És un objecte que representa un edifici concret

- Es representa amb una terna `(s, h, e)`
s és el punt d'inici
h és l'altura
e és el punt final
amb e > s i h > 0


### Skylines

Què és un *skyline*?
És un objecte que representa un grup d'edifics a contrallum

Es poden crear de les següents maneres:
- un sol edifici: `(s, h, e)`
- un conjunt d'edificis: `[(s1, h1, e1), ... (sn, hn, en)]`
- un cojunt d'edificis aleatoris `{n,h,w,s,e}`
n és el numero d'edificis
h és l'altura màxima
w és l'amplada màxima
s és el mínim punt d'inici
e és el màxim punt final
amb n >= 0, h >= 0, w > 0, e > s

Operacions amb *skylines*: 
Un `skyline` és també:
* `skyline + skyline`: unió de skylines
* `skyline * skyline`: intersecció de skylines
* `-skyline`: efecte mirall
* `skyline * NUM`: duplicació NUM vegades
* `skyline + NUM`: trasllat NUM unitats cap a la dreta
* `skyline - NUM`: trasllat NUM unitats cap a l'esquerra

### Instruccions

Aquet bot incorpora les següents comandes: (també disponibles amb la comanda `/help` del del xat)

* /start: inicia el bot, missatge de benvinguda
* /help: mostra les comandes disponibles
* /author: mostra l'informació de l'autor del bot
* /lst: llista els skylines definits en la memòria de l'intèrpret
* /clean: elimina els skylines definits en la memòria de l'intèrpret
* /save [id]: guarda l'skyline 'id' de la memòria de l'intèrpret en la memòria del bot
* /load [id]: carrega l'skyline 'id' de la memòria del bot a la memòria de l'intèrpret
* /sky : llista els skylines guardats a la memòria del bot

El bot estarà atent a tots els missatges que li envieu i els intentarà interpretar com a instruccions.

Instruccions:

* Assignació: `ID := skyline`, assigna l'*skyline* a ID i mostra el resultat
On ID és un identificador alfanumèric que comença amb una lletra
* Avaluació: `skyline`, avalua *skyline* i mostra el resultat

## Authors

* **Guillem Bartrina Moreno** - *Projecte sencer*

