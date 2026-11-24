## Dokument styli w formacie .tsowws
Domyślnie korzystamy z domyślnego stylu dla okien w winmanagerze, jednak ze względu na możliwość modowania naszej gry w wzdłuż i w szerz, można zarządzać stylami i układem okien, w tym poradniku dowiesz się, jak poprawnie utworzyć dokument styli dla okien winmanagera
> Podczas czytania poradnika zalecamy korzystanie z oprogramowania graficznego tj. [Krita](https://krita.org), ponieważ jest ono również open-source jak nasza gra, i wszelka grafika naszej gry została utworzona właśnie w Kricie (nie licząc logo oraz tła głównego).

## Układ dokumentu
Czym jest dokument w formacie .tsowws? Zatem jest to format zapisu stylów. Dzięki temu formatowi możemy określić okna graficzne a w szczególności ich wygląd. Obok znajdziemy przykład ikony „X”, który może zostać użyty do stylu okna: ![obrazek x](https://tbomt.7m.pl/img/x.png). Jak zatem użyć ten przycisk? W teorii możnaby napisać całą strukturę i wygląd paska górnego w Pygame, biorąc pod uwagę współrzędne okna i resztę zmiennych oraz utrudnień, które wymyśliliśmy tworząc tę grę ;).
### Rozpoczęcie tematu struktury
```
$TSOWWSFILEv1
---UP---
X=~images/x.png|https://tbomt.7m.pl/img/x.png
```
> Slash "/" jest domyślnie używany na Linuxach i MacOS, jeśli jesteś użytkownikiem systemu Windows, niestety możesz mieć problem z tym poradnikiem. Weź pod uwagę, że w twoim przypadku będą to po prostu slashe "\\". Mimo tego prosimy, abyś używał w pliku styli slash domyślny, ponieważ slash systemu Microsoft może kolidować z Pythonem3.

Podsumowując kolejno linijki pliku tsowws (czyli TBOMT Styles Of Winmanager Window System):
1. *`$TSOWWSFILEv1`* - deklarujemy wersję stylów, TWinmanager w nowszych wersjach dostosuje się do starszych wersji stylów, o to się nie musisz martwić. Na razie używaj domyślnie tej linijki.
2. *`---up---`* - rozpoczynamy pokazywanie góry okna, czyli paska posiadającego właśnie "X", "-". Pod tym zaczynamy deklarację wszystkiego, co jest w pasku górnym okna.
3. *`X=~images/x.png|https://tbomt.7m.pl/img.png`* - deklarujemy, że przycisk "X" ma być plikiem z folderu `~images/x.png` (co oprogramowanie czytające style odczytuje jako np. `/home/liveuser/tbomt/images/x.png`), lub jeśli nie ma pliku w folderze, odczytuje to jako `https://tbomt.7m.pl/img/x.png`, to strona internetowa gdzie właściwie znajduje się ten plik, a potem pobiera go, aby następnym razem był pobierany już z folderu.
## Wszystkie znaczniki i ich wyjaśnienia
Aby móc stworzyć porządny styl, podajemy wszystkie możliwe znaczniki do tworzenia styli.
### Znaczniki deklarujące typy
- *`$TSOWWSFILE`*, po tym dopisujemy tylko v1 jak wcześniej lub inną wersję, jeśli korzystasz z menedżera stylu opisanego w tym poradniku, powinieneś użyć właśnie v1.
### Znaczniki rozdzielające i części
#### *`---general---`*
> Aby zadeklarować ogólne zasady, obecnie należy pamiętać, że nie ma zbyt dużo wszystkiego, gra jeszcze nie jest skończona, dlatego staramy się robić wszystko na tyle, aby dało się to w przyszłości edytować, zatem jeśli dacie nam trochę czasu, dopracujemy zasady okien!
- *`color=`*<*`Tutaj wstawiasz kolor w formacie r|g|b, np. "color=255|255|255" czyli biały`*>
#### *`---up---`*: górna część okna
> Aby deklarować, co ma być w tej części, powinniśmy używać czegoś takiego, jak zmienne (lub w tym przypadku stałe, choć wiadomo o co chodzi)
- *`X=`*<*`Wprowadzasz miejsce pliku, jeśli znajduje się pod katalogiem głównym użyj „~” a następnie podaj lokalizację pliku`*>|<*`Podaj miejsce pliku w internecie`*>
> np. *`X=~images/x.png|`[https://tbomt.7m.pl/img/x.png](https://tbomt.7m.pl/img/x.png)*, jeśli zdjęcie jest w katalogu głównym TBOMT/images, jest pobierane z tego katalogu (np. może to być /home/liveuser/tbomt/images/x.png, w przeciwnym razie pobierane jest ze strony internetowej https://tbomt.7m.pl/img/x.png](https://tbomt.7m.pl/img/x.png)
- *`M`*, to samo co z *`X`*, tylko, że to przycisk minimalizowania.
- *`FLSC`* to samo co z *`M`* i *`X`*, tylko, że to przycisk maksymalizowania okna
- *`sFLSC`* to samo co poprzednie tylko, że to przycisk odmaksymalizowywania okna

## Przypomnienie
> Ten poradnik zawiera obecnie wszystkie dostępne opcje naszego menedżera styli dla winmanagera, ale pamiętaj, że nie jest ich za dużo, ponieważ staramy się rozwijać grę i dopiero na późniejszym etapie będziemy rozwijać poszczególne dodatki, jeśli chcesz przejąć projekt winmanagera i dalej go rozwijać napisz do nas!

>Uwaga! Jeśli plik styli nie posiada wszystkich elementów tj. właśnie przycisk X, zostanie użyty domyślny plik styli. Aby pobrać styl okna wystarczy otworzyć ustawienia winmanagera, a następnie otworzyć ustawienia styli okien, można tam tworzyć swoje style (choć na ten moment nie jest to dostępne).
