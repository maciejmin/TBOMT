#v1.0|https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/compiler.py
#program czyta extensions.todo i wsadza pliki do programu
print("Compiler initialized!")
#[insert/rewrite, line, what, tabs, in subprocess?]
import easygui
import os
import time
import requests
import updater
if os.name == "nt":
    print("Windows user, using \\.")
    slash = "\\"
else:
    print("Wow! Linux or MacOs, using basic slash /.")
    slash = "/"
try:
    import addons_settings_adder
except:
    file = open("addons_settings_adder.py","w+",encoding="utf-8")
    file.write(requests.get("https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/addons_settings_adder.py").text)
    file.close()
    import addons_settings_adder
def load(dodatek,katalog): #Ładuje dodatek do listy do ładowania
    # Przykład użycia, otrzymuje (happytbomt.py, extensions/moreextensions)
    file = open(katalog+slash+dodatek,"r",encoding="utf-8")
    print("Weryfikowanie, czy dodatek ma poprawną składnię ładowania...")
    dodatek_readed = file.read().splitlines()
    #Sprawdzanie wersji AddonEditorVersion
    line_list = []
    recent_i = 0
    print(dodatek_readed[1])
    for i in range(len(dodatek_readed[1])): #druga linia
        if dodatek_readed[1][i] == "|":
            line_list.append(dodatek_readed[1][recent_i:i])
            recent_i = i+1
    line_list.append(dodatek_readed[1][recent_i:])
    print(line_list)
    if line_list[0] == "#AEV=1.0": #sposób dodatków 1.0 AddonsEditorVersion
        print(dodatek+", sposób ładowania: AddonsEditorVersion=1.0")
        print("Sporządzam listę do ładowania...")
        file.close()
        file = open("extensionsload.todo","r+",encoding="utf-8")
        for i in range(len(dodatek_readed)):
            if dodatek_readed[i] == "#-#": #zaczynamy kombinowanie
                break
        i += 1 #dodajemy o 1, wiadomo teraz ze od tego sie zaczyna
        print(dodatek_readed[i])
        for i in range(i,len(dodatek_readed)):
            if dodatek_readed[i][0] != "#":
                print("Comment error, character \""+dodatek_readed[i][0]+"\", nie jest komentarzem, a powinien. Odwoływanie linijki na ten raz.")
            else:
                print(i)
                file.write(dodatek_readed[i][1:]+"\n")
    else:
        print("Nieznana metoda czytania.")
