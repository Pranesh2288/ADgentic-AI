# 🤖 ADgentic AI

AI-driven pipeline for generating brand-aligned ad images with autonomous quality control.

## 📝 Description
ADgentic AI operationalizes an end-to-end workflow that transforms a marketing brief into a polished DALL-E 3 visual. The system ingests the brief, retrieves proven prompt patterns via RAG, synthesizes an optimized prompt, generates the image, critiques it with GPT-4 Vision, and iterates until it meets brand style expectations.


## ✨ Key Features
* **Brief Conversion:** Converts PDF briefs into structured documents for downstream processing.
* **Prompt Retrieval:** Retrieves past successful prompts using embeddings + ChromaDB for style continuity.
* **Prompt Synthesis:** Synthesizes high-fidelity prompts with GPT-4 + LlamaIndex Orchestration.
* **Visual QA:** Generates images via DALL-E 3 and performs visual QA with GPT-4 Vision.
* **Auto-Iteration:** Auto-iterates prompts when alignment scores fall below a defined threshold.


## 🚀 Getting Started

### 📦 Dependencies
* Python 3.10+
* LlamaIndex
* ChromaDB
* OpenAI API (GPT-4, DALL-E 3, Vision)

### 🛠️ Installing
Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

## ℹ️ Help
If retrieval fails, ensure ChromaDB persist directory is initialized.


## 📜 Version History
* **0.1** — Initial Release

## ⚖️ License
MIT License
