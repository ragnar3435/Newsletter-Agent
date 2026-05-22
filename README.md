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

- Supports two modes:
  - Fully Autonomous Mode  
  - Human Approval Mode  

---

## Streamlit UI Dashboard

- Step-by-step agent visualization  
- Terminal-style execution logs  
- Real-time article and newsletter display  

---

## One-Click Execution

streamlit run NewsLetterAgent.py

---

# System Architecture

User Goal
↓
Planning Agent (LLM)
↓
Web Research (Tavily API)
↓
Article Summarization (LLM)
↓
Newsletter Generation (LLM)
↓
Critic / Reflection Agent (LLM)
↓
Improved Newsletter Output
↓
Save + Display + (Optional Approval)

---

# Example Workflow

1. User enters goal:
Create a weekly newsletter on latest AI agent news

2. System automatically:
- searches latest news
- extracts 5–7 articles
- summarizes each article
- generates newsletter
- critiques and improves output

3. Final output:
- clean markdown newsletter
- saved locally as newsletter.md
- displayed in Streamlit UI

---

# Tech Stack

- Python
- Streamlit
- LangChain Groq (Llama 3.3 70B)
- Tavily Search API
- Multi-step LLM agent architecture

---

# Project Structure

NewsLetterAgent.py     Main Streamlit AI agent app
requirements.txt       Dependencies
demo video.mp4         Demo of running system

---

# Installation

## 1. Clone repository

git clone https://github.com/your-username/newsletter-agent.git
cd newsletter-agent

---

## 2. Install dependencies

pip install -r requirements.txt

---

## 3. Add API keys

GROQ_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here

---

## 4. Run the application

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

Implements multi-step reasoning instead of a single LLM call.

---

## Reflection-Based Improvement

The system evaluates its own output and improves it iteratively.

---

## Tool-Augmented AI

Combines:
- LLM reasoning
- Web search tools
- iterative refinement

---

## Production-Style UI

Streamlit dashboard simulates real-world AI product interfaces.

---

# Demo

A short demo video is included in the repository:

demo video.mp4

It shows:
- user input
- agent workflow execution
- newsletter generation
- final output display

---

# Notes

- API keys required for Groq and Tavily
- Designed for educational/demo purposes
- No external database required

---

# Summary

This project demonstrates a mini autonomous AI agent system capable of:

- multi-step reasoning
- tool usage
- self-evaluation
- structured newsletter generation
- interactive UI execution
