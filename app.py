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

# --- Custom Pastel CSS Styling ---
st.markdown("""
    <style>
    body {
        background-color: #fdf6f0;
        font-family: 'Segoe UI', sans-serif;
    }
    .stApp {
        background-color: #fdf6f0;
        padding: 2rem;
    }
    h1 {
        text-align: center;
        color: #5c5470;
        font-size: 2.8rem;
        margin-bottom: 0.5rem;
    }
    h4 {
        text-align: center;
        color: #998eac;
        font-size: 1.1rem;
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
    }
    .stTextInput > label {
        font-weight: 500;
        color: #4b3c58;
    }
    .stButton > button {
        background-color: #d7c0d0;
        color: #4b3c58;
        border: none;
        padding: 0.5rem 1.5rem;
        border-radius: 10px;
        font-weight: 600;
    }
    .stButton > button:hover {
        background-color: #c5adc5;
    }
    hr {
        margin-top: 1rem;
        margin-bottom: 1.5rem;
        border: none;
        border-top: 1px solid #ddd;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title and Description ---
st.markdown("<h1>AI Tool Recommender</h1>", unsafe_allow_html=True)
st.markdown("<h4>Find the best AI tools based on your task</h4>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# --- Input Field ---
user_prompt = st.text_input("What do you want to accomplish?", placeholder="e.g., generate an image of a mountain landscape")

# --- Recommendation Logic ---
if st.button("Find Recommendations"):
    if not user_prompt.strip():
        st.warning("Please enter a task to receive AI tool recommendations.")
    else:
        category = classify_task(user_prompt)
        st.markdown("<hr>", unsafe_allow_html=True)

        if category and category in ai_db:
            st.markdown(f"<h4 style='color: #4b3c58;'>Category detected: {category.title()}</h4>", unsafe_allow_html=True)

            st.markdown("#### Top Recommendations")
            for tool in ai_db[category]["best"]:
                st.markdown(f"- [{tool['name']}]({tool['url']})")

            st.markdown("#### Other Options")
            for tool in ai_db[category]["middle"]:
                st.markdown(f"- [{tool['name']}]({tool['url']})")

            st.markdown("#### Least Recommended")
            for tool in ai_db[category]["worst"]:
                st.markdown(f"- [{tool['name']}]({tool['url']})")

        else:
            st.error("No matching category found. Try rephrasing your task.")

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 13px; color: #a8a3b0;'>Built by Rashi Raj | Streamlit Deployment</p>",
    unsafe_allow_html=True
)
