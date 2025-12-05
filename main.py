#Menu
#1.product list
#2.product rasmiylashtirish
#3.rasmiylashtirishni korsatish
#4.Exit
class Product:
    def __init__(self,name,price,qty):
        self.name = name
        self.price = price
        self.qty = qty
class Catalog:
    def __init__(self,name):
        self.name = name
        self.products = []

class Order:
    def __init__(self,product,qty):
        self.product = product
        self.qty = qty
p1 = Product("Olma",20000,2)
p2 = Product("Nok",15000,2)

c1 = Catalog("1-catalog")
c1.products = [p1,p2]
for i in c1.products:
    print(f"{i.name} {i.price}UZS {i.qty}kg")
print()



