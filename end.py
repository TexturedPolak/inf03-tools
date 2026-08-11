import subprocess
import get_last
import sqlite3
def main():
    id = get_last.main()
    if get_last != False:
        subprocess.run(("podman", "stop", id))
        print(f"Wstrzymano kontener {id}")
        conn = sqlite3.connect('database.sqlite3')
        cursor = conn.cursor()
        cursor.execute('UPDATE arkusze SET status = "zakonczone" WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        print("Oznaczono jako zakonczone :)")
        return True
    else:
        return False