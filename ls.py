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
        print(f"{row[0]} : {row[1]}")
    conn.commit()
    conn.close()




