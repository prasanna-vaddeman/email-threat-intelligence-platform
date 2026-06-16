# Architecture Overview

## System Architecture

The Email Threat Intelligence Platform follows a production-oriented Machine Learning architecture designed to demonstrate the complete ML lifecycle from inference to monitoring.

### Components

#### Frontend

- Streamlit
- User Email Input
- TXT File Upload
- Prediction Dashboard
- Threat Score Visualization

#### Backend

- FastAPI
- Pydantic Validation
- REST API Endpoints
- Health Monitoring
- Metrics Endpoint

#### Machine Learning Pipeline

1. Text Preprocessing
2. Feature Engineering
3. TF-IDF Vectorization
4. StandardScaler
5. XGBoost Inference
6. Threat Analysis

#### Storage

- Supabase PostgreSQL

Stores:

- Prediction History
- Monitoring Metadata

#### Monitoring

- Prometheus
- Grafana

Tracks:

- Prediction Volume
- Spam Detection Rate
- API Errors
- CPU Usage
- Memory Usage
- Latency

#### Deployment

- Railway (Backend)
- Streamlit Cloud (Frontend)

---

## Architecture Diagram

See:

![Architecture Diagram](../images/architecture.png)