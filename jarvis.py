
# ==============================
# IMPORT REQUIRED LIBRARIES
# ==============================
import speech_recognition as sr  # For speech recognition
import pyttsx3  # For text-to-speech
import webbrowser  # To open websites
import datetime  # For date and time
import os  # For file and system operations
import wikipedia  # To fetch summaries from Wikipedia
import smtplib  # For sending emails
import random  # For random selections (jokes, songs)
import sys  # System-specific parameters and functions
import logging  # For logging events and errors
from logging.handlers import RotatingFileHandler  # To limit log file size
import requests  # For API requests
from dotenv import load_dotenv  # To load environment variables

# ==============================
# LOAD ENVIRONMENT VARIABLES
# ==============================
load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
SMTP_SERVER = os.getenv("SMTP_SERVER", "sandbox.smtp.mailtrap.io")
SMTP_PORT = int(os.getenv("SMTP_PORT", 2525))
OPENWEATHER_API = os.getenv("OPENWEATHER_API")
NEWS_API = os.getenv("NEWS_API")

# ==============================
# SETUP LOGGING
# ==============================


handler = RotatingFileHandler("logs/jarvis.log", maxBytes=500_000, backupCount=3)
logging.basicConfig(
    handlers=[handler],
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Jarvis started successfully.")

# ==============================
# JARVIS CLASS
# ==============================
class Jarvis:
    def __init__(self):
        # Initialize speech recognizer
        self.recognizer = sr.Recognizer()

        # Map user commands to functions for easy extension
        self.commands = {
            "time": self.tell_time,
            "date": self.tell_date,
            "play music": self.play_music,
            "wikipedia": self.search_wikipedia,
            "joke": self.tell_joke,
            "quote": self.tell_quote,
            "weather": self.get_weather,
            "news": self.get_news,
            "meaning of": self.dictionary,
            "send email": self.prepare_email,
            # Windows applications
            "open notepad": lambda: self.open_app("notepad.exe"),
            "open calculator": lambda: self.open_app("calc.exe"),
            # Websites
            "open youtube": lambda: webbrowser.open("https://youtube.com"),
            "open google": lambda: webbrowser.open("https://google.com"),
            "open instagram": lambda: webbrowser.open("https://instagram.com"),
            "open facebook": lambda: webbrowser.open("https://facebook.com"),
            "open chatgpt": lambda: webbrowser.open("https://chatgpt.com"),
        }

    # ==============================
    # SPEECH OUTPUT
    # ==============================
    def speak(self, text):
        """Speak out text using pyttsx3 and also log it"""
        print(f"Jarvis: {text}")
        logging.info(f"Jarvis says: {text}")
        try:
            engine = pyttsx3.init("sapi5")
            engine.setProperty("rate", 150)  # Speech speed
            voices = engine.getProperty("voices")
            if voices:
                engine.setProperty("voice", voices[0].id)  # Set voice
            engine.say(text)
            engine.runAndWait()
            engine.stop()
        except Exception as e:
            logging.error(f"Speech error: {e}")

    # ==============================
    # LISTEN TO USER
    # ==============================
    def listen(self, timeout=5, phrase_time_limit=7):
        """Listen to microphone and return recognized text"""
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.7)
            print("Listening...")
            try:
                audio = self.recognizer.listen(
                    source, timeout=timeout, phrase_time_limit=phrase_time_limit
                )
                query = self.recognizer.recognize_google(audio, language="en-in")
                print(f"User: {query}")
                logging.info(f"User said: {query}")
                return query.lower()
            except sr.UnknownValueError:
                return "none"
            except Exception as e:
                logging.error(f"Listening error: {e}")
                return "none"

    # ==============================
    # HELPER: API FETCH
    # ==============================
    def fetch_api(self, url, headers=None, timeout=8):
        """Make safe API requests with logging"""
        try:
            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"API error for {url}: {e}")
            return None

    # ==============================
    # BASIC FUNCTIONS
    # ==============================
    def tell_time(self):
        """Tell the current time"""
        time_str = datetime.datetime.now().strftime("%H:%M:%S")
        self.speak(f"The time is {time_str}")

    def tell_date(self):
        """Tell the current date"""
        date_str = datetime.datetime.now().strftime("%d %B %Y")
        self.speak(f"Today's date is {date_str}")

    # ==============================
    # MUSIC FUNCTION
    # ==============================
    def play_music(self):
        """Play a random music file from 'music_library' folder"""
        music_dir = "music_library"
        try:
            songs = os.listdir(music_dir)
            if songs:
                song = random.choice(songs)
                os.startfile(os.path.join(music_dir, song))
                self.speak(f"Playing {song}")
            else:
                self.speak("No songs found in your music folder.")
        except Exception as e:
            logging.error(f"Music error: {e}")
            self.speak("Unable to play music. Please check the folder path.")

    # ==============================
    # EMAIL FUNCTION
    # ==============================
    def send_email(self, to, content):
        """Send email via SMTP"""
        if not EMAIL_USER or not EMAIL_PASS:
            self.speak("Email credentials are missing in .env file.")
            return
        try:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            message = f"Subject: Jarvis Mail\n\n{content}"
            server.sendmail(EMAIL_USER, to, message)
            server.quit()
            self.speak("Email sent successfully.")
        except Exception as e:
            logging.error(f"Email error: {e}")
            self.speak("I couldn’t send the email. Please check SMTP settings.")

    # ==============================
    # WIKIPEDIA SEARCH
    # ==============================
    def search_wikipedia(self, query):
        """Search Wikipedia and speak a short summary"""
        topic = query.replace("wikipedia", "").strip()
        self.speak(f"Searching Wikipedia for {topic}")
        try:
            summary = wikipedia.summary(topic, sentences=2)
            self.speak(summary)
        except Exception:
            self.speak("Sorry, I could not find that on Wikipedia.")

    # ==============================
    # JOKES AND QUOTES
    # ==============================
    def tell_joke(self):
        """Fetch a random joke from API or fallback list"""
        data = self.fetch_api("https://v2.jokeapi.dev/joke/Any")
        if data and "type" in data:
            if data["type"] == "single":
                self.speak(data["joke"])
            else:
                self.speak(f"{data['setup']} ... {data['delivery']}")
        else:
            fallback_jokes = [
                "Why don't programmers like nature? It has too many bugs.",
                "Why did the computer go to the doctor? Because it caught a virus."
            ]
            self.speak(random.choice(fallback_jokes))

    def tell_quote(self):
        """Fetch a random quote from API or fallback list"""
        data = self.fetch_api("https://api.quotable.io/random")
        if data and "content" in data:
            self.speak(f"Here’s a quote: {data['content']} — by {data['author']}")
        else:
            fallback_quotes = [
                "The future depends on what you do today. — Mahatma Gandhi",
                "Success is not final, failure is not fatal. — Winston Churchill",
                "Believe you can and you're halfway there. — Theodore Roosevelt",
                "Dream big and dare to fail. — Norman Vaughan"
            ]
            self.speak(random.choice(fallback_quotes))

    # ==============================
    # WEATHER FUNCTION
    # ==============================
    def get_weather(self, command=None):
        """Get weather info for a given city"""
        if not OPENWEATHER_API:
            self.speak("Weather API key is missing in .env.")
            return
        city = "Bhubaneswar"  # Default city
        if command and "weather in" in command:
            city = command.split("weather in")[-1].strip()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API}&units=metric"
        data = self.fetch_api(url)
        if data and "main" in data:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            self.speak(f"The weather in {city} is {desc} with {temp} degrees Celsius.")
            logging.info(f"Weather fetched for {city}: {desc}, {temp}°C")
        else:
            self.speak("Unable to fetch weather right now.")
            logging.error(f"Weather fetch failed for {city}")

    # ==============================
    # NEWS FUNCTION
    # ==============================
    def get_news(self):
        """Fetch top news headlines"""
        if not NEWS_API:
            self.speak("News API key is missing in .env.")
            return
        url = f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={NEWS_API}"
        data = self.fetch_api(url)
        if data and data.get("articles"):
            self.speak("Here are the top news headlines:")
            for article in data["articles"][:5]:
                self.speak(article.get("title", ""))
        else:
            self.speak("No news available right now.")

    # ==============================
    # DICTIONARY FUNCTION
    # ==============================
    def dictionary(self, word):
        """Get the meaning of a word"""
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.strip()}"
        data = self.fetch_api(url)
        if data and isinstance(data, list):
            meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
            self.speak(f"The meaning of {word} is: {meaning}")
        else:
            self.speak(f"Sorry, I couldn't find the meaning of {word}.")

    # ==============================
    # OPEN WINDOWS APPLICATION
    # ==============================
    def open_app(self, app_name):
        """Open a Windows app like Notepad or Calculator"""
        if sys.platform == "win32":
            os.system(app_name)
        else:
            self.speak("This command is only supported on Windows.")

    # ==============================
    # EMAIL PREPARATION
    # ==============================
    def prepare_email(self, *_):
        """Listen for email content and send it"""
        self.speak("What should I say?")
        content = self.listen()
        if content != "none":
            self.send_email("test@example.com", content)

    # ==============================
    # MAIN RUN LOOP
    # ==============================
    def run(self):
        """Start Jarvis assistant and keep listening for commands"""
        self.speak("I am on. What can I do for you?")
        while True:
            command = self.listen()
            if command == "none":
                continue

            # Exit condition
            if "exit" in command or "stop" in command:
                self.speak("Goodbye!")
                logging.info("Jarvis exited by user command.")
                break

            # Check if the command matches any predefined commands
            handled = False
            for key, func in self.commands.items():
                if key in command:
                    if key == "meaning of":
                        word = command.replace("meaning of", "").strip()
                        func(word)
                    elif key == "wikipedia":
                        func(command)
                    elif key == "weather":
                        func(command)  # Pass command for dynamic city
                    else:
                        func()
                    handled = True
                    break

            # If command not recognized, search on Google
            if not handled:
                self.speak("I can search that on Google.")
                webbrowser.open("https://www.google.com/search?q=" + command.replace(" ", "+"))
                logging.info(f"Command not recognized, searched Google: {command}")


# ==============================
# RUN JARVIS
# ==============================
if __name__ == "__main__":
    assistant = Jarvis()
    assistant.run()
