# 🦺 Safety & Risk Tracker

A lightweight **Safety, Health, Environment & Quality (SHEQ)** risk management application designed to help operations teams log, track, and analyse workplace hazards, risks, and corrective actions.

This project reflects real-world safety and risk management practices drawn from mining and industrial operations, translated into a modern, data-driven system.

---

## 🎯 Purpose

The Safety & Risk Tracker was built to:

* Digitise hazard identification and risk assessment
* Improve visibility of safety issues and corrective actions
* Support data-driven safety decision-making
* Provide an auditable trail for SHEQ compliance

The system is suitable for **mining, construction, manufacturing, and industrial environments**.

---

## 🧠 Key Features

* Hazard logging and categorisation
* Risk severity and likelihood scoring
* Corrective action tracking
* Incident history and audit trail
* Simple REST API for integration
* Lightweight database for fast setup

---

## 🛠️ Tech Stack

* **Backend:** FastAPI (Python)
* **Database:** SQLite
* **API Docs:** OpenAPI / Swagger (auto-generated)
* **Architecture:** Modular, REST-based design

---

## 📂 Project Structure

```
safety-risk-tracker/
│── main.py                # FastAPI application entry point
│── models.py              # Data models
│── schemas.py             # Pydantic schemas
│── database.py            # Database configuration
│── crud.py                # CRUD operations
│── requirements.txt       # Project dependencies
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Axulo-Inc/safety-risk-tracker.git
cd safety-risk-tracker/safety-risk-tracker/safety-risk-tracker
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
uvicorn main:app --reload
```

---

## 🔍 API Documentation

Once running, access the interactive API documentation:

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📊 Example Use Cases

* Daily hazard identification in underground or surface operations
* Safety officer tracking corrective actions
* SHEQ audits and inspections
* Operational risk trend analysis

---

## 🧪 Project Status

🟡 **MVP (Minimum Viable Product)**

Planned enhancements:

* Authentication & role-based access
* Frontend dashboard (React / Next.js)
* PostgreSQL support
* Analytics & reporting module
* Deployment via Docker

---

## 👨‍💼 Author

**Thabang Alfred Motsoahae**
Founder & CEO – Axulo Inc.
Business Analyst | Data & Operations | Tech Entrepreneurship

* LinkedIn: [https://www.linkedin.com/in/thabang-motsoahae-10272b96](https://www.linkedin.com/in/thabang-motsoahae-10272b96)
* GitHub: [https://github.com/Axulo-Inc](https://github.com/Axulo-Inc)

---

## 📄 License

This project is licensed under the MIT License. Feel free to use, modify, and build upon it.

---

> *"Safety is not a priority — it is a value."*
