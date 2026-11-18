# Document Reader Agent (CrewAI + Ollama)

An AI agent built with CrewAI that reads an internal document and answers questions about it. It runs on a local LLM through Ollama, so there are no API costs and nothing leaves your machine.

## How it works

1. A sample internal document (a PDF with made-up facts) sits in the `knowledge/` folder.
2. CrewAI loads it as a knowledge source.
3. A single agent uses the local model (`llama3.2`) to answer the question you set in `main.py`.

The document contains invented facts, so you can check that answers come from the file and not from the model's general knowledge.

## Prerequisites

- Python 3.12 (3.15 is too new for some dependencies)
- [Ollama](https://ollama.com) installed and running, with `llama3.2` pulled
- Git Bash or any terminal

## Setup

```bash
git clone https://github.com/YOURUSERNAME/REPO-NAME.git
cd REPO-NAME
py -3.12 -m venv venv
source venv/Scripts/activate
pip install crewai litellm
crewai install
```

Create a `.env` file (never commit it) with the model settings, for example:

```
MODEL=ollama/llama3.2
```

Check the exact variable names your project uses in `src/` and match them.

## Run

```bash
ollama list      # confirm llama3.2 is installed
crewai run
```

Change the question in `src/<package_name>/main.py`.

## Changes from the original example

- Adapted from CrewAI's `meta_quest_knowledge` example
- Edited `crew.py`, `main.py`, `agents.yaml` and `tasks.yaml` for a single document-reader agent
- Switched the model to `llama3.2` (the one available locally)
- Added `litellm` as a dependency

## Status and limits

- The crew runs end to end with a local model and a knowledge source.
- Small local models can give generic answers. Answer accuracy against the document has not been fully tested yet.
- Whole-document knowledge sources need an embedding model, so check the embedder setting if you see embedding errors.

## Credits

Based on the CrewAI examples repository and the AI-assisted DevOps series by Abhishek Veeramalla and Krish Naik.
