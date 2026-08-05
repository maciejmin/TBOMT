#vTest_0.0.9
print("[0.0] Uruchamiam Początek Nowożytności, inicjuję czas")
import time
czas_od_startu = time.time()
def cosp(tekst): #czas_od_startu_podaj
    global czas_od_startu
    print("["+str(round(time.time()-czas_od_startu,8))+"] "+str(tekst))

cosp("Importuję podstawowe biblioteki zewnętrzne...")
try:
    import subprocess, os, sys
except:
    input("Brak potrzebnych bibliotek, aby uruchomić TBOMT. Dotknij enter aby opuścić grę.")
cosp("Sprawdzam system operacyjny")
if os.name == "nt":
    print("setting slash by \\.")
    skos = "\\"
else:
    print("WOW, Linux or MacOs, setting slash by default /")
    skos = "/"
cosp("Importuję dodatkowe biblioteki zewnętrzne...")
try:
    import easygui
    import requests
except:
    if os.name == "nt":
        print("You are on Windows, wait, we are installing important thinks")
        os.system("pip install easygui")
        os.system("pip install requests")
        try:
            import easygui
            import requests
        except:
            print("Package can't be installed. We must kill the process.")
            exit()
    else:
        try:
            import requests
        except:
            print("Twój system operacyjny jest niekompletny, spróbuj doinstalować requests: pip3/pip install requests lub sudo apt install python3/python requests")
            exit()
        print("You are on systems like Linux or MacOs, so we must use basic commands.")
        os.system("python3 -m pip install easygui")
        try:
            import easygui
        except:
            print("Package can't be installed. We must kill the process.")
            exit()
cosp("Sprawdzam dane o instalacji gry...")
if os.path.dirname(__file__) != os.getcwd():
    w = easygui.msgbox("Gra prawdopodobnie została otwarta ręcznie w nie poprawnym folderze. Zmienimy jej katalog na poprawny!","TBOMT")
    if w == None:
        easygui.msgbox("Bye!")
        exit()
    else:
        os.chdir(os.path.dirname(__file__))
cosp("Sprawdzam zależności...")
try:
    import updater
except:
    w = easygui.buttonbox("Musimy użyć internetu, aby pobrać potrzebny plik."," ",["OK","Anuluj"])
    if w == "OK":
        file = open("updater.py","w+",encoding="utf-8")
        file.write(requests.get("https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/updater.py").text)
        file.close()
        import updater
    elif w == "Anuluj":
        w = easygui.buttonbox("Gra nie może działać bez aktualizatora. Musimy użyć sieci, w przeciwnym razie będzie konieczność zamknięcia gry ze względu na możliwość wysypania się gry."," ",["Wyłącz TBOMT","Aktualizuj"])
        if w == "OK":
            file = open("updater.py","w+",encoding="utf-8")
            file.write(requests.get("https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/updater.py").text)
            file.close()
            import updater
        else:
            exit()
    else:
        exit()
def check_requirements():
    if os.path.exists("opened_data.data"): #to znaczy że już zainstalowano
        try:
            file = open("requirements_tbomt.list","r")
            file_content = file.read().splitlines()
            for i in file_content:
                for j in range(len(i)): #sprawdzamy każdy znak w danej linii
                    if i[j] == "|":
                        if os.path.exists(i[:j]):
                            print(i[:j],"OK.")
                        else:
                            print(i[:j],"ERROR.")
                            print("fixing now...")
                            file = open(i[:j],"w+",encoding="utf-8")
                            file.write(requests.get(i[j+1:]).text)
                            file.close()

        except Exception as e:
            print(e)
            easygui.textbox("Nie można sprawdzić plików. Wygląda na to, że updater nie wygenerował checklisty. Spójrz na logikę poniżej:"," ","Tylko wersja 1.2 (lub wyższa) updatera generuje check listy. Jeżeli jest niższa niż 1.1, nie może się zaaktualizować do wyższej wersji przez brak możliwości ładowania sources_addera. Oznacza to również, że żaden dodatek nie może się zaaktualizować, ponieważ sources_adder w ogóle się nie uruchamia. Zalecane jest teraz zaaktualizowanie przez program sources_addera (a nie przez updatera), a następnie uruchomienie go. Spowoduje to, że updater zostanie zaaktualizowany, a checklista dodatków zostanie uzupełnionia.\n\n\nProgram zrobi to za ciebie.")
            file = open("sources_adder.py","w+")
            file.write(requests.get("https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/sources_adder.py").text)
            file.close()
            import sources_adder
            sources_adder.update_updater()
            updater.add_requirements()
            check_requirements()
