import statements


class Patient:
    def __init__(self,pesel,kursor,polaczenie):
        self.pesel=pesel
        self.polaczenie=polaczenie
        self.kursor=kursor
        self.id = self.kursor.execute("SELECT id FROM pacjenci where pesel = %s", self.pesel)
        self.choice()

    def choice(self):
        # print("to jest pacjent w srodku")
        # print("S-show my appointments, M - make a new appointment, D-delete an appointment,
        # C-check prescribed medicine, Q-exit")
        while True:
            dec = statements.Stat.getInputPatient()
            if dec=="S":
                # print("Weszlo do if")
                self.select_app()
            elif dec=='M':
                self.new_app()
            elif dec=='D':
                self.del_app()
            elif dec=='C':
                self.check_medicine()
            elif dec=="Q":
                print("Login finished")
                break
            else:
                print("Wrong character. Try again")

    def select_app(self):
        print()
        print("Your appointments: ")

        # self.kursor.execute("SELECT * FROM pacjenci where pesel = %s", self.pesel)
        self.kursor.execute("SELECT * FROM szczegoly_wizyty where pesel = %s", self.pesel)
        pacjenci = self.kursor.fetchall()
        DATE_APP = 1
        SPEC = 7
        DOC_NAME = 8
        DOC_SURNAME = 9
        print()
        for row in pacjenci:
            print(row[DATE_APP], row[SPEC], row[DOC_NAME], row[DOC_SURNAME])
        print()

    def new_app(self):
        print()
        print("To schedule an appointment,please select a number corresponding to your doctor ")
        self.kursor.execute("SELECT * FROM lekarze")
        pacjenci = self.kursor.fetchall()
        while True:
            print()
            for row in pacjenci:
                DR_ID = 0
                DOC_NAME = 1
                DOC_SUR = 2
                SPEC = 3
                print(row[DR_ID], row[DOC_NAME], row[DOC_SUR], row[SPEC])
            print()
            dec = input("Type doctor/'s id: ")
            print()
            if dec.isdigit():
                if 0 < int(dec) <= len(pacjenci):
                    val = self.make_app(dec, self.id)
                    if val == 0:
                        print("You decided to go to main menu")
                        break
                    else:
                        print("The appointment is correctly added")
                        break
                else:
                    print("Number which you entered is out of range. Try again.")
                    continue
            else:
                print("Wrong character entered. Press ENTER to exit to main menu or press T to Try again")
                zm = 0
                zm = input().upper()
                if zm == 'T':
                    continue
                else:
                    break

    def make_app(self,dr_id,patient_id):
        self.dr_id = dr_id
        self.patient_id = patient_id
        print()
        print("Type preferred date of appointment")
        day = input("day: ")
        month = input("month: ")
        year = input("year: ")
        date_of_app = year + "-" + month + "-" + day
        print(date_of_app)


        if (day.isdigit() and (1 <= int(day) <= 31)) and (month.isdigit() and (1 <= int(month) <= 12)) and \
                (year.isdigit() and (2019 <= int(year) <= 2025)):
            print("You typed correct date")
            self.kursor.execute("Insert into wizyty (id_pacjenta,id_lekarza, data_wizyty) values (%s,%s,%s)",
                                (self.patient_id, self.dr_id,date_of_app))
            self.polaczenie.commit()

        else:
            print("Wrong date entered. Press any character to try again or press q to exit to main manu")
            dec = input().upper()
            if dec == 'Q':
                return 0
            else:
                self.new_app()

    def del_app(self):
        print()
        print("Delete selected appointment ")
        self.kursor.execute("SELECT * FROM szczegoly_wizyty where pesel = %s", self.pesel)
        appointments = self.kursor.fetchall()
        APP_NUMB = 0
        DATE_APP = 1
        SPEC = 7
        DOC_NAME = 8
        DOC_SURNAME = 9
        patient_app = set()
        while True:
            print()
            for row in appointments:
                print("App number: " + str(row[APP_NUMB]) + "\t Date: " + str(row[DATE_APP]) + "\t Doctor details:  " +
                      str(row[SPEC]) + " " + str(row[DOC_NAME]) + " " + str(row[DOC_SURNAME]))
                patient_app.add(row[APP_NUMB])
            print()
            print("Select an appointment to delete and press corresponding number")
            print(patient_app)
            dec = input()
            if dec.isdigit() and (int(dec) in patient_app):
                self.kursor.execute("DELETE FROM wizyty WHERE id_pacjenta = %s and nr_wizyty = %s", (self.id,dec))
                dec = input("Are you sure to delete this appointment Y/N").upper()

                if (dec == 'Y'):
                    self.polaczenie.commit()
                    print("Appointment canceled")
                    break
                else:
                    self.polaczenie.rollback()
                    print("No change in your appointments")
                    break
            else:
                print("Wrong number entered. Press ENTER to exit to main menu or press T to Try again")
                zm = 0
                zm = input().upper()
                if zm == 'T':
                    continue
                else:
                    break

    def check_medicine(self):
        print()
        print("Medicine prescribed for you ")
        self.kursor.execute("SELECT * FROM leki_pacjentow where pesel = %s", self.pesel)
        pacjenci = self.kursor.fetchall()
        print()
        for row in pacjenci:
            SPEC = 3
            DOC_NAME = 4
            DOC_SUR = 5
            MED = 9
            print(row[MED] + " prescribed by " + row[DOC_NAME] + " " + row[DOC_SUR] + " - " + row[SPEC])
        print()