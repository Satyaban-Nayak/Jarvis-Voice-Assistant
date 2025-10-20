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

| Category | Achievement |
|----------|-------------|
|**Core AI Interaction**|🎤 **Robust Voice Interface**: Implemented a full Speech-to-Text (STT) to Text-to-Speech (TTS) pipeline using `speech_recognition` and `pyttsx3`, enabling seamless, bi-directional voice interaction.|
|**System & Desktop Control**|💻 **Desktop Automation**: Developed core functions to interact with the local operating system, including launching native Windows applications (`notepad.exe`, `calc.exe`) and playing local music files.|
|**API & Web Integration**|🌐 **Multi-API Integration**: Successfully integrated and handled requests from four different external APIs (`OpenWeatherMap`, `NewsAPI`, `JokeAPI`, `Quotable.io`) to fetch real-time and dynamic information.|
|**Modular Design**|🧩 **Extensible Command System**: Utilized a Python dictionary (`self.commands`) to map voice keywords to specific functions, allowing for easy extension and maintenance of new commands ("skills").|
|**Professional Practices**|🛡️ **Secure Credential Handling**: Implemented `.env` file management using `python-dotenv` to securely load API keys and credentials, preventing hard-coding in the source code.|
|**Error Handling & Logging**|📝 **Comprehensive Logging**: Integrated the logging module with a Rotating File Handler to record system events, user commands, and errors (including API and speech failures), ensuring robust debugging and performance monitoring.|


---

## 💡 Future Enhancements

🚀 **Add Graphical User Interface (GUI)** —  
Integrate a simple GUI using **Tkinter** or **PyQt5** to control Jarvis visually, view logs, and trigger voice commands easily. 

🎤 **Add Custom Wake Word Detection** —   
Implement a wake phrase like **“Hey Jarvis”** to start listening automatically instead of continuous listening. 

💌 **Add Smart Email Contact Book** —  
Save and manage frequently used email contacts in a **JSON or CSV file**, so Jarvis can send mails by name (e.g., “Send email to Riya”). 

🌦️ **Add Dynamic City Detection for Weather** —  
Use **geolocation APIs** to automatically detect the user's city for weather updates without mentioning it manually.

---

## 🧑‍💻 Author

Satyaban Nayak  
🎓 MCA Student | 💡 Data Analytics & Python Enthusiast




 


