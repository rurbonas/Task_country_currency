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
