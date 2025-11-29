import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
from openai import OpenAI
import datetime
import json
import os

# -----------------------------
# 🔥 LOAD ENVIRONMENT VARIABLES
# -----------------------------
firebase_json_str = os.environ.get("FIREBASE_KEY")
firebase_db_url = os.environ.get("FIREBASE_DB_URL")
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Validate env vars
if not firebase_json_str:
    st.error("❌ FIREBASE_KEY not found in environment variables!")
if not firebase_db_url:
    st.error("❌ FIREBASE_DB_URL not found!")
if not openai_api_key:
    st.error("❌ OPENAI_API_KEY missing!")

# -----------------------------
# 🔥 FIREBASE INITIALIZATION
# -----------------------------
try:
    if not firebase_admin._apps:
        firebase_dict = json.loads(firebase_json_str)
        cred = credentials.Certificate(firebase_dict)

        firebase_admin.initialize_app(cred, {
            "databaseURL": firebase_db_url
        })

    content_ref = db.reference("/social_media_posts")

except Exception as e:
    st.error(f"🔥 Firebase initialization failed: {e}")

# -----------------------------
# 🔥 OPENAI SETUP
# -----------------------------
client = OpenAI(api_key=openai_api_key)

def generate_social_media_content(topic, platform, tone):
    prompt = f"""
    Generate a professional social media post.

    Platform: {platform}
    Tone: {tone}
    Topic: {topic}

    Include:
    - Catchy opening line
    - Main message
    - Call-to-action
    - 3 relevant hashtags
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# -----------------------------
# 🔥 SAVE TO FIREBASE
# -----------------------------
def save_to_firebase(topic, platform, tone, output):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_ref.push({
        "topic": topic,
        "platform": platform,
        "tone": tone,
        "content": output,
        "timestamp": now
    })

# -----------------------------
# 🔥 STREAMLIT UI
# -----------------------------
st.title("✨ AI Social Media Agent")
st.write("Generate high-quality social media posts for any platform.")

topic = st.text_input("Enter Topic")
platform = st.selectbox("Select Platform", ["Instagram", "Twitter", "LinkedIn", "Facebook", "YouTube"])
tone = st.selectbox("Choose Tone", ["Professional", "Friendly", "Motivational", "Informative", "Funny"])

if st.button("Generate Post"):
    if topic.strip() == "":
        st.error("Please enter a topic first!")
    else:
        with st.spinner("Generating AI content..."):
            output = generate_social_media_content(topic, platform, tone)

        st.success("Content Generated Successfully!")
        st.write("### ✨ Your AI Generated Post:")
        st.write(output)

        save_to_firebase(topic, platform, tone, output)
        st.info("Saved to Firebase Database!")

if st.checkbox("View Past Generated Posts"):
    data = content_ref.get()

    if data:
        st.subheader("🗂 Past Posts from Database")
        for key, value in data.items():
            st.write(f"**Topic:** {value['topic']}")
            st.write(f"**Platform:** {value['platform']}")
            st.write(f"**Tone:** {value['tone']}")
            st.write(f"**Content:** {value['content']}")
            st.write(f"**Time:** {value['timestamp']}")
            st.write("---")
    else:
        st.info("No previous posts found.")
