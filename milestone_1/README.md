# Milestone 1: Environment Setup & Architecture  
## High-Throughput Log Analytics & Monitoring Engine

---

## Objective

This milestone focuses on:

- Environment configuration  
- Log and anomaly schema design  
- System architecture definition  
- Data flow documentation  
- Initial pipeline testing  

---

## 1. Environment Setup

Configured development environment with:

- Python 3.x  
- Dask  
- Ray  
- Pandas  
- scikit-learn  
- Streamlit  

### Installation

```bash
pip install dask ray pandas scikit-learn streamlit
```

Dask and Ray were initialized and tested successfully.

---

## 2. Log Schema

Each log record contains:

- Timestamp  
- Log Level  
- Source  
- Message  

This structure enables efficient processing and analysis.

---

## 3. Anomaly Schema

Each anomaly record includes:

- Anomaly_ID  
- Timestamp  
- Log_Level  
- Message  
- Anomaly_Score  
- Severity  
- Detection_Method  
- Status  

This ensures structured alerting and monitoring.

---

## 4. Architecture Flow

Log Sources  
→ Log Ingestion & Parsing  
→ Distributed Processing (Dask / Ray)  
→ Anomaly Detection  
→ (Alerting + Storage)  
→ Dashboard  

---

## 5. Initial Testing

Validated:

- Log ingestion  
- Parsing accuracy  
- Distributed processing  
- Data flow across modules  

---

## Status

Milestone 1 Completed Successfully.
