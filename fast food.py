menu = ["Burger", "Fries", "Pizza", "Drink"]
order = []


def display_menu() -> object:
    print("Menu:")
    item: str
    for i, item in enumerate(menu, start=1):
        print(f"{i}. {item}")


def add_to_order(item_number):
    if item_number < 1 or item_number > len(menu):
        print("Invalid item number!")
    else:
        order.append(menu[item_number - 1])
        print(f"Added {menu[item_number - 1]} to your order.")


def view_order():
    print("Your order:")
    for item in order:
        print(item)


def main():
    while True:
        print("\nOptions:")
        print("1. View Menu")
        print("2. Place Order")
        print("3. View Order")
        print("4. Exit")
        choice = input("Enter the option number: ")

        if choice == "1":
            display_menu()
        elif choice == "2":
            while True:
                item_input = input("Enter the item number to add (or 'Done' to finish): ")
                if item_input.lower() == "done":
                    break
                else:
                    item_number = int(item_input)
                    add_to_order(item_number)
        elif choice == "3":
            view_order()
        elif choice == "4":
            print("Goodbye! Your order contains:")
            view_order()
            break
        else:
            print("Invalid option!")


main()
