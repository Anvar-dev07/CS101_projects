from abc import abstractmethod ,ABC 
class Basket(ABC):
    def __init__(self, shopper):
        self.shopper=shopper
    @abstractmethod
    def total(self):
        pass

class Mini(Basket):
    def total(self):
        return 25_000

class Family(Basket):
    def total(self):
        return 90_000

class Bulk(Basket):
    def total(self):
        return 250_000
    
class CheckoutSystem:
    def __init__(self):
        self.purchases=[]
    
    def add(self,basket:Basket):
        self.purchases.append(basket)

    def run(self, bill, loyalty):
            bill.print_bill(self.purchases)
            loyalty.notify(self.purchases)

class Bill(ABC):
    @abstractmethod
    def print_bill(self,purchases):
        pass

class PaperBill(Bill):
    def print_bill(self, purchases):
        for purchase in purchases:
            print(f"Bill ({purchase.shopper}) = ({purchase.total()})")

class Loyalty(ABC):
    @abstractmethod
    def notify(self,purchases):
        pass

class EmailLoyalty(Loyalty):
    def notify(self,purchases):
        for purchase in purchases:
            print(f"LOYALTY -> {purchase.shopper} Earned points for {purchase.total()}")

store = CheckoutSystem()
store.add(Mini("Kakashi"))
store.add(Family("Itachi"))
store.add(Bulk("Hinata"))

store.run(PaperBill(), EmailLoyalty())
