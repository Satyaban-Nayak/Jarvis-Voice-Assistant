# 🤖 Jarvis – AI Desktop Voice Assistant 🎙️  

Jarvis is an AI-powered **desktop voice assistant** built using **Python**, capable of performing daily computer tasks, fetching real-time data, and interacting with users through natural speech.  

It combines **speech recognition**, **text-to-speech**, **API integration**, and **automation** to bring a personal assistant experience to your desktop.  

---

## 🚀 Features  

🗣️ **Voice Interaction** – Listens to your commands and responds intelligently  
🌦️ **Weather Updates** – Fetches live weather data using OpenWeather API  
📰 **News Headlines** – Reads the latest news from NewsAPI  
📚 **Knowledge Assistant** – Searches Wikipedia and provides dictionary meanings  
🎵 **Entertainment** – Plays local music, tells jokes, and shares motivational quotes  
📧 **Email Sender** – Sends emails securely using SMTP and `.env` credentials  
🪟 **Desktop Automation** – Opens system apps like Notepad & Calculator  
🌐 **Web Navigation** – Opens websites like YouTube, Google, Instagram, ChatGPT, etc.  
📊 **Logging System** – Maintains activity and error logs with rotating log files  

---

## 🧠 Tech Stack  

| Category | Technologies |
|-----------|--------------|
| **Language** | Python |
| **APIs Used** | OpenWeather API, NewsAPI, DictionaryAPI, Wikipedia API |
| **Libraries** | `speech_recognition`, `pyttsx3`, `requests`, `wikipedia`, `dotenv`, `smtplib`, `logging`, `webbrowser`, `datetime`, `os`, `random` |
| **Concepts** | Automation, Voice Recognition, NLP Basics, API Integration, Data Handling |

---

## ⚙️ Installation & Setup  

### 1️⃣ Clone the Repository 
```bash
git clone https://github.com/<your-username>/Jarvis-Voice-Assistant.git
cd Jarvis-Voice-Assistant
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Create a .env File
Add your API keys and credentials:
```bash
EMAIL_USER=your_email@example.com  
EMAIL_PASS=your_password  
SMTP_SERVER=sandbox.smtp.mailtrap.io  
SMTP_PORT=2525  
OPENWEATHER_API=your_openweather_api_key  
NEWS_API=your_news_api_key  
```
### 4️⃣ Prepare Your Music Folder
Create a folder named music_library in the project directory and add some .mp3 files.

### 5️⃣ Run the Assistant
```bash
python jarvis.py
```
---

## 🎯 Example Voice Commands

🕒 **“What’s the time?”**  
📅 **“What’s the date today?”**  
🌦️ **“What’s the weather in Bhubaneswar?”**  
📰 **“Tell me today’s news.”**  
📚 **“Search Python programming on Wikipedia.”**  
📧 **“Send email.”**  
🎵 **“Play music.”**  
🪟 **“Open Notepad.”**  
🔍 **“Open YouTube.”**  
😄 **“Tell me a joke.”**  
🗣️ **“Meaning of innovation.”**  
🛑 **“Exit” or “Stop”**  

---

## 🧠 Project Achievements

✅ Integrated multiple APIs to fetch, process, and present real-time data  
✅ Designed a modular architecture for easy expansion of commands  
✅ Implemented rotating logs for performance tracking  
✅ Combined data analytics, automation, and AI in one smart desktop tool  

---

## 💡 Future Enhancements

🚀 Add a GUI (Graphical User Interface) using tkinter or PyQt5  
🗣️ Integrate ChatGPT API for natural conversations  
🎧 Enable system-wide audio feedback  
📊 Add analytics dashboard for voice command usage  

---

## 🧑‍💻 Author

Satyaban Nayak  
🎓 MCA Student | 💡 Data Analytics & Python Enthusiast




 


