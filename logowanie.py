import pymysql



"""
obiekt kursora:

Aby móc wykonywać operacje na bazie, potrzebujemy obiektu tzw. kursora
sluzy do pobierania oraz modyfikacji danych w bazie danych.


"""
class Helper:

    @classmethod
    def getConnectionMessage(cls):
        print ("Polaczenie ustanowione. Wiadomosc z helpera")
    @classmethod
    def getinput(cls):
        dec = input("S-show, I-insert, D-delete, U-update, Q-exit").upper()
        return dec


class DBConnect:
    def __init__(self):
        try:
            self.conn = pymysql.connect("localhost","root","piotrek123","test_python")
            print("polaczenie ustanowione")
            Helper.getConnectionMessage()
            self.logowanie()
        except:
            print ("bledne dane logowania")
    def logowanie(self):
        login = input("podaj login")
        passw = input("podaj haslo")

        self.cursor = self.conn.cursor()

        self.cursor.execute("Select * from logowanie where login = %s and passwd = %s", (login, passw))
        resultsLogs = self.cursor.fetchall()

        if(len(resultsLogs)==1):
            print ("Zalogowano w systemie")
            self.menu()
        else:
            print ("niepoprawny login lub haslo")
            self.logowanie()
    def menu(self):

        while True:
            dec = Helper.getinput()
            if(dec=="S"):
                print("Weszlo do if")
                self.select()
            elif dec == "I":
                self.insert()
                #print(help(input)) - tak otrzymuje pomoc, jeszcze jest dir
            elif(dec=="D"):
                self.delete()
            elif(dec=="U"):
                self.update()
            elif(dec=="Q"):
                print("Wyszedles z programu")
                break
            else:
                print("Bledny wybor. Sprobuj jeszcze raz")
    def update(self):
        self.select()
        pesel            = input("pesel")
        imie             = input("imie")
        nazwisko         = input("nazwisko")
        nowy_pesel       = input("nowy_pesel")
        data_ur          = input("data_ur")
        self.cursor.execute(" UPDATE pracownicy SET imie =%s,nazwisko=%s,pesel=%s,data_ur=%s WHERE pesel = %s",(imie,nazwisko,nowy_pesel,data_ur, pesel))
        dec              = input("Czy na pewno chcesz uaktualnic rekord T/N").upper()

        if (dec == 'T'):
            self.conn.commit()
            print("uaktualniono rekord")
        else:
            self.conn.rollback()
            print("come to MENU")

    def delete(self):

        self.select()
        pesel = input("pesel")
        self.cursor.execute(" DELETE FROM pracownicy WHERE pesel = %s", pesel)
        dec = input("Czy na pewno chcesz usunac rekord T/N").upper()

        if (dec == 'T'):
            self.conn.commit()
            print("usunieto rekord")
        else:
            self.conn.rollback()
            print ("come to MENU")



    def insert(self):
        imie = input("imie")
        nazwisko = input("nazwisko")
        pesel = input("pesel")
        data = input("data")
        self.cursor.execute("INSERT INTO pracownicy (imie,nazwisko,pesel, data_ur) values (%s,%s,%s,%s)",(imie,nazwisko,pesel,data))
        print("Jestesmy tutaj")
        self.conn.commit()


    def select(self):
        print("weszlo do select")

        self.cursor.execute("SELECT * FROM pracownicy")
        print("pracownicy")
        pracownicy = self.cursor.fetchall()
        print(pracownicy[0][0:3])
        print("pracownicy")
        i = 0
        print (type(pracownicy))
        for row in pracownicy:
            NAME = 1
            SURNAME = 2
            PESEL = 3
            DATA_URODZENIA = 4
            print(row[NAME], row[SURNAME], row[PESEL], row[DATA_URODZENIA])




DBConnect = DBConnect()


#urllib sprawdzic w necie
#mwarycha@gmail.com