
# Stock Portfolio Management System

portfolio = {}

def add_stock():
    name = input("Enter stock name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per share: "))

    portfolio[name] = {
        "quantity": quantity,
        "price": price
    }

    print("Stock added successfully!\n")


def view_portfolio():
    if not portfolio:
        print("Portfolio is empty!\n")
        return

    print("\n----- STOCK PORTFOLIO -----")
    total = 0

    for name, details in portfolio.items():
        value = details["quantity"] * details["price"]
        total += value

        print("Stock Name:", name)
        print("Quantity:", details["quantity"])
        print("Price:", details["price"])
        print("Total Value:", value)
        print("----------------------")

    print("Total Investment Value:", total, "\n")


def main():
    while True:
        print("===== STOCK PORTFOLIO =====")
        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_stock()
        elif choice == "2":
            view_portfolio()
        elif choice == "3":
            print("Thank you for using Stock Portfolio!")
            break
        else:
            print("Invalid choice!\n")


main()