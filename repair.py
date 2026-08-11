import subprocess
import get_last
import sqlite3
def main():
    id = get_last.main()
    if get_last != False:
        subprocess.run(("podman", "stop", id))
        print(f"Wstrzymano kontener {id}")
        subprocess.run(("podman", "rm", "-f", id))
        print(f"Usunięto kontener {id}")
        conn = sqlite3.connect('database.sqlite3')
        cursor = conn.cursor()
        cursor.execute("SELECT id, sciezka, port FROM arkusze WHERE id = ?", (id,))
        rows = cursor.fetchall()
        if len(rows) >= 1:
            sciezka = rows[0][1]
            port = rows[0][2]
        else:
            print(f"Nieoczekiwany błąd :(")
            return False
        conn.commit()
        conn.close()
        subprocess.run(("podman", "run", "-d", "-p", f"{str(port)}:80", "-v", f"{sciezka}:/var/www/html:z", "--name", id, "texturedpolak/inf03"))
        print(f"Uruchomiono nowy kontener {id}")
        print(f"http://localhost:{port}/")
        print(f"http://localhost:{port}/phpmyadmin")
        return True
    else:
        return False