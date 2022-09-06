from lib2to3.pgen2.token import SLASHEQUAL


class Cuenta():

    def __init__(self, pro, sal, mon):
        self.__propietario = pro
        self.__saldo = sal
        self.__moneda = mon

    # Getters 
    def get_saldo(self):
        return self.__saldo
    def get_Propietario(self):
        return self.__propietario
    def get_Moneda(self):
        return self.__moneda
    #Setters
    def set_moneda(self, moneda):
        self.__moneda = moneda

