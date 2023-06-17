class Human:
    default_name = "--"
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}, House: {self.__house}, Money: {self.__money}")

    @staticmethod
    def default_info():
        print('Default name:', Human.default_name)
        print('Default age: ', Human.default_age)

    def make_deal(self, house, price):
            self.__house = house
            self.__money -= price

    def earn_money(self):
        self.__money += 4000
        print(f'Earned money. Current money: {self.__money}')

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.make_deal(house, price)
        else:
            print('Not enough money')

class House:

    def __init__(self, area, price):
        self.area = area
        self.price = price

    def final_price(self, discount):
        return self.price * discount

class SmallHouse(House):

    def __init__(self, price):
        super().__init__(40, price)


Human.default_info()
human = Human(name='Egor', age=24)
human.info()
s_house = SmallHouse(price=8000)
human.earn_money()
human.buy_house(s_house, discount=0.9)
human.earn_money()
human.buy_house(s_house, discount=0.9)
human.info()




