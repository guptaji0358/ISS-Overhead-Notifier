# Project - ISS Overhead Notifier
# --------------------------------

import requests
from datetime import datetime, UTC
import smtplib
import time

# ----------------------------
# YOUR DATA
# ----------------------------

#DONT Share With Anyone
user_gmail = "ENTER YOUR ACTIVE EMAIL"
user_password = "ENTER YOUR SPECIAL PASSWORD"

MY_LAT = 26.203725
MY_LONG = 78.157363

# ----------------------------
# CHECK ISS POSITION
# ----------------------------
def is_iss_overhead():
    print("\nChecking ISS position...")
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print("ISS Latitude:", iss_latitude)
    print("ISS Longitude:", iss_longitude)

    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True
    
    return False

# ----------------------------
# CHECK IF NIGHT
# ----------------------------
def is_night():
    print("Checking day/night...")
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        }
    
    response = requests.get("https://api.sunrise-sunset.org/json",
                            params=parameters)
    
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now(UTC).hour

    print("Sunrise (UTC):", sunrise)
    print("Sunset (UTC):", sunset)
    print("Current UTC hour:", time_now)

    if time_now >= sunset or time_now <= sunrise:
        return True
    return False

# ----------------------------
# SEND EMAIL
# ----------------------------
def send_email():
    print("Sending email...")
    with smtplib.SMTP("smtp.gmail.com", 587) as connect:
        connect.starttls()
        connect.login(user=user_gmail, password=user_password)
        connect.sendmail(from_addr=user_gmail,
                         to_addrs=user_gmail,
                         msg="Subject:Look Up!\n\nISS is above you in the sky!")
        
    print("Email sent!")


# ----------------------------
# MAIN LOOP
# ----------------------------
print("ISS Notifier Started...")

while True:
    time.sleep(20)
    iss = is_iss_overhead()
    night = is_night()

    print("ISS overhead:", iss)
    print("Is night:", night)
    if iss and night:
        send_email()