class Pet:
    def init(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50
        self.energy = 50
        self.happiness = 50

    def feed(self):
        if self.hunger > 30:
            self.hunger -= 20
            self.happiness += 10
            print(f"{self.name} поїв і тепер щасливиЙ!")
        else:
            print(f"{self.name} не хоче їсти.")

    def play(self):
        if self.energy >= 20:
            self.happiness += 70
            print(f"{self.name} бавиться")
        else:
            print(f"{self.name} втомлений, щоб гратись.")
    def status(self):
        print(f"""
        Ім'я: {self.name}
        Вид: {self.species}
        Голод: {self.hunger}
        Енергія: {self.energy}
        Щасливий: {self.happiness}
        """)


# дз 3
class Car:
   def __init__(self, title, year):
       self.title = title
       self.year = year
       self.status = "available"

class Garage:
   def __init__(self):
       self.cars = []
   def add_car(self, car):
       self.cars.append(car)
   def remove_car(self, car):
       self.cars.remove(car)
   def lend_car(self, car):
       if car.status == "available":
           car.status = "lent"
           print(f"{car.title} by has been lent out.")
       else:
           print("Sorry, this car is not available.")
   def return_car(self, car):
       if car.status == "lent":
          car.status = "available"
          print(f"{car.title} by  has been returned.")
       else:
           print("This car was not lent out.")


           # dz4
           import random
           from typing import Self
           class va:
               def __init__(self, number):
                   self.__number = number

           def __encapsulate(self):
               operand = random.choice(['+', '-', '*', '/'])

           operand = random.randint(1, 10)
           if operand == '+':
               self.__number += operand
           elif operand == '-':
               self.__number -= operand
           elif operand == '*':
               self.__number *= operand
           elif operand == '/':
               self.__number /= operand

           def get_result(self):
               self.__encapsulate()

           Self__number
           number = int(input("Введіть число: "))
           cipher = va(number)
           result = cipher.get_result()
           print("Результат: ", get_result)