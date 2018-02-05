import cx_Oracle

class SingletonDBConnection():
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        if not hasattr(self, "connection"):
            try:
                self.connection = cx_Oracle.connect('e1384492', 'C','10.57.4.60/DECINFO.edu')
            except cx_Oracle.DatabaseError as e:
                error, = e.args
                print("Erreur de commande")
                print(error.code)
                print(error.message)
                print(error.context)

    def getConnection(self):
        return self.connection

    def closeConnection(self):
        self.connection.close()