from order import Order
from product import Product
from discount import Discount


order1 = Order()

order1.products.append(Product("Laptop", 1000))
order1.discount = Discount("New Year", 100)
order1.payment_method = "Card"

order2 = order1.clone()

order2.payment_method = "Cash"

print("Original order:")
order1.show()

print("\nCloned order:")
order2.show()
