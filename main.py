from inventory_manager import InventoryManager
from factory import PizzaFactory
from topping_decorator import ToppingDecorator
from payment import CreditCardPayment, PayPalPayment


inventory = InventoryManager()
print("Welcome to the Pizza Restaurant!")

while True:
    print("\n1. Margherita ($10)\n2. Pepperoni ($15)\n0. Exit")
    pizza_choice = input("Choose your pizza: ").strip()

    if pizza_choice == '0':
        print("Thank you for visiting!")
        break

    pizza = PizzaFactory.create_pizza(pizza_choice)

    while True:
        print("\nToppings:\n1. Cheese ($1)\n2. Olives ($0.5)\n3. Mushrooms ($0.7)\n4. Finish")
        topping_choice = input("Add topping: ").strip()
        toppings_map = {
            "1": ("Cheese", 1.0),
            "2": ("Olives", 0.5),
            "3": ("Mushrooms", 0.7),
        }

        if topping_choice == "4":
            break
        elif topping_choice in toppings_map:
            name, cost = toppings_map[topping_choice]
            if inventory.use_item(name):
                pizza = ToppingDecorator(pizza, name, cost)
        else:
            print("Invalid topping choice.")

    print(f"\nYour order: {pizza.get_description()}\nTotal: ${pizza.get_cost():.2f}")

    while True:
        print("\nPayment Methods:\n1. PayPal\n2. Credit Card")
        payment_choice = input("Choose payment: ").strip()
        if payment_choice == "1":
            payment = PayPalPayment()
            break
        elif payment_choice == "2":
            payment = CreditCardPayment()
            break
        else:
            print("Invalid payment method.")

    payment.pay(pizza.get_cost())
    print("\nRemaining Inventory:", inventory.inventory)
    print("Order replaced successfully\n")