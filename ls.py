import sqlite3

def main(status: str = None):
    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()
    if status == None:
        cursor.execute("SELECT id, status FROM arkusze ORDER BY rok ASC, sesja ASC, numer ASC;")
    else: 
        cursor.execute("SELECT id, status FROM arkusze WHERE status = ? ORDER BY rok ASC, sesja ASC, numer ASC;", (status,))
    rows = cursor.fetchall()
    #print(rows)
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

def przedmiot(przedmiot: str):
    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()
    
    cursor.execute('SELECT arkusze.id, arkusze.status FROM arkusze LEFT JOIN "arkusz-przedmiot" ON "arkusz-przedmiot".id_arkusza = arkusze.id LEFT JOIN przedmioty ON przedmioty.id WHERE id_przedmiotu = ? ORDER BY rok ASC, sesja ASC, numer ASC;', (przedmiot,))

    rows = cursor.fetchall()
    #print(rows)
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




