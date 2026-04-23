#vTest|https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/extensiondownloader.py
#program służy do pobrania extensions z katalogu extensions, następnie wgranie go do pliku to_do.extensions, który zawiera każdą linię itd. w której która extension. Potem otwiera compiler.py który wysyła wszystko do program.py ale przed tem tqorzy kopię zapasową tego poprzedniego pliku.
import os
if os.name == "nt":
    slash = "\\" #system microsoft
else:
    slash = "/" #Linux, MacOs
katalog_ex = os.getcwd() #oznacza katalog programu
try:
    for i in os.listdir(katalog_ex+slash+"extensions"):
        print(i)
except Exception as e:
    import easygui
    easygui.msgbox("Coś poszło nie tak. Plik:\n"+__file__+"\nBłąd:\n"+str(e)+"\nJeżeli błąd jest nietrudny do naprawienia, możesz to zrobić. W przeciwnym razie skontaktuj się z nami. Musimy przerwać program.")
    if str(e)[:9] == "[Errno 2]":
        easygui.msgbox("Wygląda na to, że błąd:\n"+str(e)+"\nJest możliwy do naprawienia! Nie wiemy tylko co go wywołało. Być może przerwałeś etap instalacji programu albo sam się przerwał.\nJest też opcja, że korzystasz z podrobionej wersji tej gry, lub nieaktualizowanej wersji testowej.\n")
        easygui.msgbox("Co teraz musisz zrobić? Możemy usunąć całą grę i przejść proces instalacji na nowo. Możesz także pobrać z naszego repozytorium folder \"Extensions\" wraz z jego zawartością.\nJeżeli nie wiesz co robić,\nsprawdzimy co poszło nie tak i zainstalujemy grę na nowo.\n")
        w = easygui.indexbox("Wybór należy do ciebie:","",["Instalacja na nowo, jeżeli wcześniej grałeś w tą grę, usunie to wszystkie dane, osiągnięcia itp.","Sprawdź brakujące pliki, funkcja eksperymentalna, coś może pójść nie tak ale raczej nic się nie stanie","Instaluj folder extensions z naszego repozytorium"])
        if w == 0:
            w = easygui.codebox("Zostaną wykonane następujące czynności (edycja tekstu poniżej nic nie zmieni):"," ","1. Stworzymy plik uninstall.py w katalogu wyżej;\n2. Uruchomimy plik uninstall.py i usuniemy dzięki niemu cały katalog "+os.getcwd()+"\n3. Po usunięciu katalogu zostanie skopiowany z internetu plik program.py zawierający instrukcję ponownej instalacji;\n4. Zostanie uruchomiona gra.")
            if w != None:
                print("Wykonuję 1/4. Tworzenie uninstall.py")
                for i in range(len(katalog_ex)-1,0,-1):
                    if katalog_ex[i] == slash:
                        break
                print(katalog_ex[:i]) #katalog powyżej
                file = open(katalog_ex[:i]+slash+"uninstall.py","w+")
                file.write("import os\nos.remove(\""+katalog_ex+"\")\nfile = open(\"program.py\",\"w+\")\nimport requests\nfile.write(requests.get(\"https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/program.py\").text)\nimport subprocess\nimport sys\nsubprocess.Popen([sys.executable, \"program.py\"])")
                import subprocess
                import sys
                subprocess.Popen([sys.executable,katalog_ex[:i]+slash+"uninstall.py"])
            else:
                easygui.msgbox("Przerwano, koniec instalacji.")
        elif w == 1:
            w = easygui.codebox("Zostaną wykonane następujące czynności (edycja tekstu poniżej nic nie zmieni):"," ","1. Sprawdzimy, których folderów brakuje (plików nie sprawdzamy, bo jest to zależne od wersji programu);\n2. Pobierzemy z internetu brakujące pliki i zainstalujemy je w potrzebnym miejscu;\n3. Przejdziemy do etapu instalacji dodatków z folderu.")
            if w != None:
                print("Wykonuję 1/3. Tworzę potrzebne pliki")
                easygui.msgbox("Nie możemy wykonać tej czynności. Błąd:\nObawiamy się, że może pójść coś nie tak ze względu na nie aktualizowanie repozytorium pod względem plików.\nMusimy przerwać działanie programu.")
            else:
                easygui.msgbox("Przerwano, koniec instalacji.")
        elif w == 3:
            w = easygui.codebox("Zostaną wykonane następujące czynności (edycja tekstu poniżej nic nie zmieni):"," ","1. Pobierzemy z internetu katalog \"extensions\" i wgramy go do katalogu programu.\n2. Przejdziemy do etapu instalacji dodatków z folderu.")
            if w != None:
                print("Wykonuję 1/2. Pobieram plik z internetu")
                import requests
                os.makedirs("extensions",exist_ok=True)
                easygui.msgbox("Nie ukończono. Nie jest jasne gdzie są pliki i foldery gry.") #trzeba utworzyć na githubie
    exit()