from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

class Margherita(Pizza):
    def get_description(self):
        return "Margherita"

    def get_cost(self):
        return 10.0

class Pepperoni(Pizza):
    def get_description(self):
        return "Pepperoni"

    def get_cost(self):
        return 15.0