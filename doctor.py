import statements

class lekarz:
    def __init__(self,pesel,kursor):
        self.pesel=pesel
        self.choice()
        self.kursor=kursor
    def choice(self):
        print("to jest pacjent w srodku")
        while True:
            dec = statements.getinput()
            if(dec=="S"):
                print("Weszlo do if")
                self.select()
            elif dec == "I":
                self.insert()
            elif(dec=="D"):
                self.delete()
            elif(dec=="U"):
                self.update()
            elif(dec=="Q"):
                print("Wyszedles z programu")
                break
            else:
                print("Bledny wybor. Sprobuj jeszcze raz")
