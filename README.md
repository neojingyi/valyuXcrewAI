# 📚 ValyuXcrewAI: Factual Assistant Powered by Valyu + CrewAI

A command line tool that allows users to ask factual questions and get reliable answers retrieved from Valyu’s `/knowledge` API, coordinated by a CrewAI agent.

---

## 🧠 Project Overview & High-Level Architecture

This project integrates three components:

- **CrewAI agent** (`KnowledgeAgent`) that acts as an intelligent information provider  
- **Custom tool** that wraps the Valyu `/knowledge` API endpoint  
- **Interactive CLI** where users can ask questions and get results

The agent uses the tool internally to fetch responses and return clean, human-friendly answers — instead of relying on a large language model’s hallucinations.

```
[User] ─▶ [CLI Input] ─▶ [CrewAI Agent] ─▶ [ValyuTool (API call)] ─▶ [Answer Output]
```

---

## Setup and Install Instructions

### 1. Clone the repository
```bash
git clone git@github.com:neojingyi/valyuXcrewAI.git
cd valyuXcrewAI
```

### 2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install required packages
```bash
pip install -r requirements.txt
```

---

## 🔐 Configuration Steps (API Keys)

Create a `.env` file in the root directory with the following:

```
OPENAI_API_KEY=sk-...
VALYU_API_KEY=your_valyu_key_here
```

---

## 🧪 How It Works

1. User runs the app and is prompted for a question  
2. The `KnowledgeAgent` receives the task and decides to invoke the `ValyuTool`  
3. `ValyuTool` calls the `/knowledge` endpoint with the user’s question  
4. The API’s response is parsed and returned to the user

---

## 🧑‍💻 Example Interaction

```bash
$ python main.py
Ask me a question:
> What is GDP?

🎯 Answer:
Gross Domestic Product (GDP) is a fundamental economic metric that reflects the total monetary value of all final goods and services produced within a country’s borders in a specific time period, typically annually or quarterly. GDP serves as a comprehensive measure of a nation’s overall economic activity and is a critical indicator of economic health. Here are the key components and implications of GDP:
.
.
.
```

---

## ⚠️ Limitations & Future Improvements

- ❌ No fallback if Valyu API fails (e.g. network errors, bad auth)  
- ❌ Only one agent (no task delegation or multi-agent strategy)  
- ❌ no GUI or web interface  
- ✅ Future: Add logging, improve validation, retry logic, and a simple frontend

---

## 🧾 Credits

Built by **Jing Yi** 
Powered by [CrewAI](https://docs.crewai.com/) and [Valyu API](https://valyu.ai)
