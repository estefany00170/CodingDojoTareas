"""ara esta tarea, agregaremos algunas funciones a la clase Usuario:
hacer_retiro(self, amount): haz que este método reduzca el balance del usuario en la cantidad especificada 
mostrar_balance_usuario(self): haz que este método imprima el nombre del usuario y el balance de cuenta en la terminal 
Ej.: “Usuario: Guido van Rossum, Balance: $150
BONUS: transfer_dinero(self, other_user, amount): 
haz que este método reduzca el balance del usuario por el monto y agrega esa cantidad al balance de otro_usuario 
"""

class User:
    def __init__(self, name, balance =0.0):
        self.name = name
        self.balance = balance
    

    def make_withdrawal(self, amount):
        self.balance-= amount

    def make_deposit(self, amount):
        self.balance+= amount
    

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.balance += amount

    def show_user_balance(self):
        print(f"User: {self.name}  Balance: {self.balance}")
    


guido = User('Guido van Rossum', 150)
ricardo = User('Ricardo B', 500)
Mary = User('Maria Ross', 10)

#Haz que el primer usuario haga 3 depósitos y 1 giro, y luego muestra sus balances
guido.make_deposit(100)
guido.make_deposit(120)
guido.make_deposit(500)
guido.show_user_balance()
guido.make_withdrawal(70)
guido.show_user_balance()
print('----------------------------')

#Haz que el segundo usuario haga 2 depósitos y 2 giros, y luego muestra sus balances
ricardo.make_deposit(250)
ricardo.make_deposit(480)
ricardo.show_user_balance()
ricardo.make_withdrawal(100)
ricardo.make_withdrawal(30)
ricardo.show_user_balance()
print('------------------------------')

#Haz que el tercer usuario haga 1 depósito y 3 giros, y luego muestra sus balance
Mary.make_deposit(500)
Mary.show_user_balance()
Mary.make_withdrawal(50)
Mary.make_withdrawal(80)
Mary.make_withdrawal(80)
Mary.show_user_balance()
print('---------------------------')

#Agrega un método transferir_dinero; haz que el primer usuario transfiera dinero al tercer usuario y luego imprime los balances de ambos usuarios
guido.transfer_money(Mary, 20)
guido.show_user_balance()
Mary.show_user_balance()
