num1 = 42       # variable declaration Numbers
num2 = 2.3      # variable declaration Float
boolean = True  # variable declaration Boolean
string = 'Hello World' #variable declaration String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration List initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration Dictionary iniatialize
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration tuples initialize
print(type(fruit)) # print to consolety type check
print(pizza_toppings[1]) # print to console List  access value
pizza_toppings.append('Mushrooms') #List add value
print(person['name']) # print to console dictionary access value
person['name'] = 'George' #dictionary change value 
person['eye_color'] = 'blue'#dictionary change value 
print(fruit[2]) # print to console tuple access value

if num1 > 45: #conditional if
    print("It's greater")
else:         #conditional else
    print("It's lower") 

if len(string) < 5: # Conditional if  length check 
    print("It's a short word!")
elif len(string) > 15: # Conditional else if  length check 
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): #for loop start
    print(x)
for x in range(2,5): #for loop 
    print(x)
for x in range(2,10,3): #for loop increment
    print(x)
x = 0
while(x < 5): #while loop start
    print(x)
    x += 1

pizza_toppings.pop()    # List delete value
pizza_toppings.pop(1)   # List delete value

print(person)           #print to console dictionary 
person.pop('eye_color') #dictionary delete value
print(person)           #print to console dictionary 

for topping in pizza_toppings: # for loop  in List 
    if topping == 'Pepperoni': #conditional if continue, for loop  in List  
        continue
    print('After 1st if statement')
    if topping == 'Olives': #conditional if break, for loop  in List 
        break

def print_hello_ten_times(): #function whith a for loop
    for num in range(10):
        print('Hello')

print_hello_ten_times() #function

def print_hello_x_times(x): #function parameter whith a for loop
    for num in range(x):
        print('Hello')

print_hello_x_times(4)  #function argument

def print_hello_x_or_ten_times(x = 10):#function parameter whith a for loop
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()# function
print_hello_x_or_ten_times(4)#function argument


"""
Bonus section
"""

#print(num3)  - NameError: name <variable name> is not defined
#num3 = 72 add value
#fruit[0] = 'cranberry' - TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) - KeyError: 'favorite_team'
# print(pizza_toppings[7]) - IndexError: list index out of range
#   print(boolean)- IndentationError: unexpected indent
# fruit.append('raspberry')  - AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)  - AttributeError: 'tuple' object has no attribute 'pop'
