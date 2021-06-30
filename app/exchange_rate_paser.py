import json
class ExchangeRates:
    def parse(self, xfile):
        try:
            with open(xfile, "r") as content:
                return json.loads(content.read())
        except SyntaxError as err:
            return "Wrong file"
