# AI Operations Assistant

## 24-Hour GenAI Intern Assignment – AI Operations Assistant

## 🎯 Objective

Build an AI system that:
- Accepts a natural language task
- Plans the required steps using an LLM
- Executes real third-party APIs
- Verifies and formats the final output
- Runs locally with a simple UI

---

## 🧠 Architecture Overview

The system is designed using three agents:

### 1. Planner Agent
- Converts the user’s natural language task into a structured JSON plan
- Decides which tools (APIs) are required

### 2. Executor Agent
- Executes each step of the plan
- Calls real external APIs
- Collects raw results

### 3. Verifier Agent
- Checks completeness and correctness of results
- Handles missing or partial data
- Produces a clean, human-readable final response

---

## 🛠️ Tools & APIs Used

- **GitHub API**  
  Used to search repositories and fetch metadata such as stars and descriptions.

- **OpenWeatherMap API**  
  Used to fetch current weather data for a given city.

---

## 🤖 LLM Usage

- The Planner Agent uses the LLM to generate a **structured JSON plan**
- The Verifier Agent uses the LLM to validate results and format the final output
- Monolithic prompts are avoided by separating responsibilities across agents

---

## 🖥️ Interface

- Built using **Streamlit**
- Provides a simple UI to:
  - Enter a natural language task
  - View planner output
  - View executor results
  - View final verified response

---

## Setup Instructions to Run Locally (localhost)

1. Clone the repository and move into the project directory:
```bash
git clone <your-repository-url>
cd ai_ops_assistant

## 📁 Project Structure

