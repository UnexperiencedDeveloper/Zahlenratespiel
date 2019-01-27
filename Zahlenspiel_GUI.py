# Copyright Tim Matzenauer
# tmatzenauer@hotmail.de


import tkinter as tk
import time
from random import randint


class App(tk.Frame):

    anzahl_versuche = 0
    zeit_abgelaufen = None
    guessed_num = 0
    random_num = 0
    akt_level = 1
    spielzeit = None
    zahlenbereich = (akt_level *10)

    def __init__(self, parent):
        super().__init__(parent)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.label_timer_variable = tk.StringVar(value="")
        self.label_timer = tk.Label(self, font="Arial 18", width=17)
        self.label_timer["textvariable"] = self.label_timer_variable
        self.label_timer.grid(row=0, column=0, rowspan=2, columnspan=2, sticky="WS")

        self.label_trys_variable = tk.StringVar(value="Übrige Versuche \n{0}".format(App.anzahl_versuche))
        self.label_trys = tk.Label(self)
        self.label_trys["textvariable"] = self.label_trys_variable
        self.label_trys.grid(row=1, column=3)

        self.label_level_variable = tk.StringVar(value="Aktuelles Level \n{0}".format(App.akt_level))
        self.label_level = tk.Label(self, textvariable = self.label_level_variable)
        self.label_level.grid(row=1, column=4)

        self.button = tk.Button(self, text="Los geht's!", command=self.startgame)
        self.button.grid(row=4, column=3)

        self.exit_button = tk.Button(self, text="Beenden", command=root.destroy) # TODO Exit funktion
        self.exit_button.grid(row=4, column=4)



        self.info_label_variable = tk.StringVar(value="") # Höher/Niedrieger
        self.info_label = tk.Label(self, width=15, height=4)
        self.info_label["textvariable"] = self.info_label_variable
        self.info_label.grid(row=5, column=3)

        self.entry = tk.Entry(self, width=15)  # Erzeugen der tk.Entry
        self.entry.grid(row=5, column=1, sticky="W")
        self.entry.bind('<Return>', self.set_guessed_number)
        self.entry.grid_remove() # Wird erst beim onClick von Button erzeugt

        self.bereich_label_variable = tk.StringVar(value="")
        self.bereich_label = tk.Label(self, textvariable=self.bereich_label_variable)
        self.bereich_label.grid(row=4, column=1)



        self.menueleiste = tk.Menu(parent)
        parent["menu"] = self.menueleiste

        self.spiel_menue = tk.Menu(self.menueleiste, tearoff = False)
        self.spiel_menue.add_command(label ="Neues Spiel") # TODO: command hinzufügen
        self.spiel_menue.add_command(label="Level ändern")
        self.spiel_menue.add_command(label="Beenden")
        self.menueleiste.add_cascade(label="Spiel", menu = self.spiel_menue)



    def startgame(self):
        App.zeit_abgelaufen = False
        App.spielzeit = (time.time() + 10 + App.akt_level) # Standardwert für Level 1

        self.label_timer.config(fg="black")
        App.guessed_num = 0  # Reseten der Guessed Num, bei Spiel-Start
        App.anzahl_versuche = (10 + App.akt_level)
        self.label_trys_variable.set("Übrige versuche \n{0}".format(App.anzahl_versuche))

        App.zahlenbereich = (App.akt_level * 10)

        self.bereich_label_variable.set("Zahlenbereich von 1 - {0}".format(App.zahlenbereich))

        self.entry.delete(0, 100)
        self.info_label_variable.set("")
        self.set_random_number()
        self.timer()
        self.engine()
        self.entry.grid()
        self.entry.focus()




    def engine(self):
        if App.zeit_abgelaufen == False:
            if App.guessed_num != App.random_num:
                if App.anzahl_versuche !=0:
                    self.after(5, self.engine) # Looped mit sich selber

                    if (App.guessed_num != 0 and App.guessed_num > App.random_num):
                        self.info_label_variable.set("Niedriger")

                    if (App.guessed_num != 0 and App.guessed_num < App.random_num):
                        self.info_label_variable.set("Höher")
                else: # Anzahl Versuche aufgebraucht
                    app.label_timer_variable.set("Versuche aufgebraucht")
                    App.zeit_abgelaufen = True
                    self.entry.grid_remove()

            else: # Richtige Zahl erraten
                print("Du hast die Richtige Zahl erreicht") # TODO für Testzwecke

                App.zeit_abgelaufen = True
                App.akt_level += 1
                App.spielzeit += 1 # Pro leveaufstieg eine Sekunde mehr

                self.info_label_variable.set("Richtige Zahl erraten!\n ({0})".format(App.guessed_num))
                self.label_level_variable.set("Aktuelles Level \n{0}".format(App.akt_level))
                self.entry.grid_remove()

            # Hier die Funktion während Spieler in der Zeit

        else:
            #print("Zeit abgelaufen") # TODO für Testzwecke

            self.entry.grid_remove()
            # Spieler außerhalb der Zeit


    def set_guessed_number(self, event):
        if not App.zeit_abgelaufen:
            print("Enter gedrückt")
            try:
                App.guessed_num = int(self.entry.get())
            except ValueError:
                pass
            self.entry.delete(0, 100)
            App.anzahl_versuche -= 1
            self.label_trys_variable.set("Übrige versuche \n{0}".format(App.anzahl_versuche))

    def set_random_number(self):
        App.random_num = randint(1,App.zahlenbereich)


    def timer(self):
        if (App.guessed_num != App.random_num and App.anzahl_versuche != 0):
            if App.spielzeit >= time.time():

                self.label_timer_variable.set("{0:.1f}".format((App.spielzeit - time.time())))
                self.after(100, self.timer)
                if (App.spielzeit-time.time() <= 3):
                    #Zeit rot färben
                    self.label_timer.config(fg="red")

            else:
                app.label_timer_variable.set("Zeit abgelaufen")
                App.zeit_abgelaufen = True


    def exit(self):
        pass


root = tk.Tk()
root.title("Zahlenratespiel")
app = App(root)
app.pack()


root.update()
root.resizable(False, False)
root.minsize(root.winfo_width(),root.winfo_height())

root.mainloop()



