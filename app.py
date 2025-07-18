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

# --- CSS for brown-beige aesthetic ---
st.markdown("""
    <style>
    body {
        background-color: #fdf5e6;
        font-family: 'Segoe UI', sans-serif;
    }
    .stApp {
        background-color: #fdf5e6;
    }
    h1 {
        color: #4e342e;
        font-size: 2.7rem;
        padding-bottom: 0.3rem;
    }
    h4 {
        color: #6d4c41;
        font-size: 1.15rem;
        margin-top: -1rem;
    }
    .stTextInput > label {
        font-size: 1.05rem;
        font-weight: 600;
        color: #5d4037;
    }
    .stTextInput input {
        font-size: 1.05rem;
        padding: 0.4rem;
    }
    .stButton > button {
        background-color: #a1887f;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        font-size: 1rem;
        padding: 0.4rem 1.2rem;
    }
    .stButton > button:hover {
        background-color: #8d6e63;
    }
    .tool-section {
        background-color: #fffaf0;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 0 10px rgba(100, 70, 50, 0.1);
    }
    .tool-section h5 {
        font-size: 1.2rem;
        color: #4e342e;
        margin-bottom: 0.7rem;
    }
    .tool-list {
        font-size: 1.02rem;
        line-height: 1.8;
        color: #3e2723;
        margin-left: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1>AI Tool Recommender</h1>", unsafe_allow_html=True)
st.markdown("<h4>Get AI tools tailored to your task 🤖</h4>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# --- Input Field ---
user_prompt = st.text_input("What do you want to accomplish?", placeholder="e.g., generate an image of a dog")

# --- Logic & Display ---
if st.button("Find Recommendations"):
    if not user_prompt.strip():
        st.warning("⚠️ Please enter a task first.")
    else:
        category = classify_task(user_prompt)
        st.markdown("<hr>", unsafe_allow_html=True)

        if category and category in ai_db:
            st.markdown(f"<h5>🔍 Category Detected: <b>{category.title()}</b></h5>", unsafe_allow_html=True)

            # Start section card
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

            st.markdown('</div>', unsafe_allow_html=True)  # end .tool-section

        else:
            st.error("❌ Couldn't find a suitable category. Try rephrasing your task.")

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 13px; color: #a1887f;'>Built by Rashi Raj | Streamlit Deployment</p>",
    unsafe_allow_html=True
)

