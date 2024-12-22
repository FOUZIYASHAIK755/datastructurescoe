def amount_converter():
    inr_rate = 83.00  # 1 USD = 83 INR
    eur_rate = 0.92   # 1 USD = 0.92 EUR
    gbp_rate = 0.78   # 1 USD = 0.78 GBP

    try:
        amt = float(input("Enter the amount in USD: "))
        if amt < 0:
            print("Amount cannot be negative!")
            return
        print(f"{amt} USD = {amt * inr_rate:.2f} INR")
        print(f"{amt} USD = {amt * eur_rate:.2f} EUR")
        print(f"{amt} USD = {amt * gbp_rate:.2f} GBP")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
amount_converter()
