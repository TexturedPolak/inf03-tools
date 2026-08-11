def notinited():
    print("Pomoc systemu Pracownia INF03:")
    print("POMOC/HELP: Wyświetla pomoc.")
    print("INIT: Inicjalizuje bazę danych.")
    print()
    print("Więcej komend dostępnych po inicjalizacji:")
    print("Zainicjalizuj najpierw bazę danych poleceniem INIT !")

def main():
    print("Pomoc systemu Pracownia INF03:")
    print("POMOC/HELP: Wyświetla pomoc.")
    print("SCAN: Skanuje foldery w poszukiwaniu nowych arkuszy.")
    print("DEL: Usuwa dany arkusz z bazy.")
    print("LS: Wyświetla dostępne arkusze w kolejności od najstarszego do najnowszego.")
    print("LS S <STATUS>: Wyświetla arkusze z danym statusem w kolejności od najstarszego do najnowszego ze wskazanym statusem.")
    print("LS P <PRZEDMIOT>: Wyświetla arkusze z danym przedmiotem w kolejności od najstarszego do najnowszego ze wskazanym statusem.")
    print("FIND: Szuka arkusza po roku, miesiącu, numerze.")
    print("START: Rozpoczyna / wznawia pracę z arkuszem. Wymaga id arkusza.")
    print("START LAST: Wznawia pracę nad ostatnio używanym arkuszem.")
    print("\tPAUSE: Kończy pracę z arkuszem w stanie niedokonczone.")
    print("\tEND: Kończy pracę z arkuszem stanie zakonczone.")
    print("\tREPAIR: Resetuje kontener do stanu zerowego.") # TODO