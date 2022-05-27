import pymem
import pymem.process
import pymem.pattern
import pymem.memory
import pymem.ressources.kernel32
import pymem.ressources.structure
import os
import time
import hashlib
import memory
import codes

from datetime import datetime
from colorama import Fore
from auth import api

def getchecksum():
    time.sleep(0)

keyauthapp = api(
    name = "PhantomClient",
    ownerid = "dhtmNBRSrd",
    secret = "cea7edec4d73abf8c15821c0b6ac5fa8b165a567e3ff0564164d92fe8d38b15c",
    version = "1.0",
    hash_to_check = getchecksum()
)

def clear():
    os.system('cls')

def logo():
    clear()
    print(Fore.CYAN + """╔═╗╦ ╦╔═╗╔╗╔╔╦╗╔═╗╔╦╗
╠═╝╠═╣╠═╣║║║ ║ ║ ║║║║
╩  ╩ ╩╩ ╩╝╚╝ ╩ ╚═╝╩ ╩
Created by @sander.reg
""" + Fore.WHITE)

def accinfo():
    print(Fore.CYAN + "Username: " + keyauthapp.user_data.username)
    print("HWID: " + keyauthapp.user_data.hwid)
    print("Expiry: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.expires)).strftime('%Y-%m-%d %H:%M:%S'))
    print("                                 ")

def menu():
    logo()
    accinfo()
    print("""1. Bypass
2. Exit""" + Fore.WHITE)

    res = input(f'{Fore.CYAN}[PHANTOM]{Fore.WHITE} Select an option: ')

    if res == "1":
        memory.ChangeMemory(codes.bypass_pattern, codes.bypass_patched, 20)
        menu()
    elif res == "2":
        os._exit(0)  
        

def login():
    logo()
    user = input(f'{Fore.CYAN}[PHANTOM]{Fore.WHITE} Username: ')
    password = input(f'{Fore.CYAN}[PHANTOM]{Fore.WHITE} Password: ')
    keyauthapp.login(user,password)
    menu()
    
    
login()