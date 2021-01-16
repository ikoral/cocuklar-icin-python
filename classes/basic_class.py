class Computer:

    def __init__(self, price):
        self.__maxprice = price

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price


mark = Computer(800)
mark.__maxprice = 30
print(mark.__maxprice)
mark.sell()


class Car:
    # global attributes (it is valid for all object created from this class)
    type = "transportation"

    # attributes
    def __init__(self, make, color):
        self.make = make
        self.color = color
        self.__max_speed = 220

    # methods
    def move_forward(self, unit):
        return f"{self.make} has moved {unit} unit."

    def get_max_speed(self):
        return self.__max_speed

    def set_max_speed(self, speed):
        self.__max_speed = speed


c = Car("b", "green")


max_speed = c.get_max_speed()
print(max_speed)

c.set_max_speed(240)
max_speed = c.get_max_speed()
print(max_speed)

print(c.__max_speed)