check_requirements()
import compiler
cosp("Składam funkcje...")
def createfile(localization_or_name,what_to_write=None,request_link=None,how_to_open="w+"): #jeżeli chcemy request_link wpisujemy None w what_to_write, przeciwnie robimy odwrotnie, jeśli nie chcemy nic to w obu miejscach None
    file = open(localization_or_name,how_to_open,encoding="utf-8")
    if what_to_write != None:
        file.write(what_to_write)
    elif request_link != None:
        r = requests.get(request_link)
        r.encoding = "utf-8"
        file.write(r.text)
    file.close()
print("Koniec, inicjacja gry zajęła "+str(time.time()-czas_od_startu)+" sekund.")
easygui.msgbox("Za chwilę zadamy kilka pytań przed startem, prosimy o chwilę cierpliwości. Gra została napisana trochę amatorsko, dlatego twórca wymaga textowego okienka zaraz obok. Ale to poprostu wyświetla informację o stanie gry.")
easygui.msgbox("Uwaga! Gra najlepiej działa na Linuxie i nie jest zalecana dla osób z epilepsją fotogenną oraz w wieku poniżej 13 lat ponieważ zawiera szybkie animacje powodujące nienadążający wzrok za efektami u młodszych osób.")
easygui.msgbox("Jeżeli znajdziesz jakikolwiek błąd zgłoś nam to na maila the_beginning_of_modern_times@galaxyhit.com a my spróbujemy to naprawić!")
def updating():
    respond = updater.update_program()
    if respond == "actual":
        easygui.msgbox("Wersja programu jest aktualna. Nie trzeba nic aktualizować.")
    elif respond == "updated":
        easygui.msgbox("Program został zaaktualizowany na nowszą wersję! Uruchomimy go ponownie aby zapewnić mu lepszą sprawność.")
        subprocess.Popen([sys.executable,__file__])
        exit()
    w = easygui.buttonbox("Uwaga, jest też możliwość, że dodatki do gry wymagają aktualizacji, takie jak np. ruch gracza itp. Czy chcesz poszukać aktualizacji dodatków?"," ",["Tak","Nie"])
    if w == "Tak":
        easygui.buttonbox("Uwaga, czy chcesz zaaktualizować listę dodatków? jeżeli nie chcesz, może być tak, że nie wszystkie dodatki będą wzięte pod uwagę podczas aktualizacji."," ",["Zaaktualizuj","Pozostań przy ostatniej aktualizacji pakietów"],default_choice="Zaaktualizuj")
        respond = updater.update_extensions()
        if len(respond) == 2:
            if respond[1][:9] == "[Errno 2]":
                w = easygui.buttonbox("Aktualizator wysypał się i wyrzucił błąd. Nasza gra jednak przewidziała, że błąd tego typu może wystąpić dlatego mamy na niego rozwiązanie.\nChodzi o to, że brakuje pliku który poda źródła dodatków, czy chcesz utworzyć ten plik?"," ",["Tak","Nie"])
                if w == "Tak": #createfile
                    createfile("sources.list")
                    w = easygui.buttonbox("Mimo to, że nie znane są nam żadne źródła zostaną one utworzone jeżeli chcesz."," ",["Poproszę","Nie, dziękuję"])
                    if w == "Poproszę":
                        w = easygui.buttonbox("Uwaga! Musimy pobrać pewną rzecz z internetu, aby mieć możliwość instalacji dodatków. Chcesz to zrobić? To może powodować opłaty w razie korzystania z sieci taryfowej."," ",["Pobierz","Nie pobieraj"])
                        if w == "Pobierz":
                            createfile("sources_adder.py",request_link="https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/sources_adder.py")
                            subprocess.run([sys.executable,os.getcwd()+skos+"sources_adder.py"])
                            w = easygui.buttonbox("Wydaje się, że udało się utworzyć potrzebne rzeczy. Czy chcesz uruchomić aktualizator dodatków ponownie?"," ",["Tak","Nie"])
                            if w == "Tak":
                                updating()
            w = easygui.indexbox("Akualizator wyrzucił błąd: szczegóły w \"Szczegóły dla programisty\". Jeśli błąd się powtarza, a gracz nie zna rozwiązania problemu można nam to zgłosić."," ",["Szczegóły dla programisty","Zaniechaj aktualizację"])
            if w == 0:
                w = easygui.codebox("Edycja tekstu poniżej nic nie zmieni. Poniżej znajdują się szczegóły wysypania się kodu aktualizatora:"," ","Aktualizator wysypał się. Informacja od aktualizatora:\n"+respond[0]+"\n\nSzczegóły błędu:\n"+respond[1]+"\n\nKliknij ok, aby przejść do gry i zaniechać aktualizację, jeżeli jednak chcesz zakończyć grę kliknij cancel lub też X.")
                if w == None:
                    easygui.msgbox("Bye!")
                    exit()
        else:
            result = ""
            for i in respond: #aby zrobic kilka linii, jak wysyla sie listę to jest nieschludnie
                result += i
                result += "\n"
            easygui.codebox("Uwaga, wygląda na to, że aktualizacja dodatków się udała! Jeżeli chcesz, możesz przeczytać log."," ",result)
            easygui.msgbox("Aby użyć nowych wersji dodatków, uruchomimy grę ponownie.")
            subprocess.Popen([sys.executable,__file__])
            exit()
