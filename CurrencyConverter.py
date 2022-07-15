
import requests

print("Kindly use the currency Abbreviation")
url = 'https://api.exchangerate.host/convert'
response = requests.get(url, params={
    "from": input("Currency you're converting from: ").upper(),
    "to": input("Currency you're converting to: ").upper(),
    "amount": float(input("Amount you're converting: "))
})

#response = requests.get(
# f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

data = response.json()['result']
from1 = response.json()["query"]['from']
to1 = response.json()["query"]['to']
amount1 = response.json()["query"]['amount']

print(
      
     #"from:" + input("Currency you're converting from: ").upper()
     #f" The result is  {from1} "
    f" {amount1}{from1} has been converted to {to1}. \n The result is  {data} "

    # f" {response.json()['amount']['from']}   is converted to '{response.json()['to']}' {data} "
    #f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")
    
)

'''
import requests

from_currency = str(
    input("Enter in the currency you'd like to convert from: ")).upper()

to_currency = str(
    input("Enter in the currency you'd like to convert to: ")).upper()

amount = float(input("Enter in the amount of money: "))

response = requests.get(
    f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

print(
    f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")
'''