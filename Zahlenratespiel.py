# Dies ist ein Simples Spiel in Python. Der Spieler muss eine zufällig generierte Zahl erraten.
# Tim Matzenauer, 28.01.2019
# Version 0.01


### IDEEN ###
"""
Spieler muss in bestimmter Zeit erraten, skalierend nach Level      CHECK
Anzahl versuche festlegen, sklaierend nach Level                    CHECK

"""
#############

from random import randint  # Importieren der Funktion Randint


def main():  # Alle 'Globalen' Variablen werden beim Start des Programms gesetzt
    level = 1
    print("")
    print("Wilkommen im Spiel!")
    print("")
    print("Du musst in diesem Spiel eine Zufallsgenerierte Zahl erraten")
    print("Sobald Du die korrekte Zahl erraten hast, steigt Dein Level und der Zufallsbereich vergrößert sich\n")
    menue(level)


def menue(level):
    # Menü anzeigen
    print("(N)eues Spiel")
    print("(L)evel ändern")
    print("(B)eenden")
    print("------------")
    print("Dein aktuelles Level: ",level, "\n")

    while True:
        try:
            aktion = input("Wie soll es weiter gehen?: ")

            if aktion == "N" or aktion == "n":
                # Prüfen der Eingabe auf Neues Spiel
                # Neues Spiel starten
                spiel_starten(level)
                break
            elif aktion == "L" or aktion == "l":
                # Level ändern
                level = level_aendern()
            elif aktion == "B" or aktion == "b":
                # Spiel beenden
                print("Auf wiedersehen :)")
                break
            else:
                print("Falsche Eingabe")
        except ValueError:
            print("Falsche Eingabe")
            continue


def spiel_starten(level):
    anzahl_versuche = 1  # Reseten der Anzahl der Versuche des Spielers, Standard ist 1

    bereich = level * 10
    zielzahl: int = randint(1, bereich)
    print("Neues Spiel beginnt, errate eine Zahl von 1 bis ", bereich)

    while True:
        tipp = int(input("Dein Tipp (0 für Aufgeben): "))
        if tipp == 0:  # prüfen ob Spieler aufgeben möchte -> zurück zum Menü
            print("")
            print("Schade, du hast aufgegeben")
            menue(level)
            break

        while tipp != zielzahl:
            anzahl_versuche += 1
            if tipp < zielzahl:
                print("Die gesuchte Zahl ist größer!")
                break
            if tipp > zielzahl:
                print("Die gesuchte Zahl ist kleiner!")
                break
        if tipp == zielzahl:
            print("LEVEL UP, Du hast die richtige Zahl ({0}) erraten!".format(zielzahl))

            if anzahl_versuche == 1:
                print("Du hast {0} versuch gebraucht!".format(anzahl_versuche))
            else:
                print("Du hast {0} versuche gebraucht!".format(anzahl_versuche))
            neues_level = level + 1
            menue(neues_level)  # Zurück zum Menü, neues Level wird als Argument übergeben
            break


def level_aendern():
    while True:
        try:

            eingabe = int(input("Gewünschtes Level wählen (1-10): "))

            if 1 <= eingabe <= 10:
                changed_level: int = eingabe

                return changed_level

            else:
                print("Auswahl muss zwischen 1 und 10 liegen")
        except ValueError:
            print("Falsche Eingabe")
            continue


main()
