from abc import ABC, abstractmethod
class Taxable:
    @abstractmethod
    def tax_amount(self):
        pass
class Describable:
    @abstractmethod
    def describe(self):
        pass
class Product(Taxable, Describable):
    def __init__(self,name,price):
        self.name=name
        self.price=price
        if price<0:
            raise ValueError(f"Invalid price: {price}")
    def tax_amount(self):
        return round(self.price * 0.10, 2)
    def describe(self):
        return f"{self.name}: ${self.price}"
class DiscountedProduct(Product):
    def __init__(self, name, price,discount:float):
        super().__init__(name, price)
        self.discount=discount
    def final_price(self):
        return round(self.price * (1 - self.discount), 2)
    def tax_amount(self):
        return round(self.final_price()*0.1,2)
    def describe(self):
      percent=int(self.discount*100)
      return f"{self.name}: ${self.price:.2f} -> ${self.final_price():.2f} (-{percent}%)"
class ImportedProduct(Product):
    def __init__(self, name, price,import_duty:float):
        super().__init__(name, price)  
        self.import_duty=import_duty
    def tax_amount(self):
       return round(self.price * 0.10 + self.price * self.import_duty, 2)
    def describe(self):
      percent=int(self.import_duty*100)
      return f"{self.name}: ${self.price:.2f} (imported, duty {percent}>%)"
class GiftCard:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def tax_amount(self):
        return 0.0
    def describe(self):
        return f"{self.name}: ${self.price:.2f} (gift card, tax-free)"
class Receipt:
    def __init__(self):
        self.list_of_lines=[]
    def add_line(self, description, tax):
        return self.list_of_lines.append((description,tax))
    def print_receipt(self):
        for description,tax in self.list_of_lines:
            print(f"{description} | tax: ${tax:.2f}")
class ShoppingCart:
    def __init__(self,customer_name):
        self.customer_name=customer_name
        self.list_of_items=[]
        self.receipt=Receipt()
    def add_item(self,item):
        return self.list_of_items.append(item)
    def checkout(self):
      print(f"Checkout for {self.customer_name}")
      subtotal = 0
      total_tax = 0
      for item in self.list_of_items:
        description=item.describe()
        tax=item.tax_amount()
        subtotal+=item.price
        total_tax+=tax
        self.receipt.add_line(description, tax)
      self.receipt.print_receipt()
      grand_total=subtotal+total_tax
      print(f"Subtotal: ${subtotal:.2f}")
      print(f"Total Tax: ${total_tax:.2f}")
      print(f"Grand Total: ${grand_total:.2f}")

      result = None
      return result

cart = ShoppingCart('Alisher')

cart.add_item(Product('Laptop', 1000))
cart.add_item(DiscountedProduct('Headphones', 200, 0.25))
cart.add_item(ImportedProduct('Chocolate', 10, 0.15))
cart.add_item(GiftCard('Steam Card', 50))

try:
    cart.add_item(Product('Bad Item', -5))
except ValueError as e:
    print(f'Skipped: {e}')

cart.checkout()

try:
    t = Taxable()
except TypeError:
    print('Cannot instantiate abstract class')
