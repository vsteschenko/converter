#!/usr/bin/env python3
def exchange():
	from forex_python.converter import CurrencyRates
	c = CurrencyRates()
	amount = int(input("Enter the amount: "))
	from_currency = input("From Currency: ").upper()
	to_currency =  input("To Currency: ").upper()
	print(from_currency, " to ", to_currency, amount)
	result = c.convert(from_currency, to_currency, amount)
	print(round(result,2))
exchange()	
