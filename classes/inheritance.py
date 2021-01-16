class Car:
    # global attributes (it is valid for all object created from this class)
    type = "transportation"

    # attributes
    def __init__(self, make, color):
        self.make = make
        self.color = color
        # self.__max_speed = 220

    # methods
    def move_forward(self, unit):
        return f"{self.make} has moved {unit} unit."

    def get_max_speed(self):
        return self.__max_speed

    def set_max_speed(self, speed):
        self.__max_speed = speed


class RaceCar(Car):
    # constructor
    def __init__(self, make, color):
        Car.__init__(self, make, color)

    # methods (It has parent methods, also we can define additional methods)
    def move_faster(self):
        print("I can move faster than ever")


new_race_car = RaceCar("MacLaren", "Red")

print(new_race_car.move_forward(5))
new_race_car.move_faster()
