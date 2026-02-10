import os

def restart_service(service_name="apache2"):
    os.system(f"sudo systemctl restart {service_name}")
    print(f"🔧 Restarted service: {service_name}")

if name == "main":
    restart_service()