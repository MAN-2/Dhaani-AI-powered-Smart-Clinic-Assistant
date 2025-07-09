# MCP LLM-Based Doctor Appointment & Reporting Assistant (Backend Only)

This project implements a natural language assistant to manage doctor appointments and generate patient visit summaries using FastAPI and LLM agent-based orchestration. It follows the **Model Context Protocol (MCP)** architecture, where an LLM dynamically selects backend tools based on user intent — such as scheduling, conflict resolution, email notifications, and summary generation.

---

## 🧠 Key Features

- CRUD operations on **doctors** and **appointments** using RESTful FastAPI endpoints (Swagger UI enabled).
- Use **natural language prompts** (via OpenRouter LLM API) to:
  - Book or reschedule appointments
  - Generate calendar event links
  - Trigger summary report tools
  - Send email confirmations
  - Generate Patient Appointment Summary
  
- Store and track **prompt history** in PostgreSQL
- Designed for **MCP-style agent tool orchestration**
- Frontend built with React (currently under development)

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

```bash
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

📹 Demo & Screenshots
Demo video and screenshots :
https://drive.google.com/file/d/1F4ne17cLwLQ1P35ZbjjChOce_kCuYqG0/view
![Screenshot (46)](https://github.com/user-attachments/assets/e45565c0-eef4-49f8-a476-c9ad45e027fb)
![Screenshot (47)](https://github.com/user-attachments/assets/36a09532-7836-4850-8472-73bad101d951)
![Screenshot (48)](https://github.com/user-attachments/assets/05e1d3eb-f3db-45cc-aa0d-ffeadd221c16)
![Screenshot (49)](https://github.com/user-attachments/assets/7cf5745b-02b9-41bf-ad25-02af29533677)
![Screenshot (50)](https://github.com/user-attachments/assets/bf8e085d-4867-414d-bea5-0ee202497604)



🧩 Tech Stack
FastAPI • LangChain • PostgreSQL • API • Google Calendar API • SMTP • React (upcoming)

📌 Project Status
Feature	Status
Appointment Booking	✅ Implemented
Appointment Deletion	✅ Implemented
LLM Agent Routing	✅ Implemented
Prompt History Logging	✅ Implemented
Google Calendar Link	⚠️ Partial (link not always returned)
Email Confirmation	✅ Functional
React Frontend	🚧 In Progress

🙋‍♂️ Author Notes
This backend was developed independently as part of a technical assignment for an internship evaluation. It allowed me to apply LLM integration, API development, and backend orchestration in a real-world setting. The backend was fully functional at the time of submission; frontend development is currently in progress.
