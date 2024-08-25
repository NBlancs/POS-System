class Products:

    name: str
    price: float
    def __init__(self, name, price):
        self.name = name
        self.price = price

class cartItem:
    product: Products
    quantity: int

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity

    
products: list [Products] = [
    Products('Apple',50),
    Products('Banana',5),
    Products('Green Apple',80),
    Products('Grapes',100),
    Products('Cherry',125),
    Products('Pineapple',75),
    Products('Dragon Fruit',40),
    Products('Jack Fruit',35),
]

cart : list [cartItem] = []

