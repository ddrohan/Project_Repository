#####################################################
def show_menu():
    print("\n=== Shop Menu ===")
    print("1. List all products")
    print("2. Find product")
    print("3. Remove product")
    print("4. Show total value")
    print("0. Exit")
#####################################################
def listProducts():
    print("\nYou Chose Option 1.")
#####################################################

def main():
    running = True
    while running:
        show_menu()
        choice = input("Enter an Option: ")
        if choice == "1":
            listProducts()
        elif choice == "2":
            print("\nYou Chose Option 2.")
        elif choice == "3":
            print("\nYou Chose Option 3.")
        elif choice == "4":
            print("\nYou Chose Option 4.")
        elif choice == "0":
            running = False
        else:
            print("\nInvalid Option, please try again...")
#####################################################
if __name__ == "__main__":
    main()
#####################################################