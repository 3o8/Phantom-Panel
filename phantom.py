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
    print(f'''{Fore.CYAN}
                                                                                                    
                            ██████  ██   ██  █████  ███    ██ ████████  ██████  ███    ███ 
                            ██   ██ ██   ██ ██   ██ ████   ██    ██    ██    ██ ████  ████ 
                            ██████  ███████ ███████ ██ ██  ██    ██    ██    ██ ██ ████ ██ 
                            ██      ██   ██ ██   ██ ██  ██ ██    ██    ██    ██ ██  ██  ██ 
                            ██      ██   ██ ██   ██ ██   ████    ██     ██████  ██      ██ 
                                                                                                  
                                                                                                  
                                                                                                  
> Created by 444#9667                                                                             
> https://www.instagram.com/sander.reg/                                                                         
''')

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
    
def menuPremium():
    logo()
    print(f"""{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}
{Fore.RESET}[{Fore.CYAN}1{Fore.RESET}]{Fore.LIGHTBLACK_EX} Aimbot                                       |{Fore.RESET}[{Fore.CYAN}10{Fore.RESET}]{Fore.LIGHTBLACK_EX} Coming Soon!
{Fore.RESET}[{Fore.CYAN}2{Fore.RESET}]{Fore.LIGHTBLACK_EX} Aim Neck                                     |{Fore.RESET}[{Fore.CYAN}11{Fore.RESET}]{Fore.LIGHTBLACK_EX} Coming Soon!
{Fore.RESET}[{Fore.CYAN}3{Fore.RESET}]{Fore.LIGHTBLACK_EX} No Recoil                                    |{Fore.RESET}[{Fore.CYAN}12{Fore.RESET}]{Fore.LIGHTBLACK_EX} Disable No Recoil
{Fore.RESET}[{Fore.CYAN}4{Fore.RESET}]{Fore.LIGHTBLACK_EX} Aim FOV                                      |{Fore.RESET}[{Fore.CYAN}13{Fore.RESET}]{Fore.LIGHTBLACK_EX} Disable Aim FOV
{Fore.RESET}[{Fore.CYAN}5{Fore.RESET}]{Fore.LIGHTBLACK_EX} No yellow                                    |{Fore.RESET}[{Fore.CYAN}14{Fore.RESET}]{Fore.LIGHTBLACK_EX} Disable No yellow
{Fore.RESET}[{Fore.CYAN}6{Fore.RESET}]{Fore.LIGHTBLACK_EX} Antena                                       |{Fore.RESET}[{Fore.CYAN}15{Fore.RESET}]{Fore.LIGHTBLACK_EX} Disable Antena
{Fore.RESET}[{Fore.CYAN}7{Fore.RESET}]{Fore.LIGHTBLACK_EX} Silent Speed                                 |{Fore.RESET}[{Fore.CYAN}16{Fore.RESET}]{Fore.LIGHTBLACK_EX} Disable Speed
{Fore.RESET}[{Fore.CYAN}8{Fore.RESET}]{Fore.LIGHTBLACK_EX} Wall Climb                                   |{Fore.RESET}[{Fore.CYAN}17{Fore.RESET}]{Fore.LIGHTBLACK_EX} Disable Wall climb
{Fore.RESET}[{Fore.CYAN}9{Fore.RESET}]{Fore.LIGHTBLACK_EX} Emulator bypass                              |{Fore.RESET}[{Fore.CYAN}X{Fore.RESET}]{Fore.RED} Exit
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────""")
    res = input(f'{Fore.CYAN}[PHANTOM]{Fore.WHITE} Select an option: ')
    if res == "1":
        memory.ChangeMemory(codes.aim_pattern, codes.aimbot_patched, 9)
        menuPremium()
    elif res == "2":
        memory.ChangeMemory(codes.aim_pattern, codes.aimneck_patched, 9)
        menuPremium()
    elif res == "3":
        memory.ChangeMemory(codes.norecoil_pattern, codes.norecoil_patched, 4)
        menuPremium()
    elif res == "4":
        memory.ChangeMemory(codes.aimfov_pattern, codes.aimfov_patched, 8)
        menuPremium()
    elif res == "5":
        memory.ChangeMemory(codes.noyellow_pattern, codes.noyellow_patched, 16)
        menuPremium()
    elif res == "6":
        memory.ChangeMemory(codes.antena_pattern, codes.antena_patched, 8)
        menuPremium()
    elif res == "7":
        memory.ChangeMemory(codes.silentspeed_pattern, codes.silentspeed_patched, 12)
        menuPremium()
    elif res == "8":
        memory.ChangeMemory(codes.fly_pattern, codes.fly_patched, 24)
        menuPremium()
    elif res == "9":
        memory.ChangeMemory(codes.bypass_pattern, codes.bypass_patched, 20)
        menuPremium()
    elif res == "10":
        os.system('cls')
        print(f"{Fore.CYAN}[PHANTOM]{Fore.WHITE} Coming soon...")
        time.sleep(3)
        menuPremium()
    elif res == "11":
        os.system('cls')
        print(f"{Fore.CYAN}[PHANTOM]{Fore.WHITE} Coming soon...")
        time.sleep(3)
        menuPremium()
    elif res == "12":
        memory.ChangeMemory(codes.norecoil_patched, codes.norecoil_pattern, 4)
        menuPremium()
    elif res == "13":
        memory.ChangeMemory(codes.aimfov_patched, codes.aimfov_pattern, 4)
        menuPremium()
    elif res == "14":
        memory.ChangeMemory(codes.noyellow_patched, codes.noyellow_pattern, 16)
        menuPremium()
    elif res == "15":
        memory.ChangeMemory(codes.antena_patched, codes.antena_pattern, 8)
        menuPremium()
    elif res == "16":
        memory.ChangeMemory(codes.silentspeed_patched, codes.silentspeed_pattern, 12)
        menuPremium()
    elif res == "17":
        memory.ChangeMemory(codes.fly_patched, codes.fly_pattern, 24)
        menuPremium()
    elif res == "X":
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