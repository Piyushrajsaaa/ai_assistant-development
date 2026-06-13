# AI Assistant Development

## Project Report — Prompt Engineering Assignment

---

## 1. PROJECT OVERVIEW

**Project Title:** AI Assistant Development  
**Technology Stack:** Python, Flask, Gemini API, HTML, CSS, JavaScript  
**Type:** Web-based AI Assistant  
**Objective:** Design and implement an AI Assistant capable of performing
multiple tasks using carefully engineered prompts.

---

## 2. OBJECTIVES

- Build a web-based AI Assistant using Flask and Google Gemini API
- Implement 4 distinct AI-powered functions
- Design 3+ prompt templates per function with varying complexity
- Create a feedback collection mechanism
- Demonstrate how prompt engineering affects AI response quality

---

## 3. SYSTEM ARCHITECTURE

CLIENT (Browser)

│

│ HTTP Requests (Fetch API / AJAX)

▼

FLASK WEB SERVER (app.py)

│

├── routes/ → URL endpoints (qa, summarize, generate, advisor)

├── services/ → Business logic + Gemini API calls

├── prompts/ → Prompt Engineering templates

└── utils/ → Feedback storage

│

▼

GOOGLE GEMINI API (gemini-2.0-flash)

│

▼

## feedback.json → Local feedback storage

## 4. FOLDER STRUCTURE

ai_assistant/

├── app.py Main Flask entry point

├── config.py Configuration & API settings

├── requirements.txt Python dependencies

├── feedback.json Auto-generated feedback storage

├── routes/

│ ├── qa_routes.py Question Answering endpoints

│ ├── summarize_routes.py Summarization endpoints

│ ├── generate_routes.py Content Generation endpoints

│ └── advisor_routes.py Study Advisor endpoints

├── services/

│ ├── gemini_service.py Gemini API wrapper

│ ├── qa_service.py QA business logic

│ ├── summarize_service.py Summarization logic

│ ├── generate_service.py Generation logic

│ └── advisor_service.py Advisor logic

├── prompts/

│ ├── qa_prompts.py 3 QA prompt templates

│ ├── summarize_prompts.py 3 Summarization prompts

│ ├── generate_prompts.py 3 Generation prompts

│ └── advisor_prompts.py 3 Advisor prompts

├── utils/

│ └── feedback_handler.py Read/write feedback.json

├── static/

│ ├── css/style.css Complete UI styling

│ └── js/main.js Frontend interactivity

└── templates/

├── base.html Shared layout

├── index.html Home page

├── qa.html Question Answering page

├── summarize.html Summarization page

├── generate.html Content Generation page

## └── advisor.html Study Advisor page

## 5. FUNCTIONS IMPLEMENTED

### Function 1: Question Answering

- **Purpose:** Answer factual and conceptual questions
- **Endpoint:** POST /qa/answer
- **Prompts:** Simple (direct), Educational (role-based), Detailed (structured)

### Function 2: Text Summarization

- **Purpose:** Summarize long text into concise format
- **Endpoint:** POST /summarize/run
- **Prompts:** Quick (2-3 sentences), Bullet (key points), Academic (formal)

### Function 3: Content Generation

- **Purpose:** Generate stories, poems, essays, and ideas
- **Endpoint:** POST /generate/run
- **Prompts:** Simple (minimal), Detailed (narrative), Structured (professional)

### Function 4: Study Advisor

- **Purpose:** Provide personalized study plans and advice
- **Endpoint:** POST /advisor/run
- **Prompts:** Quick (tips), Roadmap (4-week plan), Expert (comprehensive guide)

---

## 6. PROMPT ENGINEERING TECHNIQUES USED

| Technique              | Definition                             | Used In                 |
| ---------------------- | -------------------------------------- | ----------------------- |
| Role Prompting         | Assigning AI a specific role           | QA Educational, Advisor |
| Output Scaffolding     | Specifying exact output structure      | QA Detailed             |
| Constrained Generation | Adding word limits and audience        | Summarize Academic      |
| Creative Scaffolding   | Guiding creativity with parameters     | Generate Detailed       |
| Persona Prompting      | "Professional writer with 10 years..." | Generate Structured     |
| Multi-aspect Prompting | Asking multiple dimensions at once     | Advisor Expert          |

---

## 7. FEEDBACK MECHANISM

- After every AI response, user sees: **"Was this response helpful?"**
- Two options: **👍 Yes** or **👎 No**
- Feedback saved to `feedback.json` with:
  - Timestamp
  - Function name
  - User input (truncated)
  - AI response (truncated)
  - was_helpful: true/false

---

## 8. TECHNOLOGIES USED

| Technology       | Version | Purpose               |
| ---------------- | ------- | --------------------- |
| Python           | 3.12    | Backend language      |
| Flask            | 3.0.0   | Web framework         |
| google-genai     | 2.8.0   | Gemini AI API         |
| python-dotenv    | 1.2.2   | Environment variables |
| HTML5            | -       | Page structure        |
| CSS3             | -       | Styling & animations  |
| JavaScript       | ES6     | Async API calls       |
| Gemini 2.0 Flash | -       | AI model              |

---

## 9. TESTING

- 12 test cases across all 4 functions
- 3 prompt styles tested per function
- Edge cases: empty input, too-short text
- All tests passing ✅

---

## 10. FUTURE SCOPE

1. **User Authentication** — Login system to save personal history
2. **Chat History** — Store and revisit past conversations
3. **Voice Input** — Speech-to-text for hands-free use
4. **PDF Upload** — Summarize uploaded documents directly
5. **Multi-language Support** — Support Hindi, Spanish, French
6. **Export Feature** — Download responses as PDF or Word
7. **Analytics Dashboard** — Visualize feedback statistics
8. **Mobile App** — React Native version

---

## 11. CONCLUSION

This project successfully demonstrates the power of prompt engineering
in building practical AI applications. By varying prompt length, tone,
style, and complexity, we achieved significantly different and more
useful outputs from the same AI model. The modular Flask architecture
ensures the project is maintainable and extensible. The feedback
mechanism provides a foundation for continuous improvement.
