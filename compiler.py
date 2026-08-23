#v0.0.1
#program czyta extensions.todo i wsadza pliki do programu
print("Compiler initialized!")
import easygui
def do():
    def compiler():
        w = easygui.indexbox("Witaj w kompilerze dodatków TBOMT, wybierz co teraz chcesz zrobić."," ",["Zaaktualizuj listę dodatków (Jeżeli ostatnio pobierano)","Przejrzyj listę i wgraj do gry"])
        if w == 0:
            print("uruchomię w tym celu extensiondownloader.py.")
            try:
                import extensiondownloader
                easygui.msgbox("Wydaje się, że zaaktualizowano listę dodatków.")
                compiler()
            except Exception as e:
                w = easygui.indexbox("Coś poszło nie tak. Możliwe, że cała lista dodatków się wysypała. Jeżeli wszystko jest ok z dodatkami nie przejmuj się tym, mimo tego możesz się znami skontaktować jeżeli to błąd."," ",["Szczegóły dla programisty","Skontaktuj się z nami","To nie istotne"])
                if w == 0:
                    easygui.codebox("Poniżej szczegóły dla programisty:"," ",e)
                elif w == 1:
                    easygui.codebox("Wyślij na maila the_beginning_of_modern_times@galaxyhit.com"," ",e)
                else:
                    compiler() #uruchamiamy ponownie
        elif w == 1:
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
                        
    compiler()

def addon_changer(name_addon): #zmienia ustawienia dodatku aby nie mieszać w głównym kodzie kompilera, podaj tu name_addon
    for i in range(len(name_addon)):
        if name_addon[i] == ".":
            nazwa = name_addon[:i]
        if name_addon[i+1:] == "addon":
            easygui.codebox(nazwa+" to jest dodatek władowany przez użytkownika, lub pakiet zalecany. Możesz zmienić poniżej jego ustawienia."," ","enabled = True")
