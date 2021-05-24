"""
Web Responses

    1XX: Hold on
    2XX: Here U go   (good to go)
    3XX: Go away (u dont have permission...)
    4XX: You screwed Up (404: element not found)
    5XX: I screwed Up (server not responding)

"""

import requests
import json
from tkinter import *
import datetime as dt

'''Kanya says app'''

# def get_quote():
#     response = requests.get(url = 'https://api.kanye.rest/')
#     data = response.json()
#     canvas.itemconfig(quote_text, text = data['quote'])

# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)

# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)

# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)

# get_quote()

# window.mainloop()


'''ISS Position'''

MY_EMAIL = "___YOUR_EMAIL_HERE____"
MY_PASSWORD = "___YOUR_PASSWORD_HERE___"
my_lat = 19.075983
my_long = 72.877655

def is_iss_overhead()
    response = requests.get(url = 'http://api.open-notify.org/iss-now.json')
    data = response.json()

    iss_lat = float(data['iss_position']['latitude'])
    iss_long = float(data['iss_position']['longitude'])

    if my_lat <= iss_lat <= my_lat - 5 and my_long <= iss_long <= my_long - 5:
        return True

def is_night():
    parameters = {
        "lat": my_lat,
        "lng": my_long,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )
