'''import streamlit as st
import json

# --- Load AI database from JSON ---
with open("ai_database.json") as f:
    ai_db = json.load(f)

# --- Classifier function to guess the category ---
def classify_task(prompt):
    prompt = prompt.lower()

    if "email" in prompt:
        return "email writing"

    if "essay" in prompt or "blog" in prompt:
        return "essay/blog writing"

    if "legal" in prompt or "contract" in prompt or "agreement" in prompt:
        return "legal writing"

    if "poem" in prompt or "poetry" in prompt or "creative" in prompt:
        return "poetry/creative"

    if ("code" in prompt or "script" in prompt) and ("generate" in prompt or "write" in prompt):
        return "code generation"

    if "debug" in prompt or "fix" in prompt:
        return "debugging code"

    if ("image" in prompt or "photo" in prompt or "art" in prompt) and "realistic" in prompt:
        return "photo-realistic image"

    if "image" in prompt or "photo" in prompt or "art" in prompt:
        return "image generation"

    if "logo" in prompt or "design" in prompt:
        return "logo/design"

    if "video" in prompt:
        return "video generation"

    if "audio" in prompt or "music" in prompt:
        return "audio/music"

    if "voice" in prompt:
        return "voice generation"

    if "summarize" in prompt or "summary" in prompt:
        return "summarization"

    if "translate" in prompt or "translation" in prompt:
        return "translation"

    if "research" in prompt or "question" in prompt or "q&a" in prompt:
        return "research/q&a"

    if "teach" in prompt or "tutor" in prompt or "education" in prompt:
        return "tutoring/education"

    if "data" in prompt or "csv" in prompt or "analysis" in prompt:
        return "data analysis"

    if "presentation" in prompt or "slides" in prompt or "powerpoint" in prompt:
        return "presentation/slides"

    if "social media" in prompt or "tweet" in prompt or "post" in prompt:
        return "social media writing"

    if "chatbot" in prompt or "faq" in prompt:
        return "chatbot building"

    if "generate" in prompt or "generating" in prompt or "create" in prompt or "make" in prompt:
        return "general generation"

    return None

# --- Streamlit UI ---
st.set_page_config(page_title="✨ AI Tool Recommender")

st.title("🤖 AI Tool Recommender")
st.write(
    """
    📌 Tell me what you want to do below, and I'll suggest the best AI tools for it.
    It will show you **Best**, **Middle**, and **Worst** options so you can choose wisely!
    """
)

# --- User input box ---
user_prompt = st.text_input("📝 What do you want to do?")

# --- Button to get recommendations ---
if st.button("🔍 Suggest AI Tools"):
    if not user_prompt.strip():
        st.warning("⚠️ Please enter what you want to do!")
    else:
        st.success(f"✅ You want to: {user_prompt}")

        category = classify_task(user_prompt)

        if category and category in ai_db:
            st.subheader(f"🔎 Category detected: {category.title()}")

            best = ai_db[category].get("best", [])
            middle = ai_db[category].get("middle", [])
            worst = ai_db[category].get("worst", [])

            # Display in columns
            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown("🌟 **Best AI Tools**")
                for tool in best:
                    st.write(f"- {tool}")

            with col2:
                st.markdown("👍 **Middle AI Tools**")
                for tool in middle:
                    st.write(f"- {tool}")

            with col3:
                st.markdown("⚠️ **Worst AI Tools**")
                for tool in worst:
                    st.write(f"- {tool}")

        else:
            st.error("❌ Sorry! I couldn't find any recommendations for that task. Try describing it differently.")
'''
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

# --- Streamlit UI ---
st.set_page_config(page_title="✨ AI Tool Recommender with Links")

st.title("🤖 AI Tool Recommender")
st.write(
    """
    📌 Tell me what you want to do below, and I'll suggest the **best AI tools**.
    Each suggestion is a direct link to the tool!
    """
)

user_prompt = st.text_input("📝 What do you want to do?")

if st.button("🔍 Suggest AI Tools"):
    if not user_prompt.strip():
        st.warning("⚠️ Please enter what you want to do!")
    else:
        st.success(f"✅ You want to: {user_prompt}")

        category = classify_task(user_prompt)

        if category and category in ai_db:
            st.subheader(f"🔎 Category detected: {category.title()}")

            st.write("✅ **Best AI tools:**")
            for tool in ai_db[category]["best"]:
                st.markdown(f"- 🌟 [{tool['name']}]({tool['url']})")

            st.write("✅ **Middle AI tools:**")
            for tool in ai_db[category]["middle"]:
                st.markdown(f"- 👍 [{tool['name']}]({tool['url']})")

            st.write("✅ **Worst AI tools:**")
            for tool in ai_db[category]["worst"]:
                st.markdown(f"- ⚠️ [{tool['name']}]({tool['url']})")

        else:
            st.error("❌ Sorry! I couldn't find any recommendations for that task. Try describing it differently.")

