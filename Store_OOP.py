# pylint: disable=print-statement
class StoreProduct(object):
    def __init__(self, name, price, weight, brand):
        self.name = name
        self.price = price
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"

    def sale(self):
        self.status = "Sold"
        return self

    def addTax(self, tax):
        self.price = self.price + (self.price*tax)
        return self

    def refund(self, reason): 
        if reason == "defective":
            self.status = "Defective"
            self.price = 0
        if reason == "like new":
            self.status = "For Sale"
        if reason == "opened":
            self.status = "Used"
            self.price = self.price - (self.price*.20)
        return self

    def displayinfo(self):
        print "Name of product: {}. Price of product: {} dollars. Weight of product: {} lbs. Product brand: {}. Status: {}".format(self.name, self.price, self.weight, self.brand, self.status)
        return self

product1 = StoreProduct("Toothbrush", 10, 2, "Colgate")
product2 = StoreProduct("guitar", 60, 10, 'fender')
product3 = StoreProduct('computer', 200, 8, 'dell')
product4 = StoreProduct('Lolypop', 2, 0.5, 'Mr. Lollys')
product5 = StoreProduct('Redvines', 4, 1, 'Redvine')
product6 = StoreProduct('Chocolate', 7, 1, 'Lindor')

class Store(object):
    def __init__(self, storename, location, owner, products):
        self.storename = storename
        self.location = location
        self.owner = owner
        self.products = products
    
    def add_product(self, name, price, weight, brand):
        self.newProduct = StoreProduct(name, price, weight, brand)
        self.products.append(self.newProduct)
        print "The {} product was added to inventory".format(self.newProduct.name)
        return self
    
    def remove_product(self, name):
        for delprod in self.products:
            if delprod.name == name:
                self.products.remove(delprod)
                print "The {} product was removed from inventory".format(delprod.name)
        return self

    def inventory(self):
        for prod in self.products:
            print "Product Info: {}".format(vars(prod))
        return self

    def displaystore(self):
        print "Store Name: {}. Location: {}. Owner: {}. Product: {}".format(self.storename, self.location, self.owner, self.products)
        return self
        
store1Arr = [product4, product5, product6]
store2Arr = [product1, product2, product3]
store1 = Store("Candy Store", "Bellevue", "Mr. Frank", store1Arr)
store2 = Store('General Store', 'Seattle', "Mrs. Bell", store2Arr)

store2.add_product("ball", 5, 7, "ballsRus").inventory().remove_product('computer').inventory().displaystore()
store1.inventory().remove_product('Redvines').inventory().displaystore()
