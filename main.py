
import os
import webbrowser
import smtplib
import pyjokes
import datetime
import speech_recognition as sr
import pyttsx3
import requests
import json

engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Speak Function
def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# Listen Function
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"You said: {command}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return command.lower()

# Send Email Function
def send_email(to, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your_email@gmail.com', 'your_password')  # Replace with valid email/password
    message = f'Subject: {subject}\n\n{content}'
    server.sendmail('your_email@gmail.com', to, message)
    server.quit()

# Weather Function
def get_weather():
    api_key = "3ab54a56e36ce3e623d48ae2746df1c6"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Hyderabad"
    complete_url = f"{base_url}appid={api_key}&q={city_name}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]["description"]
        temp = main["temp"]
        speak(f"The temperature in {city_name} is {temp} degrees Celsius with {weather}.")
    else:
        speak("City Not Found")

# File Search Function
def search_files():
    speak("What file are you looking for?")
    filename = take_command()
    search_path = "C:\\"  # Root directory
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            file_path = os.path.join(root, filename)
            speak(f"File found at {file_path}")
            print(file_path)
            return
    speak("File not found")

# Main function to handle command
def handle_command(command):
    if 'open notepad' in command:
        speak("Opening Notepad")
        os.system("notepad.exe")

    elif 'open calculator' in command:
        speak("Opening Calculator")
        os.system("calc.exe")

    elif 'open chrome' in command:
        speak("Opening Google Chrome")
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(chrome_path)

    elif 'open ms word' in command:
        speak("Opening Microsoft Word")
        word_path = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
        os.startfile(word_path)

    elif 'open spotify' in command:
        speak("Opening Spotify")
        spotify_path = r"C:\Users\admin\AppData\Roaming\Spotify\Spotify.exe"
        os.startfile(spotify_path)

    elif 'play youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif 'tell me a joke' in command:
        joke = pyjokes.get_joke()
        speak(joke)

    elif 'search for file' in command:
        search_files()

    elif 'weather' in command:
        get_weather()

    elif 'set alarm' in command:
        speak("Please tell me the time to set alarm in HH:MM format")
        alarm_time = take_command()
        speak(f"Alarm set for {alarm_time}")
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M")
            if current_time == alarm_time:
                speak("Wake up! Alarm time reached!")
                break

    elif 'send email' in command:
        speak("Who is the recipient?")
        to = take_command()
        speak("What is the subject?")
        subject = take_command()
        speak("What is the message?")
        message = take_command()
        try:
            send_email(to, subject, message)
            speak("Email sent successfully")
        except:
            speak("Failed to send email")

    elif 'exit' in command or 'quit' in command or 'goodbye' in command:
        speak("Goodbye! Assistant is shutting down.")
        exit()

    else:
        speak("Sorry, I didn't understand that command.")
    
# Main Program Loop
if __name__ == "__main__":
    while True:
        command = take_command()
        if command == "none":
            continue
        handle_command(command)