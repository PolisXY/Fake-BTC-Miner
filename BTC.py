from colorama import Fore
import time
import secrets
from random import randint
import os

os.system("mode con cols=92 lines=52")
os.system("title " + f"Wallet Miner || PolisXY || Total mined: 0.00 BTC")

btcval = 22830.411
total_btc_mined = {}

while True:
    os.system("cls")
    print(Fore.YELLOW + "Wallet Miner || PolisXY")
    print(Fore.WHITE + "Total mined:")
    for wallet, btc in total_btc_mined.items():
        print(f"{wallet}: {btc:.2f} BTC (${btc * btcval:,.2f})")
    print("\n================= MENU =================")
    print("1. Start mining")
    print("2. Exit\n")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        wallet_address = input("\nEnter your wallet address: ")
        print("\n" + Fore.WHITE + "> " "["+ Fore.GREEN +"+"+ Fore.WHITE +"] Validating wallet address...")
        time.sleep(2)
        print("\n[INFO] Starting mining to wallet address:", wallet_address, "\n")
        time.sleep(2)
        
        
        while True:
            time.sleep(.01)
            ranInt = randint(0, 2500)
            if ranInt <= 1:
                randomBTC = randint(1,100)/100
                if wallet_address in total_btc_mined:
                    total_btc_mined[wallet_address] += randomBTC
                else:
                    total_btc_mined[wallet_address] = randomBTC
                total_mined_btc = sum(total_btc_mined.values())
                os.system("title " + f"Wallet Miner || PolisXY || Total mined: {total_mined_btc:.2f} BTC")
                print(Fore.WHITE + "> ["+ Fore.GREEN +"+"+ Fore.WHITE +"] " "0x"+ secrets.token_hex(20) + " > " +  Fore.WHITE + str(randomBTC) + Fore.GREEN + " BTC" + Fore.WHITE + "("+ Fore.GREEN +"$" + str("{:,}".format(round(btcval*randomBTC,2))) + Fore.WHITE + ") to " + wallet_address)

                answer = None
                for i in range(10, 0, -1):
                    print(Fore.BLUE + f">> Continue in {i} seconds... (Y/N)", end="\r")
                    time.sleep(2)
                    if i == 1:
                        print("\r", " "*50, end="\r")
                answer = input("\r> Would you like to continue? (Y/N) [10]: ").strip().lower()
                if answer == "":
                    answer = "y"
                    time.sleep(5)
                
                if answer == "n":
                    print("\n[INFO] Stopping mining...\n")
                    break
                elif answer != "y":
                    print("\n[ERROR] Invalid choice, please try again.\n")
                    continue
                else:
                    print("\n[INFO] Resuming mining...\n")
            else:
                print(Fore.WHITE + "> ["+ Fore.RED +"?"+ Fore.WHITE +"] " "0x"+ secrets.token_hex(20) + " > "+ Fore.WHITE +"0.00 "+ Fore.RED + "BTC" +Fore.WHITE+ "("+ Fore.RED +"$0.00"+ Fore.WHITE +")")
    
    elif choice == "2":
        print("\n[INFO] Exiting program...\n")
        break
    
    else:
        print("\n[ERROR] Invalid choice, please try again.\n")
