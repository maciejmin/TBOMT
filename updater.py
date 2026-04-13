def update():
    print("Uruchamiam uaktualniacz, sprawdzam aktualizacje za pomocą funkcji requests oraz repozytorium Github TBOMT, czekaj...")
    try:
        file = open("program.py","r+")
    except:
        print("Wygląda na to, że wystąpił błąd z pobieraniem pliku z katalogu. Może się okazać, że uruchamiasz np. w VS CODE, może to powodować, iż program próbuje pobrać z innego katalogu niż z tego. Upewnij się, że otwierasz program.py w miejscu programu.")
        print("Przerywam działanie programu w tym momencie.")
    current_version = file.read()[0] #pierwsza linia
    import requests
    web_file = requests.get("https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/program.py").text
    if web_file[0] == current_version:
        return "actual" #te same wersje
    else:
        #aktualizujemy
        import os
        os.remove("program.py")