print(os.listdir())
if len(os.listdir()) == 1:
    print("It's ok, we're only installing important thinks, you can find it below. Do not close this frame please.")
    w = easygui.textbox("Krótka notatka, nie zmieściliśmy jej w mniejszym okienku."," ","Uwaga! Wygląda na to, że jesteś w pustym folderze. Prawdopodobnie pobrałeś grę jako pierwszą pośród wszystkich plików w tym folderze. Jeżeli przeglądarka lub curl (czy coś tam innego) pobiera właśnie w to miejsce, zalecamy zainstalowanie gry w innym folderze niż ten. Jest też możliwość, że poprostu pobrano grę i przed otwarciem przemieszczono ją do innego folderu, mniejsza z tym.\n\nJeżeli chcesz zainstalować grę w tym katalogu ("+os.getcwd()+"), poprostu kliknij OK, w przeciwnym razie (czyli jeżeli chcesz instalować gdzieś indziej) kliknij cancel (lub X u góry okna) i wpisz potem w osobnym okienku katalog instalacji.")
    if w == None:
        w = easygui.enterbox("Tutaj wprowadź katalog instalacji, jeżeli nie wiesz o co chodzi (lub po prostu się nie znasz), kliknij OK. Jeżeli nie chcesz jednak instalować gry, kliknij cancel.","Początek Nowożytności - instalacja",os.path.expanduser("~")+skos+"tbomt")
        if w == None:
            easygui.msgbox("Bye!")
            exit()
        else:
            print("Wait...")
            os.makedirs(w, exist_ok=True)
            createfile(w+skos+"opened_data.data","0")
            createfile(w+skos+"program.py",request_link="https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/program.py")
            createfile(w+skos+"uninstall.py","import os\nos.remove(\""+__file__+"\")")
            createfile(w+skos+"updater.py",request_link="https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/updater.py")
            print(sys.executable)
            subprocess.Popen([sys.executable, w+skos+"program.py"],cwd=w)
            exit()
