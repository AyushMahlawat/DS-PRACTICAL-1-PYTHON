def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the element is found
    return -1  # Return -1 if the element is not found

def main():
    while True:
        print("\n1. Input 1D array")
        print("2. Linear search for an element")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            # Input 1D array
            try:
                n = int(input("Enter the size of the array: "))
                arr = []
                for _ in range(n):
                    element = int(input("Enter an element: "))
                    arr.append(element)
                print("Array:", arr)
            except ValueError:
                print("Invalid input. Please enter valid integers.")

        elif choice == '2':
            # Linear search for an element
            try:
                if not arr:
                    print("Array is empty. Please input an array first.")
                    continue

                target = int(input("Enter the element to search: "))
                index = linear_search(arr, target)

                if index != -1:
                    print(f"Element {target} found at index {index}.")
                else:
                    print(f"Element {target} not found in the array.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        elif choice == '3':
            # Exit the program
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option (1/2/3).")

if __name__ == "__main__":
    main()
