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
Gross Domestic Product (GDP) is a key economic indicator that measures the total monetary value of all final goods and services produced within a country's borders over a specified period, typically a year or a quarter. 
It serves as a vital metric of a nation’s economic performance, indicating growth or decline in economic health. 
GDP can be assessed through three primary approaches: the production approach, the expenditure approach, and the income approach, each offering different perspectives of economic activity. 
Despite its significance, GDP has limitations since it does not capture income inequality, environmental costs, or non-market transactions, necessitating the use of additional indicators for a holistic economic assessment.
```

---

## ⚠️ Limitations & Future Improvements

### 1. Error Handling: 
There is no fallback mechanism for cases when the Valyu API fails (e.g., due to network issues or invalid API keys).  
*Future: Implement robust error handling, including retries and alternative flows.*

### 2. Multi-Agent Strategy:
The current setup uses a single CrewAI agent.
*Future: Explore multi-agent coordination and task delegation for even richer interactions.*

### 3. Interface Enhancements:
The tool is presently CLI-only.
*Future: Develop a graphical or web based interface and improve query validation..*
---

## 🧾 Credits

Built by **Jing Yi** 
Powered by [CrewAI](https://docs.crewai.com/) and [Valyu API](https://valyu.ai)
