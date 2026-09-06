#vTest
print("instaling desktop shortcut...")
import os
if os.name == "nt":
    print("Windows user.")
else:
    print("Wow! Linux or MacOs.")
    #pobieranie ikony do obecnego folderu
    file = open("icon.ico","wb")
    import requests
    file.write(requests.get("https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/icon.ico").content)
    #ukończono ikonę
    #tworzenie pliku /usr/share/applications
    file.close()
    file = open(os.path.expanduser("~")+"/.local/share/applications/tbomt.desktop","w+",encoding="utf-8")
    file.write("[Desktop Entry]\nType=Application\nName=TBOMT\nGenericName=Game\nComment=Play The Beginning Of Modern Times game!\nIcon="+os.getcwd()+"/icon.ico"+"\nKeywords=tbomt;TBOMT;The;Beginning;of;modern;times;The Beginning Of Modern Times;Game;\nMimeType=x-scheme-handler/tbomt;\nCategories=Game;\nTerminal=false\nPrefersNonDefaultGPU=false\nSingleMainWindow=true\nExec=python3 \""+os.getcwd()+"/program.py\"") #tu nalezy wpisać ten desktop entry
