# Azure-wrapper-
Azure Playground Prompt Wrapper API             
⚙️ Azure Playground Prompt Wrapper API
This project was developed during my internship at UnisLink, designed to streamline interactions with AI models on Microsoft Azure's Playground. The system automates sending prompts and receiving responses using a structured, authenticated API, with support for Excel input/output handling.

📌 Project Overview
The main objective was to create a wrapper system that takes prompts from an Excel file, forwards them to an internal chatbot (simulating Azure OpenAI API behavior), and logs the responses to a new Excel output file.

This allowed non-technical users and internal teams to test prompt behavior efficiently and securely.

🔑 Key Features
📄 Excel Prompt Integration: Accepts prompt + comment from Excel and returns AI-generated responses.

🔁 End-to-End Workflow: Input → Prompt API → Output file (Excel).

🔐 Bearer Token Authentication: Secured access to the /chat endpoint using header-based authentication.

🚀 FastAPI Backend: Lightweight, production-ready Python backend.

🧠 Prompt Logging: Stores and logs each request for traceability and improvement.

⚙️ Multithreaded Processing: Handles large Excel files with faster execution using Python's ThreadPoolExecutor.

🛠️ Tech Stack
Python 3

FastAPI

Pandas

OpenPyXL

Uvicorn

ThreadPoolExecutor

Logging (standard library)

📂 Folder Structure
graphql
Copy
Edit
├── app.py               # FastAPI app with /chat endpoint
├── process.py           # Reads Excel, calls API, writes output
├── my_prompts.xlsx      # Sample input file
├── response_output.xlsx # Generated output file
├── logs/                # Logged prompt/response activity
💡 Real-World Impact
This wrapper helped streamline prompt testing on Azure Playground by simplifying the input/output process and reducing manual effort. It also provided a safe and structured testing environment with authentication and logging features.

