# AI Newsletter Agent (Autonomous AI System)

An autonomous AI agent that generates a weekly AI agent newsletter by researching latest news, summarizing top articles, and producing a polished markdown report with a reflection-based improvement loop.

The system includes a Streamlit interface, supports human-in-the-loop control, and runs fully from a single execution flow.

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
Save + Display + Optional Approval  

---

# Example Workflow

User enters goal:  
Create a weekly newsletter on latest AI agent news  

System automatically:
- Searches latest news  
- Extracts 5–7 articles  
- Summarizes each article  
- Generates newsletter  
- Critiques and improves output  

Final output:
- Clean markdown newsletter  
- Saved locally as newsletter.md  
- Displayed in Streamlit UI  

---

# Tech Stack

- Python  
- Streamlit  
- LangChain Groq (Llama 3.3 70B)  
- Tavily Search API  
- Multi-step LLM agent architecture  

---

# Project Structure

NewsLetterAgent.py → Main Streamlit AI agent app  
requirements.txt → Dependencies  
demo video.mp4 → Demo of running system  

---

# Installation

## 1. Clone repository

```bash
git clone https://github.com/ragnar3435/newsletter-agent.git
cd newsletter-agent
