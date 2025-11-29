# 🎯 AI Social Media Agent — Text Post Generator
# ✨ AI Social Media Agent (Text Post Generator)

## 1. Overview
AI Social Media Agent generates professional social media text posts (Instagram, Twitter, LinkedIn, Facebook, YouTube) using an OpenAI model and saves posts to Firebase Realtime Database.

## 2. Features
- Generate platform-specific social media text posts
- Choose tone: Professional / Friendly / Motivational / Informative / Funny
- Save generated posts to Firebase Realtime Database
- View past generated posts from DB

## 3. Limitations
- Text-only (no video in this submission)
- Requires OpenAI API key and Firebase service account
- Realtime DB usage may be limited by Firebase rules & quotas

## 4. Tech stack & APIs
- Frontend: Streamlit (Python)
- AI: OpenAI API (gpt-4o-mini / chat completions)
- Database: Firebase Realtime Database via firebase-admin
- Hosting: Render (or Streamlit Cloud / Render)
- Environment: Python 3.11+

## 5. Project Structure
SocialMediaAgent/
├─ app.py
├─ requirements.txt
├─ README.md
├─ .gitignore
└─ assets/
## 6. Setup & Run Locally
1. Clone repo:
   ```bash
   git clone https://github.com/<your-username>/<repo>.git
   cd <repo>
Create virtual env & install:

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt


Create .env locally (do not commit) or set env vars:

OPENAI_API_KEY=sk-...
FIREBASE_DB_URL=https://your-project-id-default-rtdb.firebaseio.com/
FIREBASE_KEY=<single-line-json-service-account>


To generate single-line JSON: run python -c "import json; print(json.dumps(json.load(open('firebase_key.json'))))"

Run:

streamlit run app.py

7. Deploy to Render (quick)

Create Render Web Service, connect GitHub repo, use Build Command:

pip install -r requirements.txt


Start Command:

streamlit run app.py --server.port $PORT --server.enableCORS false


In Render dashboard add Environment Variables:

OPENAI_API_KEY = your key

FIREBASE_DB_URL = your DB URL

FIREBASE_KEY = single-line JSON string of your service account

8. Architecture (see architecture.md)

High level: Streamlit UI → OpenAI call → (optional) save to Firebase → Firebase Realtime DB stores posts.

9. Potential improvements

Add short vertical video generation (TTS + images + MoviePy)

Add authentication for users

Add multi-platform formatting & image attachments

Add analytics dashboard for generated post performance

