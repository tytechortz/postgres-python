import requests
from json import JSONDecodeError

# number = input("Enter a number: ")
# try:
#     print(int(number) * 2)
# except ValueError:
#     print("You didn't enter a base 10 number, try again")


r = requests.post('http://text-processing.com/api/sentiment', data={'text': 'hello world'})
try:
    label = r.json()['label']
    print(label)
except JSONDecodeError:
    print("Could not decode JSON response")

