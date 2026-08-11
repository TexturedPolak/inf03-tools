import sqlite3
import subprocess

def main(id: str = None, przedmiot: str = None):
    if przedmiot == None:
        print("Podaj przedmiot (PSI/PAI/TIABD/DOM)")
        print()
        przedmiot = input("(START)>> ").upper()
        print("\033c", end='')

    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM przedmioty WHERE id = ?", (przedmiot,))
    rows = cursor.fetchall()
    if len(rows) >= 1 and przedmiot != "":
        if przedmiot != rows[0][0]:
            print(f"Niepoprawny przedmiot: {przedmiot} !")
            return "/"
        
    elif przedmiot != "":
        print(f"Niepoprawny przedmiot: {przedmiot} !")
        return "/"
        
    if id == None:
        print("Podaj id arkusza (INF.03-XX-XX.XX-SG)")
        print()
        id = input("(START)>> ").upper()
        print("\033c", end='')

        

    cursor.execute("SELECT id FROM arkusze WHERE id = ?", (id,))
    rows = cursor.fetchall()

    if len(rows) >= 1:
        if rows[0][0] != id:
            print(f"Niepoprawne id: {id} !")
            return "/"
    else:
        print(f"Niepoprawne id: {id} !")
        return "/"

    cursor.execute("SELECT id, status, sciezka, port FROM arkusze WHERE id = ?", (id,))
    rows = cursor.fetchall()
    if len(rows) >= 1:
        status = rows[0][1]
        sciezka = rows[0][2]
        port = rows[0][3]
    else:
        print(f"Nieoczekiwany błąd :(")
        return "/"

    match status:
        case "nierozpoczete":
            if przedmiot != "":
                cursor.execute('INSERT INTO "arkusz-przedmiot" ("id_arkusza", "id_przedmiotu") VALUES (?, ?)', (id, przedmiot))
                conn.commit()
            else:
                print("Nie podano przedmiotu dla nowego arkusza !")
                return
            subprocess.run(("podman", "run", "-d", "-p", f"{str(port)}:80", "-v", f"{sciezka}:/var/www/html:z", "--name", id, "texturedpolak/inf03"))
            cursor.execute('UPDATE arkusze SET status = "niedokonczone" WHERE id = ?', (id,))
            conn.commit()
        case "niedokonczone" | "zakonczone":
            if przedmiot != "":
                cursor.execute('SELECT "id_przedmiotu" FROM "arkusz-przedmiot" WHERE "id_arkusza" = ?',(id,))
                rows = cursor.fetchall()
                if len(rows) >= 1:
                    obecne = [row[0] for row in rows]
                else:
                    obecne = []
                if przedmiot not in obecne:
                    cursor.execute('INSERT INTO "arkusz-przedmiot" ("id_arkusza", "id_przedmiotu") VALUES (?, ?)', (id, przedmiot))
                    conn.commit()
            subprocess.run(("podman", "start", id))

    cursor.execute('UPDATE config SET last = ? WHERE id = "default"', (id,))

    cursor.execute("SELECT id, status FROM arkusze WHERE id = ?", (id,))
    rows = cursor.fetchall()
    for row in rows:
        id = row[0]
        cursor.execute('SELECT przedmioty.id FROM przedmioty LEFT JOIN "arkusz-przedmiot" ON "arkusz-przedmiot".id_przedmiotu = przedmioty.id LEFT JOIN arkusze ON arkusze.id = "arkusz-przedmiot".id_arkusza WHERE arkusze.id = ?;', (id,))
        przedmioty_rows = cursor.fetchall()
        przedmioty = ""
        for przedmiot_row in przedmioty_rows:
            przedmioty += przedmiot_row[0] + " "
        
        print(f"{row[0]} : {row[1]} {przedmioty}")



    conn.commit()
    conn.close()

    subprocess.run(["code", sciezka])
    subprocess.run(["google-chrome",f"http://localhost:{port}/" , f"http://localhost:{port}/phpmyadmin"])
    subprocess.run(["xdg-open", sciezka])




    print("Uruchomiono pomyślnie:")
    print(f"http://localhost:{port}/")
    print(f"http://localhost:{port}/phpmyadmin")

    return f"http://localhost:{port}/"

    