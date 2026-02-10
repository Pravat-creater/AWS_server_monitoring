import os

def ping_server(host="8.8.8.8"):
    response = os.system(f"ping -c 1 {host}")
    if response == 0:
        return "Network OK"
    else:
        return "Network DOWN"

if name == "main":
    print(ping_server())