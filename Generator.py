import colorama, os, random, string
from colorama import Fore

# made by xinj/lure, dont skid or sell this tool

def generate(len, user_amnt):
    f = open('usernames.txt', 'w')
    for i in range(user_amnt):
        str = "".join(random.choice(string.ascii_lowercase) for i in range(len) )
        f.write(str + '\n')
        str = ""
    input(f"[{Fore.GREEN}+{Fore.WHITE}] Done Generating! Press Enter to close.")
    exit()
def get_random_stringn(length):
    letters = string.ascii_lowercase
    numbers = string.digits
    result_str = ''.join(random.choice(letters + numbers) for i in range(length))
    return result_str
os.system('cls')
print(Fore.RED+"""
  ██████  ▄▄▄     ▓██   ██▓
▒██    ▒ ▒████▄    ▒██  ██▒
░ ▓██▄   ▒██  ▀█▄   ▒██ ██░
  ▒   ██▒░██▄▄▄▄██  ░ ▐██▓░
▒██████▒▒ ▓█   ▓██▒ ░ ██▒▓░
▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░  ██▒▒▒ 
░ ░▒  ░ ░  ▒   ▒▒ ░▓██ ░▒░ 
░  ░  ░    ░   ▒   ▒ ▒ ░░  
      ░        ░  ░░ ░     
                   ░                                                                                                                                                                                                                                                                 
[+] Discord: Lure#0001
[+] Instagram: xinj
[+] Server: discord.gg/lies
"""+Fore.WHITE)
gen_amnt = int(input(f"[{Fore.RED}?{Fore.WHITE}] How many letters?: "))
user_amnt = int(input(f"[{Fore.RED}?{Fore.WHITE}] How many usernames?: "))
print("")
generate(gen_amnt, user_amnt)
