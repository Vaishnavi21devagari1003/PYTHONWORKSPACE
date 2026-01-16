class Calling:
    def feature1(self):
        print("Calling feature")


# Parent class 2
class Texting:
    def feature2(self):
        print("Texting feature")


# Child class (Multiple Inheritance)
class SmartPhone(Calling, Texting):
    def explore(self):
        print("Exploring features of SmartPhone")

phone = SmartPhone()
phone.feature1()
phone.feature2()
phone.explore()