import os
import json
import requests
import time

from datetime import datetime
from auth import api
from colorama import Fore

def getchecksum():
    time.sleep(0)

keyauthapp = api(
    name = "PhantomClient",
    ownerid = "dhtmNBRSrd",
    secret = "cea7edec4d73abf8c15821c0b6ac5fa8b165a567e3ff0564164d92fe8d38b15c",
    version = "1.0",
    hash_to_check = getchecksum()
)

def logo():
    os.system('cls')
    print(f'''{Fore.CYAN}
                                                                                                    
                            ██████  ██   ██  █████  ███    ██ ████████  ██████  ███    ███ 
                            ██   ██ ██   ██ ██   ██ ████   ██    ██    ██    ██ ████  ████ 
                            ██████  ███████ ███████ ██ ██  ██    ██    ██    ██ ██ ████ ██ 
                            ██      ██   ██ ██   ██ ██  ██ ██    ██    ██    ██ ██  ██  ██ 
                            ██      ██   ██ ██   ██ ██   ████    ██     ██████  ██      ██ 
                                                                                                  
                                                                                                                                                                                              
> Created by 444#9667                                                                             
> https://www.instagram.com/sander.reg/                                                                         
''')

def remove():
    url = "https://pinballcrush.sea.freefiremobile.com/api/spin?access_token=AC182257074B52CF4EC6D9F5EB506A452A9A01B7A804F05CC24859E2EE8360F18159652912E5C6FDCB09DA70559C3412279B90A70CB39110929FD3B572E986FC2B8EEB1E44BC382819681665F0CFA549"
    headers = {'Host': 'pinballcrush.sea.freefiremobile.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0', 'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'de,en-US;q=0.7,en;q=0.3', 'Accept-Encoding': 'gzip, deflate, br', 'Content-Type': 'application/json;charset=utf-8', 'X-CSRFToken': 'lheXRezZo6M83mEhBablfIL1wYSUUPsnZCTV6AFQ2YWhwCzaNqQHwcTRB4Bje5IH', 'Content-Length': '9', 'Origin': 'https://pinballcrush.sea.freefiremobile.com', 'Connection': 'keep-alive', 'Referer': 'https://pinballcrush.sea.freefiremobile.com/?access_token=AC182257074B52CF4EC6D9F5EB506A452A9A01B7A804F05CC24859E2EE8360F18159652912E5C6FDCB09DA70559C3412279B90A70CB39110929FD3B572E986FC2B8EEB1E44BC382819681665F0CFA549&lang=en&region=EUROPE', 'Cookie': 'csrftoken=lheXRezZo6M83mEhBablfIL1wYSUUPsnZCTV6AFQ2YWhwCzaNqQHwcTRB4Bje5IH; eventtoken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2Nlc3NfdG9rZW4iOiJBQzE4MjI1NzA3NEI1MkNGNEVDNkQ5RjVFQjUwNkE0NTJBOUEwMUI3QTgwNEYwNUNDMjQ4NTlFMkVFODM2MEYxODE1OTY1MjkxMkU1QzZGRENCMDlEQTcwNTU5QzM0MTIyNzlCOTBBNzBDQjM5MTEwOTI5RkQzQjU3MkU5ODZGQzJCOEVFQjFFNDRCQzM4MjgxOTY4MTY2NUYwQ0ZBNTQ5IiwicmVnaW9uIjoiRVVST1BFIiwicmVnaW9uX2xhbmciOiJFVVJPUEVfZW4iLCJ1aWQiOjExNTIwOTgyOTgsIm5pY2tuYW1lIjoiSUNFXHUzMTY0VklPTEVOVCEiLCJ0eXBlIjoxLCJleHAiOjE2NTM4NDgzNTh9.UUpXCHZISHs0c3QMtm7qXFp6Fh3XE3iUsr0pfu4qYrQ; _ga=GA1.4.388692535.1653752939; _gid=GA1.4.990916641.1653752939; _ga=GA1.2.388692535.1653752939; _gid=GA1.2.990916641.1653752939; _ga_WJL67QFQPX=GS1.1.1653752939.1.1.1653755241.0; _gat_gtag_UA_220297702_23=1', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin'}
    body = {"num":1}
    requests.put(url, json=body, headers=headers)

def menu():
    logo()
    print(f"""{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}""")
    print(f"{Fore.RESET}[{Fore.CYAN}1{Fore.RESET}]{Fore.LIGHTBLACK_EX} Remove Diamonds {Fore.RESET}")
    print(f"{Fore.RESET}[{Fore.CYAN}X{Fore.RESET}]{Fore.RED} Exit")
    print(f"""{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}""")
    res = input(f'{Fore.CYAN}[PHANTOM]{Fore.WHITE} Select an option: ')
    if res == "1":
        os.system('cls')
        logo()
        print(f"""{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}""")
        res = input(f'{Fore.CYAN}[PHANTOM]{Fore.WHITE} How many diamonds would you like to remove: ')
        os.system('cls')
        logo()
        number = int(res) / 20
        print(f'{Fore.CYAN}[PHANTOM]{Fore.WHITE} Removing diamonds...')
        for num in range(int(number)):
            remove()
        print(f'{Fore.CYAN}[PHANTOM]{Fore.WHITE} {res} diamonds have been removed.')
        time.sleep(3)
            
    elif res == "X":
        os._exit(0)
    else:
        menu()

def accinfo():
    print(Fore.CYAN + "Username: " + keyauthapp.user_data.username)
    print("HWID: " + keyauthapp.user_data.hwid)
    print("Subscription: " + keyauthapp.user_data.subscription)
    print("Expiry: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.expires)).strftime('%Y-%m-%d %H:%M:%S'))
    input(Fore.WHITE + "Press any key to go to the menu...")

def login():
    logo()
    user = input(f'{Fore.CYAN}[PHANTOM]{Fore.WHITE} Username: ')
    password = input(f'{Fore.CYAN}[PHANTOM]{Fore.WHITE} Password: ')
    keyauthapp.login(user,password)
    os.system('cls')
    logo()
    accinfo()
    if keyauthapp.user_data.subscription == "tools":
        menu()
    else:
        os.system('cls')
        print(f'{Fore.CYAN}[PHANTOM]{Fore.WHITE} Your account does not have access to this tool.')
        time.sleep(5)
        
login()