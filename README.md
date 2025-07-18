# AI Tool Recommender

This is a Streamlit app that recommends AI tools based on the task you type (e.g., “write an essay on AI”).

## 🔍 How it Works
- Classifies the task into a category like "essay writing"
- Looks up the category in `ai_database.json`
- Recommends: ✅ Best, 👍 Middle, ⚠️ Worst tools
- Tools are clickable links. No tokens or API needed!

## Tech Stack
- Python
- Streamlit
- JSON

## Files
- `app.py`: Streamlit app logic
- `ai_database.json`: Tool database
- `requirements.txt`: Python dependencies

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py

