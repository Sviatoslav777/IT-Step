# class Pet:
#     def init(self, name, species):
#         self.name = name
#         self.species = species
#         self.hunger = 50
#         self.energy = 50
#         self.happiness = 50
#
#     def feed(self):
#         if self.hunger > 30:
#             self.hunger -= 20
#             self.happiness += 10
#             print(f"{self.name} поїв і тепер щасливиЙ!")
#         else:
#             print(f"{self.name} не хоче їсти.")
#
#     def play(self):
#         if self.energy >= 20:
#             self.happiness += 70
#             print(f"{self.name} бавиться")
#         else:
#             print(f"{self.name} втомлений, щоб гратись.")
#     def status(self):
#         print(f"""
#         Ім'я: {self.name}
#         Вид: {self.species}
#         Голод: {self.hunger}
#         Енергія: {self.energy}
#         Щасливий: {self.happiness}
#         """)
#
#
# # дз 3
# class Car:
#    def __init__(self, title, year):
#        self.title = title
#        self.year = year
#        self.status = "available"
#
# class Garage:
#    def __init__(self):
#        self.cars = []
#    def add_car(self, car):
#        self.cars.append(car)
#    def remove_car(self, car):
#        self.cars.remove(car)
#    def lend_car(self, car):
#        if car.status == "available":
#            car.status = "lent"
#            print(f"{car.title} by has been lent out.")
#        else:
#            print("Sorry, this car is not available.")
#    def return_car(self, car):
#        if car.status == "lent":
#           car.status = "available"
#           print(f"{car.title} by  has been returned.")
#        else:
#            print("This car was not lent out.")
#
#
#            # dz4
#            import random
#            from typing import Self
#            class va:
#                def __init__(self, number):
#                    self.__number = number
#
#            def __encapsulate(self):
#                operand = random.choice(['+', '-', '*', '/'])
#
#            operand = random.randint(1, 10)
#            if operand == '+':
#                self.__number += operand
#            elif operand == '-':
#                self.__number -= operand
#            elif operand == '*':
#                self.__number *= operand
#            elif operand == '/':
#                self.__number /= operand
#
#            def get_result(self):
#                self.__encapsulate()
#
#            Self__number
#            number = int(input("Введіть число: "))
#            cipher = va(number)
#            result = cipher.get_result()
#            print("Результат: ", get_result)




# my_list = [1,2,3]
# iterator = iter(my_list)
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))



# def raise_to(number, max_degree):
#     i = 0
#     for _ in range(max_degree):
#         yield number**i
#         i+=1
#
# res = raise_to(123456,10)
# print(res)
# for _ in res:
#     print(_)
#
#
#
# class Helper:
#     def __init__(self, work):
#         self.work = work
#     def __clal__(self, work):
#         return f"1 - {self.work}, 2 - {work}"
#
# helper = Helper("Homework")
#
# print(helper("cleaning"))







def raise_to(number, max_degree):
    i = 0
    for _ in range(max_degree):
        yield number**i
        i+=1

res = raise_to(2,10)
print(res)
for _ in res:
    print(_)


    def divider(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Ви не можете ділити на нуль!")
            return 0
        except TypeError:
            print("Ви не можете ділити нечислові значення!")
            return 0
        except ValueError:
            print("Ви не можете ділити нечислові значення!")
            return 0


    data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}
    result = []
    for key in data:
        res = divider(key, data[key])
        result.append(res)
    print(result)

    # дз модулі та класи
    import colorama

    dir(colorama)
    pip
    install
    colorama


    # дз ітератори
    class MyIterable:

        def __init__(self, data):
            self.data = data

        def __iter__(self):
            for item in self.data:
                yield item


    iterable = MyIterable([1, 2, 3, 4, 5])

    for item in iterable:
        print(item)

    # дз логування
    import time


    def measure_execution_time(func, *args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return result, execution_time


    # приклад тесту
    def test_function(n):
        if n == 0:
            return 1
        return n * test_function(n - 1)


    def run_test():
        result, exec_time = measure_execution_time(test_function, 5)
        print(f"Result: {result}, Execution Time: {exec_time:.4f} seconds")
        assert result == 120
        assert exec_time > 0


    run_test()







#дз сайти
class CurrencyConverter:
   def __init__(self):
       self.rates = {}
   def get_rates(self):
       response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?money")
       data = response.()
       for item in data:
           self.rates[item['cc']] = item['rate']
   def convert(self, amount, from_currency, to_currency):
       if from_currency != "USD":
           amount = amount / self.rates[from_currency]
       amount = round(amount * self.rates[to_currency], 2)
       return amount
converter = CurrencyConverter()
converter.get_rates()
while True:
   try:
       amount = float(input("Enter the amount of currency: "))
       from_currency = input("Enter the currency code of the amount you entered: ")
       to_currency = "USD"
       converted_amount = converter.convert(amount, from_currency.upper(), to_currency)
       print("The amount of {} {} is equal to {:.2f} USD".format(amount, from_currency.upper(), converted_amount))
       break
   except KeyError:
       print("Invalid currency code entered. Please try again.")
   except ValueError:
       print("Invalid input entered. Please try again.")



#дз БД погода львів
import sqlite3
conn = sqlite3.connect('weather.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS weather
            (date_time TEXT, temperature REAL)''')
conn.commit()
conn.close()
import requests
url = 'https://ua.sinoptik.ua/погода-львів'
response = requests.get(url)
if response.status_code == 200:
   html = response.content
else:
   print('Не вдалося отримати сторінку')
from bs4 import BeautifulSoup
soup = BeautifulSoup('html.parser')
today_weather = soup.find('div', {'class': 'weatherToday'}).('div', {'class': 'temperature'}).text
today_temperature = int(today_weather.split('°')[0])
print(f"Температура сьогодні: {today_temperature}°C")








