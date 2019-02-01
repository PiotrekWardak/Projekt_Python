class Stat:

    @classmethod
    def getConnectionMessage(cls):
        print ("Connected with database")

    @classmethod
    def getConnectionFailedMessage(cls):
        print("Connection to database failed")

    @classmethod
    def log_in(cls):
        print("Press P if you are a patient")
        print("Press D if you are a doctor")
        print("Press X to close a program")

    @classmethod
    def welcome_message(cls):
        print("Welcome to our clinic!")

    @classmethod
    def goodbye_message(cls):
        print("Thank you for visiting us!")

    @classmethod
    def getInputPatient(cls):
        dec = input("S-show my appointments,\nM - make a new appointment,\nD-delete an appointment,\nC-check prescribed medicine,\nQ-exit").upper()
        return dec

    @classmethod
    def getInputDoctor(cls):
        dec = input("S - show my appointments,\nD - delete an appointment,\nI - enter medicine to appropriate app.\n"
                    "C - check prescribed medicine,\nQ - exit").upper()
        return dec