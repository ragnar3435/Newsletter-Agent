# AI Newsletter Agent (Autonomous AI System)

An autonomous AI agent that generates a weekly AI agent newsletter by researching the latest news, summarizing top articles, and producing a structured markdown report with a reflection-based improvement loop.

The system includes a Streamlit interface, supports human-in-the-loop control, and runs end-to-end from a single execution flow.

---

# Features

## Autonomous Agent Pipeline

Planning → Research → Summarization → Writing → Reflection → Final Output

---

## Live Web Research

- Uses Tavily Search API  
- Fetches latest AI agent-related news articles  
- Automatically selects most relevant sources  

---

## LLM-Based Summarization

- Uses Groq (Llama 3.3 70B)
- Produces structured article summaries  
- Extracts key insights from each source  

---

## Reflection / Critique Loop

- Evaluates generated newsletter quality  
- Improves clarity, structure, and redundancy  
- Regenerates improved final output  

---

## Human-in-the-Loop Mode

- Fully Autonomous Mode (no approval required)
- Human Approval Mode (step-by-step review)

---

## Streamlit UI Dashboard

- Step-by-step execution visibility  
- Clean terminal-style logs  
- Displays:
  - fetched articles
  - summaries
  - final newsletter  

---

## One-Click Execution

Run the application:

streamlit run NewsLetterAgent.py

---

# System Architecture

User Goal
↓
Planning Agent
↓
Web Research (Tavily API)
↓
Article Extraction
↓
LLM Summarization
↓
Newsletter Generation
↓
Reflection / Critique
↓
Final Improved Output
↓
Save + Streamlit Display

---

# Example Workflow

1. User enters goal:
Create a weekly newsletter on latest AI agent news

2. System executes:
- searches web
- extracts 5–7 articles
- summarizes each article
- generates newsletter
- improves via reflection loop

3. Output:
- markdown newsletter
- saved as newsletter.md
- displayed in Streamlit UI

---

# Tech Stack

- Python
- Streamlit
- LangChain (Groq integration)
- Llama 3.3 70B
- Tavily Search API
- Autonomous multi-step agent system

---

# Project Structure

NewsLetterAgent.py
requirements.txt
demo video.mp4

---

# Installation

## 1. Clone repository

git clone https://github.com/your-username/newsletter-agent.git
cd newsletter-agent

---

## 2. Install dependencies

pip install -r requirements.txt

---

## 3. Environment Variables

Create a `.env` file in the root directory:

GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here

Important:
- no quotes
- no spaces around "="
- do not commit .env to GitHub
- add .env to .gitignore

---

## 4. Run application

streamlit run NewsLetterAgent.py

---

# Requirements

streamlit
langchain
langchain-groq
tavily-python
python-dotenv

---

# Key Design Highlights

## True Agentic System
Multi-step reasoning instead of single LLM call.

## Reflection Loop
Self-evaluates and improves output quality.

## Tool-Augmented AI
Uses:
- LLM reasoning
- web search
- iterative refinement

## Production UI
Streamlit shows full execution pipeline clearly.

---

# Demo

demo video.mp4

Shows:
- user input
- autonomous execution
- article research
- summarization
- final newsletter generation

---

# Notes

- Requires Groq + Tavily API keys
- No database required
- Designed for evaluation/demo use

---

# Summary

This system demonstrates an autonomous AI agent capable of:

- planning
- web research
- summarization
- reflection-based improvement
- structured newsletter generation
