import os
try:
    import easygui
except:
    if os.name() == "nt":
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

if len(os.getcwd()) == 1:
    print("It's ok, we're only installing important thinks, you can find it below. Do not close this frame please.")
elif not "opened_data.data" in os.getcwd():
    w = easygui.enterbox("Nie znaleźliśmy żadnego pliku z zapisanymi danymi dotyczącymi poprzedniego otwarcia aplikacji, ale wygląda na to, że w tym folderze już są pliki. Zaleca się, aby gra znajdowała się w jednym folderze, ponieważ tworzy własne pliki, co może w przyszłości powodować problemy z czytelnością. Chcesz wybrać folder, w którym ta gra będzie zlokalizowana, czy wybrać domyślny folder dla tej gry? Jeżeli chcesz, wpisz nazwę tego folderu i kliknij \"OK\". W przeciwnym razie kliknij przycisk cancel, będziemy wiedzieli wtedy, że nie chcesz instalować.","Początek Nowożytności - instalacja",os.path.expanduser("~")+"/tbomt")
    if w == None:
        easygui.msgbox("Bye!")
    else:
        print("Wait...")
        os.makedirs(w, exist_ok=True)
        file = open(w+"/opened_data.data","w+")
        file.write("0")
        file.close()
        file = open(w+"/program.py")
        import requests
        file.write()
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

pygame.init()  # initialize pygame modules (including font)

x = 1920
y = 1080
okno = pygame.display.set_mode([x, y], pygame.RESIZABLE | pygame.DOUBLEBUF)
pygame.display.set_caption("Life Simulation")

clock = pygame.time.Clock()  # smooth the frame rate and resizing


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
        [is_hovered, is_clicked]: Lista gdzie is_hovered=1 jeśli mysz jest nad elementem, 
                                  is_clicked=1 jeśli przycisk myszy jest wciśnięty nad elementem.
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
        is_hovered = 1 if button_rect.collidepoint(mouse_pos) else 0
        is_clicked = 1 if is_hovered and pygame.mouse.get_pressed()[0] else 0
        return [is_hovered, is_clicked]

    surface.blit(surf, rect)
    
    # Sprawdzenie hover i click
    mouse_pos = pygame.mouse.get_pos()
    is_hovered = 1 if rect.collidepoint(mouse_pos) else 0
    is_clicked = 1 if is_hovered and pygame.mouse.get_pressed()[0] else 0
    return [is_hovered, is_clicked]


game = "menu"

while game != "quit":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = "quit"
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
        draw_text(okno, "center", "Welcome to the Life Simulation!", (round(x / 2), round(y / 2 - y / 20)), size=round((x + y) / 100), font_name="Monospace")
        draw_text(okno, "center", "Enter saved file with simulation data", (round(x / 2), round(y / 2 + y / 20)), size=round((x + y) / 200), font_name="Monospace", is_button=True)

    pygame.display.update()
    clock.tick(60)  # ogranicz do ~60 FPS

pygame.quit()
