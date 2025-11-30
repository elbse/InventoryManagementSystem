print("==== INVENTORY MANAGEMENT SYSTEM ====")

class InventoryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


class InventoryManager:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, price):
        item = InventoryItem(name, quantity, price)
        self.items.append(item)
        print(f"Item '{name}' added to inventory.")

    def display_items(self):
        if not self.items:
            print("No items in inventory.")
            return

        print("\n=== INVENTORY ITEMS ===")
        for item in self.items:
            total_price = item.quantity * item.price
            print(f"Name: {item.name}")
            print(f"Quantity: {item.quantity}")
            print(f"Price: ₱{item.price:.2f}")
            print(f"Total Value: ₱{total_price:.2f}")
            print("----------------------------")
    
    def update_quantity(self, name, new_quantity):
        for item in self.items:
            if item.name.lower() == name.lower():
                item.quantity = new_quantity
                print(f"Quantity of '{name}' updated to {new_quantity}.")
                return
        print(f"Item '{name}' not found in inventory.")

    def calculate_total_inventory_value(self):
        total_value = sum(item.quantity * item.price for item in self.items)
        print(f"\nTotal Inventory Value: ₱{total_value:.2f}")


# ============================
# MAIN PROGRAM LOOP
# ============================

inventory = InventoryManager()

# Sample default items
inventory.add_item("Soap", 10, 20.00)
inventory.add_item("Shampoo", 5, 15.00)
inventory.add_item("Rice (1kg)", 20, 55.00)

while True:
    print("""
====== MENU ======
1. Add Item
2. Update Item Quantity
3. Show Inventory
4. Calculate Total Inventory Value
5. Exit
""")

    choice = input("Enter your choice: ")

    
    if choice == "1":
        name = input("Enter item name: ")
        
        try:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price (₱): "))
        except ValueError:
            print("❌ Invalid input! Quantity must be a number, price must be a valid amount.")
            continue

        inventory.add_item(name, quantity, price)

    elif choice == "2":
        name = input("Enter item name to update: ")
        
        try:
            new_quantity = int(input("Enter new quantity: "))
        except ValueError:
            print("❌ Invalid input! Quantity must be a number.")
            continue

        inventory.update_quantity(name, new_quantity)

    elif choice == "3":
        inventory.display_items()

    elif choice == "4":
        inventory.display_items()
        inventory.calculate_total_inventory_value()

    elif choice == "5":
        print("Exiting program. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please enter a number from 1–5.")
