from products import Product
from store import Store


def list_products(store: Store):
    """
    Lists all active products in the store.
    """
    print("\nAvailable Products:")
    products = store.get_all_products()
    for product in products:
        print(product.show())


def show_total_quantity(store: Store):
    """
    Displays the total quantity of products in the store.
    """
    print(f"\nTotal quantity of products in store: {store.get_total_quantity()}")


def make_order(store: Store):
    """
    Allows the user to make an order by selecting products and quantities.
    """
    products = store.get_all_products()
    shopping_list = []
    print("\nEnter product number and quantity (e.g., 1 2 to buy 2 of the first product).")
    while True:
        print("\nProducts:")
        for idx, product in enumerate(products, 1):
            print(f"{idx}. {product.show()}")
        print(f"{len(products) + 1}. Done ordering.")

        try:
            choice = int(input("Choose a product (1-{}): ".format(len(products) + 1)))
            if choice == len(products) + 1:
                break
            elif 1 <= choice <= len(products):
                quantity = int(input(f"Enter quantity for {products[choice - 1].name}: "))
                shopping_list.append((products[choice - 1], quantity))
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

    try:
        total_price = store.order(shopping_list)
        print(f"\nYour total is: ${total_price:.2f}")
    except Exception as e:
        print(f"Error while placing the order: {e}")


def start(store: Store):
    """
    Displays a menu and interacts with the store.
    """
    while True:
        print("\nStore Menu:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                list_products(store)
            elif choice == 2:
                show_total_quantity(store)
            elif choice == 3:
                make_order(store)
            elif choice == 4:
                print("Thank you for visiting the store!")
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")


# the initial stock of inventory given from the exercise
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = Store(product_list)

if __name__ == "__main__":
    start(best_buy)
