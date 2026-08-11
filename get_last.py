import sqlite3
def main():
    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()
    
    cursor.execute('SELECT last FROM config WHERE id = "default"')
    rows = cursor.fetchall()
    if len(rows) >= 1:
        id = rows[0][0]
    else:
        print("Hę?")
        return False
    
    cursor.execute('SELECT id FROM arkusze WHERE id = ?', (id,))
    rows = cursor.fetchall()
    if len(rows) >= 1:
        if id != rows[0][0]:
            print(f"Nie istnieje taki arkusz: {id} !")
            return False
    else:
        print(f"Nie istnieje taki arkusz: {id} !")
        return False
    
    conn.commit()
    conn.close()

    return id