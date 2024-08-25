from os import name, system
from getpass import getpass
from products import Products
from products import cartItem
from products import products
from products import cart
from functools import reduce

def greetings():
    print('\u001b[35m')
    print(

   """

██████╗░██╗░░░░░░█████╗░███╗░░██╗░█████╗░░█████╗░  ░██████╗████████╗░█████╗░██████╗░███████╗
██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔══██╗██╔══██╗  ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝
██████╦╝██║░░░░░███████║██╔██╗██║██║░░╚═╝██║░░██║  ╚█████╗░░░░██║░░░██║░░██║██████╔╝█████╗░░
██╔══██╗██║░░░░░██╔══██║██║╚████║██║░░██╗██║░░██║  ░╚═══██╗░░░██║░░░██║░░██║██╔══██╗██╔══╝░░
██████╦╝███████╗██║░░██║██║░╚███║╚█████╔╝╚█████╔╝  ██████╔╝░░░██║░░░╚█████╔╝██║░░██║███████╗
╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░  ╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝                                                                                                                                                                                                                                        
   """
    )
    print('\033[0;0m')

def auth():
    while True:
        greetings()
        print('Please Login to Continue')

        print('\033[0;0m') 

        username: str = input('Username: ')
        password: str = getpass('Password: ')

        if username == 'admin' and password == '123':
            print('\033[92mAuthentication Success! ')
            print('\033[0;0m') 
            print('Press ENTER to continue ')

            input()
            clear_terminal()
            return

        print('\033[91m Username or password not found!\n Press ENTER to continue ')

        input()
        clear_terminal()


def clear_terminal():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def show_products():
    while True:
        print("\033[1;32m")
        print("""Select to add to cart!: 
======================================================""")   
        for itx, i in enumerate(products):
            print(f"{itx+1}. {i.name} - Price: {i.price}")

        print("""=======================================================
Type 'end' to Exit""")
        selected = input("Select Item:")

        if selected.isdigit() and 0 <= int(selected) <= len(products):
            while True:
                qty = input("Quantity: ")
                try:
                    qty = int(qty)
                    if qty > 0:
                        clear_terminal()

                        for item in cart:
                            if item.product == products[int(selected)-1]:
                                item.quantity = qty
                                break
                        
                        else:
                            item = cartItem(product=products[int(selected)-1], quantity=qty)
                            cart.append(item)
                        return
                    else:
                        print("\033[91mInvalid Input: Quantity must be greater than 0")
                        print("\033[0;0m")
                        print("Press ENTER to continue")
                        input()
                        clear_terminal()  
                        continue
                except ValueError:
                    print("\033[91mInvalid Input: Quantity must be a positive integer")
                    print("\033[0;0m")
                    print("Press ENTER to continue")
                    input()
                    clear_terminal()  
                    continue         
        print("\033[91mInvalid Input\n")
        print("\033[0;0m") 
        print("Press ENTER to continue")
        input()
        clear_terminal()  
        continue

def show_cart():
    print("\033[1;32m")
    print(
        """Your Cart: 
======================================================
        """)
    for itx,i in enumerate(cart):
        print(f'{itx}. {i.product.name} - ${i.product.price} - x{i.quantity} Subtotal : P{i.calculate_subtotal()}')

    print("""\n======================================================""")
    print("\t   Thank you for shopping with us\n\t\t  Here's your receipt")
    print ("\n\t\t    Type 'end' to Exit")

    print ("\t\t    Total: " + f'P {reduce(lambda a,b: a + b.calculate_subtotal(),cart , 0.00)}')
    while True:
        selected = input("Enter the item number to remove (or type 'end' to exit): ")
        if selected.isdigit() and 0 <= int(selected) < len(cart):
            del cart[int(selected)]
            clear_terminal()
            return
        elif selected == "end":
            clear_terminal()
            return
        print("\033[91mInvalid Input")
        print("\033[0;0m")
        print("Press ENTER to continue")
        input()


def complete_transaction():  
    print("\033[1m")
    print("\033[3m")
    print("\033[1;32m")
    print("\n\n\t\t   Blanco's Store")
    print("\033[0;0m")
    print("\033[1;32m")
    print("======================================================\n\n")
    show_cart()
    while True:
        choice = input("\n\n\t\tPlease type 'back' to go back or 'confirm' to confirm purchase: ")
        if choice.lower() == 'back':
            display_main_menu()
        elif choice.lower() == 'confirm':
            print(f"\n\n\t\tThe total amount to pay is: P {reduce(lambda a,b: a + b.calculate_subtotal(),cart , 0.00)}")
            print("\n\n\t\tPlease enter your balance: ")
            while True:
                try:
                    balance = float(input())
                    total = reduce(lambda a,b: a + b.calculate_subtotal(),cart , 0.00)
                    if balance < total:
                        print("\n\n\t\tInvalid Balance. Please try again.")
                    elif balance == total:
                        print("\n\n\t\tThank you for purchasing")
                        break
                    else:
                        print("\n\n\t\tThank you for purchasing")
                        print("\n\n\t\tChange: " + f'P {balance - total}')
                        break
                except ValueError:
                    print("\n\n\t\tInvalid Input. Please try again.")
            break
        else:
            print("\n\n\t\tInvalid Input. Please try again.")
  
def display_main_menu():

    valid_input = True
    while valid_input:
        print("\033[1;32m")
        print("\033[1m")
        print("\033[3m")
        print("\n\n\t\t   Blanco's Store")
        print(
            """
======================================================
1. Buy Products
2. View Cart | Remove Products
3. Complete Transaction

Type "end" to Exit
======================================================
    """
        )
        selected = input('Select an option: ')

        if selected == '1':
            show_products()
 
        elif selected == '2':
            show_cart()

        elif selected == '3':
            complete_transaction()
        elif selected.lower() == 'end':
            exit()
        else:
            valid_input = False
            print('\033[91m Invalid Input')
            print('Press ENTER to continue ')

            input()
            if name == 'nt': 
                system('cls')
            else: 
                system('clear')


if __name__ == '__main__':
    auth()

    while True:
        display_main_menu()
