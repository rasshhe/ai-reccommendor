"""import streamlit as st

st.title("AI Recommender App")

st.write("Enter what you want to do, and get AI tool suggestions!")

prompt = st.text_input("What do you want to do?")

if st.button("Suggest Tools"):
    if prompt:
        st.success(f"✅ You want to: {prompt}")
        st.write("👉 Recommended AI tools:")
        st.write("1. OpenAI GPT-4 (best for writing, research, coding)")
        st.write("2. Claude (great for summarizing, chat)")
        st.write("3. DALL-E (image generation)")
        st.write("4. Midjourney (high-quality art)")
    else:
        st.warning("Please enter a task or prompt!")"""

"""import streamlit as st

st.set_page_config(page_title="AI Tool Recommender")

st.title("🔮 AI Tool Recommender")
st.write("Tell me what you want to do, and I'll suggest the best AI tools!")

# Input from user
user_task = st.text_input("What do you want to do?")

if st.button("Suggest AI Tools"):
    if user_task:
        st.success(f"✅ You want to: {user_task}")
        
        # Very simple hardcoded logic
        if "write" in user_task.lower() or "essay" in user_task.lower():
            st.write("👉 Best tools for writing:")
            st.write("- **OpenAI GPT-4** (Best overall for text generation)")
            st.write("- **Claude** (Excellent summarization and chat)")
        
        elif "photo" in user_task.lower() or "image" in user_task.lower() or "art" in user_task.lower():
            st.write("👉 Best tools for images:")
            st.write("- **DALL-E** (Prompt-based image generation)")
            st.write("- **Midjourney** (High-quality art)")
        
        elif "research" in user_task.lower():
            st.write("👉 Best tools for research:")
            st.write("- **OpenAI GPT-4** (Advanced research assistant)")
            st.write("- **Perplexity AI** (Real-time search with sources)")
        
        else:
            st.write("👉 General-purpose AI tools:")
            st.write("- **GPT-4** (Text, code, research)")
            st.write("- **Claude** (Chat, summarization)")
            st.write("- **DALL-E** (Images)")
            st.write("- **Midjourney** (Art)")
            st.write("- **Perplexity** (Search-based answers)")

    else:
        st.warning("⚠️ Please enter what you want to do!")
"""

'''import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Tool Recommender + ChatGPT Helper")

st.title("🔮 AI Tool Recommender")
st.write("Enter what you want to do. I'll suggest the best AI tools and even help you do it!")

# User input
user_task = st.text_input("What do you want to do?")

# Secret OpenAI key
openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")

# Optional: Let user choose model
model_choice = st.selectbox(
    "Choose Model",
    ["gpt-3.5-turbo", "gpt-4"]
)

if st.button("Suggest AI Tools and Generate"):

    if not user_task:
        st.warning("⚠️ Please enter what you want to do!")
    elif not openai_api_key:
        st.warning("⚠️ Please enter your OpenAI API Key!")
    else:
        st.success(f"✅ You want to: {user_task}")

        # Recommendations
        if "write" in user_task.lower() or "essay" in user_task.lower():
            st.subheader("👉 Recommended tools for writing:")
            st.write("- **OpenAI GPT-4** (Best overall for text generation)")
            st.write("- **Claude** (Excellent summarization and chat)")

        elif "photo" in user_task.lower() or "image" in user_task.lower() or "art" in user_task.lower():
            st.subheader("👉 Recommended tools for images:")
            st.write("- **DALL-E** (Prompt-based image generation)")
            st.write("- **Midjourney** (High-quality art)")

        elif "research" in user_task.lower():
            st.subheader("👉 Recommended tools for research:")
            st.write("- **OpenAI GPT-4** (Advanced research assistant)")
            st.write("- **Perplexity AI** (Real-time search with sources)")

        else:
            st.subheader("👉 General-purpose AI tools:")
            st.write("- **GPT-4** (Text, code, research)")
            st.write("- **Claude** (Chat, summarization)")
            st.write("- **DALL-E** (Images)")
            st.write("- **Midjourney** (Art)")
            st.write("- **Perplexity** (Search-based answers)")

        # Call ChatGPT to actually do the work
        st.subheader("💬 ChatGPT Answer to Your Task:")

        with st.spinner("Contacting ChatGPT..."):
            try:
                client = OpenAI(api_key=openai_api_key)
                response = client.chat.completions.create(
                    model=model_choice,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": user_task}
                    ]
                )
                answer = response.choices[0].message.content
                st.success("✅ Response from ChatGPT:")
                st.write(answer)

            except Exception as e:
                st.error(f"❌ Error calling OpenAI: {e}")
'''

