import products
import store

def start(best_buy):
    """Runs the main user interface for the store."""
    while True:
        print("\n1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            for product in best_buy.get_all_products():
                print(product.show())
        elif choice == "2":
            print(f"Total quantity in store: {best_buy.get_total_quantity()}")
        elif choice == "3":
            shopping_list = []
            while True:
                product_name = input("Enter product name (or type 'done' to finish): ")
                if product_name == "done":
                    break
                quantity = int(input(f"Enter quantity for {product_name}: "))
                product = None
                for p in best_buy.get_all_products():
                    if p.name == product_name:
                        product = p
                        break
                if product:
                    shopping_list.append((product, quantity))
                else:
                    print(f"Product {product_name} not found.")
            total_price = best_buy.order(shopping_list)
            print(f"Total order price: {total_price} dollars.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct("Windows License", price=125),
        products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]
    best_buy = store.Store(product_list)
    start(best_buy)
