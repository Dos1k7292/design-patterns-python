import copy


class Order:

    def __init__(self):
        self.products = []
        self.discount = None
        self.payment_method = ""

    def clone(self):
        return copy.deepcopy(self)

    def show(self):
        print("Payment:", self.payment_method)

        for product in self.products:
            print(product.name, product.price)

        if self.discount:
            print("Discount:", self.discount.name)
