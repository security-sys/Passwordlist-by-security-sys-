import readline
from colorama import Fore
print(Fore.CYAN + "credits to me")
print(Fore.GREEN + "telegram https://t.me/py66666")


# dont misuse this use it for educational purposes only


word = input("show wordlist? Y-N:")
if word == "Y": 
 f = open("Passwordlist.txt", "r")
 print(f.read())
elif word == "N":
  print(Fore.RED + "exiting")


#yeah kinda shit code but i will improve soon