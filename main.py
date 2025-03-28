import products
import store  # Import the Store class from store.py
import promotions


def start(store):
    """Displays the menu and handles user input."""
    while True:
        print("\n1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            for product in store.get_all_products():
                print(product.show())
        elif choice == "2":
            print(f"Total quantity in store: {store.get_total_quantity()}")
        elif choice == "3":
            shopping_list = []
            while True:
                product_name = input("Enter product name (or 'done' to finish): ")
                if product_name.lower() == "done":
                    break
                quantity = int(input(f"Enter quantity for {product_name}: "))
                product = next((p for p in store.get_all_products() if p.name == product_name), None)
                if product:
                    shopping_list.append((product, quantity))
                else:
                    print("Product not found.")
            total_price = store.order(shopping_list)
            print(f"Total price: {total_price}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    """Main function to run the store."""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct("Windows License", price=125),
        products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]

    store_instance = store.Store(product_list)

    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    start(store_instance)


if __name__ == "__main__":
    main()
