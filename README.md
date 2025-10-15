# Jarvis AI Voice Assistant 🎙️🤖

Jarvis is a Python-based **AI desktop assistant** built as part of my MCA placement project.  
It can take voice commands, interact with web APIs, open applications, and assist with daily tasks.

---

## 🚀 Features
- 🎤 **Voice Interaction** (Speech Recognition + Text-to-Speech)
- ⏰ **Time & Date** announcements
- 🎵 **Play Music** from local folder
- 📖 **Wikipedia Search**
- 📧 **Send Email** (SMTP via Mailtrap)
- 🌦️ **Weather Updates** (OpenWeatherMap API)
- 📰 **Latest News Headlines** (NewsAPI)
- 😂 **Random Jokes** (JokeAPI)
- 💡 **Motivational Quotes** (Quotable API)
- 📚 **Dictionary** (Free Dictionary API)
- 🌐 **Open Websites** (Google, YouTube, Instagram, Facebook, ChatGPT)
- 🖥️ **Open System Apps** (Notepad, Calculator – Windows only)

---

## 🛠️ Tech Stack
- **Python 3**
- `speech_recognition` – Voice input
- `pyttsx3` – Text-to-Speech
- `requests` – API calls
- `wikipedia` – Knowledge lookup
- `dotenv` – Secure API keys
- `smtplib` – Email sending
- `logging` – Error logging

---

## 📂 Project Structure
Jarvis_Project/
│── jarvis.py # Main code
│── .env # API keys & credentials
│── requirements.txt # Dependencies
│── logs/jarvis.log # Log file
│── music_library/ # Songs folder
│── README.md # Documentation


🎯 Demo Commands

“What’s the time?”
“Tell me today’s date.”
“Play music.”
“Open YouTube.”
“Wikipedia Narendra Modi.”
“Send email.”
“Tell me a joke.”
“What’s the weather?”
“Give me news.”
“Meaning of technology.”
“Give me a quote.”
“Exit.”