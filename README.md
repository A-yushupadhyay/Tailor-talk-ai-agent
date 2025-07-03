# 🤖 TailorTalk AI Calendar Agent

An intelligent AI-powered scheduling assistant built with FastAPI, Google Calendar API, and Gemini LLM — deployed fully on Render and Streamlit Cloud.

> Built for the TailorTalk.ai internship assignment 🚀

![Screenshot (350)](https://github.com/user-attachments/assets/a713abbe-044a-4290-8e7c-7ad77f12f6da)


![Screenshot (351)](https://github.com/user-attachments/assets/20c484c0-0a91-466f-8754-40c36f23a650)


![Screenshot (352)](https://github.com/user-attachments/assets/b64f7612-47d4-4fa1-9527-674a9be95ab5)


![Screenshot (358)](https://github.com/user-attachments/assets/cfbad9b5-7f0e-4933-a048-0b3ba0628e1e)





---

## 🌐 Live Demo

🔗 **Frontend (Streamlit App):** [👉 Launch TailorTalk Assistant](https://tailor-talk-ai-agent-k7tdj9t4sdnlsvudgxzoer.streamlit.app/)  
🔗 **Backend (FastAPI on Render):** [👉 API Endpoint](https://tailor-talk-ai-agent.onrender.com)

---

## 🧠 Features

- 🗓️ Check Google Calendar availability for any date (`today`, `tomorrow`, or `YYYY-MM-DD`)
- 📅 Book slots dynamically with natural language (e.g. “Book a 3PM meeting tomorrow for onboarding”)
- 🤖 Gemini-powered fallback for natural responses
- ⚙️ Fully serverless deployment with secure env variables
- 🌍 Clean Streamlit-based chat UI

---

## 💡 Sample Queries

```txt
Check availability on 2025-07-10  
Book a meeting today at 3PM for onboarding  
Schedule a call tomorrow at 10AM for demo  
What is TailorTalk and why is it interesting?  
Tell me something motivational  
```

🛠️ Tech Stack
Layer       ->	Tech
Frontend	  ->  Streamlit
Backend	    ->  FastAPI + Uvicorn
AI Model	  ->  Gemini Pro (via google-generativeai)
Calendar API->  Google Calendar (OAuth service account)
Agent Logic	->  LangChain (light) + custom tools
Hosting	    ->  Render (backend), Streamlit Cloud (UI)

🔐 Environment Variables (Set on Render)
```
GOOGLE_CREDS_BASE64=<base64-encoded service account JSON>
GOOGLE_API_KEY=<your Gemini API Key>
🚀 How to Run Locally
Clone the repo:


git clone https://github.com/A-yushupadhyay/Tailor-talk-ai-agent
cd Tailor-talk-ai-agent
Set up your virtual environment and install:


pip install -r backend/requirements.txt
Create a .env file in /backend with:


GOOGLE_API_KEY=your_gemini_api_key
GOOGLE_CREDS_BASE64=your_base64_service_json
Run backend:

cd backend
uvicorn main:app --reload
Run frontend:


streamlit run frontend/app.py


```
🙋‍♂️ Author
Ayush Upadhyay
Phone no - 9616180577
Email: puskaru202@gmail.com
Built with ❤️ for TailorTalk.ai Internship Assignment
