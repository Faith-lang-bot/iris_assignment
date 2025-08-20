# ASSIGNMENT ONE
class Superhero:
    def __init__(self, name, power, strength_level):
        self.name = name
        self.power = power
        self._strength_level = strength_level  

    def show_identity(self):
        print(f"I am {self.name}, and I have the power of {self.power}.")

    def attack(self):
        print(f"{self.name} attacks with {self.power} at strength level {self._strength_level}!")

class FlyingSuperhero(Superhero):
    def __init__(self, name, power, strength_level, flight_speed):
        super().__init__(name, power, strength_level)
        self.flight_speed = flight_speed

    def attack(self):
        print(f"{self.name} soars through the sky and attacks with {self.power} at speed {self.flight_speed} km/h!")

hero1 = Superhero("Shadow", "Invisibility", 75)
hero2 = FlyingSuperhero("SkyBlaze", "Flame Wings", 90, 300)

hero1.show_identity()
hero1.attack()

hero2.show_identity()
hero2.attack()

#ASSIGNMENT TWO
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving ")

class Plane(Vehicle):
    def move(self):
        print("Flying ")

class Boat(Vehicle):
    def move(self):
        print("Sailing ")

# Test polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
