import requests 
import json 

x = requests.get('https://jbvalues-app.herokuapp.com/itemdata2')
response = json.loads(x.text)

items = {}
advanced = {}

BLACK = '\x1b[30m'
RED = '\x1b[31m'
GREEN = '\x1b[32m'
YELLOW = '\x1b[33m'
BLUE = '\x1b[34m'
MAGENTA = '\x1b[35m'
RESET = '\x1b[0m' # Reset all formatting

print_formatted = lambda s: print(s + RESET)

for i in response['vehicles']:
    actual = response['vehicles'][i]
    items[actual['name'].lower().replace(' ', '')] = actual['value']
    advanced[actual['name'].lower().replace(' ', '')] = {'value': actual['value'], 'trend': actual['trend'].lower()}

for i in response['cosmetics']:
    actual = response['cosmetics'][i]
    items[actual['name'].lower().replace(' ', '')] = actual['value']
    advanced[actual['name'].lower().replace(' ', '')] = {'value': actual['value'], 'trend': actual['trend'].lower()}

# fixes
items['concept'] = '2,500,000'
items['m12'] = items['molten']
items['421s'] = items['megalodon']
items['ufo'] = '500,000'

def main():
    your = input(f'{GREEN}Type your trade: ').strip().split(' ')
    tmp = []
    for i in your:
        for j in items:
            if i in j:
                tmp.append(i)
                break # break patch
    your = tmp 

    them = input(f'{YELLOW}Type his trade: ').strip().split(' ')
    tmp = []
    for i in them:
        for j in items:
            if i in j:
                tmp.append(i)
                break # break patch
    
    your_value = sum([int(items[i].replace(',','')) for i in your])
    his_value = sum([int(items[i].replace(',','')) for i in them])

    your_value = f'{your_value:,.2f}'
    his_value = f'{his_value:,.2f}'

    your_value = your_value[:your_value.index('.')]
    his_value = his_value[:his_value.index('.')]
    
    print()

    print_formatted(f'{GREEN}Your trade value: {BLUE}{your_value}')
    print_formatted(f'{YELLOW}His trade value: {BLUE}{his_value}')

    print()

    difference = int(your_value.replace(",", "")) - int(his_value.replace(",", ""))
    if difference > 0:
        difference = f"{RED}LOSING!{RESET} Your trade is higher by {RED}{difference}{RESET}\n\t\t{BLACK}--> If you accept it, his profit will be higher"
    elif difference < 0: 
        difference = f"{GREEN}WINNING!{RESET} Your trade is lower by {GREEN}{abs(difference)}{RESET}\n\t\t{BLACK}--> If you accept it, your profit will be higher"
    elif difference == 0:
        difference = f'{BLUE}FAIR!{RESET} Your trade has the same value as his trade'

    print_formatted(f'{YELLOW}Difference: {difference}')


while True:
    main()
