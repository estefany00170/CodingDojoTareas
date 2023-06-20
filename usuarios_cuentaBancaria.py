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

class User:
    cuentas = []
    def __init__(self, name, cuenta = CuentaBancaria(balance = 0.0)):
        self.name = name
        self.cuentas.append(cuenta)

    def add_accounts(self, cuenta):
        self.cuentas.append(cuenta)
    

    def make_withdrawal(self, amount, index):
        self.cuentas[index].retiro(amount)

    def make_deposit(self, amount, index):
        self.cuentas[index].depósito(amount)
    

    def transfer_money(self, other_user, amount, index1, index2):# index1 es el índice de la cuenta desde la que se quiere transferir y index2 es el índice de la cuenta a la que se quiere transferir
        self.make_withdrawal(amount, index1) # retirar el monto de la cuenta del usuario que transfiere
        other_user.cuenta[index2].depósito(amount) # depositar el monto en la cuenta del usuario que recibe


    def show_user_balance(self):
        print(f"User: {self.name}")
        for i, cuenta in enumerate(self.cuentas): 
            print(f"Cuenta {i}: Balance: ${cuenta.balance:.2f}")

cuenta_ricardo = CuentaBancaria(balance=5000)
cuenta_Mary = CuentaBancaria(balance=200)
cuenta_eli =  CuentaBancaria(balance=3000)
cuenta_guido = CuentaBancaria(balance=150)
cuenta_guido2 = CuentaBancaria(balance=50)

guido = User('Guido van Rossum',cuenta_guido)
eli = User('Eli Falcon', cuenta_eli)
Mary = User('Mary Rodez', cuenta_Mary)
ricardo = User('Ricardo Bdtk', cuenta_ricardo)


guido.show_user_balance()
eli.show_user_balance()
guido.show_user_balance()
guido.add_accounts(cuenta_guido2)


