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
""")

def accinfo():
    print(Fore.CYAN + "Username: " + keyauthapp.user_data.username)
    print("HWID: " + keyauthapp.user_data.hwid)
    print("Subscription: " + keyauthapp.user_data.subscription)
    print("Expiry: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.expires)).strftime('%Y-%m-%d %H:%M:%S'))
    input(Fore.WHITE + "Press any key to go to the menu...")

def menuBypass():
    logo()
    print("""1. Bypass
2. Exit""" + Fore.WHITE)

    res = input(f'{Fore.CYAN}[PHANTOM]{Fore.WHITE} Select an option: ')

    if res == "1":
        memory.ChangeMemory(codes.bypass_pattern, codes.bypass_patched, 20)
        menuBypass()
    elif res == "2":
        os._exit(0)  

def combat():
    logo()
    print("""
1. AimBot
2. AimNeck
3. Aim FOV
4. Aim Lock
5. No recoil
X. Back to menu""")
    res = input(f'{Fore.CYAN}[PHANTOM]{Fore.WHITE} Select an option: ')
    if res == "1":
        memory.ChangeMemory(codes.aim_pattern, codes.aimbot_patched, 9)
        combat()
    elif res == "2":
        memory.ChangeMemory(codes.aim_pattern, codes.aimneck_patched, 9)
        combat()
    elif res == "3":
        memory.ChangeMemory(codes.aimfov_pattern, codes.aimfov_patched, 8)
        combat()
    elif res == "4":
        memory.ChangeMemory(codes.aimlock_pattern, codes.aimlock_patched, 8)
        combat()
    elif res == "5":
        memory.ChangeMemory(codes.norecoil_pattern, codes.norecoil_patched, 4)
        combat()
    elif res == "X":
        menuPremium()
    else:
        combat()

def visual():
    logo()
    print("""
1. Antena
2. No yellow
3. Silent Speed hack
4. Fly Hack
X. Back to menu""")
    res = input(f'{Fore.CYAN}[PHANTOM]{Fore.WHITE} Select an option: ')
    if res == "1":
        memory.ChangeMemory(codes.antena_pattern, codes.antena_patched, 8)
        visual()
    elif res == "2":
        memory.ChangeMemory(codes.noyellow_pattern, codes.noyellow_patched, 16)
        visual()
    elif res == "3":
        memory.ChangeMemory(codes.silentspeed_pattern, codes.silentspeed_patched, 12)
    elif res == "4":
        memory.ChangeMemory(codes.fly_pattern, codes.fly_patched, 24)
    elif res == "X":
        menuPremium()
    else:
        visual()

def utils():
    logo()
    print("""
1. Emulator bypass
2. Back to menu""")
    res = input(f'{Fore.CYAN}[PHANTOM]{Fore.WHITE} Select an option: ')
    if res == "1":
        memory.ChangeMemory(codes.bypass_pattern, codes.bypass_patched, 20)
        menuPremium()
    elif res == "X":
        menuPremium()
    else:
        utils()
    
def menuPremium():
    logo()
    print("""
1. Combat menu
2. Visual menu
3. Utils
4. Exit""")
    res = input(f'{Fore.CYAN}[PHANTOM]{Fore.WHITE} Select an option: ')
    if res == "1":
        combat()
    elif res == "2":
        visual()
    elif res == "3":
        utils()
    elif res == "4":
        os._exit(0)
    else:
        menuPremium()

def login():
    logo()
    user = input(f'{Fore.CYAN}[PHANTOM]{Fore.WHITE} Username: ')
    password = input(f'{Fore.CYAN}[PHANTOM]{Fore.WHITE} Password: ')
    keyauthapp.login(user,password)
    os.system('cls')
    logo()
    accinfo()
    if keyauthapp.user_data.subscription == "bypass":
        menuBypass()
    elif keyauthapp.user_data.subscription == "premium":
        menuPremium()
    
    
login()