from os import name, system
from getpass import getpass
from functools import reduce


class Product:
    name: str
    price: float

    def __init__(self, name, price):
        self.name = name
        self.price =price

class CartItem:
    product: Product
    quantity: int

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
       

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity

products : list [Product] = [
    Product('Apple', 120 ),
    Product('Orange', 50 ),
    Product("Grapes", 400),
    Product('Green Apple', 200 ),
    Product('Strawberry', 300 ),
    Product("Mango", 350),
]


cart : list [CartItem] = []
    
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
        print('Please login to continue')

        print('\033[0;0m') 

        username: str = input('Username : ')
        password: str = getpass('Password: ')

        if username == 'admin' and password == '369':

            print('\033[92mAuthentication Success! ')
            print('\033[0;0m') 
            print('Press ENTER to continue ')

            input()
            clear_terminal()
            return

        print('\033[91m Username or password not found!\n Press ENTER to continue ')

        input()
        clear_terminal()
        
def clear_terminal ():
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
            print(f"{itx+1}. {i.name}  - P{i.price}")

        print("""=======================================================
Type 'end' to Exit""")
        selected = input("Select item: ")

        if selected.isdigit() and 0 <= int(selected) <= len(products):
            while True:
                qty = input("Quantity: ")
                try:
                    qty = int(qty)
                    if qty > 0:
                        clear_terminal()

                        # check if the product is already in the cart
                        for item in cart:
                            if item.product == products[int(selected)-1]:
                                # update the quantity of the existing cart item
                                item.quantity = qty
                                break
                        else:
                            # add a new cart item to the cart
                            item = CartItem(product=products[int(selected)-1], quantity=qty)
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
        clear_terminal()


def complete_transaction():  
    print("\033[1m")
    print("\033[3m")
    print("\033[1;32m")
    print("\n\n\t\t   Blanco's Store")
    print("\033[0;0m")
    print("\033[1;32m")
    print("======================================================\n\n")
    show_cart()
    input()
    print("\n\n======================================================\n")
  
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