elif not "opened_data.data" in os.listdir():
    w = easygui.enterbox("Nie znaleźliśmy żadnego pliku z zapisanymi danymi dotyczącymi poprzedniego otwarcia aplikacji, ale wygląda na to, że w tym folderze już są pliki. Zaleca się, aby gra znajdowała się w jednym folderze, ponieważ tworzy własne pliki, co może w przyszłości powodować problemy z czytelnością. Chcesz wybrać folder, w którym ta gra będzie zlokalizowana, czy wybrać domyślny folder dla tej gry? Jeżeli chcesz, wpisz nazwę tego folderu i kliknij \"OK\". W przeciwnym razie kliknij przycisk cancel, będziemy wiedzieli wtedy, że nie chcesz instalować.","Początek Nowożytności - instalacja",os.path.expanduser("~")+skos+"tbomt")
    if w == None:
        easygui.msgbox("Bye!")
        exit()
    else:
        print("Wait...")
        os.makedirs(w, exist_ok=True)
        createfile(w+skos+"opened_data.data","0")
        createfile(w+skos+"program.py",request_link="https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/program.py")
        createfile(w+skos+"uninstall.py","import os\nos.remove(\""+__file__+"\")")
        createfile(w+skos+"updater.py",request_link="https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/updater.py")
        print(sys.executable)
        subprocess.Popen([sys.executable, w+skos+"program.py"],cwd=w)
        exit()
try:
    import pygame
except:
    if os.name == "nt":
        print("You are on Windows, wait, we are installing important thinks")
        os.system("pip install pygame")
        try:
            import pygame
        except:
            print("Package can't be installed. We must to kill the process.")
            exit()
    else:
        print("You are on systems like Linux or MacOs, so we must to use basic commands.")
        os.system("python3 -m pip install pygame")
        try:
            import pygame
        except:
            print("Package can't be installed. We must to kill the process.")
            exit()
#szukanie pliku uninstall.py
w = easygui.buttonbox("Czy chcesz sprawdzić aktualizacje gry? Jeżeli będzie taka możliwość zaaktualizujemy automatycznie program. To wymaga połączenia internetowego co może powodować opłaty."," ",["Tak","Nie"])
if w == "Tak":
    updating()
if os.path.exists("uninstall.py"):
    print("Jest śmieć pozostały po instalacji. Usuniemy go automatycznie!")
    print("uninstalling!")
    subprocess.run([sys.executable, "uninstall.py"])
    os.remove("uninstall.py")
if os.path.exists("icon.png"):
    pass
else:
    import requests
    file = open("icon.png","wb")
    file.write(requests.get("https://raw.githubusercontent.com/maciejmin/TBOMT/main/icon.png").content)
    file.close()
x = 1920
y = 1080
def pygame_inicjalizacja(): #używane na początku i po importach rzeczy specjalnych
    global icon, okno, clock, current_scroll
    pygame.init()  # initialize pygame modules (including font)
    icon = pygame.image.load("icon.png")
    okno = pygame.display.set_mode([x, y], pygame.RESIZABLE | pygame.DOUBLEBUF)
    pygame.display.set_caption("Początek Nowożytności")
    pygame.display.set_icon(icon)

    clock = pygame.time.Clock()  # smooth the frame rate and resizing

    # Obsługa scrolla
    current_scroll = False  # False, 1 (scroll góra), lub -1 (scroll dół)

pygame_inicjalizacja()

