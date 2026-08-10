import os
import sqlite3
import random
def main():
    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()

    program_path = os.path.abspath(".")
    cursor.execute('SELECT directory FROM config WHERE id = "default"')
    path = cursor.fetchall()
    if len(path) >= 1:
        path = path[0][0]
    else:
        raise Exception("Path is not set!")
    os.chdir(os.path.abspath(path))
    lata = os.listdir(".")
    lata = [rok for rok in lata if rok[0] == "2" and len(rok) == 4]
    #print(lata)

    odnaleziono = 0
    for rok in lata:
        sesje = os.listdir(rok)
        sesje = [sesja for sesja in sesje if sesja == "czerwiec" or sesja == "styczeń"]
        #print(sesje)
        for sesja in sesje:
            arkusze = os.listdir(os.path.join(rok, sesja))
            arkusze = [arkusz for arkusz in arkusze if arkusz.isnumeric()]
            #print(arkusze)
            for arkusz in arkusze:

                # Pole id

                #print(f"{rok}/{sesja}/{arkusz}")
                # Numer arkusz
                if len(arkusz) == 2:
                    numer_arkusz = arkusz
                elif len(arkusz) == 1:
                    numer_arkusz = "0"+arkusz
                # Numer rok
                numer_rok = rok[2:]
                # Numer sesja
                if sesja == "czerwiec":
                    numer_sesja = "06"
                elif sesja == "styczeń":
                    numer_sesja = "01"
                id = f"INF.03-{numer_arkusz}-{numer_rok}.{numer_sesja}-SG" 
                #print(id)

                cursor.execute('SELECT id FROM arkusze WHERE id = ?;', (id,))
                rows = cursor.fetchall()

                #print(len(rows))

                if len(rows) >=1:
                    continue
                # Pole ścieżka

                sciezka = os.path.abspath(os.path.join(rok, sesja, arkusz))
                #print(sciezka)

                # Pole plik-arkusz
                
                plik_arkusz = f"inf_03_{rok}_{numer_sesja}_{numer_arkusz}_SG.pdf"
                if not os.path.exists(os.path.join(sciezka, plik_arkusz)):
                    print(f"(plik_arkusz) {os.path.join(sciezka, plik_arkusz)} nie istnieje !")

                # Pole plik-ocenianie
               
                plik_ocenianie = f"INF_03_{rok}_{numer_sesja}_{numer_arkusz}_SG_zo.pdf"
                plik_ocenianie2 = f"INF_03_{rok}_{numer_sesja}_{numer_arkusz}_SG_zo.xlsx"
                if not os.path.exists(os.path.join(sciezka, plik_ocenianie)):
                    plik_ocenianie = plik_ocenianie2
                    if not os.path.exists(os.path.join(sciezka, plik_ocenianie)):
                        print(f"(plik_ocenianie) {os.path.join(sciezka, plik_ocenianie)} lub .pdf nie istnieje !")

                # Pole plik-archiwum
                
                plik_archiwum = [archiwum for archiwum in os.listdir(sciezka) if archiwum[-3:] in ["zip", ".7z", "rar"]]
                if len(plik_archiwum) >= 1:
                    plik_archiwum = plik_archiwum[0]
                else:
                    plik_archiwum = None
                    print(f"(plik_archiwum) {id} Nie odnaleziono archiwum !")

                # Pole port

                cursor.execute('SELECT port FROM arkusze;')
                rows = cursor.fetchall()
                zajete = []
                if len(rows) >= 1:
                    zajete = [int(row[0]) for row in rows]
                port = random.randint(20000, 30000)
                while port in zajete:
                     port = random.randint(20000, 30000)

                # Zapytanie

                cursor.execute('INSERT INTO arkusze ("id", "sciezka", "plik_arkusz", "plik_ocenianie", "plik_archiwum", "rok", "sesja", "numer", "port") VALUES (?,?,?,?,?,?,?,?,?);', (id, sciezka, plik_arkusz, plik_ocenianie, plik_archiwum, int(numer_rok), int(numer_sesja), int(numer_arkusz), port))
                odnaleziono += 1

    print(f"Nowo odnalezionych arkuszy: {odnaleziono}")
            
    conn.commit()
    conn.close()
    os.chdir(program_path)
    
