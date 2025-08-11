## Dhaani: AI Powered Smart Clinical Assistant
Dhaani is an intelligent doctor dashboard and clinical assistant designed to streamline healthcare professionals’ workflow. It integrates appointment management, patient tracking, and AI-powered natural language assistance to empower modern medical practice.

 ## Features
- CRUD operations on **doctors** and **appointments** using RESTful FastAPI endpoints (Swagger UI enabled).
- Use **natural language prompts** (via OpenRouter LLM API) to:
  - Book or reschedule appointments
  - Generate calendar event links
  - Trigger summary report tools
  - Send email confirmations
  - Generate Patient Appointment Summary
  

- Designed for **MCP-style agent tool orchestration**
- Frontend built with React 

Doctor Dashboard:
Manage your patients, appointments, and availability from a clean, intuitive React interface.

## Smart AI Chat Assistant:
Built-in AI agent that understands natural language commands like “list my patients,” “show today’s schedule,” or “send follow-up email,” and executes corresponding tasks automatically.

Appointment Management:
Book, reschedule, and cancel appointments easily with automated backend support.

Patient Management:
View detailed patient records, summaries, and generate comprehensive reports.

Follow-Up Emails:
Automatically compose and send professional follow-up emails after visits.

Real-Time Interactive UI:
Features include an availability calendar, upcoming appointments list with detailed tooltips, and a 3D brain visualization background for a modern user experience.

Tech Stack
Frontend: React, React Router, Tailwind CSS, react-calendar, react-icons , Glb models

Backend: FastAPI, SQLAlchemy, PostgreSQL , Python ,PostgreSQL  , API • Google Calendar API  , SMTP 

AI Services: OpenRouter API for LLM interactions with custom prompt engineering and tool integration

Other: Date-fns for datetime handling

## Installation
Clone the repository

Install backend dependencies:
pip install -r requirements.txt

Install frontend dependencies:
npm install within the frontend folder

Configure environment variables for API keys and database connection

Run backend server:
uvicorn app.main:app --reload

Run frontend:
npm start

Usage
Log in as a doctor to access the dashboard.

Manage your schedule and appointments.

Use the natural language chat assistant to query or command the system — e.g., “List my patients,” or “Reschedule appointment .”

Monitor real-time updates and interact with visual components like the 3D medical brain.

This project implements a natural language assistant to manage doctor appointments and generate patient visit summaries using FastAPI and LLM agent-based orchestration. It follows the **Model Context Protocol (MCP)** architecture, where an LLM dynamically selects backend tools based on user intent — such as scheduling, conflict resolution, email notifications, and summary generation.

---

## 
---

## 💬 Sample Prompt

> Book an appointment with Dr. Ahuja on 2025-07-14 at 10:00, user@mail.com

**Agent Output:**
- Appointment booked successfully  
- Google Calendar link returned  
- Confirmation email sent to user  
- Tool used: `book_appointment`  
- Logged in prompt history

---

## ⚠️ Credentials & Privacy

This repository **does not include sensitive credentials** like:
- `.env` (API keys, email/password, DB URL)
- `credentials.json` (Google API)

For local testing, you'll need to manually create a `.env` file and download your own `credentials.json`. See code comments for environment variable usage and setup instructions.

---

## 📦 Installation & Running Locally

### 1. Clone the Repository

``bash
git clone https://github.com/your-username/MCP-LLM-Appointment-System.git
cd MCP-LLM-Appointment-System

2. Create and Activate a Virtual Environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt

4. Add Your .env and credentials.json
Create a .env file in the root directory (see .env.example)

Place your credentials.json from Google Cloud Console in the same folder

5. Run the FastAPI Server
bash
Copy
Edit
uvicorn app.main:app --reload
Then open http://localhost:8000/docs to access Swagger UI and test the API endpoints.
bash

## 📹 Demo & Screenshots
Demo video and screenshots :
https://drive.google.com/file/d/1F4ne17cLwLQ1P35ZbjjChOce_kCuYqG0/view

![Screenshot (38)](https://github.com/user-attachments/assets/d70bd2ad-38cb-4e4e-bdfa-6c0ca06d404c)
![Screenshot (47)](https://github.com/user-attachments/assets/0a8600b0-0c33-4149-aad0-33a42913bc9a)
![Screenshot (48)](https://github.com/user-attachments/assets/2a47e60b-35f7-473f-9b0f-d2a4691322f4)
![Screenshot (49)](https://github.com/user-attachments/assets/c7a84977-cf33-4040-9b8e-3ad27b692218)
![Screenshot (50)](https://github.com/user-attachments/assets/2f06442a-1c0e-40c2-84c3-02a6618ead63)