import streamlit as st

st.set_page_config(page_title="✨ AI Tool Recommender")

st.title("🤖 AI Tool Recommender")
st.write(
    """
    📌 Enter what you want to do below, and I'll suggest the best AI tools to help you!
    For each recommended tool, you'll get a direct link to try it online.
    """
)

# User input
user_task = st.text_input("📝 What do you want to do? (e.g., write an essay, generate art, research paper)")

if st.button("🔍 Suggest AI Tools"):
    if not user_task.strip():
        st.warning("⚠️ Please describe what you want to do!")
    else:
        st.success(f"✅ You want to: {user_task}")

        task = user_task.lower()

        # Email writing
        if any(k in task for k in ["email"]):
            st.subheader("✉️ Recommended Tools for Email Writing:")
            st.link_button("🌐 ChatGPT", "https://chat.openai.com/")
            st.link_button("🌐 Claude", "https://claude.ai/")

        # Essay / blog writing
        elif any(k in task for k in ["essay", "blog", "article"]):
            st.subheader("📝 Recommended Tools for Essay / Blog Writing:")
            st.link_button("🌐 ChatGPT", "https://chat.openai.com/")
            st.link_button("🌐 Claude", "https://claude.ai/")

        # Legal writing
        elif "legal" in task or "agreement" in task or "contract" in task:
            st.subheader("⚖️ Recommended Tools for Legal Writing:")
            st.link_button("🌐 Harvey AI", "https://www.harvey.ai/")
            st.link_button("🌐 ChatGPT", "https://chat.openai.com/")

        # Poetry / creative
        elif "poem" in task or "poetry" in task or "story" in task:
            st.subheader("🎨 Recommended Tools for Poetry / Creative Writing:")
            st.link_button("🌐 ChatGPT", "https://chat.openai.com/")
            st.link_button("🌐 Claude", "https://claude.ai/")

        # Code generation
        elif "code" in task and ("write" in task or "generate" in task):
            st.subheader("💻 Recommended Tools for Code Generation:")
            st.link_button("🌐 ChatGPT", "https://chat.openai.com/")
            st.link_button("🌐 GitHub Copilot", "https://github.com/features/copilot")

        # Debugging
        elif "debug" in task or "fix" in task:
            st.subheader("🛠️ Recommended Tools for Debugging Code:")
            st.link_button("🌐 ChatGPT", "https://chat.openai.com/")
            st.link_button("🌐 GitHub Copilot", "https://github.com/features/copilot")

        # Image generation
        elif "image" in task or "art" in task or "drawing" in task:
            st.subheader("🎨 Recommended Tools for Image Generation:")
            st.link_button("🌐 DALL-E", "https://openai.com/dall-e")
            st.link_button("🌐 MidJourney", "https://www.midjourney.com/")

        # Photo-realistic images
        elif "photo" in task or "realistic" in task:
            st.subheader("📸 Recommended Tools for Photo-Realistic Images:")
            st.link_button("🌐 DALL-E", "https://openai.com/dall-e")
            st.link_button("🌐 Leonardo AI", "https://leonardo.ai/")

        # Logo / design
        elif "logo" in task or "design" in task:
            st.subheader("🎨 Recommended Tools for Logo / Design:")
            st.link_button("🌐 Looka", "https://looka.com/")
            st.link_button("🌐 Canva", "https://www.canva.com/")

        # Video generation
        elif "video" in task:
            st.subheader("🎥 Recommended Tools for Video Generation:")
            st.link_button("🌐 Pika Labs", "https://pika.art/")
            st.link_button("🌐 Runway ML", "https://runwayml.com/")

        # Audio / music
        elif "music" in task or "audio" in task or "tune" in task:
            st.subheader("🎵 Recommended Tools for Audio / Music Generation:")
            st.link_button("🌐 Suno AI", "https://suno.ai/")
            st.link_button("🌐 Soundraw", "https://soundraw.io/")

        # Voice generation
        elif "voice" in task:
            st.subheader("🗣️ Recommended Tools for Voice Generation:")
            st.link_button("🌐 ElevenLabs", "https://elevenlabs.io/")
            st.link_button("🌐 PlayHT", "https://play.ht/")

        # Summarization
        elif "summarize" in task or "summary" in task:
            st.subheader("📝 Recommended Tools for Summarization:")
            st.link_button("🌐 ChatGPT", "https://chat.openai.com/")
            st.link_button("🌐 Claude", "https://claude.ai/")

        # Translation
        elif "translate" in task:
            st.subheader("🌐 Recommended Tools for Translation:")
            st.link_button("🌐 DeepL", "https://www.deepl.com/")
            st.link_button("🌐 Google Translate", "https://translate.google.com/")

        # Research / Q&A
        elif "research" in task or "question" in task or "q&a" in task:
            st.subheader("📚 Recommended Tools for Research / Q&A:")
            st.link_button("🌐 Perplexity AI", "https://www.perplexity.ai/")
            st.link_button("🌐 ChatGPT", "https://chat.openai.com/")

        # Tutoring / education
        elif "teach" in task or "learn" in task or "education" in task:
            st.subheader("📘 Recommended Tools for Tutoring / Education:")
            st.link_button("🌐 ChatGPT", "https://chat.openai.com/")
            st.link_button("🌐 Khan Academy", "https://www.khanacademy.org/")

        # Data analysis
        elif "data" in task or "csv" in task or "analyze" in task:
            st.subheader("📊 Recommended Tools for Data Analysis:")
            st.link_button("🌐 ChatGPT (Code Interpreter)", "https://chat.openai.com/")
            st.link_button("🌐 DataRobot", "https://www.datarobot.com/")

        # Presentation / slides
        elif "slide" in task or "presentation" in task or "powerpoint" in task:
            st.subheader("📑 Recommended Tools for Presentations / Slides:")
            st.link_button("🌐 Tome AI", "https://tome.app/")
            st.link_button("🌐 Beautiful.ai", "https://www.beautiful.ai/")

        # Social media writing
        elif "tweet" in task or "social media" in task or "instagram" in task:
            st.subheader("📱 Recommended Tools for Social Media Writing:")
            st.link_button("🌐 Copy.ai", "https://www.copy.ai/")
            st.link_button("🌐 Jasper", "https://www.jasper.ai/")

        # Chatbot building
        elif "chatbot" in task or "bot" in task:
            st.subheader("🤖 Recommended Tools for Chatbot Building:")
            st.link_button("🌐 Botpress", "https://botpress.com/")
            st.link_button("🌐 Dialogflow", "https://cloud.google.com/dialogflow")

        # General catch-all
        else:
            st.subheader("✨ General-Purpose AI Tools:")
            st.link_button("🌐 ChatGPT", "https://chat.openai.com/")
            st.link_button("🌐 Claude", "https://claude.ai/")
            st.link_button("🌐 Perplexity AI", "https://www.perplexity.ai/")
            st.link_button("🌐 DALL-E", "https://openai.com/dall-e")
