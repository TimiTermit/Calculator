
def add(x, y):
    return x + y #DODAWANIE

def subtract(x, y): #ODEJMOWANIE
    return x - y

def multiply(x, y): #MNOŻENIE
    return x * y

def divide(x, y): #DZIELENIE
    if y == 0: #JEZELI y=0  TO WYŚWIETLA ŻE NIE MOZNA DZIELIC PRZEZ 0
        return "Blad!!! Nie mozna dzielic przez zero" 
    return x / y #POWRÓT DO x/y 

while True: #MENU KALKULATORA
    print("Menu Kalkulatora:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnozenie")
    print("4. Dzielenie")
    print("5. Wyjscie")

    choice = input("Podaj swoj wybor (1-5): ") #WYBIERASZ OD 1-5

    if choice == "1": #DODAWANIE
        num1 = float(input("Wpisz 1 cyfre: "))
        num2 = float(input("Wpisz 2 cyfre: "))
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == "2": #ODEJMOWANIE
        num1 = float(input("Wpisz 1 cyfre: "))
        num2 = float(input("Wpisz 2 cyfre: "))
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == "3":#MNOŻENIE
        num1 = float(input("Wpisz 1 cyfre: "))
        num2 = float(input("Wpisz 2 cyfre: "))
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == "4": #DZIELENIE
        num1 = float(input("Wpisz 1 cyfre: "))
        num2 = float(input("Wpisz 2 cyfre: "))
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif choice == "5": #5 TO WYJŚCIE
        print("Dowidzenia!")
        break
    else:
        print("Zly Wybór, Spróbuj ponownie.") #JEŻELI COŚ INNEGO NIŻ 1-5 TO ZŁY WYBÓR