from pizza import Pizza

class ToppingDecorator(Pizza):
    def __init__(self, pizza, name, cost):
        self.pizza = pizza
        self.name = name
        self.cost = cost

    def get_description(self):
        return f"{self.pizza.get_description()} + {self.name}"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost