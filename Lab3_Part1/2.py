import random


class Composition:

    def __init__(self, name: str, price = int, quantity: int = 1):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, number):
        if not isinstance(number, int):
            raise TypeError
        if number <= 0:
            raise ValueError
        self.price = number

    @property
    def quantity(self):
        return self.quantity

    @quantity.setter
    def quantity(self, number):
        if not isinstance(number, int):
            raise TypeError
        if number <= 0:
            raise ValueError
        self.quantity = number

    def __gt__(self, other):
        if isinstance(other, Composition):
            return self.price > other.price
        if isinstance(other, (int, float)):
            return self.price > other

    def __lt__(self, other):
        if isinstance(other, Composition):
            return self.price < other.price
        if isinstance(other, (int, float)):
            return self.price < other

    def __str__(self):
        return f'Name: {self.name}. Price: {self.price}. Quantity: {self.quantity}'


class Order:
    def __init__(self):
        self.stuff = []
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.stuff):
            self.index += 1
            return self.stuff[self.index-1]
        raise StopIteration

    def __len__(self):
        return len(self.stuff)

    def __add__(self, other):
        if isinstance(other, Order):
            list = []
            for product in self.stuff:
                list.append(product)
            for product in other.stuff:
                list.append(product)
            return list
        if isinstance(other, str):
            list = []
            for product in self.stuff:
                list.append(product)
            list.append(other)
            return list

        return NotImplemented

    __radd__ = __add__


def report(order, compositions):
   if not isinstance(order, Order):
       raise TypeError
   if not isinstance(compositions, list):
       raise TypeError

   names = list(lambda a: a.name, compositions)

   report = "Report about availability:\n"

   def print_info(name, compositions):
       for item in compositions:
           if name == item.name:
               return item

   for item in order:
       if item in names:
           report += f"{item} is available. {print_info(item, compositions)}"
       else:
           report += f"There is no {item} in stock"

   return report



a = []

for i in range(5):
    a.append(Composition(f'{i+1}', random.randint(3, 10), random.randint(10, 100)))

b = Order()
b = b + "5"
b = b + "7"
c = Order + "1"
c = c + b

print(report(c, a))


