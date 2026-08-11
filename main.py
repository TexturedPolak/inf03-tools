#!/usr/bin/python
import os
import pomoc
import init
import sys
import scan
import delete
import sqlite3
import ls
import find
import start
import start_last
import pause
import end
import repair

#arguments = sys.argv
#if len(arguments) >=2:
    #folder = os.path.abspath(arguments[1])
#else:
    #folder = os.path.abspath(".")
    #folder = None
def check_init():
    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="config";')
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    if len(rows) == 0:
        return False
    else:
        return True

inited = check_init()
# Menu główne
print("\033c", end='')
print("Witaj w systemie Pracownia INF03")
print("Skrypt ułatwia pracę z repozytorium.")
print("Co dzisiaj robimy?")
if not inited:
    print("* Zainicjalizuj najpierw bazę danych poleceniem INIT !")
url = "/"
while True:
    inited = check_init()
    print("")
    if not inited:
        komenda = input("(INIT ONLY)>> ")
    if inited:
        komenda = input(f"({url})>> ")
    print("\033c", end='')
    match komenda.lower():
        case "pomoc" | "help" if inited:
            pomoc.main()
        case "pomoc" | "help":
            pomoc.notinited()
        case "init" if not inited:
            init.main()
        case "scan" if inited:
            scan.main()
        case "del" if inited:
            delete.main()
        case "ls" if inited:
            ls.main()
        case "ls s nierozpoczete" if inited:
            ls.main("nierozpoczete")
        case "ls s niedokonczone" if inited:
            ls.main("niedokonczone")
        case "ls s zakonczone" if inited:
            ls.main("zakonczone")
        case "ls status":
            print("nierozpoczete", "niedokonczone", "zakonczone")
        case "ls p psi":
            ls.przedmiot("PSI")
        case "ls p pai":
            ls.przedmiot("PAI")
        case "ls p tiabd":
            ls.przedmiot("TIABD")
        case "ls p dom":
            ls.przedmiot("DOM")
        case "find" if inited:
            find.main()
        case "start" if inited:
            url = start.main()
        case "start last" if inited:
            url = start_last.main()
        case "pause" if inited and url != "/":
            if pause.main() == True:
                url = "/"
        case "end" if inited and url != "/":
            if end.main() == True:
                url = "/"
        case "repair" if inited and url != "/":
            repair.main()
        case _ if inited:
            print(f"Nie odnaleziono komendy {komenda.upper()} !")
        case _:
            print(f"Nie odnaleziono komendy {komenda.upper()} ,")
            print(f"albo jest niedostepna w obecnym stanie.")
            print("Zainicjalizuj najpierw bazę danych poleceniem INIT !")
            