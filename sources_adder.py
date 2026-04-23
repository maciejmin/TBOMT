#vTest|https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/sources_adder.py
#program służy do pobrania extensions z katalogu extensions i ich wrzut do pliku sources.list oraz z tego folderu
import os
if os.name == "nt":
    slash = "\\"
else:
    slash = "/"
files = os.listdir(".")
sources = open("sources.list","w+")
for i in files:
    if i[-3:] == ".py": #ten plik pobieramy
        file = open(i,"r")
        sources.write(file.read().splitlines()[0][1:]+"|"+i+"\n")
        file.close()
files = os.listdir(os.getcwd()+slash+"extensions")
for i in files:
    if i[-3:] == ".py": #ten plik pobieramy
        file = open(i,"r")
        sources.write(file.read().splitlines()[0][1:]+"|"+i+"\n")
        file.close()
