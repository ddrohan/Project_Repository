#####################################################
from product import Product


def show_menu():
    print("\n=== Shop Menu ===")
    print("1. List all products")
    print("2. Find product")
    print("3. Remove product")
    print("4. Show total value")
    print("5. Add a Product")
    print("0. Exit")
#####################################################
def listProducts(products):
    print("\n" + str(products))
#####################################################
def findProducts():
    print("\nYou Chose Option 2.")
#####################################################
def removeProducts():
    print("\nYou Chose Option 3.")
#####################################################
def findTotalValue():
    print("\nYou Chose Option 4.")
#####################################################
def addProduct(products):
    print("\nPlease Enter a Product.")
    product = input("> ")
    products.append(product)
#####################################################

def main():

    products = ["Ball","Racket","Golf Clubs"]
    product = Product("Tennis Ball", 2.99)
    products.append(str(product))
    running = True
    while running:
        show_menu()
        choice = input("Enter an Option: ")
        if choice == "1": listProducts(products)
        elif choice == "2": findProducts()
        elif choice == "3": removeProducts()
        elif choice == "4": findTotalValue()
        elif choice == "5": addProduct(products)
        elif choice == "0": running = False
        else:
            print("\nInvalid Option, please try again...")
#####################################################
if __name__ == "__main__":
    main()
#####################################################