
import os
import time
import requests

def handle_command(command, speak):
    if "weather" in command:
        get_weather("Hyderabad", speak)
    elif "reminder" in command:
        speak("Setting a reminder for 10 seconds.")
        time.sleep(10)
        speak("Reminder! Time is up.")
    elif "open" in command and "notepad" in command:
        os.system("notepad")
    else:
        speak("Sorry, I didn't understand that.")

def get_weather(city, speak):
    api_key = "3ab54a56e36ce3e623d48ae2746df1c6"  # Replace with your real API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        data = requests.get(url).json()
        temp = data['main']['temp']
        speak(f"The temperature in {city} is {temp} degrees Celsius.")
    except:
        speak("Unable to fetch weather information.")
