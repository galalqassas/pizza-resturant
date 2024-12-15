from pizza import Margherita, Pepperoni
from inventory_manager import InventoryManager

class PizzaFactory:
    @staticmethod
    def create_pizza(choice):
        inventory = InventoryManager()
        pizza_map = {"1": "Margherita", "2": "Pepperoni"}
        if choice in pizza_map and inventory.use_item(pizza_map[choice]):
            return Margherita() if choice == "1" else Pepperoni()
        raise ValueError("Invalid pizza type")