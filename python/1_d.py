def reverse_array(arr):
    return arr[::-1]

def main():
    while True:
        print("\n1. Input 1D Array")
        print("2. Reverse the Array")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            array = list(map(int, input("Enter space-separated elements of the array: ").split()))
            print("Array input successful!")

        elif choice == 2:
            if 'array' in locals():
                reversed_array = reverse_array(array)
                print("Reversed Array:", reversed_array)
            else:
                print("Error: Array not initialized. Please input the array first.")

        elif choice == 3:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
