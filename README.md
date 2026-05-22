# 📡 Semiconductor Intelligence Scout (SIS)

An AI-driven framework for cross-border semiconductor industry monitoring. 

## 🎯 The Problem
The semiconductor industry is hyper-competitive, and global data is fragmented across languages (Korean, Chinese, Dutch, etc.). Standard search tools often miss local industry-specific events and policy updates.

## 🛠 Features
- **Model-Agnostic Architecture:** Supports any LLM via LangChain (default: Local Llama3).
- **Country-Native Agents:** Automatically translates queries to native languages for better coverage.
- **Privacy First:** Designed to run locally using Ollama and Brave Search APIs.
- **Multi-Modal Support:** Capable of indexing text, video titles, and audio transcriptions.

## 🚦 How to Run
1. Clone the repo.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set your `BRAVE_SEARCH_API_KEY` in a `.env` file.
4. Run the GUI: `streamlit run app.py`.
