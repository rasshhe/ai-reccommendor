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
st.set_page_config(page_title="AI Tool Recommender", layout="wide")

# --- UI Styling ---
st.markdown("""
    <style>
    body {
        background-color: #2e1f17;
        background-image: linear-gradient(145deg, #2e1f17 60%, #3b2a22 100%);
        font-family: 'Segoe UI', sans-serif;
    }
    .stApp {
        background-color: transparent;
    }
    h1 {
        text-align: center;
        color: #f5ede0;
        font-size: 3.8rem;
        letter-spacing: 1.2px;
        font-weight: bold;
    }
    h4 {
        text-align: center;
        color: #fcecd6;
        font-size: 1.5rem;
        margin-top: -1.2rem;
        font-weight: 400;
    }
   .stTextInput > label {
       font-size: 1.15rem;
        color: #fce3cc;
         font-weight: 600;
   }
   .stTextInput input {
       font-size: 1.1rem;
        padding: 0.6rem;
         border-radius: 10px;
         background-color: #fef6ec;   
         color: #3e2723;              
         border: 1px solid #d7ccc8;
    }

    .stButton > button {
        background-color: #a9746e;
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 10px;
        font-size: 1.1rem;
        padding: 0.5rem 1.5rem;
        margin-top: 10px;
    }
    .stButton > button:hover {
        background-color: #875a54;
    }
    .tool-section {
        background-color: #fef3e6;
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 0 20px rgba(100, 80, 60, 0.15);
    }
    .tool-section h5 {
        font-size: 1.5rem;
        color: #4e342e;
        margin-bottom: 1rem;
        font-weight: bold;
    }
    .tool-list {
        font-size: 1.15rem;
        line-height: 1.9;
        color: #3e2723;
        margin-left: 1rem;
    }
    hr {
        border: none;
        border-top: 1px solid #cbbfb5;
        margin: 20px 0;
    }
    .footer {
        text-align: center;
        font-size: 0.9rem;
        color: #d2bba0;
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1>AI Tool Recommender</h1>", unsafe_allow_html=True)
st.markdown("<h4>Find the perfect AI tool for your next task ✨</h4>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# --- Input Field ---
user_prompt = st.text_input("What do you want to accomplish?", placeholder="e.g., summarize a research paper")

# --- Tool Recommender Logic ---
if st.button("Find Recommendations"):
    if not user_prompt.strip():
        st.warning("⚠️ Please enter a task first.")
    else:
        category = classify_task(user_prompt)
        st.markdown("<hr>", unsafe_allow_html=True)

        if category and category in ai_db:
            st.markdown(f"<h5 style='color: #ffe0c0;'>🔍 Category Detected: <b>{category.title()}</b></h5>", unsafe_allow_html=True)

            st.markdown('<div class="tool-section">', unsafe_allow_html=True)

            st.markdown('<h5>🌟 Best AI Tools</h5>', unsafe_allow_html=True)
            st.markdown('<div class="tool-list">', unsafe_allow_html=True)
            for tool in ai_db[category]["best"]:
                st.markdown(f"- [{tool['name']}]({tool['url']})")
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<h5>👍 Middle AI Tools</h5>', unsafe_allow_html=True)
            st.markdown('<div class="tool-list">', unsafe_allow_html=True)
            for tool in ai_db[category]["middle"]:
                st.markdown(f"- [{tool['name']}]({tool['url']})")
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<h5>⚠️ Least Recommended</h5>', unsafe_allow_html=True)
            st.markdown('<div class="tool-list">', unsafe_allow_html=True)
            for tool in ai_db[category]["worst"]:
                st.markdown(f"- [{tool['name']}]({tool['url']})")
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.error("❌ Couldn't find a suitable category. Try rephrasing your task.")

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div class='footer'>Made with ☕ by Rashi Raj | Fall Theme Edition 🍂</div>", unsafe_allow_html=True)

