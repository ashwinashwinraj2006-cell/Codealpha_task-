# ============================================================
# TASK 2: Stock Portfolio Tracker
# ============================================================

import csv
import os

# Hardcoded stock prices dictionary
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185,
    "META": 500,
    "NFLX": 650,
    "NVDA": 875,
}


def display_available_stocks():
    """Display all available stocks with their prices."""
    print("\n" + "=" * 40)
    print("   AVAILABLE STOCKS & PRICES (USD)")
    print("=" * 40)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<8} :  ${price:>8,.2f}")
    print("=" * 40)


def get_portfolio_input():
    """Prompt user to enter stock names and quantities."""
    portfolio = {}

    print("\nEnter your stock holdings.")
    print("Type 'done' when finished.\n")

    while True:
        symbol = input("Enter stock symbol (e.g., AAPL): ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"  ⚠  '{symbol}' is not in our stock list. Try again.\n")
            continue

        try:
            qty = int(input(f"  Enter quantity for {symbol}: ").strip())
            if qty <= 0:
                print("  ⚠  Quantity must be a positive number. Try again.\n")
                continue
        except ValueError:
            print("  ⚠  Invalid quantity. Please enter a whole number.\n")
            continue

        if symbol in portfolio:
            portfolio[symbol] += qty
            print(f"  ✓  Updated {symbol}: total {portfolio[symbol]} shares.\n")
        else:
            portfolio[symbol] = qty
            print(f"  ✓  Added {symbol} x{qty}.\n")

    return portfolio


def calculate_portfolio(portfolio):
    """Calculate value of each holding and total investment."""
    results = []
    total = 0.0

    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        results.append({
            "symbol": symbol,
            "quantity": qty,
            "price_per_share": price,
            "total_value": value,
        })

    return results, total


def display_portfolio_summary(results, total):
    """Print a formatted portfolio summary to the console."""
    print("\n" + "=" * 60)
    print("              PORTFOLIO SUMMARY")
    print("=" * 60)
    print(f"  {'Stock':<8} {'Qty':>6}  {'Price/Share':>13}  {'Total Value':>13}")
    print("-" * 60)

    for row in results:
        print(
            f"  {row['symbol']:<8} {row['quantity']:>6}  "
            f"${row['price_per_share']:>12,.2f}  "
            f"${row['total_value']:>12,.2f}"
        )

    print("-" * 60)
    print(f"  {'TOTAL INVESTMENT':>36}   ${total:>12,.2f}")
    print("=" * 60)


def save_to_txt(results, total, filename="portfolio_result.txt"):
    """Save portfolio summary to a .txt file."""
    with open(filename, "w") as f:
        f.write("STOCK PORTFOLIO SUMMARY\n")
        f.write("=" * 60 + "\n")
        f.write(f"{'Stock':<8} {'Qty':>6}  {'Price/Share':>13}  {'Total Value':>13}\n")
        f.write("-" * 60 + "\n")
        for row in results:
            f.write(
                f"{row['symbol']:<8} {row['quantity']:>6}  "
                f"${row['price_per_share']:>12,.2f}  "
                f"${row['total_value']:>12,.2f}\n"
            )
        f.write("-" * 60 + "\n")
        f.write(f"{'TOTAL INVESTMENT':>37}   ${total:>12,.2f}\n")
    print(f"\n  ✓  Result saved to '{filename}'")


def save_to_csv(results, total, filename="portfolio_result.csv"):
    """Save portfolio summary to a .csv file."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock Symbol", "Quantity", "Price Per Share (USD)", "Total Value (USD)"])
        for row in results:
            writer.writerow([
                row["symbol"],
                row["quantity"],
                row["price_per_share"],
                row["total_value"],
            ])
        writer.writerow([])
        writer.writerow(["", "", "TOTAL INVESTMENT", round(total, 2)])
    print(f"  ✓  Result saved to '{filename}'")


def ask_save_option():
    """Ask the user if they want to save results and in what format."""
    print("\nWould you like to save the results?")
    print("  1 - Save as .txt")
    print("  2 - Save as .csv")
    print("  3 - Save both")
    print("  4 - Don't save")

    choice = input("\nEnter choice (1/2/3/4): ").strip()
    return choice


# ─── MAIN PROGRAM ───────────────────────────────────────────

def main():
    print("\n╔══════════════════════════════════╗")
    print("║   STOCK PORTFOLIO TRACKER v1.0   ║")
    print("╚══════════════════════════════════╝")

    display_available_stocks()

    portfolio = get_portfolio_input()

    if not portfolio:
        print("\n  No stocks entered. Exiting.\n")
        return

    results, total = calculate_portfolio(portfolio)
    display_portfolio_summary(results, total)

    choice = ask_save_option()

    if choice == "1":
        save_to_txt(results, total)
    elif choice == "2":
        save_to_csv(results, total)
    elif choice == "3":
        save_to_txt(results, total)
        save_to_csv(results, total)
    else:
        print("\n  Results not saved.")

    print("\n  Thank you for using Stock Portfolio Tracker!\n")


if __name__ == "__main__":
    main()
