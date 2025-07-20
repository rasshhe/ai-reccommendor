# AI Tool Recommender  
Streamlit App for Task-Based AI Tool Suggestions

## Overview  
This project is a lightweight AI tool recommendation system that suggests the best, middle, and worst tools for a given task. It uses a local JSON database to categorize user input and display tool suggestions with direct links—no external API or tokens required.

## Features  
Task Classification  
- Accepts any user-defined task as input (e.g., "write an essay", "remove background")  
- Classifies the task into predefined categories stored in a JSON file  

AI Tool Recommendation  
- Recommends:
  -  Best tool
  -  Middle tool
  -  Least recommended tool  
- Tools are displayed as clickable links  
- Feedback is dynamic and instantly updates based on user input

User Interface  
- Developed using Streamlit  
- Simple and interactive frontend  
- Supports live text input and formatted results display  

## Technical Stack  
Language: Python  
Framework: Streamlit  
Data Format: JSON  
No authentication or external API required

## Project Structure  
app.py — Main Streamlit application logic  
ai_database.json — Local database of categorized AI tools  
requirements.txt — Python dependency file  
README.md — Project description and usage instructions  

## How to Run  
1. Clone the repository  
2. Install the dependencies:  
   ```bash
   pip install -r requirements.txt
3.Launch the app:
  '''bash
    streamlit run app.py

Author
Rashi Raj
B.Tech Computer Science (AIML)
University of Petroleum and Energy Studies
[GitHub Profile](https://github.com/rasshhe)

