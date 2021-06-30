# Exchange Rate by Country task
**User story:** 
As a user I would like to be able to enter country currency code and find out the exchange rate.

Our JSON file
```python
"base": "EUR",
  "date": "2017-07-26",
  "rates": {
	"AUD": 1.4717,
	"BGN": 1.9558,
	"BRL": 3.6806,
	"CAD": 1.4576,
	"CHF": 1.1152,
	"CNY": 7.8646,
	"CZK": 26.047,
	"DKK": 7.4368,
	"GBP": 0.89275,
	"HKD": 9.0959,
	"HRK": 7.4128,
	"HUF": 305.57,
	"IDR": 15507.0,
	"ILS": 4.1569,
	"INR": 74.938,
	"JPY": 130.26,
	"KRW": 1303.9,
	"MXN": 20.664,
	"MYR": 4.9889,
	"NOK": 9.2893,
	"NZD": 1.5678,
	"PHP": 58.948,
	"PLN": 4.2613,
	"RON": 4.5632,
	"RUB": 69.705,
	"SEK": 9.5705,
	"SGD": 1.585,
	"THB": 38.996,
	"TRY": 4.1406,
	"USD": 1.1644,
	"ZAR": 15.2
```
Exchange rate code and exception handling
```python
import json
class ExchangeRates:
    def parse(self, xfile, country):
        try:
            with open(xfile, "r") as content: # open file into contents variable
                exchange = json.load(content) # JSON object as dictionary
                rates = exchange["rates"][country]
                return rates
        except FileNotFoundError as err:
            return "File not found"
        except KeyError as err:
            return "Bad country code"

    def list(self, xfile):
        try:
            with open(xfile, "r") as content: # open file into contents variable
                exchange = json.load(content)  # JSON object as dictionary
                rates = exchange["rates"]
                for key in rates.keys():
                    print(key)
                return
        except FileNotFoundError as err:
            return "File not found"
```
Main program code
```python
from app.exchange_rate_paser import ExchangeRates

parse = ExchangeRates()
xfile = "exchange_rates.json" # input("Name of the file you would like to open? >> ")

print("Choose to continue: \n"
          "1. 'CONVERT' to see the currency against the EUR \n"
          "2. 'OTHER' to choose other currencies \n"
          "3. 'LIST' to see country codes \n"
          "4. 'HELP' to see the menu \n"
          "5. 'EXIT' to quit")

while True:
    choice = str(input("What would you like to do >> ").upper())
    if choice == 'CONVERT':
        country = input("What country code would you like to see >> ").upper()
        first_currency = parse.parse(xfile, country)
        print(f"The EUR is {first_currency} {country}")
        continue
    elif choice == 'OTHER':
        country = x1 = input("Choose a starting currency >> ").upper()
        first_currency = parse.parse(xfile, country)
        country = input("Choose your second currency >> ").upper()
        second_currency = parse.parse(xfile, country)
        final_currency = second_currency / first_currency
        print(f"1 {x1} is {final_currency} {country}")
        continue
    elif choice == 'LIST':
        print(parse.list(xfile))
        continue
    elif choice == 'HELP':
        print("Choose to continue: \n"
              "1. 'CONVERT' to see the currency against the EUR \n"
              "2. 'OTHER' to choose other currencies \n"
              "3. 'LIST' to see country codes \n"
              "4. 'HELP' to see the menu \n"
              "5. 'EXIT' to quit")
        continue
    elif choice == 'EXIT':
        break
    else:
        print("Invalid input")
```
### Example
```python
Choose to continue: 
1. 'CONVERT' to see the currency against the EUR 
2. 'OTHER' to choose other currencies 
3. 'LIST' to see country codes 
4. 'HELP' to see the menu 
5. 'EXIT' to quit
What would you like to do >> other
Choose a starting currency >> gbp
Choose your second currency >> usd
1 GBP is 1.304284514141697 USD
What would you like to do >> eixt
Invalid input
What would you like to do >> exit
```