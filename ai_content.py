import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="AI Content Generator", layout="wide")

st.title("AI Content Generator")

topic = st.text_input("Enter Topic")

tone = st.selectbox(
    "Tone",
    ["Formal", "Casual", "Technical", "Creative"]
)

content_type = st.selectbox(
    "Content Type",
    ["Blog Post", "LinkedIn Post", "Twitter Thread"]
)

word_limit = st.slider("Word Limit", 50, 500, 150)

def build_prompt(topic, tone, ctype, limit):
    return f"""
    Generate a {ctype} on the topic: {topic}.

    Tone: {tone}
    Length: approximately {limit} words

    Ensure the content is engaging, clear, and well-structured.
    """

if st.button("Generate"):
    if topic.strip() == "":
        st.warning("Enter a topic")
    else:
        prompt = build_prompt(topic, tone, content_type, word_limit)

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        result = response.choices[0].message.content

        st.subheader("Generated Content")
        st.write(result)