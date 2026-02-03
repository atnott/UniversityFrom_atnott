class Product:
    def __init__(self, name, price, weight):
        self.__name = name
        self.__price = price
        self.__weight = weight

    def getName(self):
        return self.__name
    
    def getPrice(self):
        return self.__price
    
    def getWeight(self):
        return self.__weight
    

class Buy(Product):
    def __init__(self, p, amount):
        name = p.getName()
        price = p.getPrice()
        weight = p.getWeight()
        super().__init__(name, price, weight)
        self.__amount = amount

        self.__full_price = price * self.__amount
        self.__full_weight = weight * self.__amount

    def getAmount(self):
        return self.__amount

    def getFullPrice(self):
        return self.__full_price

    def getFullWeight(self):
        return self.__full_weight

class Check(Buy):
    def __init__(self, b):
        amount = b.getAmount()
        super().__init__(b, amount)

    def __repr__(self):
        return (f"Товар: {self.getName()}\n"
                f"Вес: {self.getFullWeight()}\n"
                f"Кол-во: {self.getAmount()}\n"
                f"Итого: {self.getFullPrice()}р")


p = Product("Помидор", 200, 50)
b = Buy(p, 2)
check = Check(b)
print(check)
