# Email Threat Intelligence Platform

> An end-to-end Machine Learning application that detects and classifies email threats as **Spam** or **Ham** using Natural Language Processing (NLP), feature engineering, and an XGBoost classifier.

---

## Live Demo

| Resource | Link |
|---|---|
| Frontend App | https://email-threat-intelligence-platform-ai.streamlit.app/ |
| Backend API | https://email-threat-intelligence-platform-production.up.railway.app/ |
| API Docs | https://email-threat-intelligence-platform-production.up.railway.app/docs |
| Monitoring Dashboard | https://prasannavaddeman.grafana.net/public-dashboards/f619b25a945540b2905c7afce72c9bf5 |
| GitHub Repository | https://github.com/prasanna-vaddeman/email-threat-intelligence-platform |

---

## Overview

This project follows the complete Machine Learning lifecycle:

- Problem Scoping
- Data Collection
- Data Preprocessing
- Feature Engineering
- Model Training & Evaluation
- Deployment
- Monitoring & Observability
- Testing

Built to demonstrate production-grade Machine Learning Engineering practices beyond model development — including API deployment, monitoring, logging, testing, and cloud deployment.

---

## Architecture

<p align="center">
  <img src="images/architecture.png" alt="System Architecture Diagram" width="800"/>
</p>

---

## ML Pipeline

```
Email Input
    ↓
Preprocessing
    ↓
Feature Engineering
    ↓
TF-IDF Vectorization
    ↓
StandardScaler
    ↓
XGBoost Prediction
    ↓
Threat Analysis
    ↓
Response Generation
```

---

## Key Features

### Email Threat Detection
- Spam vs Ham classification
- Spam probability estimation
- Threat score calculation
- Threat level categorization

### NLP Processing
- Text cleaning & lowercasing
- Tokenization
- Stopword removal
- Stemming
- Email content normalization

### Feature Engineering
- TF-IDF vectorization
- URL count
- HTML tag count
- Uppercase ratio
- Spam keyword count
- Special character count
- Exclamation count

### Deployment
- FastAPI backend
- Streamlit frontend
- Railway deployment
- Streamlit Cloud deployment

### Monitoring & Observability
- Prometheus metrics collection
- Grafana dashboards
- Application logging
- Health monitoring

### Testing
- API endpoint testing
- Validation testing
- Metrics endpoint testing
- Preprocessing unit testing

---

## Technology Stack

| Layer | Technologies |
|---|---|
| Machine Learning | Python, Scikit-Learn, XGBoost, Pandas, NumPy, SciPy |
| Backend | FastAPI, Pydantic, Uvicorn |
| Frontend | Streamlit |
| Database | Supabase (PostgreSQL) |
| Monitoring | Prometheus, Grafana |
| Testing | Pytest |
| Deployment | Railway, Streamlit Cloud |

---

## Project Structure

```text
email-threat-intelligence-platform/

├── backend/            # FastAPI backend services
├── frontend/           # Streamlit frontend application
├── monitoring/         # WhyLogs monitoring
├── tests/              # Pytest test suite
├── docs/               # Project documentation
├── models/             # Trained ML models
├── artifacts/          # Vectorizers and scalers
├── deployment/         # Prometheus configuration
├── notebooks/          # Development notebooks
├── images/             # Architecture diagrams and screenshots

├── README.md
├── requirements.txt
├── Procfile
└── pytest.ini
```

---

## API Endpoints

### Health Check

```http
GET /email/health
```

### Email Prediction

```http
POST /email/predict
```

**Example Request:**

```json
{
  "email_text": "Congratulations! You won a free iPhone."
}
```

### Metrics

```http
GET /metrics
```

---

## Monitoring & Observability

The application exposes Prometheus metrics through the `/metrics` endpoint.

### Tracked Metrics

| Metric | Description |
|---|---|
| `email_predictions_total` | Total number of email predictions |
| `spam_predictions_total` | Total spam predictions |
| `prediction_errors_total` | Total prediction errors |
| `process_cpu_seconds_total` | CPU usage |
| `process_resident_memory_bytes` | Memory usage |
| `prediction_latency_ms` | Prediction latency in milliseconds |

### Grafana Dashboard Panels

- Total Emails Processed
- Spam Predictions
- Prediction Errors
- Backend Status
- CPU Usage
- Memory Usage
- Prediction Latency

---

## Testing

Run all tests:

```bash
pytest -v
```

**Test Coverage:**

- Health endpoint testing
- Metrics endpoint testing
- Prediction endpoint testing
- Input validation testing
- Preprocessing unit testing

**Example Result:**

```
5 passed
```

---

## Future Improvements

- Data Drift Monitoring
- Automated Retraining Pipeline
- CI/CD Automation
- Model Versioning
- Advanced Threat Intelligence Features

---

## Project Focus Areas

- Machine Learning Engineering
- MLOps Fundamentals
- NLP Applications
- Model Deployment
- Monitoring & Observability
- Production ML Systems

---

## Author

**Prasanna Vaddeman**

Machine Learning practitioner focused on building end-to-end ML systems — from data collection to production deployment.

### Certifications

- [Machine Learning Specialization](https://learn.deeplearning.ai/certificates/4106eebd-1e50-4139-990b-6d4660e33b87) — DeepLearning.AI & Stanford University (Andrew Ng)
- [IBM Data Science Professional Certificate](https://coursera.org/share/0b1469cc5665f11dc15b37a778118963) — IBM & Coursera