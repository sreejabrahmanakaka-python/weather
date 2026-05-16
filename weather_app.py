import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "ba79082864b5cf7a26acb0a2f72b7900"

def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showerror("Error", "Please enter a city name!")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", "City not found!")
            return

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        condition = data["weather"][0]["description"]

        result = f"""
City: {city}
Temperature: {temp}°C
Feels Like: {feels_like}°C
Humidity: {humidity}%
Wind Speed: {wind} m/s
Condition: {condition}
"""

        result_label.config(text=result)

    except:
        messagebox.showerror("Error", "Network issue!")

# ---- GUI Design ----
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")

title = tk.Label(root, text="Weather App", font=("Arial", 16))
title.pack(pady=10)

city_entry = tk.Entry(root, width=30, font=("Arial", 12))
city_entry.pack(pady=10)

search_btn = tk.Button(root, text="Get Weather", command=get_weather)
search_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11), justify="left")
result_label.pack(pady=20)

root.mainloop()