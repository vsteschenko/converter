#!/usr/bin/env python3
from forex_python.bitcoin import BtcConverter

def get_price():
    currency = input("Enter the currency (e.g., USD, EUR, GBP): ").upper()
    b = BtcConverter()
    price = b.get_latest_price(currency)
    print(f"Latest price of one Bitcoin in {currency}: {price}")

def convert_to_btc():
    amount = float(input("Enter the amount: "))
    currency = input("Enter the currency (e.g., USD, EUR, GBP): ").upper()
    b = BtcConverter()
    btc_amount = b.convert_to_btc(amount, currency)
    print(f"{amount} {currency} is equivalent to {btc_amount:.8f} BTC")

def convert_from_btc():
    amount = float(input("Enter the amount of BTC: "))
    currency = input("Enter the currency to convert to (e.g., USD, EUR, GBP): ").upper()
    b = BtcConverter()
    converted_amount = b.convert_btc_to_cur(amount, currency)
    print(f"{amount:.8f} BTC is equivalent to {converted_amount:.2f} {currency}")

def main():
    print("Select an option:")
    print("1. Get Price of BTC")
    print("2. Convert Currency to BTC")
    print("3. Convert BTC to Currency")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        get_price()
    elif choice == '2':
        convert_to_btc()
    elif choice == '3':
        convert_from_btc()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