def do():
    if not os.path.exists("addons_settings.info"):
        addons_settings_adder.refresh()
    def compiler():
        w = easygui.indexbox("Witaj w kompilerze dodatków TBOMT, wybierz co teraz chcesz zrobić. Jeśli obawiasz się jakiejś funkcji, poprosimy cię o potwierdzenie działania!"," ",["Właduj","Zaaktualizuj listę","Przejrzyj listę","Przywróć"])
        if w == 1:
            w = easygui.indexbox("Aktualizowanie listy dodatków, dzięki temu program będzie znał wszystkie dodatki i spisze ich aktualizacje. Nie wymaga dostępu do internetu.","Compiler",["Kontynuuj","Wróć"])
            if w == 0:
                print("uruchomię w tym celu extensiondownloader.py.")
                try:
                    import extensiondownloader
                    easygui.msgbox("Wydaje się, że zaaktualizowano listę dodatków.")
                    compiler()
                except Exception as e:
                    w = easygui.indexbox("Coś poszło nie tak. Możliwe, że cała lista dodatków się wysypała. Jeżeli wszystko jest ok z dodatkami nie przejmuj się tym, mimo tego możesz się znami skontaktować jeżeli to błąd."," ",["Szczegóły dla programisty","Skontaktuj się z nami","To nie istotne"])
                    if w == 0:
                        easygui.codebox("Poniżej szczegóły dla programisty:"," ",str(e))
                    elif w == 1:
                        easygui.codebox("Wyślij na maila the_beginning_of_modern_times@galaxyhit.com"," ",str(e))
                    else:
                        compiler() #uruchamiamy ponownie
            elif w == 1:
                compiler()
        elif w == 2:
            w = easygui.indexbox("Zarządzaj dodatkami, możesz edytować ich parametry, choć zwykle nie jest to potrzebne. Możesz wyłączać tam też dodatki.","Compiler",["Kontynuuj","Wróć"])
            if w == 0:
                file = open("extensions.todo","r",encoding="utf-8")
                dodatki = file.read()
                try:
                    w = easygui.choicebox("Wybierz dodatek i nim zarządzaj!"," ",dodatki.splitlines())
                except:
                    w = easygui.codebox("Wybierz dodatek, i nim zarządzaj. Zmień konkretną linię z dodatkiem, którym chcesz zarządzać np. zamiast \"noise.py|basic extension\", wpisz w tym miejscu \"example|example\". Uwaga! Możesz edytować tylko jeden jednocześnie."," ",dodatki)
                    if w == dodatki:
                        w = easygui.indexbox("Wygląda na to, że nie chcesz edytować żadnego dodatku. Co teraz?"," ",["Wróć do TBOMT","Rozpocznij na nowo edycję dodatków"])
                        if w == 1:
                            compiler()
                    else:
                        print(w,dodatki)
                        w = w.splitlines()
                        for i in range(len(w)):
                            if w[i] != dodatki.splitlines()[i]: #ta linia edytowana
                                #sprawdzamy edytowaną linię
                                name_addon = dodatki.splitlines()[i]
                                addon_changer(name_addon)
            elif w == 1:
                compiler()
        elif w == 0:
            w = easygui.indexbox("Załaduj dodatki do gry, jeśli przerwiesz w trakcie gra może się nie uruchomić następnym razem. Wszystkie dodatki po prostu zostaną na nowo załadowane do pliku gry.","Compiler",["Kontynuuj","Wróć"])
            if w == 0:
                print("Czyszczę listę do ładowania...")
                file = open("extensionsload.todo","w+",encoding="utf-8")
                file.close()
                print("Sprawdzam, czy istnieje pierwotna wersja programu...")
                try:
                    file = open("program.noaddons","r",encoding="utf-8")
                    version_old = file.read()
                    file.close()
                    print("Exists.")
                    #porównujemy wtedy wersje
                    file = open("program.py","r",encoding="utf-8")
                    if file.read().splitlines()[0] == version_old.splitlines()[0]:
                        print("Same version.")
                    else:
                        w = easygui.buttonbox("Obecna wersja programu jest nowsza niż wersja bez dodatków. Czy chcesz zaaktualizować grę, zanim załadujesz dodatki?","Compiler",["Tak","Nie"])
                        if w == "Tak":
                            updater.update_program()
                        elif w == "None":
                            w = easygui.indexbox("Nie przerywaj teraz, coś złego może się stać z TBOMT (chociaż nie próbowaliśmy)."," ",["Przerwij mimo tego","Ok, nie przerywaj"])
                            if w != 1:
                                exit()
                    #aktualizujemy program.py na program.noaddons
                    file.close()
                    file = open("program.py","w+",encoding="utf-8")
                    file.write(version_old)
                    file.close()
                    print("Zapisano.")
                except:
                    #nie istnieje, musimy więc pobrać z obecnego
                    file = open("program.py","r",encoding="utf-8")
                    version_old = file.read()
                    file.close()
                    file = open("program.noaddons","w+",encoding="utf-8")
                    file.write(version_old)
                    file.close()
                    print("Zapisano.")
                print("[  OK  ]")
                print("Załadowuję dodatki.")
                #ładujemy dodatki do gry
                print("Czytam dodatki i tryby zapisu, wywołuję funkcję...")
                file = open("extensions.todo","r",encoding="utf-8")
                dodatki = file.read().splitlines()
                for i in range(len(dodatki)):
                    line_list = []
                    for j in range(len(dodatki[i])):
                        if dodatki[i][j] == "|":
                            line_list.append(dodatki[i][:j])
                            break
                    line_list.append(dodatki[i][j+1:])
                    print(line_list[0], "loading now...")
                    try:
                        if line_list[1] == "basic extension":
                            load(line_list[0],"extensions"+slash+"basicextensions")
                        else:
                            load(line_list[0],"extensions"+slash+"basicextensions")
                    except:
                        print("Failed to load",line_list[0],"too short file to read.")
                        print("\n")
                print("Uruchamiam funkcję kompilującą główny program...")
                compile()
            elif w == 1:
                compiler()
    compiler()

