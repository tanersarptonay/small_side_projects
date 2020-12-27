import requests
import sys
try:
    first_currency = input("First Currency: ")
    second_currency = input("Second currency: ")
    list = first_currency.split()

    url = "http://data.fixer.io/api/latest?access_key=f1f81ca084667abcc78dd2ce9e307370&symbols={},{}&format=10".format(list[1],second_currency)
    response = requests.get(url)
    json_data = response.json()

    actual_amount = json_data["rates"][second_currency] * float(list[0])
    print("{0:.2f}".format(actual_amount))

except KeyError:
    sys.stderr.write("Please input the currency names correct.")
    sys.stderr.flush()

except IndexError:
    sys.stderr.write("\nPlease do not forget to input the amount of the currency you would like to convert.")
    sys.stderr.flush()