# langgraph-example

This repository contains the sample code I created while following along this tutorial [LangGraph Tutorial - How to Build Advanced AI Agent Systems](https://www.youtube.com/watch?v=1w5cCXlh7JQ).

Before getting started, make sure you have uv installed on your local system.

To start a new project, perform the following steps:
1. Run `uv init `.
2. Run `uv add python-dotenv langgraph "langchain[anthropic]" ipykernel`.
3. Create `.env` file and place the Anthropic API key as variable: `ANTHROPIC_API_KEY=`.
4. Run an agent as `uv run basic.py` (or any other agent that is in this repo).

To use the existing uv setup:
1. Navigate to this project root directory. 
2. Install this project dependencies with command `uv sync`. 
3. Create `.env` file and place the Anthropic API key as variable: `ANTHROPIC_API_KEY=`.
4. Run an agent as `uv run basic.py` (or any other agent that is in this repo).

To add LangSmith observability,
add to the `.env` file the following variables:

```
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=<your-api-key>
LANGSMITH_PROJECT=<project-name>
```
