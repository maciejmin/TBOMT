## Poradnik: jak utworzyć dodatek do gry TBOMT w języku polskim.
jeśli ktoś chce pomóc, może zrobić wersję angielską tego pliku i wysłać nam na naszego maila (the_beginning_of_modern_times@galaxyhit.com) podając co chce, aby było umieszczone w ramach podziękowania.
## Kroki:
1. Wymagania
2. Co zamieścić
3. Jak zrobić
4. Gdzie wrzucić
5. Dla zaawansowanych
## 1. wymagania
Ważną rzeczą jest, aby użytkownik znał Pythona na poziomie conajmniej podstawowym, jeżeli chce utworzyć dosyć poważne rozszerzenie. Wymagane są rzeczy typu
1. znajomość zmiennych, list w Pythonie;
2. wiedza na temat tworzenia funkcji;
3. jeżeli chcemy zrobić rozszerzenie które edytuje np. generowanie terenu potrzebujemy znajomości struktury plików na różnych systemach, pobierania źródeł z internetu (aby nie zapełniać niepotrzebnie miejsca na komputerze użytkownika), edycji plików funkcją open() i biblioteką Pythona „os”.

Jeżeli chcesz się dowiedzieć więcej o różnych plikach wbudowanych w naszej grze zajrzyj do punktu 4.
## 2. Co zamieścić
Osobiście najbardziej lubimy chyba zwykłe dodatki broni, mikstur itd. Nie zaszkodzi również, jeżeli będzie edycja animacji gracza, dodania innych postaci, biomów a nawet całkowita edycja mechaniki gry, rób tylko co chcesz!
## 3. Jak zrobić
Ten krok może wydawać się skomplikowany, ponieważ to już czysty Python. Jeżeli chcesz zrobić edycję skinów czy coś, wystarczy, że pobierzesz coś, co niedługo zrobimy. Spokojnie, możesz już zaczynać! Jeżeli chodzi jednak o dodatek do gry w formie czegoś nowego musisz bazować się na tym:
zaraz podam przykładową funkcję (bo na tym opierają się dodatki) ale jak na razie powiem, że należy pamiętać, że celem dodatku jest uruchomienie pewnej jego funkcji w pewnym fragmencie programu np.
```
#v1.1.2
import os
os.system("cls") #funkcja czyszcząca terminal
print("hi!")
```
To był fragment kodu w oryginale, plik extensiondownloader.py pobiera twój dodatek i zamiast takiego kodu, wychodzi taki:
```
#v1.1.2
import os, extensions.twoj_dodatek #zaimportowano twój dodatek
os.system("cls")
print("hi!")
extensions.twoj_dodatek.example() #dodanie twojej funkcji z dodatku
```
jak widać, dodano dwie rzeczy:
1. zamiast zwykłego `import os`, pojawiło się `import os, extensions.twoj_dodatek`, dlaczego? Otóż program właśnie zaimportował twój dodatek razem z innym (`import os` to akurat nie dodatek, a biblioteka ale to było w celu przykładu).
2. Dodano linię kodu `extensions.twoj_dodatek.example()`, który powoduje wywołanie funkcji w twoim dodatku

