import os
import requests
import time

from auth import api
from colorama import Fore

user_path = '/'.join(os.getcwd().split('\\', 3)[:3])
drive_letter = os.getcwd().split('\\', 1)[0]+'/'
winUsername = os.getlogin()

link = requests.get("https://pastebin.com/raw/GikAJyX1").content

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

def menu():
    global path
    logo()
    print(f"""{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}""")
    print(f"{Fore.RESET}[{Fore.CYAN}1{Fore.RESET}]{Fore.LIGHTBLACK_EX} Download at Desktop {Fore.RESET}")
    print(f"{Fore.RESET}[{Fore.CYAN}2{Fore.RESET}]{Fore.LIGHTBLACK_EX} Download at Documents {Fore.RESET}")
    print(f"{Fore.RESET}[{Fore.CYAN}3{Fore.RESET}]{Fore.LIGHTBLACK_EX} Download at Downloads {Fore.RESET}")
    print(f"{Fore.RESET}[{Fore.CYAN}X{Fore.RESET}]{Fore.RED} Exit")
    print(f"""{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}""")
    res = input(f'{Fore.CYAN}[PHANTOM]{Fore.WHITE} Select an option: ')
    if res == "1":
        path = f"{drive_letter}/Users/{winUsername}/Desktop"
        os.system('cls')
        logo()
        download()
    elif res == "2":
        path = f"{drive_letter}/Users/{winUsername}/Documents"
        os.system('cls')
        logo()
        download()
    elif res == "3":
        path = f"{drive_letter}/Users/{winUsername}/Downloads"
        os.system('cls')
        logo()
        download()
    elif res == "X":
        os._exit(0)

def login():
    logo()
    user = input(f'{Fore.CYAN}[PHANTOM]{Fore.WHITE} Username: ')
    password = input(f'{Fore.CYAN}[PHANTOM]{Fore.WHITE} Password: ')
    keyauthapp.login(user,password)
    os.system('cls')
    menu()

def download():
    print(f"""{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}""")
    print(f'{Fore.CYAN}[PHANTOM]{Fore.WHITE} Downloading latest version of Phantom at {path}')
    with open(f'{path}/Phantom.exe', 'wb') as f:
        f.write(requests.get(link).content)
    print(f'{Fore.CYAN}[PHANTOM]{Fore.WHITE} Phantom has been installed')
    time.sleep(3)
    os._exit(0)
        
login()