def draw_text(
    surface,
    align,
    text,
    pos,
    size=24,
    font_name="Arial",
    color=(255, 255, 255),
    bg=None,
    bold=False,
    italic=False,
    aa=True,
    is_button=False,
    button_padding=(12, 8),
    button_color=(50, 50, 50),
):
    """Renderuj tekst na `surface` z zadanym wyrównaniem.

    Args:
        surface: Pygame surface do rysowania.
        align: "topleft", "topright", "center", "midtop", "midbottom", "bottomleft", "bottomright".
        text: Tekst do wyświetlenia.
        pos: [x, y] - współrzędne pozycji.
        size: Rozmiar czcionki.
        font_name: Nazwa czcionki systemowej.
        color: Kolor tekstu (RGB).
        bg: Kolor tła (RGB) lub None.
        bold: Pogrubienie.
        italic: Kursywa.
        aa: Antyaliasing.
        is_button: Jeśli True, renderuje przycisk z tłem + padding.
        button_padding: Padding dla przycisku (x, y).
        button_color: Kolor tła przycisku.

    Returns:
        [is_hovered, is_clicked, scroll]: Lista gdzie is_hovered=1 jeśli mysz jest nad elementem, 
                                         is_clicked=1 jeśli przycisk myszy jest wciśnięty nad elementem,
                                         scroll=1 (scroll góra), -1 (scroll dół), False (brak scrollu).
    """

    font = pygame.font.SysFont(font_name, size, bold=bold, italic=italic)
    surf = font.render(str(text), aa, color, bg)
    rect = surf.get_rect()

    # Wspierane wyrównania
    align = align.lower()
    if align in ("center", "centre"):
        rect.center = pos
    elif align == "topleft":
        rect.topleft = pos
    elif align == "topright":
        rect.topright = pos
    elif align == "bottomleft":
        rect.bottomleft = pos
    elif align == "bottomright":
        rect.bottomright = pos
    elif align == "midtop":
        rect.midtop = pos
    elif align == "midbottom":
        rect.midbottom = pos
    else:
        # Jeżeli wyrównanie nieznane, użyj topleft
        rect.topleft = pos

    # If this should be a button, draw a padded rectangle behind the text.
    if is_button:
        padding_x, padding_y = button_padding
        button_rect = rect.inflate(padding_x * 2, padding_y * 2)
        pygame.draw.rect(surface, button_color, button_rect, border_radius=6)
        surface.blit(surf, rect)
        
        # Sprawdzenie hover i click
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = True if button_rect.collidepoint(mouse_pos) else False
        is_clicked = True if is_hovered and pygame.mouse.get_pressed()[0] else False
        
        # Sprawdzenie scrolla gdy mysz jest nad przyciskiem
        scroll = current_scroll if is_hovered else False
        
        return [is_hovered, is_clicked, scroll]

    surface.blit(surf, rect)
    
    # Sprawdzenie hover i click
    mouse_pos = pygame.mouse.get_pos()
    is_hovered = 1 if rect.collidepoint(mouse_pos) else 0
    is_clicked = 1 if is_hovered and pygame.mouse.get_pressed()[0] else 0
    
    # Sprawdzenie scrolla gdy mysz jest nad elementem
    scroll = current_scroll if is_hovered else False
    
    return [is_hovered, is_clicked, scroll]

def buttonbox(question:str,buttons:list,text_size:int,buttons_size:int): #maine
        global clicked
        draw_text(okno,"center","       ",[round(x/2),round(y/2)],round((x + y) / 10),"Monospace",is_button=True,button_padding=[10,100])
        draw_text(okno,"center",question,[round(x/2),round(y/3.2)],round((x + y) / text_size),"Monospace",is_button="False")
        for i in range(len(buttons)):
            if draw_text(okno,"center",buttons[i],[round(x/len(buttons))*i+round(x/len(buttons)/2),round(y/1.5)],round((x + y) / buttons_size),"Monospace",is_button=True)[0]:
                if draw_text(okno,"center",buttons[i],[round(x/len(buttons))*i+round(x/len(buttons)/2),round(y/1.5)],round((x + y) / buttons_size),"Monospace",is_button=True,color=[0,0,0],button_color=[255,255,255])[1]:
                    clicked = str(i)
                elif clicked == str(i):
                    clicked = False
                    return i
        if clicked == str(i):
            clicked = False
            return i

