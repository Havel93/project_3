# project_3
Projekt pro získání certifikátu Engeto akademie.
## Co projekt dělá?
Tento projekt slouží k extrahování volebních výsledků z roku 2017. Odkaz naleznete [zde](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)

## Jak nainstalovat knihovny?
Knihovny, které jsou použity v kódu naleznete v souboru requirements.txt. Verze pythonu je 3.11. Doporučuje se nové vývojové prostředí.
```console
pip --version                       #overi verzi pythonu
pip install -r requirements.txt     #snad nainstaluje knihovny
```
## Jak spustit projekt?
K spuštění souboru vysledky_voleb.py potřebujete dva povinné argumenty.
Prvním je odkaz na okres
Druhý je název souboru, do kterého budou data uložena.
Po zadání obou argumentů se vám vytvoří CSV soubor s výsledky hlasování v zadaném okresu.

## Ukázka průběhu
V našem případě stahujeme data z okresu Plzeň-sever.
První argument: "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=4&xnumnuts=3205"
Druhý argument: "vysledky_plzen-sever.csv"

Spuštění programu:

```console
 python vysledky_voleb.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=4&xnumnuts=3205" "vysledky_plzen-sever.csv"
```

Průběh:
```console
STAHUJI DATA Z VYBRANEHO URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=4&xnumnuts=3205
```
Uložení a ukončení:
```console
UKLADAM DO SOUBORU: vysledky_plzen-sever.csv
UKONCUJI electin-scraper
```

Částečný výstup:
```
code	location	registred...
566756	Bdeněves	510	367...	
558656	Bezvěrov	551	259...
```






