inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

while True:
    print("\n===== INVENTORY CONTROL SYSTEM =====")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\n--- Current Inventory ---")
        for i, item in enumerate(inventory, 1):
            print(i, item)

    elif choice == "2":
        item = input("Enter item to add: ")
        inventory.append(item)
        print(item, "added to inventory.")

    elif choice == "3":
        item = input("Enter item to remove: ")
        if item in inventory:
            inventory.remove(item)
            print(item, "removed from inventory.")
        else:
            print("Item not found!")

    elif choice == "4":
        inventory.sort()
        print("Inventory sorted alphabetically.")
        for i, item in enumerate(inventory, 1):
            print(i, item)

    elif choice == "5":
        print("Thank you! Exiting Inventory System.")
        break

    else:
        print("Invalid choice! Please enter 1 to 5.")

