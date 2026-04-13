#vTest
import os
if os.name == "nt":
    print("setting slash by \\.")
    skos = "\\"
else:
    print("WOW, Linux or MacOs, setting slash by default /")
    skos = "/"
try:
    import easygui
except:
    if os.name == "nt":
        print("You are on Windows, wait, we are installing important thinks")
        os.system("pip install easygui")
        try:
            import easygui
        except:
            print("Package can't be installed. We must to kill the process.")
            exit()
    else:
        print("You are on systems like Linux or MacOs, so we must to use basic commands.")
        os.system("python3 -m pip install easygui")
        try:
            import easygui
        except:
            print("Package can't be installed. We must to kill the process.")
            exit()
easygui.msgbox("Uwaga! Gra najlepiej działa na Linuxie i nie jest zalecana dla osób z epilepsją fotogenną oraz w wieku poniżej 13 lat ponieważ zawiera szybkie animacje powodujące nienadążający wzrok za efektami u młodszych osób.")
easygui.msgbox("Jeżeli znajdziesz jakikolwiek błąd zgłoś nam to na maila the_beginning_of_modern_times@galaxyhit.com a my spróbujemy to naprawić!")
w = easygui.buttonbox("Czy chcesz sprawdzić aktualizacje gry? Jeżeli będzie taka możliwość zaaktualizujemy automatycznie program. To wymaga połączenia internetowego co może powodować opłaty."," ",["Tak","Nie"])
if w == "Tak":
    import updater
    updater.update()
def createfile(localization_or_name,what_to_write=None,request_link=None,how_to_open="w+"): #jeżeli chcemy request_link wpisujemy None w what_to_write, przeciwnie robimy odwrotnie, jeśli nie chcemy nic to w obu miejscach None
    file = open(localization_or_name,how_to_open)
    if what_to_write != None:
        file.write(what_to_write)
    elif request_link != None:
        import requests
        file.write(requests.get(request_link).text)
    file.close()
print(os.listdir())
if len(os.listdir()) == 1:
    print("It's ok, we're only installing important thinks, you can find it below. Do not close this frame please.")
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
        import sys
        import subprocess
        print(sys.executable)
        subprocess.Popen([sys.executable, w+skos+"program.py"])
        exit()
try:
    import pygame
except:
    if os.name() == "nt":
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
if os.path.exists("uninstall.py"):
    w = easygui.buttonbox("Jesteś w zapisanym")
    print("uninstalling!")
    import subprocess
    import sys
    subprocess.run([sys.executable, "uninstall.py"])
    os.remove("uninstall.py")
pygame.init()  # initialize pygame modules (including font)
if os.path.exists("icon.png"):
    pass
else:
    import requests
    file = open("icon.png","wb")
    file.write(requests.get("https://raw.githubusercontent.com/maciejmin/TBOMT/main/icon.png").content)
    file.close()
x = 1920
y = 1080
icon = pygame.image.load("icon.png")
okno = pygame.display.set_mode([x, y], pygame.RESIZABLE | pygame.DOUBLEBUF)
pygame.display.set_caption("Początek Nowożytności")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()  # smooth the frame rate and resizing

# Obsługa scrolla
current_scroll = False  # False, 1 (scroll góra), lub -1 (scroll dół)


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
        draw_text(okno,"center","       ",[round(x/2),round(y/2)],round((x + y) / 10),"Monospace",is_button=True,button_padding=[10,100])
        draw_text(okno,"center",question,[round(x/2),round(y/3.2)],round((x + y) / text_size),"Monospace",is_button="False")
        for i in range(len(buttons)):
            if draw_text(okno,"center",buttons[i],[round(x/len(buttons))*i+round(x/len(buttons)/2),round(y/1.5)],round((x + y) / buttons_size),"Monospace",is_button=True)[0]:
                if draw_text(okno,"center",buttons[i],[round(x/len(buttons))*i+round(x/len(buttons)/2),round(y/1.5)],round((x + y) / buttons_size),"Monospace",is_button=True,color=[0,0,0],button_color=[255,255,255])[1]:
                    return i

game = "menu"
rozmiar = ["Bardzo malutki (1 biom)","Malutki (2 biomy)","Mały (3 biomy)","Zwykły (5 biomów)","Duży (6 biomów) Zalecany","Bardzo duży (8 biomów)","Wielki (10 biomów)","Ogromny (15 biomów)","Gigantyczny (20 biomów)"]
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
                game = "create"
        if draw_text(okno, "center", "Otwórz ustawienia", (round(x / 2), round(y / 2 + y / 20)), size=round((x + y) / 200), font_name="Monospace", is_button=True,color=[255,255,255])[0]:
            if draw_text(okno, "center", "-  Otwórz ustawienia  -", (round(x / 2), round(y / 2 + y / 20)), size=round((x + y) / 200), font_name="Monospace", is_button=True,color=[0,0,0],button_color=[255,255,255])[1]:
                game = "settings"
        if draw_text(okno, "center", "Wyjdź z gry", (round(x / 2), round(y / 2 + y / 10)), size=round((x + y) / 200), font_name="Monospace", is_button=True,color=[255,255,255])[0]:
            if draw_text(okno, "center", "-  Wyjdź z gry  -", (round(x / 2), round(y / 2 + y / 10)), size=round((x + y) / 200), font_name="Monospace", is_button=True,color=[0,0,0],button_color=[255,255,255])[1]:
                game = "quit"
    elif game == "create":
        try:
            file = open("datas.data","r+") #był wcześniej utworzony świat
            game = "open_world"
        except: #najwidoczniej trzeba utworzyć
            if buttonbox("Tworzenie świata, dobierz odpowiednie tobie opcje:",["Wróć","Ok"],100,100) == 0:
                game = "menu"
            elif buttonbox("Tworzenie świata, dobierz odpowiednie tobie opcje:",["Wróć","Ok"],100,100) == 1:
                #ustaw tutaj grę i zapisz i graj game = "play"
                pass
            scroll += draw_text(okno, "center", "Rozmiar świata: "+rozmiar[scroll], (round(x / 2), round(y / 2)), size=round((x + y) / 200), font_name="Monospace", is_button=True,color=[0,0,0],button_color=[255,255,255])[2]
            if scroll <= -1:
                scroll = 0
            elif scroll >= 9:
                scroll = 8
    pygame.display.update()
    clock.tick(60)  # ogranicz do ~60 FPS

pygame.quit()
