# 📡 Semiconductor Intelligence Scout (SIS)

An AI-driven framework for cross-border semiconductor industry monitoring, operating entirely locally and privacy-first.

## 🎯 The Problem
The semiconductor industry is hyper-competitive, and global data is fragmented across languages (Korean, Chinese, Dutch, etc.). Standard search tools often miss local industry-specific events and policy updates due to language barriers.

## 🛠 Features
- **Privacy First & Local LLM:** Powered by local **Llama 3** via **Ollama**, ensuring no data or search queries leave your machine.
- **Country-Native Agents:** Automatically translates and structures search queries into native languages (e.g., Korean for South Korea, Mandarin for Taiwan) for maximum OSINT coverage.
- **Zero API Costs:** Integrated with a clean web-scraping layer using DuckDuckGo, completely eliminating the need for paid search engine APIs.
- **Streamlit GUI:** A sleek, user-friendly control panel for quick intelligence gathering.

## 🚦 How to Run

### 1. Prerequisites
* Install **[Ollama](https://ollama.com/)** on your machine.
* Pull the Llama 3 model via your terminal:
  ```bash
  ollama run llama3
