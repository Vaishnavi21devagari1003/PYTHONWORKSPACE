from abc import ABC, abstractmethod

class Electronics(ABC):
    @abstractmethod
    def play_video(self):
        pass

class Laptop(Electronics):
    def play_video(self):
        print("Press play button from keypad")

class Mobile(Electronics):
    def play_video(self):
        print("Press playb button from keypad")

laptop=Laptop()
laptop.play_video()

mobile=Mobile()
mobile.play_video()