def update_array(arr):
    for i in range(len(arr)):
        if i % 2 == 0:
            arr[i] += 5
        else:
            arr[i] *= 2

def main():
    arr = []
    
    while True:
        print("\n1. Input 1D Array")
        print("2. Update Array (Multiply odd-indexed by 2, Add 5 to even-indexed)")
        print("3. Display Array")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            size = int(input("Enter the size of the array: "))
            arr = [int(input(f"Enter element {i+1}: ")) for i in range(size)]
        elif choice == 2:
            if not arr:
                print("Array is empty. Please input an array first.")
            else:
                update_array(arr)
                print("Array updated successfully.")
        elif choice == 3:
            if not arr:
                print("Array is empty. Please input an array first.")
            else:
                print("Current Array:", arr)
        elif choice == 4:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
