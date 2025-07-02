cart = []

while True:
    command = int(input(
        "Enter a number (1: Show Cart, 2: Add to cart, 3: Remove item from cart and 4: To exit): "))

    if command == 1:
        if cart:
            print(f"Your cart item:", end=" ")
            for i in cart:
                print(i.capitalize(), end=", ")
            print()
        else:
            print("Your cart is empty")
    elif command == 2:
        while True:
            product = input(
                "Enter your product's name to add to your cart or enter 'Exit': ")
            if product.lower() == "exit":
                break
            else:
                cart.append(product.lower())
    elif command == 3:
        if cart:
            print(f"Your cart item:", end=" ")
            for i in cart:
                print(i, end=", ")
            print()
            deleted_product = input(
                "Enter product name that you want to remove: ")
            if cart.count(deleted_product):
                cart.remove(deleted_product)
            else:
                print(
                    f"{deleted_product.capitalize()} not exist in your cart to remove")
        else:
            print("Your cart is empty")
    elif command == 4 or not command:
        break
