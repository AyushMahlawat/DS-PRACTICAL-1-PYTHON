def display_array(arr):
    print("Array:", arr)

def insert_element(arr, position, element):
    arr.insert(position, element)
    print(f"Element {element} inserted at position {position}.")

def main():
    array = []
    
    while True:
        print("\nMenu:")
        print("1. Display Array")
        print("2. Insert Element")
        print("3. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_array(array)
        elif choice == 2:
            position = int(input("Enter the position to insert the element: "))
            element = int(input("Enter the element to insert: "))
            insert_element(array, position, element)
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
