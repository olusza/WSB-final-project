# WSB-final-project

## Testy automatyczne modułów

Obecnie są dostępne dwa moduły: 

* Logowanie (kod LG)
* Rejestracja (kod RU)

W katalogu Modul\_{kod\_modułu} znajdują się pliki z testami automatycznymi dla modułu. W celu uruchomienia testów należy uruchomić plik kontroler\_{kod\_modułu}.py

Przykład dla modułu Rejestracji:
```
$ cd Modul_RU
$ python kontroler_RU.py
```
## Wymagania:
* Selenium WebDriver
* Sterowniki dla przeglądarek: Chrome (chromedriver), Firefox (geckodriver) oraz Edge (Microsoft WebDriver)