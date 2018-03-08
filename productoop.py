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

product1.addTax(.10).sale().refund("opened").displayinfo()

'''Failed attempt ( still maybe relevant?)
    def inventory(self):
        for prod in self.products:
            print "Product Info: {}".format(vars(prod))
            """
            prodinfo = [attr for attr in dir(prod) if not callable(getattr(prod, attr)) and not attr.startswith("__")]
            print prodinfo
            for idx in range(0,len(prodinfo)):
                identify = prodinfo[idx]
                print identify
                print prod.price
                #print prod[prodinfo[idx]]
                #print prod[identify]
                #print prod.identify
            """
            def __str__(self):
    return 
'''
