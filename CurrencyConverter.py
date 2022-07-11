
import requests

url = 'https://api.exchangerate.host/convert'
response = requests.get(url, params={
    "from": input("Currency you're converting from: ").upper(),
    "to": input("Currency you're converting to: ").upper(),
    "amount": float(input("Amount you're converting: "))
})
data = response.json()['result']
#from1 = response.json()["from"]
#to1 = response.json()["to"]
#amount1 = response.json()["amount"]

print(
      
    f" {params['from']} The result is  {data} "
    #f" {amount1}{from1} has been converted to {to1}. /n The result is  {data} "

    # f" {response.json()['amount']['from']}   is converted to '{response.json()['to']}' {data} "
    #f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")
    
)