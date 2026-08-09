import sqlite3
import os

def main():
    print("Podaj ścieżkę do folderu z arkuszami:")
    print()
    path = input("(INIT)>> ")
    print("\033c", end='')

    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="config";')
    rows = cursor.fetchall()

    if len(rows) == 0:
        inited = False
    else:
        inited = True

    if not inited:
        with open("database.sql", "r") as file:
            commands = file.read().split(";")
            for command in commands:
                cursor.execute(command+";")
        conn.execute('UPDATE config SET directory=? WHERE id = "default"', (os.path.abspath(path),))
        conn.commit()
        conn.close()

        print(f"Zainicjalizowano pomyślnie ze ścieżką {path} :)")
    else:
        print("Baza już zainicjalizowana.")
        #print("Chodziło ci o SCAN?")