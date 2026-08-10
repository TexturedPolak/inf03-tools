import sqlite3
import subprocess

def main():
    print("Podaj id arkusza do usunięcia:")
    print()
    id = input("(DEL)>> ")
    print("\033c", end='')
    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM arkusze WHERE id = ?;', (id,))
    rows = cursor.fetchall()
    if len(rows) >= 1:
        cursor.execute('DELETE FROM arkusze WHERE id = ?;', (id,))
        cursor.execute('DELETE FROM "arkusz-przedmiot" WHERE "id_arkusza" = ?',(id,))
        subprocess.run(("podman","rm","-f", id))
        print(f"Usunięto {id}")
    else:
        print(f"{id} nie istnieje !")

    conn.commit()
    conn.close()