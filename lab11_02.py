def car_band():
    car_brands_number = int(input("Enter the number of car brands you want to input: "))
    car_brands = []
    for i in range(car_brands_number):
        brand = input(f"Enter the name of car brand {i + 1}: ")
        car_brands.append(brand)

    print("\n======== Car Brands List ========")
    print(f"Oridinal Car Brand List: {car_brands}")
    print(f"Sorted Car Brand List: {sorted(car_brands)}")

def product_price():
    product_number = int(input("How many products do you want to input? "))
    product_prices = []
    for i in range(product_number):
        price = float(input(f"Enter the price of product {i + 1}: "))
        product_prices.append(price)
    print(f"Total Prices: {product_prices}")
    print(f"Average Price: {sum(product_prices) / len(product_prices):.2f}")

def sale_qty():
    sale_number = int(input("How many sales quantities do you want to input? "))
    sale_quantities = []
    for i in range(sale_number):
        quantity = int(input(f"Enter the quantity of sale {i + 1}: "))
        sale_quantities.append(quantity)
    print(f"Sales Quantities List : {sale_quantities}")
    print(f"Highest Sale Quantity : {max(sale_quantities)}")
    print(f"Lowest Sale Quantity  : {min(sale_quantities)}")

def main():
    while True:
        print("\n======== Menu ========")
        print("1. Car Brands")
        print("2. Product Prices")
        print("3. Sale Quantities")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            car_band()
        elif choice == '2':
            product_price()
        elif choice == '3':
            sale_qty()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()