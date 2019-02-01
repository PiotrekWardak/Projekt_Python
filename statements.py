class Stat:

    @classmethod
    def getConnectionMessage(cls):
        print ("Polaczenie z bazą zostało nawiązane")

    @classmethod
    def getConnectionFailedMessage(cls):
        print("Polaczenie z bazą zostało nawiązane")

    @classmethod
    def log_in(cls):
        print("Nacisnij P jesli jestes pacjentem")
        print("Nacisnij L jeśli jesteś lekarzem")
        print("Nacisnij X aby wyjsc z programu")

    @classmethod
    def welcome_message(cls):
        print("Witamy w naszej przychodni!")

    @classmethod
    def getInputPatient(cls):
        dec = input("S-show my appointments, M - make a new appointment, D-delete an appointment, C-check prescribed medicine, Q-exit").upper()
        return dec