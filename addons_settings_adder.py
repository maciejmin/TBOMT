#v1.0|https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/addons_settings_adder.py
import os
if os.name == "nt":
    print("System Microsoft Windows, używanie \\.")
    slash = "\\"
else:
    print("Domyślne ustawienia ze względu na korzystanie z Linuxa albo MacOS.")
    slash = "/"
def refresh():
    check()
    print("[  OK  ] Sprawdzono foldery, krok 2: sprawdzanie plików ustawień dodatków, wczytywanie...")
    print("Uruchamianie extension_downloader.py...")
    import extensiondownloader
    print("[  OK  ] Odświeżono listę dodatków.")
    print("Wczytywanie extensions.todo...")
    file = open("extensions.todo","r",encoding="utf-8")
    extensions_list = file.read().splitlines()
    for i in range(len(extensions_list)): #każda linia
        nazwa = ""
        for j in range(len(extensions_list[i])): #każdy znak
            if extensions_list[i][j] == "|":
                nazwa = extensions_list[i][:j]
                break
        if extensions_list[i][j+1:] == "addon":
            print(nazwa[:-3].capitalize(),"to dodatek wgrany przez użytkownika. Wgrywanie ustawień tego dodatku jako „addon”.")
            if os.path.exists("extensions"+slash+"moreextensions"+slash+"settings"+slash+nazwa):
                print("[  OK  ] Istniejąca paczka ustawień dodatku, ustawienia można przywrócić w zarządzaczu dodatków gdy zostawi się tylko wpis „reset” po edycji.")
            else:
                file = open("extensions"+slash+"moreextensions"+slash+"settings"+slash+nazwa,"w+",encoding="utf-8")
        if extensions_list[i][j+1:] == "basic extension":
            print(nazwa[:-3].capitalize(),"to dodatek podstawowy. Wgrywanie ustawień tego dodatku jako „basic extension”.")
            if os.path.exists("extensions"+slash+"moreextensions"+slash+"settings"+slash+nazwa):
                print("[  OK  ] Istniejąca paczka ustawień dodatku, ustawienia można przywrócić w zarządzaczu dodatków gdy zostawi się tylko wpis „reset” po edycji.")
            else:
                file = open("extensions"+slash+"basicextensions"+slash+"settings"+slash+nazwa,"w+",encoding="utf-8")
                file.write("enabled=True")

def check():
    print("ckecking",os.getcwd()+slash+"extensions"+slash+"basicextensions"+slash+"settings...")
    if os.path.exists("extensions"+slash+"basicextensions"+slash+"settings"): #sprawdzamy, dodajemy
        print("[  OK  ]")
    else:
        print("Not exists. Adding...")
        os.makedirs("extensions"+slash+"moreextensions"+slash+"settings",exist_ok=True)
        print("[  OK  ]: Utworzono pomyślne foldery nadrzędne.")
    #drugie sprawdzamy
    print("ckecking",os.getcwd()+""+slash+"extensions"+slash+"moreextensions"+slash+"settings...")
    if os.path.exists("extensions"+slash+"moreextensions"+slash+"settings"): #sprawdzamy, dodajemy
        print("[  OK  ]")
    else:
        print("Not exists. Adding...")
        os.makedirs("extensions"+slash+"moreextensions"+slash+"settings",exist_ok=True)
        print("[  OK  ] Utworzono pomyślne foldery nadrzędne.")
    
