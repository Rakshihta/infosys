# 🔍 High-Throughput Log Analytics & Monitoring Engine

A production-level distributed log analytics and real-time anomaly detection system built with Python, Ray, and Dask.

> *"From raw logs to actionable insights — in real time."*

---

## 🏗️ Architecture

```
Raw Logs (Generator / Server Logs)
         ↓
Ingestion Layer       → ingestion.py
         ↓
Parallel Parsing      → parser.py + processor.py (Ray)
         ↓
Distributed Analytics → aggregator.py (Dask)
         ↓
Anomaly Detection     → detector.py (Z-score, 3 signals)
         ↓
         ├── Email Alerts     → notifier.py (Gmail SMTP)
         └── Live Dashboard   → app.py (Streamlit + Plotly)
```

---

## 📁 Project Structure

```
log_analytics_engine/
│
├── main.py                        # Entry point
├── output_logs.json               # Processed logs (auto-generated)
├── anomalies.json                 # Detected anomalies (auto-generated)
├── requirements.txt               # Dependencies
├── .env                           # Credentials (never commit!)
├── .gitignore
│
├── simulate/
│   ├── __init__.py
│   ├── log_generator.py           # Generates realistic logs (90/10 split)
│   └── streaming.py               # Real-time streaming engine
│
└── pipeline/
    ├── __init__.py
    │
    ├── ingestion/
    │   ├── __init__.py
    │   └── ingestion.py           # Reads raw log lines from file
    │
    ├── processing/
    │   ├── __init__.py
    │   ├── parse.py               # Ray remote log parser
    │   ├── processor.py           # Parallel processing with Ray
    │   └── aggregator.py          # Dask analytics + storage
    │
    ├── anomaly/
    │   ├── __init__.py
    │   └── detector.py            # Z-score anomaly detection
    │
    ├── alerts/
    │   ├── __init__.py
    │   └── notifier.py            # Gmail SMTP email alerts
    │
    └── dashboard/
        ├── __init__.py
        └── app.py                 # Streamlit live dashboard
```

---

## ⚙️ Tech Stack

| Technology | Purpose |
|---|---|
| **Ray** | Parallel log parsing across CPU cores |
| **Dask** | Distributed analytics on large datasets |
| **Z-score** | Statistical anomaly detection |
| **Streamlit** | Live monitoring dashboard |
| **Plotly** | Interactive charts and visualizations |
| **Gmail SMTP** | Real-time email alerting |
| **python-dotenv** | Secure credential management |

---

## 🚀 Setup & Installation

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd log_analytics_engine
```

### 2. Create and activate virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure credentials
Create a `.env` file in the project root:
```
SENDER_EMAIL=yourgmail@gmail.com
EMAIL_PASSWORD=your16charapppassword
RECIPIENT_EMAIL=yourgmail@gmail.com
```

> **Note:** Generate an App Password from [Google Account → Security → App Passwords](https://myaccount.google.com). Requires 2-Step Verification to be enabled.

---

## ▶️ Running the System

### Start the streaming engine + alerts:
```bash
python main.py
```

### Start the live dashboard (in a separate terminal):
```bash
python -m streamlit run pipeline/dashboard/app.py
```

Open your browser at `http://localhost:8501`

---


## 🔒 Security

- Credentials stored in `.env` file — never hardcoded
- `.env` added to `.gitignore` — never pushed to GitHub
- Gmail App Password used — not main account password
- SSL encryption for all email transmission

---


