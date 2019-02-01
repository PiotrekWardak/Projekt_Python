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
            print ("Error. Connection with database failed.")
    def logowanie(self):
        statements.Stat.log_in()
        funkcja = input().upper()

        if funkcja == 'L':
            print('Logging to doctor\'s account')
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
            print('Logging to patient account')
            pesel = input("podaj pesel")
            haslo = input("podaj haslo")
            self.kursor = self.polaczenie.cursor()
            self.kursor.execute("Select * from pacjenci where pesel = %s and haslo = %s", (pesel, haslo))
            results_pacjenci = self.kursor.fetchall()
            if (len(results_pacjenci) == 1):
                print("Login Succeeded")

                patient.Patient(pesel, self.kursor, self.polaczenie)
                print("Program closed")
            else:
                print("niepoprawny login lub haslo")
                self.logowanie()
        elif funkcja == 'X':
            print("Program closed")

        else:
            print("Wprowadzone dane nie istnieją. Spróbuj ponownie")
            self.logowanie()


