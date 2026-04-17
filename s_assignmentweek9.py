from dataclasses import dataclass,field
@dataclass
class Product:
    name:str
    price:float
    quantity:int
    def value(self) -> float:
        return self.price*self.quantity
@dataclass
class Warehouse:
    name:str
    products:list[Product]=field(default_factory=list)
    total_value:float=field(init=False)
    
    def __post_init__(self):
        self.update_total_value()
    def update_total_value(self):
         self.total_value=round(sum(product.value() for product in self.products),1)
    def add_product(self, product: Product):
        self.products.append(product)
        self.update_total_value()
    def sell(self, product_name: str, qty: int) -> bool:
            for product in self.products:
                if product.name==product_name:
                    if product.quantity>=qty:
                        product.quantity-=qty
                        self.update_total_value()
                        return True
                    else:
                        return False
            return False
    def restock(self, product_name: str, qty: int):
        for product in self.products:
            if product.name==product_name:
                product.quantity+=qty
                self.update_total_value()
                return
    def report(self) -> str:
            lines = [f"{self.name} Inventory:"]
            for product in self.products:
                lines.append(
                    f"{product.name}: {product.quantity} units @ ${product.price:.2f} each")
            lines.append(f"Total value: ${self.total_value:.2f}")
            return "\n".join(lines)

p1 = Product("Laptop", 999.99, 10)
p2 = Product("Mouse", 29.99, 50)
p3 = Product("Keyboard", 79.99, 30)

w = Warehouse("TechDepot")
w.add_product(p1)
w.add_product(p2)
w.add_product(p3)

print(w.total_value)
print(w.sell("Laptop", 3))
print(w.sell("Laptop", 20))
w.restock("Mouse", 25)
print(w.report())
