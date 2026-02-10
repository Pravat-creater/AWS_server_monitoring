import datetime

def create_incident(issue):
    incident = {
        "id": datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
        "issue": issue,
        "severity": "P1",
        "status": "OPEN",
        "created_at": str(datetime.datetime.now())
    }

    with open("logs/incidents.txt", "a") as file:
        file.write(str(incident) + "\n")

    print("🚨 Incident Created:", incident)

if name == "main":
    create_incident("High CPU detected")