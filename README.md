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

```
email-threat-intelligence-platform/
│
├── artifacts/
│   ├── advanced_feature_columns.pkl
│   ├── advanced_hybrid_tfidf_vectorizer.pkl
│   ├── advanced_manual_feature_scaler.pkl
│   ├── hybrid_tfidf_vectorizer.pkl
│   ├── label_encoder.pkl
│   ├── manual_feature_scaler.pkl
│   └── tfidf_vectorizer.pkl
│
├── backend/
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── monitoring/
│   │   ├── __init__.py
│   │   └── metrics.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── email_schema.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── feature_engineering.py
│   │   ├── inference.py
│   │   ├── preprocessing.py
│   │   └── vectorization.py
│   ├── storage/
│   │   ├── __init__.py
│   │   ├── postgres.py
│   │   └── prediction_store.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── logger.py
│   │   └── threat_utils.py
│   ├── __init__.py
│   └── main.py
│
├── configs/
│   └── config.yaml
│
├── data/
│   ├── feature_engineered/
│   │   ├── advanced_emails_feature_engineered.csv
│   │   └── emails_feature_engineered.csv
│   ├── interim/
│   │   └── emails_cleaned.csv
│   ├── processed/
│   │   └── emails_dataset.csv
│   └── raw/
│       ├── easy_ham_1/
│       ├── easy_ham_2/
│       ├── spam_1/
│       └── spam_2/
│
├── deployment/
│   └── monitoring/
│       ├── Dockerfile
│       └── prometheus.yml
│
├── docs/
│   ├── architecture.md
│   ├── deployment.md
│   └── monitoring.md
│
├── frontend/
│   ├── .streamlit/
│   │   └── config.toml
│   ├── components/
│   │   ├── __init__.py
│   │   ├── feature_panel.py
│   │   ├── header.py
│   │   ├── input_panel.py
│   │   ├── kpi_cards.py
│   │   ├── model_metrics.py
│   │   ├── prediction_payload.py
│   │   ├── sidebar.py
│   │   ├── system_health.py
│   │   └── threat_panel.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── api_client.py
│   └── app.py
│
├── images/
│   └── architecture.png
│
├── logs/
│   └── app.log
│
├── models/
│   ├── advanced_logistic_regression_model.pkl
│   ├── advanced_random_forest_model.pkl
│   ├── advanced_xgboost_model.pkl
│   ├── decision_tree_model.pkl
│   ├── logistic_regression_model.pkl
│   ├── naive_bayes_model.pkl
│   ├── random_forest_model.pkl
│   └── xgboost_model.pkl
│
├── monitoring/
│   ├── logs/
│   │   └── profiles/
│   ├── __init__.py
│   ├── monitoring_service.py
│   ├── whylabs_config.py
│   └── whylogs_logger.py
│
├── notebooks/
│   ├── 01_project_understanding.ipynb
│   ├── 02_email_parsing_experiments.ipynb
│   ├── 03_text_preprocessing.ipynb
│   ├── 04_exploratory_data_analysis.ipynb
│   ├── 05_feature_engineering.ipynb
│   ├── 06_model_training.ipynb
│   └── 07_inference_pipeline.ipynb
│
├── tests/
│   ├── __init__.py
│   ├── test_health.py
│   ├── test_invalid_request.py
│   ├── test_metrics.py
│   ├── test_predict.py
│   └── test_preprocessing.py
│
├── .env
├── .env.example
├── .gitignore
├── Procfile
├── pyproject.toml
├── pytest.ini
└── README.md
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