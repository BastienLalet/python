class Order:
    def init (self,quantity,price,buy=True):
        self.quantity=quantity
        self.price=price
        self.buy=buy

    def is_sell(self):
        return not self.buy

o= Order(5,11,0)
print(o.quantity)
print(o.is_sell())