Podsumowując te wycinki: jak w takim razie wygląda dodatek? Otóż proszę bardzo, poniżej jest przykład:
```
#v1.0|https://tbomt.7m.pl/extensions/twoj_dodatek.py
def example():
	print("Dodatek działa!")
#-#
#i|4|extensions.twoj_dodatek.example()
```
I to tyle. Przestudiujmy więc każdą linijkę kodu:
1. `#v1.0|https://tbomt.7m.pl/extensions/twoj_dodatek.py` - Jedna z ważniejszych linijek kodu! Jej rozkład jest następujący, dzielimy tą linię na 3 części: "v1.0", "|" i "http...k.py" czyli 1. wersja, 2. taki "|" znak, 3. link. To należy podać. Pierwsza część: Twórca dodatku umieszcza dowolny tekst, który przy każdej następnej aktualizacji dodatku **powinien zostać zmieniony**. Dlaczego? Bo oznacza on wersję gry i nasza gra podczas aktualizacji (plik "updater.py" na repozytorium) sprawdza, czy wersja programu w lokalnym pliku jest inna niż wersja programu w pliku na stronie źródła (o stronie źródła w trzeciej części pierwszej linijki kodu), jeżeli jest inna: Aktualizuj dodatek/program, jeśli nie, nic nie rób. Tak działa mechanika aktualizacji naszej gry. Część druga: "|", do czego służy to oddzielenie? Wstawiamy je pomiędzy wersją, a linkiem, dzięki temu nasz program wie, jak odróżnić te dwie rzeczy od siebie, co jest szczegółem, dla ciebie **poprostu musi tam być**. Trzecia część, czyli link. Link do twojego pliku w internecie, należy pamiętać o tym, aby link był z https:// na początku (bądź http:// dla starszych witryn lub bez szyfrowania SSL) oraz o tym że ma być pełny link, na przykładzie linków firmy Google: nie `https://g.co/program`, tylko `https://g.co/program`**`.py`**.
2. `def example():` - definicja funkcji. W parze z trzecią linijką. Potem zostaje wywołana ta funkcja.
3. `print("Dodatek działa!")` - wewnątrz funkcji. W parze z drugą linijką. Gdy funkcja zostanie uruchomiona, na konsoli wyświetla się napis „Dodatek działa!”.
4. `#-#` - (dwa hasztagi i myślnik wewnątrz) bardzo ważna linijka, dzięki niej, program wie, że tutaj funkcje się kończą. Po tym nie wstawiamy funkcji, tylko linijki typu linijka 5.
5. `#i|4|extensions.twoj_dodatek.example()`, to już (prawie) nie jest Python. Tą linijkę trzeba albo zapamiętać, albo mieć ten podręcznik stale otwarty podczas programowania dodatków. Co tu się dzieje? Znowu dzielimy na części ten fragment, tym razem na 5. ***1.*** "`i`", ***2.*** "`|`", ***3.*** "4", ***4.*** "|" i ***5.*** "`ext...e()`". Co to oznacza? Zacznijmy od pierwszego: `i` oznacza dla nas "insert" czyli wstaw linijkę swojego kodu który jest w piątej części (bo działa to tak, że twój dodatek planuje w której linii kodu ma zadziałać). Wpisujemy tutaj sposób, my mamy dwa sposoby: "i" i "r", i oznacza insert, która wstawia po którejś linijce np. w czwartej linijce (na przykładzie poprzedniego programu) znajduje się "`print("hi!")`", wpisując "i" jako sposób wstawiania, a następnie (co będzie w 3 części) 4, wiemy, że mamy wstawić twój kod po linijce czwartej (czyli po `print("hi!")`). Używając funkcji "r", co oznacza re-write, program nasz wie, że mamy po prostu zamienić tą linijkę z wymyśloną przez twórcę dodatku np. gdy zamiast `print("Welcome.")` chcemy zrobić postać bardziej przyjazną, dlatego wstawiamy `print("Hi!")`. ale o tym będzie też w następnych krokach. 2. "|", oddzielenie: raczej tylko dla naszej wiedzy, dla ciebie - po prostu musi ono być w tym miejscu. 3. "4", oznacza w której linijce ma zostać wykonana czynność opisana w kroku 1. 4. "|", ponownie oddzielenie. 5. Linijka kodu która ma zostać wstawiona zgodnie z oczekiwaniami kroku 1. i 3.

I to wszystko, linijek typu linijka  5. można wstawić kilka jedna pod drugą, oraz umieścić kilka funkcji we wcześniejszych linijkach jeżeli chcemy zrobić bardziej rozbudowane rozszerzenie.

## 4. Gdzie wrzucić
Program pyta przy instalacji dodatku o nazwę dodatku. Wtedy wykonuje proces pobierania tego dodatku ze strony tbomt.7m.pl/extensions/{nazwa dodatku}. Można tam wrzucić dodatek, ale jeszcze tego nie zrobiliśmy więc można utworzyć swoje źródło, tak jak na Linux jest Flathub, Snap, Debian oldstable packages itp. tak też można robić swoje źródła w naszej grze! Zachęcamy do tego a twórcy TBOMT z chęcią wypromują utworzone źródło. Jeżeli już się to uda, należy wprowadzić konkretny katalog strony aby zainstalować źródło. Np. program pyta: wprowadź nowe źródło z którego można będzie pobierać dodatki, podać należy wtedy link do konkretnego pliku który jest napisany w ten sposób (nazwę pliku można zmienić ale najlepiej aby miała .source na końcu), dla profesjonalizmu: prosimy nie wstawiać spacji w nazwie pliku a poniżej przykład:
#### wyswietlana-nazwa-zrodla.source
```
moje-zrodlo.com/extensions
```
Ta jedna linijka poprostu podaje źródło wszystkich paczek, jeżeli użytkownik chce dodatek ze strony moje-zrodlo.com/extensions/przykladowy-dodatek.py, wystarczy, że wybierze źródło, które podawane jest jako poprostu nazwa pliku (uznajmy, że mamy dwa źródła: nazwa pliku: abc, strona abc.com i nazwa pliku: cba, strona: cba.com), podane zostaną obie nazwy pliku podczas wyboru źródła: cba i abc. To wszystko jeżeli chodzi o źródła.
## 5. Dla zaawansowanych
Ci, co są zaawansowani niech sobie studiują otwarty kod programu, bo ja im nie będę nic tłumaczyć hihi.