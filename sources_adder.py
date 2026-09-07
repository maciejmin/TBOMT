#v1.1.2|https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/sources_adder.py
#program służy do pobrania extensions z katalogu extensions i ich wrzut do pliku sources.list oraz z tego folderu
import os
import requests
def refresh():
    if os.name == "nt":
        slash = "\\"
    else:
        slash = "/"
    try:
        files = os.listdir(".")
        sources = open("sources.list","w+",encoding="utf-8")
        for i in files:
            if i[-3:] == ".py" and "__init__.py" != i: #ten plik pobieramy
                file = open(i,"r",encoding="utf-8")
                sources.write(file.read().splitlines()[0][1:]+"|"+i+"\n")
                file.close()
        files = os.listdir(os.getcwd()+slash+"extensions")
        for i in files:
            if i[-3:] == ".py" and i != "__init__.py": #ten plik pobieramy
                file = open(i,"r",encoding="utf-8")
                sources.write(file.read().splitlines()[0][1:]+"|"+i+"\n")
                file.close()
    except:
        print("Błąd, prawdopodobnie nie ma folderu z dodatkami. Zostanie on zrobiony!")
        try:
            import extensionsinstaller
        except:
            file = open("extensionsinstaller.py","w+",encoding="utf-8")
            file.write("https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/extensionsinstaller.py")
            file.close()
            import extensionsinstaller
        extensionsinstaller.do()
def update_updater():
    file = open("updater.py","w+",encoding="utf-8")
    file.write(requests.get("https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/updater.py").text)
    file.close()