def addon_changer(name_addon): #zmienia ustawienia dodatku aby nie mieszać w głównym kodzie kompilera, podaj tu name_addon
    for i in range(len(name_addon)):
        if name_addon[i] == ".":
            nazwa = name_addon[:i]
        if name_addon[i+1:] == "addon":
            easygui.codebox(nazwa+" to jest dodatek władowany przez użytkownika, lub pakiet zalecany. Możesz zmienić poniżej jego ustawienia."," ","enabled = True")
        else:
            easygui.codebox(nazwa+" to jest dodatek domyślny, prawdopodbnie jest wymagany przez grę. Jeśli nie boisz się, że gra się nie uruchomi lub przerwie w połowie, możesz edytować jego ustawienia. W przeciwnym razie kliknij „cancel”."," ","enabled = True")
def compile(): #kompiluje do programu
    print("OK, compiling now...")
    try:
        file = open("extensionsload.todo","r",encoding="utf-8")
        w = "Tak"
    except:
        w = easygui.buttonbox("Problem przy kompilowaniu. Nie można znaleźć pliku kompilowania, czy chcesz go wygenerować?"," ",["Tak","Wróć do TBOMT"])
        if w == "Tak":
            easygui.msgbox("Po przejściu do głównego okna, naciśnij „Właduj”.")
            do()
            compile()
            w = "Coś innego niż tak"
        else:
            w = "Coś innego niż tak"
    if w == "Tak":
        whattocompile = file.read().splitlines()
        file.close()
        compiling = [] #ma podzielic sie na kolejne listy liń
        for i in range(len(whattocompile)):
            poprzednie_j = 0
            compiling.append([])
            for j in range(len(whattocompile[i])):
                if whattocompile[i][j] == "|":
                    compiling[i].append(whattocompile[i][poprzednie_j:j])
                    poprzednie_j = j+1
            compiling[i].append(whattocompile[i][poprzednie_j:])
        print(compiling)
        #posortujemy najpierw dodatki
        posortowano = False
        while posortowano == False:
            #sortujemy
            posortowano = True
            for i in range(len(compiling)):
                try:
                    if int(compiling[i][1]) < int(compiling[i+1][1]): #mamy na myśli jeden, czyli linijkę kodu
                        #jest mniejszy niz nastepca, musimy więc ich zamienić miejscami
                        poprzednicompiling1 = compiling[i]
                        compiling[i] = compiling[i+1]
                        compiling[i+1] = poprzednicompiling1
                        posortowano = False
                    elif int(compiling[i][1]) == int(compiling[i+1][1]): #jeśli jest równe
                        if compiling[i][0] == "i" and compiling[i+1][0] == "r": #jeśli są takie same to bez znaczenia, jeśli mamy tutaj r lub i, wpiszemy pierwsze i
                            poprzednicompiling1 = compiling[i]
                            compiling[i] = compiling[i+1]
                            compiling[i+1] = poprzednicompiling1
                            posortowano = False
                        elif compiling[i][0] == "r" and compiling[i+1][0] == "i":
                            poprzednicompiling1 = compiling[i+1]
                            compiling[i+1] = compiling[i]
                            compiling[i] = poprzednicompiling1
                            posortowano = False
                        else:
                            pass #albo to albo to, bez znaczenia
                except:
                    pass #bo po prostu trudno xd
        print(compiling)
        print("\n\n\n[  OK  ] Udało się przesortować listę dodatków")
        print("Rozpoczynam kompilowanie, nie przerywaj tego procesu.")
        file = open("program.noaddons","r",encoding="utf-8")
        programfile = file.read().splitlines() #potem będziemy iteracjami i sprawdzać, jeśli linia to ta to wklejamy
        file.close()
        kolejnedzialanie = 0 #rozpoczynamy indexy działan do wykonania, beda sie one zmieniac co 1 przy kazdym wykonanym dzialaniu.
        for i in range(len(programfile),0,-1): #i to będzie linijka każda
            #sprawdzamy, jeśli ta linijka ma akurat to zgodnie z sortowaniem, wklej to albo podmień
            if int(compiling[kolejnedzialanie][1]) == i:
                if compiling[kolejnedzialanie][0] == "i":
                    programfile.insert(i,"\t"*int(compiling[kolejnedzialanie][3])+compiling[kolejnedzialanie][2])
                else:
                    programfile[i] = "\t"*int(compiling[kolejnedzialanie][3])+compiling[kolejnedzialanie][2]
        print("Zakończono kompilowanie. Teraz zapis do głównego programu. Aby odzyskać bezdodatkową wersję programu, otwórz kompiler (przez ustawienia TBOMT) i naciśnij „przywróć”.")
        file = open("program.py","w+",encoding="utf-8")
        time.sleep(1)
        for i in programfile:
            file.write(str(i)+"\n")
        print("Powodzenie")
do()
