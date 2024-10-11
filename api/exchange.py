# JUST A CONSOLE APP USING FREE API KEY TO CONVERT CURENCIES
# I MADE ANOTHER FILE WHICH HAS A KEY VALUE LIST SO I COULD LIST THE AVAILABLE CURRENCIES

import requests
from list_currency import *

# SET API KEY AND URL
api_key = "YOUR API KEY"
base_url = f'https://v6.exchangerate-api.com/v6/5debba90e9588f90e1a23140/latest/'

print('\n------- WELCOME TO THE CURRENCY CONVERTER -------')

def list_currencies():
    print("\nOur currencies: ")
    print(48*'-')
    currencies = list(list_currency.keys())
    for i in range (0, len(currencies), 10):
        print(", ".join(currencies[i:i+10]))
    print(48*'-')

def list_menu():
    print('\n------- MENU -------')
    print('1. List currencies available')
    print('2. Exchange now')
    print('3. Exit')

def get_user_input():
    base_currency = input('\nInput your currecy code from the list: ').upper()
    target_currency = input('Input your target currency code from the list: ').upper()
    amount = float(input('Input the amount you want to convert: '))
    return base_currency, target_currency, amount

def convert_currency(base_currency, target_currency, amount):
    url = f'{base_url}{base_currency}'
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        print('Error fetching data from API.')
        return

    if target_currency not in data['conversion_rates']:
        print('Invalid currency code.')
        return

    rate = data['conversion_rates'][target_currency]
    converted_amount = amount * rate
    print(f'\n{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}')

while True:
    list_menu()
    choice = input('Enter your the menu number: ')
    if choice == '1':
        list_currencies()

    elif choice == '2':
        base_currency, target_currency, amount = get_user_input()
        convert_currency(base_currency, target_currency, amount)

    elif choice == '3':
        print('\nThanks for using our converter!')
        print('Exiting...')
        break

    else:
        print('Invalid input please try again.')

