from app.exchange_rate_paser import ExchangeRates

parse = ExchangeRates()


country = input("What country code would you like to see >> ").upper()
xfile = "exchange_rates.json" # input("Name of the file you would like to open? >> ")

print(parse.parse(xfile, country))