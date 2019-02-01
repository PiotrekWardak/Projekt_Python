import pymysql
import statements
import patient
import doctor


class Base:
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

        if funkcja == 'D':
            print('Logging to doctor\'s account')
            pesel = input("Enter PESEL number: ")
            haslo = input("Enter password: ")
            self.kursor = self.polaczenie.cursor()
            self.kursor.execute("Select * from lekarze where pesel_lek = %s and haslo_lek = %s", (pesel, haslo))
            results_lekarze = self.kursor.fetchall()
            if (len(results_lekarze) == 1):
                print("Login succeeded")
                doctor.Doctor(pesel, self.kursor, self.polaczenie)
            else:
                print("Wrong PESEL number or password")
                self.logowanie()

        elif funkcja=='P':
            print('Logging to patient account')
            pesel = input("Enter PESEL number: ")
            haslo = input("Enter password: ")
            self.kursor = self.polaczenie.cursor()
            self.kursor.execute("Select * from pacjenci where pesel = %s and haslo = %s", (pesel, haslo))
            results_pacjenci = self.kursor.fetchall()
            if (len(results_pacjenci) == 1):
                print("Login Succeeded")

                patient.Patient(pesel, self.kursor, self.polaczenie)
                print("Program closed")
            else:
                print("Wrong PESEL number or password")
                self.logowanie()
        elif funkcja == 'X':
            print("Program closed")

        else:
            print("Entered data do not exist. Please try again. ")
            self.logowanie()


