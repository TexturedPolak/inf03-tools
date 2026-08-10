import sqlite3
import subprocess

def main():
    print("Podaj przedmiot (PSI/PAI/TIABD/DOM)")
    print()
    przedmiot = input("(START)>> ").upper()
    print("\033c", end='')

    #if przedmiot not in ("PSI", "PAI", "TIABD", "DOM"):
        #print(f"Niepoprawny przedmiot: {przedmiot} !")
        #return

    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM przedmioty WHERE id = ?", (przedmiot,))
    rows = cursor.fetchall()
    if len(rows) >= 1:
        if przedmiot != rows[0][0]:
            print(f"Niepoprawny przedmiot: {przedmiot} !")
            return "/"
        
    else:
        print(f"Niepoprawny przedmiot: {przedmiot} !")
        return "/"
        

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
            cursor.execute('INSERT INTO "arkusz-przedmiot" ("id_arkusza", "id_przedmiotu") VALUES (?, ?)', (id, przedmiot))
            conn.commit()
            subprocess.run(("podman", "run", "-d", "-p", f"{str(port)}:80", "-v", f"{sciezka}:/var/www/html:z", "--name", id, "texturedpolak/inf03"))
            cursor.execute('UPDATE arkusze SET status = "niedokonczone" WHERE id = ?', (id,))
            conn.commit()
        case "niedokonczone" | "zakonczone":
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

    conn.commit()
    conn.close()

    subprocess.run(["code", sciezka])
    subprocess.run(["google-chrome",f"http://localhost:{port}/" , f"http://localhost:{port}/phpmyadmin"])
    subprocess.run(["xdg-open", sciezka])

    print("Uruchomiono pomyślnie:")
    print(f"http://localhost:{port}/")
    print(f"http://localhost:{port}/phpmyadmin")

    return f"http://localhost:{port}/"

    