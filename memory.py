import pymem
import pymem.process
import pymem.pattern
import pymem.memory
import pymem.ressources.kernel32
import pymem.ressources.structure
import time
import os

from colorama import Fore

def pattern_scan_all(handle, pattern, *, return_multiple=False):
    next_region = 0
    found = []
    while next_region < 0x7FFFFFFF0000:
        next_region, page_found = pymem.pattern.scan_pattern_page(
            handle,
            next_region,
            pattern,
            return_multiple=return_multiple
        )
        if not return_multiple and page_found:
            return page_found
        if page_found:
            found += page_found
    if not return_multiple:
        return None
    return found

def ChangeMemory(pattern, patched, count):
    try:
        pm = pymem.Pymem("HD-Player.exe")
        os.system('cls')
        print(f"{Fore.CYAN}[PHANTOM]{Fore.WHITE} Applying...")
        results = pattern_scan_all(pm.process_handle, pattern, return_multiple=True)
    except:
        print("Scan failed, Please running this when you are in game not lauching the game! try again")
        time.sleep(3)
        os._exit(0)
    isFound = False
    gotPatched = True

    if results :
        gotPatched = False
        isFound = True

    if isFound and not gotPatched :
        for addr in results:
            pymem.memory.write_bytes(pm.process_handle, addr, patched, count)
        gotPatched = True
        print(f"{Fore.CYAN}[PHANTOM]{Fore.WHITE} Applied")
        time.sleep(1)