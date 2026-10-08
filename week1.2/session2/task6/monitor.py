# Week 1.2, Session 2: Task 6

temperature = int(input("What is the machine's temperature in degrees Celsius? "))
pressure = int(input("What is the machine's pressure in PSI? "))
operationalStatus = int(input("What is the machine's operational status? (1 for operating, 0 for stopped) "))

if temperature > 80:
    print("The temperature is too high. It is recommended to shut the machine down.")
elif temperature >= 50 and temperature <=80:
    print("The machine temperature is within safe limits.")
else:
    print("The machine temperature is low. No action is required.")

if pressure > 100:
    print("High pressure detected. Maintenance recommended.")
elif pressure >= 50 and pressure <=80:
    print("The machine pressure is stable")
else:
    print("The machine pressure is low. The system is operating normally")

if operationalStatus == 1 and (temperature > 80 or pressure > 100):
    print("The machine is running in unsafe conditions. It is recommend to shut it down.")
elif operationalStatus == 1:
    print("The machine is operating normally.")
else:
    print("The machine has stopped. No immediate action needed.")

actionsTaken = input("What actions were taken? ")

from datetime import datetime

with open("machine_log.txt","a") as f:
    f.write(f" \n Current time: {datetime.now()} ")
    f.write(f"The temperature is {temperature}\u00B0C. The pressure is {pressure} PSI. The operational status is {operationalStatus}. ")
    f.write(f"Actions taken: {actionsTaken}")

