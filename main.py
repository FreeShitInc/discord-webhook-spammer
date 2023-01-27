import requests,json,string,random,colorama
from time import sleep
from colorama import init
i = 0

init()

banner = f"""
{colorama.Fore.RED}███████╗██████╗ ███████╗███████╗███████╗██╗  ██╗██╗████████╗
{colorama.Fore.GREEN}██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║██║╚══██╔══╝  
{colorama.Fore.RED}█████╗  ██████╔╝█████╗  █████╗  ███████╗███████║██║   ██║      
{colorama.Fore.GREEN}██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ╚════██║██╔══██║██║   ██║    
{colorama.Fore.RED}██║     ██║  ██║███████╗███████╗███████║██║  ██║██║   ██║     
{colorama.Fore.GREEN}╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝ 
{colorama.Fore.RED}Created By FreeShit ║ Dev: segations#2344 ║ getfreeshit.today
{colorama.Fore.GREEN}
"""

print(banner)

Webhook = input("Webhook: ")
username = input(f"{colorama.Fore.GREEN}Username: ")
message = input(f"{colorama.Fore.RED}Message: ")
amount = input(f"{colorama.Fore.GREEN}Amount: ")

#############################################
headers = {'Content-Type':'application/json'}
#############################################



for x in range(int(amount)):

    RandUsername = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(6))
    
    payload = json.dumps({
        "username": username + "_" + RandUsername,
        "content": message 
    })
    
    i +=1
    
    r = requests.post(Webhook, headers=headers, data=payload)
    if r.status_code == 204:
        print(f"{colorama.Fore.GREEN}[✔️] Sent Message Successfully [✔️] - " + str(i))
    if r.status_code == 429:
        print(f"{colorama.Fore.RED}[❌] Discord Did a RateLimit [❌] - " + str(r.json()["retry_after"]))
        sleep(r.json()["retry_after"])
