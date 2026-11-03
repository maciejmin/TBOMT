#v0.0.2|https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/extensions/basicextensions/noise.py
#AEV=1.0|v0.1
#Program służy do generowania świata dzięki losowym itp.
import time
import showy
def generate(scroll):
    teraz_procent = 0
    najnizszy_procent = 1000000000000
    rozmiar = [1,2,3,5,6,8,10,15,20]
    table = [] #tablica dwuwymiarowa max.y=rozmiar*100, x to samo
    import random
    maxx = rozmiar[scroll]*100
    maxy = rozmiar[scroll]*100
    maxkratka2 = maxy*maxx
    print("Generowanie terenu rozpocznie się teraz, łączna wielkość terenu wynosić będzie zatem",maxkratka2,"kratek.")
    for i in range(maxy):
        table.append([])
        for j in range(maxx):
            table[i].append("")
    for i in range(rozmiar[scroll]):
        table[random.randint(0,len(table))][random.randint(0,len(table[0]))] = random.choice(["a","b","c","d","e","f"])
        #print(random.choice(["a","b","c"]))
    #mamy wygenerowane pierwsze cos, teraz rozszerzamy teren
    y = 0 #przechodzimy po wysokości
    x = 0 #przechodzimy po szerokości
    #proces poniżej powtarzać dopóki nie będzie czarnych pól
    is_blacks = True #Czarne pola, będzie sprawdzane w pętli.
    czas_startu = time.time()
    while is_blacks:
        czas_startu_polecenia = time.time()
        while y < maxy: #wybieramy każdy y
            while x < maxx: #wybieramy każdy x
                if table[y][x] != "": #można zacząć rozszerzanie
                    if y > 0: #można generować nad kropką
                        if table[y-1][x] == "": #nie ma tam jeszcze nic, można generować
                            table[y-1][x] = str(table[y][x])
                    if y < maxy-1: #można generować pod kropką
                        if table[y+1][x] == "": #nie ma tam jeszcze nic, można generować
                            table[y+1][x] = str(table[y][x])
                            y += 1
                    #strefa x
                    if x > 0: #można generować po lewo od x
                        if table[y][x-1] == "": #nie ma nic można generować
                            table[y][x-1] = str(table[y][x])
                    if x < maxx-1:
                        if table[y][x+1] == "":
                            table[y][x+1] = str(table[y][x])
                            x += 1
                x += 1
                #print(x,y)
            y += 1
            x = 0
            #print(y)
        any_bioms = False
        is_blacks = False
        ilosc_laczna_pustych = 0
        for y in range(maxy): #y
            for x in range(maxx): #x
                if table[y][x] == "":
                    is_blacks = True
                    ilosc_laczna_pustych += 1
                if table[y][x] != "":
                    any_bioms = True
                    #print("\""+table[x][y]+"\"")
        print("Po tej rundzie jest:",ilosc_laczna_pustych,"pozostałych miejsc do wypełnienia.")
        try:
            wczesniejszy_procent = teraz_procent
            if teraz_procent-wczesniejszy_procent < najnizszy_procent:
                najnizszy_procent = teraz_procent-wczesniejszy_procent
            teraz_procent = ilosc_laczna_pustych/maxkratka2*100
            print("Pozostało zatem",teraz_procent,"%.")
            print("Odjęto więc ostatnio",teraz_procent-wczesniejszy_procent)
            print("Najniższy procent:",najnizszy_procent)
            print("Wyliczony przybliżony czas do końca:",(time.time()-czas_startu)/(maxkratka2-ilosc_laczna_pustych)*ilosc_laczna_pustych,"sekund.")
            print("Wyliczony czas do końca na podstawie poprzedniego czasu zadania:",(time.time()-czas_startu_polecenia)*(teraz_procent/(wczesniejszy_procent-teraz_procent)))
        except:
            print("Ukończono!")
        if any_bioms != True:
            print("no bioms!")
            break
        x = 0
        y = 0
    return table
#-#
#i|292|noise.generate(scroll)|2|True
showy.show(generate(5))
