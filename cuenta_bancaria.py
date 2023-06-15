
class CuentaBancaria:

    cuentas = []

    def __init__(self, tasa_interés=0.01, balance=0.0): 
        self.tasa_interés = tasa_interés
        self.balance = balance
        CuentaBancaria.cuentas.append(self)
    
    @classmethod
    def mostrar_info_cuentas(cls):
        for cuenta in cls.cuentas: 
            cuenta.mostrar_info_cuenta() # llamar al método mostrar_info_cuenta en cada cuenta en la lista cuentas para mostrar su información
    
    
    def depósito(self, amount):
        self.balance += amount
        return self
    
    def retiro(self, amount):  
        if self.balance >= amount:                           
            self.balance -= amount
        else:
            self.balance -= 5
            print("Fondos insuficientes: cobrando una tarifa de $5")
        return self
    
    def mostrar_info_cuenta(self):
        print(f"Balance: {self.balance} " )
        return self
    
    def generar_interés(self):
        interes = self.balance * self.tasa_interés
        self.balance += interes
        return self


cuenta1 = CuentaBancaria(balance=100)
cuenta2 = CuentaBancaria(balance=80)

"""Para la primera cuenta, haz 3 depósitos y 1 retiro, luego genera intereses y muestra la 
información de la cuenta, todo en una línea de código (es decir, encadenando)"""

cuenta1.depósito(50).depósito(70).depósito(86.3).retiro(10.3).generar_interés().mostrar_info_cuenta()

"""Para la segunda cuenta, haz 2 depósitos y 4 retiros, luego genera intereses y muestra la información de la cuenta, 
todo en una línea de código (es decir, encadenando)"""

cuenta2.depósito(10).depósito(5).retiro(15).retiro(8).retiro(10).retiro(63).generar_interés().mostrar_info_cuenta()

CuentaBancaria.mostrar_info_cuentas()