from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

API_KEY = "e949e8679b4bcfbe5da0a0fe3773c941"

def get_weather():
    city = city_entry.get().strip()

    if city == "":
        messagebox.showerror("Error", "Please enter a city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", "City not found")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        description = data["weather"][0]["description"].title()

        icon_code = data["weather"][0]["icon"]
        icon_url = f"https://openweathermap.org/img/wn/{icon_code}@4x.png"

        icon_response = requests.get(icon_url)
        icon_image = Image.open(BytesIO(icon_response.content))
        icon_photo = ImageTk.PhotoImage(icon_image)

        weather_icon.config(image=icon_photo)
        weather_icon.image = icon_photo

        city_label.config(text=city.title())

        result_label.config(
            text=f"{temp}°C\n\n"
                 f"{description}\n\n"
                 f"💧 Humidity: {humidity}%\n"
                 f"🌬 Wind: {wind} m/s"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))

root = Tk()
root.title("Weather App")
root.geometry("500x650")
root.resizable(False, False)
root.configure(bg="#121212")

title_label = Label(
    root,
    text="🌤 Weather App",
    font=("Segoe UI", 24, "bold"),
    bg="#121212",
    fg="white"
)
title_label.pack(pady=20)

city_entry = Entry(
    root,
    font=("Segoe UI", 14),
    width=25,
    justify="center",
    bd=0,
    bg="#1E1E1E",
    fg="white",
    insertbackground="white"
)
city_entry.pack(ipady=10, pady=10)

search_button = Button(
    root,
    text="Search",
    command=get_weather,
    font=("Segoe UI", 12, "bold"),
    bg="#00B4D8",
    fg="white",
    activebackground="#0096C7",
    relief="flat",
    cursor="hand2",
    padx=25,
    pady=8
)
search_button.pack(pady=15)

weather_icon = Label(
    root,
    bg="#121212"
)
weather_icon.pack(pady=10)

city_label = Label(
    root,
    text="",
    font=("Segoe UI", 20, "bold"),
    bg="#121212",
    fg="white"
)
city_label.pack()

result_label = Label(
    root,
    text="Enter a city and click Search",
    font=("Segoe UI", 14),
    bg="#121212",
    fg="#D9D9D9",
    justify="center"
)
result_label.pack(pady=25)

footer = Label(
    root,
    text="Powered by OpenWeatherMap",
    font=("Segoe UI", 9),
    bg="#121212",
    fg="gray"
)
footer.pack(side=BOTTOM, pady=10)

root.mainloop()
