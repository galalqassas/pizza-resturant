# Design Patterns in the Pizza Restaurant Project

In the Pizza Restaurant project, several design patterns are used to make the system organized and easy to maintain. Below are the main patterns applied:

## 1. Factory Pattern

### 1.1. Description
The Factory Pattern creates objects without specifying the exact class. It provides a method to create objects based on input.

### 1.2. Before Applying the Pattern
Before using the Factory Pattern, creating different pizza types required multiple `if-else` statements scattered in the code.

### 1.3. Code Example
```
class PizzaFactory:
    @staticmethod
    def create_pizza(choice):
        inventory = InventoryManager()
        pizza_map = {"1": "Margherita", "2": "Pepperoni"}
        if choice in pizza_map and inventory.use_item(pizza_map[choice]):
            return Margherita() if choice == "1" else Pepperoni()
        raise ValueError("Invalid pizza type")
```


## Over Engineering

**Over Engineering** means making a system more complicated than necessary. It can make the code hard to understand and maintain.

### Example in Pizza Project
Adding too many patterns for a simple project.

```
# over complex for simple payment
class BitcoinPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount:.2f} using Bitcoin. Payment Successful!")
```

Instead, keep it simple with necessary payment methods.
