import statements


class Doctor:
    def __init__(self,pesel,kursor, polaczenie):
        self.pesel=pesel
        self.kursor = kursor
        self.polaczenie=polaczenie
        self.id_lek = self.kursor.execute("SELECT id_lek FROM lekarze where pesel_lek = %s", self.pesel)
        # print(self.id_lek)
        self.choice()

    def choice(self):
        # print("to jest lekarz w srodku")
        # dec = input("S-show my appointments,\n D-delete an appointment,\n I-enter medicine to appropriate app.\n  "
        #             "C-check prescribed medicine,\n U-update prescribed medicine,\n M-delete prescribed medicine,\n "
        #             "Q-exit").upper()

        while True:
            dec = statements.Stat.getInputDoctor()
            if(dec=="S"):
                # print("Weszlo do if")
                self.show_app()
            elif dec == "I":
                self.insert_med()
            elif(dec=="D"):
                self.del_app()
            elif(dec=="C"):
                self.check_med()
            elif(dec=="Q"):
                print("Login finished")
                break
            else:
                print("Wrong character. Try again")

    def check_med(self):
        print()
        print("Medicine prescribed by you")
        self.kursor.execute("SELECT nr_wizyty, nazwa_leku, imie, nazwisko, pesel FROM leki_pacjentow where id_lekarza = %s", self.id_lek)
        pacjenci = self.kursor.fetchall()
        APP_NUMBER = 0
        MEDICINE_NAME =1
        PAT_NAME = 2
        PAT_SURNAME = 3
        PAT_PESEL = 4
        print()
        for row in pacjenci:
            print(row[APP_NUMBER], row[MEDICINE_NAME], row[PAT_NAME], row[PAT_SURNAME], row[PAT_PESEL])
        print()
        input("Press any button to continue")


    def insert_med(self):
        print()
        self.kursor.execute("SELECT nr_wizyty, imie, nazwisko, pesel FROM pacjenci_bez_lekow where id_lekarza = %s and nazwa_leku is NULL", self.id_lek)
        medicine = self.kursor.fetchall()
        if len(medicine) != 0:
            print()
            print("Following patients do not have their medicine prescribed yet: ")
            print()
            APP_NUMBER = 0
            PAT_NAME = 1
            PAT_SURNAME = 2
            PAT_PESEL = 3
            PRE_MEDICINE = set()
            while True:
                for row in medicine:
                    # print(row[0],row[1],row[2],row[3])
                    print("Appointment number: " + str(row[APP_NUMBER]) + "\tPatient details: " + str(row[PAT_NAME]) + " " + str(row[PAT_SURNAME]) + " " + str(row[PAT_PESEL]))
                    PRE_MEDICINE.add(row[APP_NUMBER])
                print()
                print("Select an appointment number to insert medicine")
                print(PRE_MEDICINE)
                dec = input()
                if dec.isdigit() and (int(dec) in PRE_MEDICINE):
                    med = input("Enter the name of medicine corresponfing to the appointment: " + str(int(dec)))
                    self.kursor.execute("Insert into przepisane_leki values (%s,%s)", (int(dec), med))
                    dec = input("Are you sure to update this record Y/N").upper()

                    if dec == 'Y':
                        self.polaczenie.commit()
                        print("Record updated")
                        break
                    else:
                        self.polaczenie.rollback()
                        print("No change in your record")
                        break

                else:
                    print("Wrong number entered. Press ENTER to exit to main menu or press T to Try again")
                    zm = 0
                    zm = input().upper()
                    if zm == 'T':
                        continue
                    else:
                        break
        else:
            print("All of your patients have an informtaion about prescribed medicine")
            print()



    def show_app(self):
        #print("show_app")
        self.kursor.execute("SELECT data_wizyty, imie, nazwisko, pesel FROM szczegoly_wizyty where id_lekarza = %s",
                            self.id_lek)
        pacjenci = self.kursor.fetchall()
        DATE_APP = 0
        PAT_NAME = 1
        PAT_SURNAME = 2
        PAT_PESEL = 3
        print()
        for row in pacjenci:
            print(row[DATE_APP], row[PAT_NAME], row[PAT_SURNAME], row[PAT_PESEL])
        print()
        a=input("Press any button to continue")

    def del_app(self):
        print("Delete app")
        self.kursor.execute("SELECT nr_wizyty, data_wizyty, imie, nazwisko, pesel FROM szczegoly_wizyty where id_lekarza = %s", self.id_lek)
        patients = self.kursor.fetchall()
        APP_NUMBER = 0
        DATE_APP = 1
        PAT_NAME = 2
        PAT_SURNAME = 3
        PAT_PESEL = 4
        doctor_app = set()
        while True:
            print()
            for row in patients:
                print("App number: " + str(row[APP_NUMBER]) + "\tPatient details: " + str(row[DATE_APP]) + " " +
                      str(row[PAT_NAME]) + " " + str(row[PAT_SURNAME]) + " " + str(row[PAT_PESEL]))
                doctor_app.add(row[APP_NUMBER])
            print()
            print("Select an appointment to delete and press corresponding number")
            print(doctor_app)
            dec = input()
            if dec.isdigit() and (int(dec) in doctor_app):
                try:
                    print(int(dec))
                    self.kursor.execute("DELETE FROM wizyty WHERE id_lekarza = %s and nr_wizyty = %s", (self.id_lek, dec))

                    dec = input("Are you sure to delete this appointment Y/N").upper()

                    if dec == 'Y':
                        self.polaczenie.commit()
                        print("Appointment canceled")
                        break
                    else:
                        self.polaczenie.rollback()
                        print("No change in your appointments")
                        break
                except:
                    print("Selected appointment can not be deleted. It has took place and you have already prescribed medicine\n")
                    break
            else:
                print("Wrong number entered. Press ENTER to exit to main menu or press T to Try again")
                zm = 0
                zm = input().upper()
                if zm == 'T':
                    continue
                else:
                    break