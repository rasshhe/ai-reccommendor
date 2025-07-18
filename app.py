import streamlit as st
import json

# --- Load AI database from JSON ---
with open("ai_database.json") as f:
    ai_db = json.load(f)

# --- Classifier function ---
def classify_task(prompt):
    prompt = prompt.lower()
    if "email" in prompt:
        return "email writing"
    if "essay" in prompt or "blog" in prompt:
        return "essay/blog writing"
    if "image" in prompt or "photo" in prompt or "art" in prompt:
        return "image generation"
    if "video" in prompt:
        return "video generation"
    if "audio" in prompt or "music" in prompt:
        return "audio/music"
    if "voice" in prompt:
        return "voice generation"
    if "code" in prompt and ("generate" in prompt or "write" in prompt):
        return "code generation"
    if "debug" in prompt or "fix" in prompt:
        return "debugging code"
    if "research" in prompt or "question" in prompt:
        return "research/q&a"
    if "presentation" in prompt or "slides" in prompt:
        return "presentation/slides"
    return None

# --- Streamlit Page Setup ---
st.set_page_config(page_title="AI Tool Recommender", layout="centered")

# --- Custom CSS for Pastel Theme ---
st.markdown("""
    <style>
    .stApp {
        background-color: #f3e8ff;  /* lavender pastel */
        font-family: 'Segoe UI', sans-serif;
    }
    h1 {
        text-align: center;
        color: #3c2a4d;
        font-size: 3rem;
    }
    h4 {
        text-align: center;
        color: #5c5470;
        font-size: 1.3rem;
        margin-top: -1rem;
    }
    .stTextInput>label {
        font-size: 1.1rem;
        color: #4a3a5a;
        font-weight: 600;
    }
    .stTextInput input {
        font-size: 1.1rem;
        padding: 0.5rem;
    }
    .stButton>button {
        background-color: #cdaefc;
        color: #2d1e40;
        border: none;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.5rem 1.5rem;
        font-size: 1.05rem;
    }
    .stButton>button:hover {
        background-color: #b999f5;
    }
    .recommendation-section h5 {
        color: #3a2d4e;
        font-size: 1.2rem;
        margin-bottom: 0.3rem;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1>AI Tool Recommender</h1>", unsafe_allow_html=True)
st.markdown("<h4>Suggesting the best AI tools based on your task 💡</h4>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# --- Input Field ---
user_prompt = st.text_input("What do you want to accomplish?", placeholder="e.g., write a blog about AI safety")

# --- Logic & Display ---
if st.button("Find Recommendations"):
    if not user_prompt.strip():
        st.warning("⚠️ Please enter a task first.")
    else:
        category = classify_task(user_prompt)
        st.markdown("<hr>", unsafe_allow_html=True)

        if category and category in ai_db:
            st.markdown(f"<h5>🔍 Category Detected: <b>{category.title()}</b></h5>", unsafe_allow_html=True)

            # Best tools
            st.markdown("#### 🌟 Best AI Tools")
            for tool in ai_db[category]["best"]:
                st.markdown(f"- [{tool['name']}]({tool['url']})")

            # Middle tools
            st.markdown("#### 👍 Middle AI Tools")
            for tool in ai_db[category]["middle"]:
                st.markdown(f"- [{tool['name']}]({tool['url']})")

            # Worst tools
            st.markdown("#### ⚠️ Least Recommended")
            for tool in ai_db[category]["worst"]:
                st.markdown(f"- [{tool['name']}]({tool['url']})")

        else:
            st.error("❌ Couldn't find a suitable category. Try rephrasing your task.")

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 13px; color: #888;'>Built by Rashi Raj | Streamlit Deployment</p>",
    unsafe_allow_html=True
)
