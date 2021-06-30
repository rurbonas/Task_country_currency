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


