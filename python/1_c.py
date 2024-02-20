def display_menu():
    print("\nMenu:")
    print("1. Input 1D array")
    print("2. Delete element from specified position")
    print("3. Display array")
    print("4. Exit")

def input_array():
    global arr
    arr = list(map(int, input("Enter space-separated elements of the array: ").split()))
    print("Array has been inputted.")

def delete_element():
    global arr
    if not arr:
        print("Array is empty. Cannot delete element.")
        return

    position = int(input("Enter the position to delete an element: "))
    if 1 <= position <= len(arr):
        del arr[position - 1]
        print("Element deleted successfully.")
    else:
        print("Invalid position. Please enter a valid position.")

def display_array():
    global arr
    if not arr:
        print("Array is empty.")
    else:
        print("Array:", arr)

arr = []

while True:
    display_menu()
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        input_array()
    elif choice == 2:
        delete_element()
    elif choice == 3:
        display_array()
    elif choice == 4:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-4).")
