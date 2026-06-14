#  AI Assistant Development

A web-based AI Assistant built with **Python**, **Flask**, and **Google Gemini API** as part of a Prompt Engineering assignment.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Render-blue)](https://ai-assistant-development-3.onrender.com)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black)](https://github.com/Piyushrajsaaa/ai_assistant-development)

---

##  Live Demo

 **[https://ai-assistant-development-3.onrender.com](https://ai-assistant-development-3.onrender.com)**

---

##  Project Overview

This AI Assistant can perform 4 distinct functions:

| #   | Function              | Description                               |
| --- | --------------------- | ----------------------------------------- |
| 1   |  Question Answering | Get clear answers to any question         |
| 2   |  Text Summarization | Summarize long text into concise format   |
| 3   |  Content Generation | Generate stories, poems, essays, ideas    |
| 4   |  Study Advisor      | Get personalized study plans and roadmaps |

---

##  Tech Stack

| Technology        | Version          | Purpose                   |
| ----------------- | ---------------- | ------------------------- |
| Python            | 3.12             | Backend language          |
| Flask             | 3.0.0            | Web framework             |
| Google Gemini API | gemini-2.0-flash | AI model                  |
| google-genai      | 2.8.0            | Official Gemini SDK       |
| HTML5 / CSS3      | -                | Frontend UI               |
| JavaScript ES6    | -                | Async API calls           |
| python-dotenv     | 1.0.0            | Secure API key management |
| Gunicorn          | 26.0.0           | Production server         |

---

##  Project Structure

ai_assistant/

├── app.py # Main Flask entry point

├── config.py # Configuration & settings

├── requirements.txt # Python dependencies

├── Procfile # Render deployment config

├── .env # API key (not in GitHub)

│

├── routes/ # URL endpoints

│ ├── qa_routes.py

│ ├── summarize_routes.py

│ ├── generate_routes.py

│ └── advisor_routes.py

│

├── services/ # Business logic

│ ├── gemini_service.py

│ ├── qa_service.py

│ ├── summarize_service.py

│ ├── generate_service.py

│ └── advisor_service.py

│

├── prompts/ # Prompt Engineering templates

│ ├── qa_prompts.py

│ ├── summarize_prompts.py

│ ├── generate_prompts.py

│ └── advisor_prompts.py

│

├── utils/

│ └── feedback_handler.py # Feedback storage

│

├── static/

│ ├── css/style.css

│ └── js/main.js

│

└── templates/

├── base.html

├── index.html

├── qa.html

├── summarize.html

├── generate.html

└── advisor.html

---

##  Prompt Engineering Techniques Used

| Technique              | Description                      | Used In             |
| ---------------------- | -------------------------------- | ------------------- |
| Role Prompting         | Assign AI a specific role        | QA, Advisor         |
| Output Scaffolding     | Specify exact output structure   | QA Detailed         |
| Constrained Generation | Word limits + audience           | Summarize Academic  |
| Creative Scaffolding   | Guide creativity with parameters | Generate Detailed   |
| Persona Prompting      | Professional writer persona      | Generate Structured |
| Multi-aspect Prompting | Multiple dimensions at once      | Advisor Expert      |

---

##  How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Piyushrajsaaa/ai_assistant-development.git
cd ai_assistant-development
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up API key

Create a `.env` file in the root folder:
Get your free key at: https://aistudio.google.com/app/apikey

### 5. Run the app

```bash
python app.py
```

### 6. Open in browser

http://127.0.0.1:5000

---

##  Testing

Run formal test cases:

```bash
python test_cases.py
```

Expected output:
PASS | QA | Simple | What is Python?

PASS | QA | Educational | Explain OOP concepts

PASS | QA | Detailed | What is Artificial Intelligence?

PASS | QA | Edge | Empty input handled → validation working correctly

PASS | Summarize | Quick | ML paragraph

PASS | Summarize | Bullet | ML paragraph

PASS | Summarize | Academic | ML paragraph

PASS | Summarize | Edge | Too short text handled → validation working correctly

PASS | Generate | Simple | Poem about autumn

PASS | Generate | Detailed | Story about a robot

PASS | Generate | Structured | Essay about AI

PASS | Generate | Idea | Science fiction novel

PASS | Advisor | Quick | DSA tips

PASS | Advisor | Roadmap | Machine Learning

PASS | Advisor | Expert | System Design interviews
**15/15 Tests Passing ✅**

---

##  Feedback Mechanism

After every AI response, users can submit feedback:

-  **Yes** — Response was helpful
-  **No** — Response was not helpful

Feedback is stored locally in `feedback.json` with timestamp, function name, and rating.

---

##  Future Scope

-  User authentication and chat history
-  PDF/document upload for summarization
-  Voice input using Web Speech API
-  Analytics dashboard for feedback stats
-  Multi-language support
-  Full cloud deployment with database

---

##  Author

**Piyush Raj**
Computer Science Student
Prompt Engineering Assignment — 2026

---

##  License

This project is for educational purposes only.
