import sqlite3

def main():
    print("Podaj rok (np. 26)")
    print()
    rok = input("(FIND)>> ")
    print("\033c", end='')
    try:
        if rok != "":
            rok = int(rok)
    except:
        print(f"Podano niepoprawny rok: {rok}")
        return
    print("Podaj miesiąc (6 lub 1)")
    print()
    miesiac = input("(FIND)>> ")
    print("\033c", end='')
    try:
        if miesiac != "":
            miesiac = int(miesiac)
    except:
        print(f"Podano niepoprawny miesiąc: {miesiac}")
        return
    print("Podaj numer (liczba)")
    print()
    numer = input("(FIND)>> ")
    print("\033c", end='')
    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()
    try:
        if numer != "":
            numer = int(numer)
    except:
        print(f"Podano niepoprawny numer: {numer}")
        return
    if rok == "" and miesiac == "" and numer == "":
        print("Szukanie INF.03-XX-XX.XX-SG...")
        print()
        cursor.execute("SELECT id, status FROM arkusze ORDER BY rok ASC, sesja ASC, numer ASC;")
    elif rok != "" and miesiac == "" and numer == "":
        print(f"Szukanie INF.03-XX-{rok:02d}.XX-SG...")
        print()
        cursor.execute("SELECT id, status FROM arkusze WHERE rok = ? ORDER BY rok ASC, sesja ASC, numer ASC;", (rok,))
    elif rok == "" and miesiac != "" and numer == "":
        print(f"Szukanie INF.03-XX-XX.{miesiac:02d}-SG...")
        print()
        cursor.execute("SELECT id, status FROM arkusze WHERE sesja = ? ORDER BY rok ASC, sesja ASC, numer ASC;", (miesiac,))
    elif rok == "" and miesiac == "" and numer != "":
        print(f"Szukanie INF.03-{numer:02d}-XX.XX-SG...")
        print()
        cursor.execute("SELECT id, status FROM arkusze WHERE numer = ? ORDER BY rok ASC, sesja ASC, numer ASC;", (numer,))
    elif rok != "" and miesiac != "" and numer == "":
        print(f"Szukanie INF.03-XX-{rok:02d}.{miesiac:02d}-SG...")
        print()
        cursor.execute("SELECT id, status FROM arkusze WHERE rok = ? AND sesja = ? ORDER BY rok ASC, sesja ASC, numer ASC;", (rok,miesiac))
    elif rok == "" and miesiac != "" and numer != "":
        print(f"Szukanie INF.03-{numer:02d}-XX.{miesiac:02d}-SG...")
        print()
        cursor.execute("SELECT id, status FROM arkusze WHERE sesja = ? AND numer = ? ORDER BY rok ASC, sesja ASC, numer ASC;", (miesiac,numer))
    elif rok != "" and miesiac == "" and numer != "":
        print(f"Szukanie INF.03-{numer:02d}-{rok:02d}.XX-SG...")
        print()
        cursor.execute("SELECT id, status FROM arkusze WHERE rok = ? AND numer = ? ORDER BY rok ASC, sesja ASC, numer ASC;", (rok,numer))
    elif rok != "" and miesiac != "" and numer != "":
        print(f"Szukanie INF.03-{numer:02d}-{rok:02d}.{miesiac:02d}-SG...")
        print()
        cursor.execute("SELECT id, status FROM arkusze WHERE rok = ? AND sesja = ? AND numer = ? ORDER BY rok ASC, sesja ASC, numer ASC;", (rok,miesiac,numer))

    rows = cursor.fetchall()
    for row in rows:
        id = row[0]
        cursor.execute('SELECT przedmioty.id FROM przedmioty LEFT JOIN "arkusz-przedmiot" ON "arkusz-przedmiot".id_przedmiotu = przedmioty.id LEFT JOIN arkusze ON arkusze.id = "arkusz-przedmiot".id_arkusza WHERE arkusze.id = ?;', (id,))
        przedmioty_rows = cursor.fetchall()
        przedmioty = ""
        for przedmiot_row in przedmioty_rows:
            przedmioty += przedmiot_row[0] + " "
        
        print(f"{row[0]} : {row[1]} {przedmioty}")
        #print(f"{row[0]} : {row[1]}")
    conn.commit()
    conn.close()