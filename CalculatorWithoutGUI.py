# Initialize variables
order_total = 0
order_items = []

while True:
    # Get user input
    user_input = input("Enter the item price (or 'q' to exit): ")

    if user_input.lower() == "q":
        if len(order_items) > 0:
            # Display the list of items and their prices
            print("\nOrder Summary:")
            for item, price in order_items:
                print(f"{item}: ${price}")
            print(f"Total Amount: ${order_total}")

            # Create a bill
            bill_filename = "order_bill.txt"
            with open(bill_filename, "w") as bill_file:
                bill_file.write("Order Summary:\n")
                for item, price in order_items:
                    bill_file.write(f"{item}: ${price}\n")
                bill_file.write(f"Total Amount: ${order_total}")

            print(f"Bill saved to '{bill_filename}'")

        else:
            print("No items were added to the order.")
        print("Thanks for shopping!")
        break
    else:
        try:
            item_price = float(user_input)
            if item_price < 0:
                print("Price cannot be negative. Please enter a valid price.")
            else:
                # Get item name and add it to the order_items list
                item_name = input("Enter the name of the item: ")
                order_items.append((item_name, item_price))
                order_total += item_price
                print(f"{item_name} added to the order. Order total: ${order_total}")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q' to exit.")
