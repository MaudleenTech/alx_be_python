# This script implements a simple menu-driven shopping list manager using Python lists.

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # 1. Add Item
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item cannot be empty.")
                
        elif choice == '2':
            # 2. Remove Item
            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove:
                try:
                    shopping_list.remove(item_to_remove)
                    print(f"'{item_to_remove}' removed from the list.")
                except ValueError:
                    # Handle case where the item is not found in the list
                    print(f"Error: '{item_to_remove}' not found in the list.")
            else:
                print("Item name cannot be empty.")
                
        elif choice == '3':
            # 3. View List
            if shopping_list:
                print("--- Your Shopping List ---")
                # Print each item with its index (starting from 1 for user-friendliness)
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
                print("--------------------------")
            else:
                print("The shopping list is currently empty.")
                
        elif choice == '4':
            # 4. Exit
            print("Goodbye!")
            break
            
        else:
            # Handle invalid choice
            print("Invalid choice. Please try again (Enter 1, 2, 3, or 4).")

if __name__ == "__main__":
    main()
