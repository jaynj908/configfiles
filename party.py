import random
import colorama
from colorama import Fore, Style
import os
from termcolor import colored, cprint


def gen_key():
    """Generat a secure password and a key to be used"""
    passwd = ''
    for k in range(31):
        k = random.choice(tag)
        if k == "''":
            k = random.choice(tag)
        passwd = passwd + k
    return passwd


# Characters used to generate a key
tag = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '&', '*', '(', ')', '+', '=', '-', '_', 'q', 'w', 'e', 'r', 't',
       'y', 'u', 'i', 'p', '[', ']', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|', '\\', 'a', 's', 'd', 'f', 'g', 'h', 'j',
       'k', 'l', ';', ':', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '<', '>', '/', '?', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

# Online Accounts
acct = ['Amazon', 'FaceBook', 'YouTube', 'Great Eyeglasses', 'Yahoo', 'Google', 'PrimeApp', 'NewEgg', 'Github', 'Microsoft', 'Home Server(user)', 'Home Server(root)',
        'FireFox', 'Pro Flowers', 'PcPartPicker', 'Bank Of America(personal)', 'Bank Of America(Commercial)', 'StackOverflow', 'Steam', 'RockStar',
        'UbiSoft', 'amdrewards', 'Acronis.com', 'Image-Line', 'Developer.Blender', 'Store.CableMod', 'DropBox', 'EKWB', 'Esurance', 'EVGA', 'Secure.EVGA',
        'LevelOneForum', 'Micro Center', 'Nvidia', 'Paypal', 'Pilot/Flying J', 'Pinterest', 'MyPrimeInc', 'ScdKey', 'Sprint', 'StashInvest', 'Twitter', 'Ubiquiti', 'Vudu',
        'World Of Trucks', 'Yahoo(Commerical']

# First remove the file containing keys
os.remove('/home/julianlynch/Documents/MyKeyPass.txt')

max_len = -1
longest_word = ''

# Find the longest string in acct
for length in acct:
    if len(length) > max_len:
        max_len = len(length)
    longest_word = length

line_count = 1

# Generate key and display a neat stdout()
for pin in acct:
    key = gen_key()
    spaces = max_len - len(pin)
    count = f'{line_count}'
    count = count.zfill(2)
    print(count, '', Fore.CYAN + pin, ' ' *
          spaces, Fore.YELLOW + key, Fore.WHITE)
    fs = ' '*spaces
    token = f'{pin}{fs} {key} \n'

    line_count = line_count + 1
    with open('/home/julianlynch/Documents/MyKeyPass.txt', 'a') as f:
        f.write(token)

print('')
cprint('!!!New keyz have been written to file!!!', 'green', attrs=['blink'])