game = "menu"
rozmiar = ["Bardzo malutki (1 biom)","Malutki (2 biomy)","Mały (3 biomy)","Zwykły (5 biomów)","Duży (6 biomów) Zalecany","Bardzo duży (8 biomów)","Wielki (10 biomów)","Ogromny (15 biomów)","Gigantyczny (20 biomów)"]
clicked = False
while game != "quit":
    current_scroll = False  # Reset scrolla na początku każdej iteracji
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = "quit"
        elif event.type == pygame.MOUSEWHEEL:
            # Obsługa scrolla: event.y zawiera kierunek (dodatni = scroll góra, ujemny = scroll dół)
            current_scroll = 1 if event.y > 0 else -1
        elif event.type == pygame.VIDEORESIZE:
            # Update window size when the user resizes the window
            x, y = event.w, event.h
            draw_text(okno,"center",str(x)+", "+str(y),[round(x/2),round(y/2)],round((x + y) / 100),"Monospace",is_button=True) # pokazuje aktualny rozmiar okna, można usunąć później, daje mozliwosc sprawdzenia czy klikniety
            if event.type != pygame.VIDEORESIZE:
                okno = pygame.display.set_mode((x, y), pygame.RESIZABLE)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if game == "menu":
                    pass
                else:
                    game = "menu"

    okno.fill((0, 0, 0))

    if game == "menu":  # gra to menu
        draw_text(okno, "center", "Początek Nowożytności", (round(x / 2), round(y / 2 - y / 20)), size=round((x + y) / 100), font_name="Monospace")
        if draw_text(okno, "center", "Graj", (round(x / 2), round(y / 2 + y / 500)), size=round((x + y) / 200), font_name="Monospace", is_button=True,color=[255,255,255])[0]:
            if draw_text(okno, "center", "-  Graj  -", (round(x / 2), round(y / 2 + y / 500)), size=round((x + y) / 200), font_name="Monospace", is_button=True,color=[0,0,0],button_color=[255,255,255])[1]:
                scroll = 4
                clicked = "create_menu" #wtedy wiadomo że trzeba poczekać na niego aż oznaczy na False
            elif clicked == "create_menu":
                clicked = False
                game = "create"
        if draw_text(okno, "center", "Otwórz ustawienia", (round(x / 2), round(y / 2 + y / 20)), size=round((x + y) / 200), font_name="Monospace", is_button=True,color=[255,255,255])[0]:
            if draw_text(okno, "center", "-  Otwórz ustawienia  -", (round(x / 2), round(y / 2 + y / 20)), size=round((x + y) / 200), font_name="Monospace", is_button=True,color=[0,0,0],button_color=[255,255,255])[1]:
                clicked = "settings_menu" #wtedy wiadomo że trzeba poczekać na niego aż oznaczy na False
            elif clicked == "settings_menu":
                clicked = False
                game = "settings"
        if draw_text(okno, "center", "Wyjdź z gry", (round(x / 2), round(y / 2 + y / 10)), size=round((x + y) / 200), font_name="Monospace", is_button=True,color=[255,255,255])[0]:
            if draw_text(okno, "center", "-  Wyjdź z gry  -", (round(x / 2), round(y / 2 + y / 10)), size=round((x + y) / 200), font_name="Monospace", is_button=True,color=[0,0,0],button_color=[255,255,255])[1]:
                clicked = "quit_menu" #wtedy wiadomo że trzeba poczekać na niego aż oznaczy na False
            elif clicked == "quit_menu":
                clicked = False
                game = "quit"
    elif game == "create":
        try:
            file = open("datas.data","r+") #był wcześniej utworzony świat
            game = "open_world"
        except: #najwidoczniej trzeba utworzyć
            if buttonbox("Tworzenie świata, dobierz odpowiednie tobie opcje:",["Wróć","Ok"],100,100) == 0:
                game = "menu"
            elif buttonbox("Tworzenie świata, dobierz odpowiednie tobie opcje:",["Wróć","Ok"],100,100) == 1:
                game = "open_world"
            scroll += draw_text(okno, "center", "Rozmiar świata: "+rozmiar[scroll], (round(x / 2), round(y / 2)), size=round((x + y) / 200), font_name="Monospace", is_button=True,color=[0,0,0],button_color=[255,255,255])[2]
            if scroll <= -1:
                scroll = 0
            elif scroll >= 9:
                scroll = 8
    elif game == "settings":
        draw_text(okno, "center", "Ustawienia Początku Nowożytności", (round(x / 2), round(y / 2 - y / 20)), size=round((x + y) / 100), font_name="Monospace")
        if draw_text(okno, "center", "Ustawienia Dodatków", (round(x / 2), round(y / 2 + y / 500)), size=round((x + y) / 200), font_name="Monospace", is_button=True,color=[255,255,255])[0]:
            if draw_text(okno, "center", "-  Zarządzaj dodatkami i ich właściwościami.  -", (round(x / 2), round(y / 2 + y / 500)), size=round((x + y) / 200), font_name="Monospace", is_button=True,color=[0,0,0],button_color=[255,255,255])[1]:
                clicked = "addons_settings" #wtedy wiadomo że trzeba poczekać na niego aż oznaczy na False
            elif clicked == "addons_settings":
                clicked = False
                game = "addons"
        if draw_text(okno, "center", "Ustawienia Graficzne", (round(x / 2), round(y / 2 + y / 20)), size=round((x + y) / 200), font_name="Monospace", is_button=True,color=[255,255,255])[0]:
            if draw_text(okno, "center", "-  Zarządzaj grafiką, cieniami itp.  -", (round(x / 2), round(y / 2 + y / 20)), size=round((x + y) / 200), font_name="Monospace", is_button=True,color=[0,0,0],button_color=[255,255,255])[1]:
                clicked = "graphics_settings" #wtedy wiadomo że trzeba poczekać na niego aż oznaczy na False
            elif clicked == "graphics_settings":
                clicked = False
                game = "graphics"
        if draw_text(okno, "center", "Wróć do menu", (round(x / 2), round(y / 2 + y / 10)), size=round((x + y) / 200), font_name="Monospace", is_button=True,color=[255,255,255])[0]:
            if draw_text(okno, "center", "-  Wróć do menu głównego Początku Nowożytności.  -", (round(x / 2), round(y / 2 + y / 10)), size=round((x + y) / 200), font_name="Monospace", is_button=True,color=[0,0,0],button_color=[255,255,255])[1]:
                clicked = "wrocdomenu_settings" #wtedy wiadomo że trzeba poczekać na niego aż oznaczy na False
            elif clicked == "wrocdomenu_settings":
                clicked = False
                game = "menu"
    elif game == "addons":
        if buttonbox("Ta opcja zostanie otwarta w nowym oknie!",["Wróć","Ok"],100,100) == 0:
            game = "settings"
        elif buttonbox("Ta opcja zostanie otwarta w nowym oknie!",["Wróć","Ok"],100,100) == 1:
            pygame.quit()
            try:
                compiler.do()
            except Exception as e:
                easygui.codebox("Niestety compiler wysypał się nieoczekiwanie. Poniżej można znaleźć szczegóły błędu oraz zgłosić je na adres email the_beginning_of_modern_times@galaxyhit.com."," ",str(e))
            pygame_inicjalizacja()
            game = "addons_exitter"
    elif game == "addons_exitter":
        w = buttonbox("Jeżeli edytowałeś dodatki, musisz uruchomić ponownie grę, aby zadziałały. Czy chcesz to zrobić teraz?",["Tak","Nie"],150,100)
        if w == 0:
            subprocess.Popen([sys.executable,__file__])
            game = "quit"
        if w == 1:
            game = "settings"
    else: #gdy nie wiadomo
        draw_text(okno, "center", "404! Nie znaleźliśmy opcji "+game+".", (round(x / 2), round(y / 2 - y / 20)), size=round((x + y) / 100), font_name="Monospace")
        if draw_text(okno, "center", "Wróć do menu głównego", (round(x / 2), round(y / 2 + y / 500)), size=round((x + y) / 200), font_name="Monospace", is_button=True,color=[255,255,255])[0]:
            if draw_text(okno, "center", "-  Wróć do menu głównego  -", (round(x / 2), round(y / 2 + y / 500)), size=round((x + y) / 200), font_name="Monospace", is_button=True,color=[0,0,0],button_color=[255,255,255])[1]:
                clicked = "wrocdomenu_404" #wtedy wiadomo że trzeba poczekać na niego aż oznaczy na False
            elif clicked == "wrocdomenu_404": #wiemy że trzeba tu poczekać
                clicked = False
                game = "menu"
    pygame.display.update()
    clock.tick(60)  # ogranicz do ~60 FPS

pygame.quit()
