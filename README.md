# 📡 Semiconductor Intelligence Scout (SIS)

An AI-driven framework for cross-border semiconductor industry monitoring. 

## 🎯 The Problem
The semiconductor industry is hyper-competitive, and global data is fragmented across languages (Korean, Chinese, Dutch, etc.). [cite_start]Standard search tools often miss local industry-specific events and policy updates[cite: 5, 13].

## 🛠 Features
- [cite_start]**Model-Agnostic Architecture:** Supports any LLM via LangChain (default: Local Llama3)[cite: 29].
- [cite_start]**Country-Native Agents:** Automatically translates queries to native languages for better coverage.
- [cite_start]**Privacy First:** Designed to run locally using Ollama and Brave Search APIs.
- [cite_start]**Multi-Modal Support:** Capable of indexing text, video titles, and audio transcriptions[cite: 14].

## 🚦 How to Run
1. Clone the repo.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set your `BRAVE_SEARCH_API_KEY` in a `.env` file.
4. Run the GUI: `streamlit run app.py`.
