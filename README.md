# AI-Content-Generator

## Project Overview

This project is a web-based AI content generator that creates text based on user input.
Users can enter a topic, select tone and content type, and generate structured content such as blog posts, LinkedIn posts, or Twitter threads.

---

## Tech Stack

* Python
* Streamlit
* Groq API
* python-dotenv

---

## Problem Statement

Creating quality content manually can be time-consuming and inconsistent.
This project automates content generation by allowing users to quickly produce structured and context-aware text based on simple inputs like topic, tone, and format.

---

## How to Run

### Clone the repository

```bash id="a1x9kp"
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### Install dependencies

```bash id="m8c2zl"
pip install -r requirements.txt
```

### Set up environment variables

Create a `.env` file in the root directory and add:

```bash id="p4w7ns"
GROQ_API_KEY=your_api_key_here
```

### Run the application

```bash id="x2d6qf"
streamlit run app.py
```

The application will open in your browser.
