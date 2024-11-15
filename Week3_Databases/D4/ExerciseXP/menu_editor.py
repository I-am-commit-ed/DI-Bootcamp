from menu_item import MenuItem
from manu_manager import MenuManager

def show_user_menu():
    while True:
        print("\nMenu Manager")
        print("V: View an Item")
        print("A: Add an Item")
        print("D: Delete an Item")
        print("U: Update an Item")
        print("S: Show the Menu")
        print("Q: Quit")
        choice = input("Choose an option: ").upper()

        if choice == 'V':
            name = input("Enter the item name: ")
            item = MenuManager.get_by_name(name)
            if item:
                print(f"Item: {item.name}, Price: {item.price}")
            else:
                print("Item not found.")
        elif choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        elif choice == 'S':
            show_restaurant_menu()
        elif choice == 'Q':
            show_restaurant_menu()
            break
        else:
            print("Invalid option. Please try again.")

def add_item_to_menu():
    name = input("Enter the item name: ")
    price = int(input("Enter the item price: "))
    item = MenuItem(name, price)
    item.save()
    print("Item was added successfully.")

def remove_item_from_menu():
    name = input("Enter the name of the item to remove: ")
    item = MenuItem(name, 0)
    try:
        item.delete()
        print("Item was deleted successfully.")
    except:
        print("Error occurred while deleting the item.")

def update_item_from_menu():
    name = input("Enter the name of the item to update: ")
    new_name = input("Enter the new name: ")
    new_price = int(input("Enter the new price: "))
    item = MenuItem(name, 0)
    try:
        item.update(new_name, new_price)
        print("Item was updated successfully.")
    except:
        print("Error occurred while updating the item.")

def show_restaurant_menu():
    items = MenuManager.all_items()
    print("\nRestaurant Menu:")
    for item in items:
        print(f"Item: {item.name}, Price: {item.price}")

if __name__ == "__main__":
    show_user_menu()
