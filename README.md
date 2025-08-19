# AI & Enterprise App Development with Python

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Frappe](https://img.shields.io/badge/Framework-Frappe-green.svg)
![LangChain](https://img.shields.io/badge/AI-LangChain-orange.svg)
![LLMs](https://img.shields.io/badge/LLM-Integration-yellow.svg)

A comprehensive 12-week training program covering **Python programming, AI/LangChain integration, and enterprise application development with Frappe Framework**.

## 🚀 Program Overview

- **Duration**: 12 Weeks (3 hours/day, 5 days/week)
- **Format**: Daily lectures (1 hour) + hands-on exercises (1 hour)
- **Prerequisites**: Basic computer literacy (no prior programming experience required)
- **Outcome**: Build production-ready AI-powered enterprise applications

## 📚 Curriculum Structure

### Module 1: Core Python & Data (Weeks 1-4)
- Python fundamentals (syntax, data structures, OOP)
- Database integration (SQL, Python-SQL connectivity)
- File I/O and virtual environments
- **Final Project**: CLI Blog Manager

### Module 2: AI & LLM Ecosystem (Weeks 5-8)
- Foundations of AI/ML and LLMs
- Vector databases and RAG pipelines
- LangChain and LangGraph implementation
- **Final Project**: Conversational RAG Agent

### Module 3: Enterprise Dev & AI (Weeks 9-12)
- Frappe Framework fundamentals
- DocType creation and customization
- Server scripting and API development
- **Final Project**: AI-Powered Library Management System

## 🛠️ Key Technologies

| Category       | Technologies                          |
|----------------|---------------------------------------|
| Core Python    | Python 3.9+, OOP, SQLite3            |
| AI/LLM Stack   | LangChain, LangGraph, RAG, Embeddings|
| Enterprise     | Frappe Framework, REST APIs          |
| Tools          | VS Code, Postman, ChromaDB           |

## 🏆 Learning Outcomes

By completing this program, you will be able to:
- Develop robust Python applications with database integration
- Implement AI features using LangChain and LLMs
- Build enterprise-grade applications with Frappe Framework
- Deploy AI-powered business solutions
- Architect systems combining traditional and AI components

## 📂 Project Showcase

### Week 4: CLI Blog Manager
```python
# Example code snippet
def add_post(db_conn, title, content):
    cursor = db_conn.cursor()
    cursor.execute("INSERT INTO posts VALUES (?, ?)", (title, content))
    db_conn.commit()

from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)
