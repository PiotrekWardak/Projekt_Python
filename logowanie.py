import pymysql
import statements
import patient
import doctor

class Baza:
    def __init__(self):
        try:
            self.polaczenie = pymysql.connect("localhost", "root", "piotrek123", "przychodnia")
            statements.Stat.getConnectionMessage()
            self.logowanie()
        except:
            print ("Błąd. Połączenie z bazą nie powiodło się.")
    def logowanie(self):
        statements.Stat.log_in()
        funkcja = input().upper()

        if funkcja == 'L':
            print('Logowanie do panelu lekarza')
            pesel = input("podaj pesel")
            haslo = input("podaj haslo")
            self.kursor = self.polaczenie.cursor()
            self.kursor.execute("Select * from lekarze where pesel_lek = %s and haslo_lek = %s", (pesel, haslo))
            results_lekarze = self.kursor.fetchall()
            print(results_lekarze)
            if (len(results_lekarze) == 1):
                print("Logowanie zakonczylo sie sukcesem")
                doctor.lekarz(pesel,self.kursor)
            else:
                print("niepoprawny login lub haslo")
                self.logowanie()

        elif funkcja=='P':
            print('Logowanie do panelu pacjenta')
            pesel = input("podaj pesel")
            haslo = input("podaj haslo")
            self.kursor = self.polaczenie.cursor()
            self.kursor.execute("Select * from pacjenci where pesel = %s and haslo = %s", (pesel, haslo))
            results_pacjenci = self.kursor.fetchall()
            if (len(results_pacjenci) == 1):
                print("Logowanie zakonczylo sie sukcesem")

                patient.Pacjent(pesel,self.kursor, self.polaczenie)
                print("Zakonczenie logowania")
            else:
                print("niepoprawny login lub haslo")
                self.logowanie()
        elif funkcja == 'X':
            print("Wyszedłeś z programu")

        else:
            print("Wprowadzone dane nie istnieją. Spróbuj ponownie")
            self.logowanie()


