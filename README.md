# Newsletter-Agent

# AI Newsletter Agent (Autonomous AI System)

An autonomous AI agent that generates a weekly AI agent newsletter by researching latest news, summarizing top articles, and producing a polished markdown report with a reflection-based improvement loop.

The system includes a Streamlit interface, supports human-in-the-loop control, and runs fully from a single execution flow.

---

# Features

## Autonomous Agent Pipeline

The system follows a structured agentic workflow:

Planning → Research → Summarization → Writing → Reflection → Final Output

---

## Live Web Research

- Uses Tavily Search API  
- Fetches latest AI agent-related news articles  
- Automatically selects top relevant sources  

---

## LLM-Based Summarization

- Each article is summarized using Groq (Llama 3.3 70B)  
- Produces concise, structured summaries  

---

## Reflection / Critique Loop

- A dedicated critic step evaluates the newsletter  
- Improves:
  - clarity
  - structure
  - redundancy
  - engagement  
- Final output is refined based on feedback  

---

## Human-in-the-Loop Mode

Supports two modes:

- Fully Autonomous Mode  
- Human Approval Mode  

---

## Streamlit UI Dashboard

- Step-by-step agent visualization  
- Terminal-style execution logs  
- Real-time article and newsletter display  

---

## One-Click Execution

Run the application using:

```bash
streamlit run NewsLetterAgent.py



