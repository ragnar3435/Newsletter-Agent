import streamlit as st
import os
from langchain_groq import ChatGroq
from tavily import TavilyClient

# =========================
# CONFIG
# =========================

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "--")  
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "--")

llm = ChatGroq(
    temperature=0,
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile"
)

tavily = TavilyClient(api_key=TAVILY_API_KEY)

# =========================
# UI SETUP
# =========================

st.set_page_config(page_title="AI Newsletter Agent", layout="wide")

st.title("🧠 AI Newsletter Agent")
st.markdown("Generate weekly AI agent newsletters using an autonomous workflow.")

goal = st.text_input(
    "Enter Goal",
    "Create a weekly newsletter on latest AI agent news"
)

mode = st.selectbox("Mode", ["Fully Autonomous", "Human-in-the-Loop"])

run = st.button("🚀 Run Agent")

# =========================
# PRETTY LOG FUNCTION
# =========================

def log(step, message, style="info"):
    if style == "info":
        st.markdown(f"### 🟦 {step}")
        st.code(message)
    elif style == "success":
        st.markdown(f"### 🟩 {step}")
        st.success(message)
    elif style == "warn":
        st.markdown(f"### 🟨 {step}")
        st.warning(message)
    elif style == "final":
        st.markdown(f"### 🟪 {step}")
        st.markdown(message)


# =========================
# AGENT PIPELINE
# =========================

def run_agent(goal):

    st.divider()

    # -------------------------
    # 1. PLANNING
    # -------------------------
    log("PLANNING", "Creating execution strategy for newsletter...")

    plan = llm.invoke(f"""
    You are an AI agent planner.

    Goal:
    {goal}

    Break this into steps:
    1. search strategy
    2. summarization plan
    3. newsletter structure
    """)

    log("PLAN OUTPUT", plan.content)

    # -------------------------
    # 2. RESEARCH
    # -------------------------
    log("RESEARCH", "Fetching latest AI agent news from web...")

    results = tavily.search(
        query="latest AI agent news 2026",
        max_results=5
    )

    articles = results["results"]

    for i, a in enumerate(articles, 1):
        st.markdown(f"**Article {i}: {a['title']}**")
        st.caption(a["url"])

    # -------------------------
    # 3. SUMMARIZATION
    # -------------------------
    log("SUMMARIZATION", "Summarizing articles using LLM...")

    summaries = []

    for i, a in enumerate(articles, 1):

        summary = llm.invoke(f"""
        Summarize this article in 80-100 words:

        Title: {a['title']}
        Content: {a.get('content','')}
        """)

        summaries.append(f"""
### {i}. {a['title']}
{summary.content}

Source: {a['url']}
""")

    log("SUMMARIES", "\n\n".join(summaries))

    # -------------------------
    # 4. NEWSLETTER GENERATION
    # -------------------------
    log("NEWSLETTER WRITER", "Generating structured newsletter...")

    newsletter_prompt = f"""
    Create a professional markdown newsletter.

    Use the following summaries:

    {summaries}
    """

    newsletter = llm.invoke(newsletter_prompt).content

    log("DRAFT NEWSLETTER", newsletter)

    # -------------------------
    # 5. CRITIC / REFLECTION
    # -------------------------
    log("CRITIC", "Reviewing newsletter quality...")

    critique = llm.invoke(f"""
    Review and improve this newsletter.

    Check:
    - clarity
    - structure
    - redundancy
    - engagement

    Newsletter:
    {newsletter}
    """)

    log("CRITIQUE", critique.content)

    # -------------------------
    # 6. FINAL VERSION
    # -------------------------
    log("FINAL NEWSLETTER", "Improving based on critique...")

    final = llm.invoke(f"""
    Improve this newsletter based on critique:

    Critique:
    {critique.content}

    Newsletter:
    {newsletter}

    Return only final markdown newsletter.
    """)

    log("FINAL OUTPUT", final.content, style="final")

    # -------------------------
    # 7. SAVE FILE
    # -------------------------
    with open("newsletter.md", "w", encoding="utf-8") as f:
        f.write(final.content)

    st.success("Saved to newsletter.md ✅")

    # -------------------------
    # HUMAN IN LOOP
    # -------------------------
    if mode == "Human-in-the-Loop":
        st.warning("Human approval required")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Approve ✅"):
                st.success("Newsletter approved!")

        with col2:
            if st.button("Reject ❌"):
                st.error("Newsletter rejected")


# =========================
# RUN
# =========================

if run:
    run_agent(goal)