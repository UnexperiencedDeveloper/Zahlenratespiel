import time
from random import randint

# Was ist neu?
# -> Zeitbegrenzung ab Level 10, skalierend mit Level
# -> begrenzte Versuche ab Level 10, skalierend mit Level



def main(): # Das Spiel wird in der main() gestartet und führt nach beendigung zu menue() zurück

    level = 1  # Spielerlevel, standardmäßiger Start bei 1

   ###### Begrüßungstext ######

    print("")
    print("Wilkommen im Spiel!")
    print("")
    print("In diesem Spiel musst Du eine Zufallsgenerierte Zahl erraten.")
    print("Der Zahlenbereich ist abhängig von deinem Level, welches mit der Zeit steigt.")
    print("Apropos Zeit! Ab einem bestimmten Level wird die Zeit begrenzt sein und deine Versuche!")
    print("Sobald Du die korrekte Zahl erraten hast, vergrößert sich der Zahlenbereich\n\n")

   ###### Begrüßungstext ######

    menue(level) # Zu beginn wird das Menü aufgerufen


# über die main() wird spiele_enginge() aufgerufen


def spielzeit_timer(level, systemzeit):    # Berechnen der Spielzeit

    spielzeit = systemzeit + int(level / 1.07)

    if level >= 10: # Zeitbegrenung erst ab Level 10, unter Level 10 wird permanent True zurückgegeben

        if time.time() < spielzeit:  # ist aktuelle Zeit größer als Spielzeit wird FALSE zurückgegeben, das Spiel wird beendet
            return True
        else:
            return False
    else:
        return True


def spiel_engine(level): # Hier läuft das Spiel, finden die Berechnungen statt
    # anzahl versuche und Zeit abhängig von Level
    anzahl_max_versuche = 100
    systemzeit = time.time()

    if level >= 10:
        anzahl_max_versuche = int(level / 1.01) # Anzahl der Maximalen Versuche -> Aktuelles Level / 1.01, sofern über Level 10

    bereich = level * 10
    zielzahl: int = randint(1, bereich)

    print("Spiel startet, rate eine Zahl zwischen 1 und {0}".format(bereich))
    ansage = ["3..", "2..", "1..", "Los"]
    for i in ansage:
        time.sleep(1)
        print(i)



    while spielzeit_timer(level, systemzeit):  # Zeitbegrenzung durch Spielzeit->While spielzeit_timer nicht abgelaufen(True)
        if anzahl_max_versuche == 0:    # Prüfen ob max Versuche aufgebraucht. Ja -> Menü. Nein -> Weiterspielen
            print("\nMaximale Anzahl der Versuche erreicht :(")
            print("{0} wäre die richtge Zahl geewesen".format(zielzahl))
            menue(level)
            break
        try:
            tipp = int(input(("Dein Tipp: (0 für Aufgeben)")))
            if tipp == 0:
                while True:         ############ Abfrage wirklich aufgeben, wenn ja -> zurück zu Menü. Nein -> weiterspielen
                    abfrage = input("Wirklich aufgeben? Du verlierst dein aktuelles Level! (J/N)").upper()
                    if abfrage == "J":
                        level = 1
                        menue(level)
                    elif abfrage == "N":
                        break
                    else:
                        print("Falsche Eingabe")
                        continue    ########### Abfrage wirklich aufgeben ############

            while tipp != zielzahl:
                if tipp < zielzahl:
                    print("Die gesuchte Zahl ist größer")
                    anzahl_max_versuche -= 1
                    break
                else:
                    print("Die gesuchte Zahl ist kleiner")
                    anzahl_max_versuche -= 1
                    break
            else:
                print("\nGlückwunsch! Du hast die richtige Zahl ({0}) erraten!".format(zielzahl))
                level += 1
                menue(level)
                break
        except ValueError: # Except für Tipp-Abfrage
            print("Falsche Eingabe")
    else:
        print("\nHoppla, die Zeit ist vorbei :(\n")
        print("Anzahl übrige Versuche: ", anzahl_max_versuche)
        print("{0} wäre die richtge Zahl geewesen".format(zielzahl))
        menue(level)



def menue(level):

    while True:
        print("------------")
        print("(S)piel starten")
        print("(L)evel ändern (aktuelles Level: {0})".format(level))
        print("(B)eenden")
        print("------------")

        eingabe = input("\nEingabe: ").upper()

        if eingabe == "S":
            print("Spiel starten")
            spiel_engine(level)
            break
        elif eingabe == "L":
            print("Level ändern")
            level_aendern(level)
            break
        elif eingabe == "B":
            print("\nAuf Wiedersehen :)")
            time.sleep(0.5)
            break
        else:
            print("\nFalsche Eingabe\n")
            continue


def level_aendern(level):


    while True:
        new_level = input("Level setzen (leer für Menü): ")
        try:
            if new_level == "":
                print("Bitte Level eingeben")
                continue
            elif new_level == " ":
                menue(level)
                break
            else:
                menue(int(new_level))
                break
        except ValueError:
            print("Neues Level muss eine Ganz-Zahl sein")
            continue



main()