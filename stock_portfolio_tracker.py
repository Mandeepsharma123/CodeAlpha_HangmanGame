# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 330,
    "AMZN": 140
}

total_investment = 0

print("===== Stock Portfolio Tracker =====")

while True:
    stock = input("\nEnter Stock Symbol (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found!")
        continue

    quantity = int(input("Enter Quantity: "))

    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f"Price per Share: ${stock_prices[stock]}")
    print(f"Investment in {stock}: ${investment}")

print("\n===============================")
print(f"Total Portfolio Value: ${total_investment}")

# Save result to a text file
with open("portfolio_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-------------------------\n")
    file.write(f"Total Portfolio Value: ${total_investment}")

print("Portfolio summary saved in portfolio_summary.txt")