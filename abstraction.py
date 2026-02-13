from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def speed(self):
        pass

class BMW(Car):
    def speed(self):
        print("200 km/h")

b = BMW()
b.speed()
