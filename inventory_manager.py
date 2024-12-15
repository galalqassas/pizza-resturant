class InventoryManager:
    def __init__(self):
        self.inventory = {
            "Margherita": 10,
            "Pepperoni": 10,
            "Cheese": 15,
            "Olives": 10,
            "Mushrooms": 12,
        }

    def is_available(self, item):
        return self.inventory.get(item, 0) > 0

    def use_item(self, item):
        if self.is_available(item):
            self.inventory[item] -= 1
            return True
        print(f"{item} is not availabe!")
        return False