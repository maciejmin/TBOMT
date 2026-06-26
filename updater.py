#v1.0|https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/updater.py
#jezeli jakis dodatek na sources.list nie ma dwóch | nalezy go pominac
def update_program():
    print("Uruchamiam uaktualniacz, sprawdzam aktualizacje za pomocą funkcji requests oraz repozytorium Github TBOMT, czekaj...")
    try:
        file = open("program.py","r+",encoding="utf-8")
    except Exception as e:
        print("Wygląda na to, że wystąpił błąd z pobieraniem pliku z katalogu. Może się okazać, że uruchamiasz np. w VS CODE, może to powodować, iż program próbuje pobrać z innego katalogu niż z tego. Upewnij się, że otwierasz program.py w miejscu programu.")
        print("Przerywam działanie programu w tym momencie.")
        return e
    current_version = ""
    readed_file = file.read()
    for i in range(len(readed_file)): #plik
        if readed_file[i] != "\n":
            current_version += readed_file[i]
        else:
            break
    import requests
    web_file = requests.get("https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/program.py").text
    web_file_version = ""
    for i in range(len(web_file)): #webfile
        if web_file[i] != "\n":
            web_file_version += web_file[i]
        else:
            break
    print(current_version,web_file_version)
    if web_file_version == current_version:
        return "actual" #te same wersje
    else:
        #aktualizujemy
        file.close()
        file = open("program.py","w+",encoding="utf-8")
        file.write(web_file)
        file.close()
        print("Powodzenie.")
        return "updated"

def update_extensions():
    import requests
    print("searching from sources.list")
    try:
        file = open("sources.list","r",encoding="utf-8")
    except Exception as e:
        return ["44, updater.py: failed opening sources.list.",str(e)]
    sources = file.read().splitlines()
    file.close()
    everyone = [] #wszystkie ze zwrotem informacji
    for i in sources: #plik caly zrodel
        current = "" #jeden z listy
        lista = [] #lista linijki, [0] = źródło, [1] = lokalizacja/nazwa
        for j in i: #linijka, bo sources oddzielane są |. np. "source.com/source.py|home/liveuser/tbomt/extensions/source.py"
            if j != "|":
                current += j
            else:
                lista.append(current)
                current = ""
        print(len(lista))
        if len(lista) == 2:
            print(i)
            lista.append(current)
            zrodlo = requests.get(lista[1]).text
            wersja_zrodla = zrodlo.splitlines()[0]
            plik = open(lista[2],"r",encoding="utf-8").read().splitlines()[0]
            if wersja_zrodla == plik:
                everyone.append(str(i)+": Up to date.")
            else:
                try:
                    file = open(i,"w+",encoding="utf-8")
                    file.write(zrodlo)
                    file.close()
                    everyone.append(str(i)+": Updated to "+wersja_zrodla+" from "+plik+"!")
                except:
                    everyone.append(str(i)+": Failure.")
    return everyone
