from enum import Enum

class CandyType(Enum):
    BAR = 1
    BUTTON = 2
    POPCORN = 3
    GUM = 4

class Candy:
    def __init__(self, name, mass, amount, price, candy_type):
        self.name = name
        self.mass = mass
        self.amount = amount
        self.price = price
        self.type = candy_type

    def ate(self):
        if self.mass * self.amount > 2000:
            return "You're on a diet!"
        return "What delicious candies!"

    def __del__(self):
        print(f"Зжерли {self.name}")

    def get_name(self):
        return self.name

    def get_mass(self):
        return self.mass

    def get_amount(self):
        return self.amount

    def get_price(self):
        return self.price

class Dinner:
    def __init__(self, day, time, candies=[]):
        self.day = day
        self.time = time
        self.candies = candies

    def add_candy(self, candy):
        self.candies.append(candy)

    def find_the_most_expensive_candies(self, n):
        sorted_candies = sorted(self.candies, key=lambda x: x.price, reverse=True)
        return sorted_candies[:n]

def main():
    Candy1 = Candy("Roshetto", 50, 5, 10, CandyType.BAR)
    Candy2 = Candy("M&M's", 100, 50, 50, CandyType.BUTTON)
    Candy3 = Candy("Orbit", 50, 5, 25, CandyType.GUM)
    Candy4 = Candy("Eclips", 50, 5, 30, CandyType.GUM)
    print(Candy1.get_name())
    print(Candy2.get_name())
    print(Candy3.get_name())
    print(Candy4.get_name())

    Dinner1 = Dinner("Monday", "8:00", [Candy1, Candy2,Candy4])
    Dinner2 = Dinner("Friday", "15:00", [Candy3])
    Dinner3 = Dinner("Tuesday", "20:00")

    print(Dinner1.day)
    print(Dinner2.day)
    print(Dinner3.day)

    Dinner3.add_candy(Candy3)
    Dinner3.add_candy(Candy2)

    expensive_candies = Dinner1.find_the_most_expensive_candies(3)
    print("Топ 3 найдорожчі цукерки:")
    for candy in expensive_candies:
        print(candy.get_name())

if __name__ == "__main__":
    main()
