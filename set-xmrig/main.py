import os
import json
import time
import pip
from config import banner


# check import module
try:
    from progress.bar import ChargingBar
except ImportError:
    pip.main(['install', '--user', 'progress'])
    from progress.bar import ChargingBar

try:
    import requests
except ImportError:
    pip.main(['install', '--user', 'requests'])
    import requests
    
def runOffline():
    banner()
    try:
        with open("set-miner/online.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            pool = loads['pool']
            algo = loads['algo']
            wallet = loads['wallet']
            password = loads['pass']
        if pool == "" or wallet == "":
            print("\n\n\033[1;31;40mไม่พบการตั้งค่า หรือ การตั้งค่าไม่ถูกต้อง\nกรุณาตั้งค่าใหม่โดยใช้คำสั่ง edit-xmrig\033[0m\n\n")

        with open("set-miner/offline.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            name = loads['name']
            cpu = loads['cpu']
        if name == "":
           name = "noname"
        if cpu == "":
           cpu = "1"
        

        print("\033[1;32;40m")
        print("POOL   =",pool)
        print("ALGO   =",algo)
        print("WALLET =",wallet)
        print("NAME   =",name)
        print("PASS   =",password)
        print("CPU    =",cpu)
        print("\033[00m\n")

        # time.sleep(2)
        os.system(f"cd miner && cd xmrig && cd build && ./xmrig -a {algo} -o {pool} -u {wallet}.{name} -p {password} -t {cpu}")
    except:
        push = {'pool': '','algo': '','wallet': '','pass': ''}
        with open("set-miner/online.json", "w") as set:
            json.dump(push, set, indent=4)
        push = {'name': '','cpu': ''}
        with open("set-miner/offline.json", "w") as set:
            json.dump(push, set, indent=4)
        
        
        
        os.system("@cls||clear")
        print("\n\n\033[1;31;40mไม่พบการตั้งค่า หรือ การตั้งค่าไม่ถูกต้อง\nกรุณาตั้งค่าใหม่โดยใช้คำสั่ง edit-xmrig\033[0m\n\n")




while True:   
    os.system("@cls||clear")
    with ChargingBar("\033[33m Starting Your Miner\033[00m") as bar:
        for i in range(100):
            time.sleep(0.02)
            bar.next()
            
        runOffline()
        break
else:
        os.system("@cls||clear")
        print("\n\n\033[1;31;40mไม่พบการตั้งค่า กรุณาตั้งค่าโดยใช้คำสั่ง edit-xmrig\033[0m\n\n")
