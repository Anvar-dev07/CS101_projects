def track_change(func):
    def wrapper(*args,**kvargs):
        result=func(*args,**kvargs)
        print(f"[STOCK] {result}")
        return result
    return wrapper
class Product:
    _all_products=[]
    def __init__(self, name, price:float, quantity:int):
        self.name=name
        self.price=price
        self.quantity=quantity
        Product._all_products.append(self)
    @track_change
    def restock(self, amount):
        self.quantity += amount
        return f"{self.name}: added {amount}, now {self.quantity}"
    @track_change
    def sell(self,amount):
        if amount>self.quantity:
            return f"Not enough {self.name} in stock"
        self.quantity-=amount
        return f"{self.name}: sold {amount}, now {self.quantity}"
    def total_value(self):
        return round(self.price * self.quantity,2)
    @classmethod
    def from_catalog(cls, entry):
        name,price,quantity=entry.split(":")
        quantity=int(quantity)
        price=float(price)
        return cls(name,price,quantity)
    @staticmethod
    def is_valid_code(code):
        valid_digits="1,2,3,4,5,6,7,8,9,0"
        if code.startswith("PRD-") and (num in valid_digits for num in code[4:]):
            return True
        return False
    @classmethod
    def warehouse_value(cls):
        total_value=sum(product.total_value() for product in cls._all_products)
        return round(total_value,2)

p1 = Product("Keyboard", 45.50, 20)
p2 = Product.from_catalog("Monitor:299.99:5")

p1.restock(10)
p1.sell(25)
p1.sell(50)
p2.sell(2)

print(f"{p1.name}: value = ${p1.total_value()}")
print(f"{p2.name}: value = ${p2.total_value()}")

print(f"Valid code 'PRD-001': {Product.is_valid_code('PRD-001')}")
print(f"Valid code 'ABC-123': {Product.is_valid_code('ABC-123')}")
print(f"Warehouse total: ${Product.warehouse_value()}")
