# 🛡️ Email Threat Intelligence Platform

> **Production-grade Machine Learning system for intelligent email threat detection and analysis**

An end-to-end ML platform that analyzes raw email content and predicts threat levels with interpretable security insights. Deployed and monitored in production with a modern FastAPI backend and interactive Streamlit frontend.

---

## 🌐 Live Demo

| Component | Link |
|-----------|------|
| **Frontend** | [Streamlit App](https://email-threat-intelligence-platform-ai.streamlit.app/) |
| **Backend API** | [FastAPI Docs](https://email-threat-intelligence-platform-production.up.railway.app/docs) |
| **API Health** | [Status Check](https://email-threat-intelligence-platform-production.up.railway.app/health) |

---

## 📋 Table of Contents

- [Overview](#overview)
- [System Architecture](#-system-architecture)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation & Setup](#-installation--setup)
- [Project Structure](#-project-structure)
- [API Documentation](#-api-documentation)
- [Model Details](#-model-details)
- [Performance Metrics](#-performance-metrics)
- [Deployment](#-deployment)
- [Monitoring & Logging](#-monitoring--logging)
- [Engineering Highlights](#-engineering-highlights)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## Overview

### Problem Statement

Email threats evolve faster than traditional spam filters can adapt. Organizations need intelligent systems that:

- Detect both spam and sophisticated phishing attempts
- Extract actionable security indicators in real-time
- Provide explainable threat intelligence
- Scale reliably in production environments
- Support continuous monitoring and observability

### Solution

This platform delivers:

✅ **Intelligent Detection** - Hybrid ML model combining NLP and engineered features  
✅ **Real-time Analysis** - Sub-100ms production inference  
✅ **Production Ready** - Deployed on Railway with health monitoring  
✅ **Explainable AI** - Detailed threat scoring and feature attribution  
✅ **Scalable Architecture** - Modular services, clean separation of concerns  

---

## 🏗 System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interface Layer                      │
│              (Streamlit Cloud - Frontend)                   │
└─────────────────────────────────────────────────────────────┘
                              ↓
                     HTTP/REST API Call
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                 FastAPI Backend (Railway)                    │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              API Route Handler                        │  │
│  │  (request validation, response formatting)          │  │
│  └──────────────────────────────────────────────────────┘  │
│                        ↓                                    │
│  ┌──────────────────────────────────────────────────────┐  │
│  │           Inference Pipeline Service                 │  │
│  │  ┌──────────────────────────────────────────────┐   │  │
│  │  │ 1. Text Preprocessing                       │   │  │
│  │  │    - Lowercasing, tokenization              │   │  │
│  │  │    - Stopword removal, stemming             │   │  │
│  │  └──────────────────────────────────────────────┘   │  │
│  │                    ↓                                 │  │
│  │  ┌──────────────────────────────────────────────┐   │  │
│  │  │ 2. Feature Engineering (Hybrid)             │   │  │
│  │  │    - TF-IDF vectorization (sparse NLP)      │   │  │
│  │  │    - Numerical threat signals (6 features)  │   │  │
│  │  │    - StandardScaler normalization           │   │  │
│  │  └──────────────────────────────────────────────┘   │  │
│  │                    ↓                                 │  │
│  │  ┌──────────────────────────────────────────────┐   │  │
│  │  │ 3. Model Inference                          │   │  │
│  │  │    - XGBoost prediction (hybrid features)    │   │  │
│  │  │    - Probability calibration                 │   │  │
│  │  │    - Threat scoring & risk analysis          │   │  │
│  │  └──────────────────────────────────────────────┘   │  │
│  │                    ↓                                 │  │
│  │  ┌──────────────────────────────────────────────┐   │  │
│  │  │ 4. Monitoring & Logging                     │   │  │
│  │  │    - WhyLogs profile generation              │   │  │
│  │  │    - Structured logging                      │   │  │
│  │  │    - Inference metrics (latency, etc)        │   │  │
│  │  └──────────────────────────────────────────────┘   │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              ↓
                      JSON Response
                    {prediction, scores, features}
```

---

## ✨ Features

### Email Classification Engine

- **Binary Classification** - Distinguishes spam (malicious) from ham (legitimate)
- **Probability Scores** - Returns calibrated probability for statistical confidence
- **Threat Levels** - Categorizes risk as Critical, High, Medium, Low, or Safe
- **Confidence Metrics** - Provides model confidence percentage

### Advanced Feature Extraction

Automatically computes security signals:

| Feature | Purpose | Type | Example |
|---------|---------|------|---------|
| **URL Count** | Detect phishing links | Numerical | 5 URLs detected |
| **HTML Tag Count** | Identify HTML-based attacks | Numerical | 12 tags found |
| **Uppercase Ratio** | Detect aggressive messaging | Numerical | 23% uppercase |
| **Special Characters** | Flag obfuscation attempts | Numerical | 45 special chars |
| **Spam Keywords** | Pattern matching | Numerical | 3 keywords detected |
| **Exclamation Count** | Urgency/emotion detection | Numerical | 3 exclamations |
| **TF-IDF Vectorization** | Semantic text patterns | Sparse NLP | 300+ dimensions |

### Multi-Format Input Support

- **Text Paste** - Direct email content input
- **TXT Files** - Upload plain text emails
- **EML Files** - Standard email format support
- **Message Input** - Direct textarea input

### Production Features

- **Fast Inference** - Optimized for real-time production usage
- **API Documentation** - Auto-generated Swagger UI
- **Health Checks** - Endpoint monitoring and availability
- **Structured Logging** - Debug-friendly log output
- **Error Handling** - Graceful failure modes

---

## 🛠 Tech Stack

### Machine Learning & NLP
- **scikit-learn** - Feature extraction and preprocessing
- **XGBoost** - Gradient boosting classifier (production model)
- **TF-IDF** - Text vectorization and feature engineering
- **NLTK** - Natural language processing utilities
- **pandas** - Data manipulation and analysis
- **joblib** - Model serialization and loading

### Backend & API
- **FastAPI** - Modern async Python web framework
- **Uvicorn** - ASGI application server
- **Pydantic** - Data validation and parsing
- **Python 3.11** - Development environment

### Frontend
- **Streamlit** - Interactive Python web app framework
- **streamlit-cloud** - Serverless deployment

### Deployment & Infrastructure
- **Railway** - Cloud platform (backend)
- **Streamlit Cloud** - Cloud platform (frontend)
- **Git/GitHub** - Version control

### Monitoring & Observability
- **WhyLogs** - Local data profiling and monitoring
- **Python logging** - Structured logging
- **UptimeRobot** - Health monitoring (uptime tracking)

### Development Tools
- **pytest** - Unit testing framework
- **black** - Code formatting
- **pylint** - Code quality analysis

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.11+
- Git
- pip (or conda)
- Virtual environment (recommended)

### Local Development

**1. Clone the repository**

```bash
git clone https://github.com/prasanna-vaddeman/email-threat-intelligence-platform.git
cd email-threat-intelligence-platform
```

**2. Create virtual environment**

```bash
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure environment variables**

```bash
# Copy example config
cp .env.example .env

# Edit .env and add your configuration
nano .env  # or use your editor
```

Environment variables needed:

```env
# Optional: WhyLabs monitoring credentials (leave empty to use local-only monitoring)
WHYLABS_API_KEY=
WHYLABS_ORG_ID=
WHYLABS_DATASET_ID=

# Configuration
SPAM_THRESHOLD=0.5
LOG_LEVEL=INFO
```

**5. Run the backend server**

```bash
cd backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at: `http://localhost:8000`  
API docs at: `http://localhost:8000/docs`

**6. Run the frontend (in separate terminal)**

```bash
streamlit run frontend/app.py
```

Frontend will be available at: `http://localhost:8501`

---

## 📁 Project Structure

```
email-threat-intelligence-platform/
│
├── backend/                          # FastAPI backend
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py                # API endpoints (POST /predict)
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── email_schema.py           # Request/response validation
│   ├── services/
│   │   ├── __init__.py
│   │   ├── inference.py              # Prediction pipeline
│   │   ├── preprocessing.py          # Text cleaning
│   │   ├── vectorization.py          # TF-IDF vectorization
│   │   ├── feature_engineering.py    # Threat signal extraction
│   │   └── [other services]
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── config.py                 # Configuration management
│   │   └── threat_utils.py           # Threat scoring logic
│   └── main.py                       # FastAPI app entry point
│
├── frontend/                         # Streamlit frontend
│   ├── components/
│   │   ├── __init__.py
│   │   ├── input_panel.py            # Email input handling
│   │   ├── prediction_payload.py     # Result display
│   │   ├── feature_panel.py          # Feature visualization
│   │   ├── kpi_cards.py              # Metrics cards
│   │   ├── header.py                 # UI header
│   │   ├── sidebar.py                # Sidebar navigation
│   │   └── system_health.py          # Health status
│   ├── services/
│   │   ├── __init__.py
│   │   └── api_client.py             # Backend API calls
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── colors.py                 # Color scheme
│   │   └── config.py                 # Frontend config
│   └── app.py                        # Streamlit entry point
│
├── monitoring/                       # Monitoring & logging
│   ├── logs/
│   │   └── profiles/                 # WhyLogs profiles
│   ├── __init__.py
│   ├── monitoring_service.py         # Logging orchestration
│   ├── whylogs_logger.py             # WhyLogs integration
│   └── whylabs_config.py             # Configuration
│
├── models/                           # Pre-trained ML artifacts
│   ├── advanced_xgboost_model.pkl    # Production model (hybrid features)
│   ├── logistic_regression_model.pkl
│   ├── random_forest_model.pkl
│   └── [other trained models]
│
├── artifacts/                        # ML artifacts
│   ├── tfidf_vectorizer.pkl          # TF-IDF feature extraction
│   ├── standard_scaler.pkl           # Numerical feature scaling
│   └── [other artifacts]
│
├── data/                             # Dataset
│   ├── raw/                          # Raw email data
│   │   ├── easy_ham_1/
│   │   ├── easy_ham_2/
│   │   ├── spam_1/
│   │   └── spam_2/
│   ├── interim/                      # Processed data
│   ├── processed/                    # Final dataset
│   └── feature_engineered/           # Hybrid feature datasets
│
├── notebooks/                        # Jupyter notebooks
│   ├── 01_project_understanding.ipynb
│   ├── 02_email_parsing_experiments.ipynb
│   ├── 03_text_preprocessing.ipynb
│   ├── 04_exploratory_data_analysis.ipynb
│   ├── 05_feature_engineering.ipynb
│   ├── 06_model_training.ipynb
│   └── 07_inference_pipeline.ipynb
│
├── tests/                            # Unit & integration tests
│   ├── __init__.py
│   ├── test_preprocessing.py
│   ├── test_inference.py
│   └── test_api.py
│
├── Procfile                          # Railway deployment config
├── requirements.txt                  # Python dependencies
├── .env.example                      # Example environment variables
├── .gitignore                        # Git ignore rules
├── README.md                         # This file
└── pyproject.toml                    # Project metadata

```

---

## 📡 API Documentation

### Base URL

**Production:** `https://email-threat-intelligence-platform-production.up.railway.app`  
**Local:** `http://localhost:8000`

### Interactive API Docs

Visit `/docs` for Swagger UI or `/redoc` for ReDoc documentation

```
https://email-threat-intelligence-platform-production.up.railway.app/docs
```

### Predict Endpoint

**Endpoint:** `POST /api/predict`

**Request Body:**

```json
{
  "email_text": "string"
}
```

**Example Request:**

```bash
curl -X POST "https://email-threat-intelligence-platform-production.up.railway.app/api/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "email_text": "CLICK HERE NOW!!! You have won $1000000. Click the link: http://example.com/scam"
  }'
```

**Response (200 OK):**

```json
{
  "prediction": "spam",
  "spam_probability": 94.23,
  "threat_score": 94,
  "confidence": 94.23,
  "threat_level": "Critical",
  "inference_ms": 45.32,
  "features": {
    "url_count": 1,
    "html_tag_count": 0,
    "uppercase_ratio": 0.2154,
    "special_char_count": 12,
    "spam_keyword_count": 3,
    "exclamation_count": 3
  }
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `prediction` | string | "spam" or "ham" |
| `spam_probability` | float | Confidence percentage (0-100) |
| `threat_score` | int | Threat severity (0-100) |
| `confidence` | float | Model confidence (0-100) |
| `threat_level` | string | Risk category (Critical/High/Medium/Low/Safe) |
| `inference_ms` | float | Latency in milliseconds |
| `features` | object | Extracted email features |

### Error Responses

**400 Bad Request:**

```json
{
  "detail": "Email text is required"
}
```

**500 Internal Server Error:**

```json
{
  "detail": "Internal server error"
}
```

---

## 🤖 Model Details

### Hybrid Feature Engineering Approach

The platform uses a **hybrid feature engineering** strategy that combines:

**1. NLP Features (Sparse)**
- TF-IDF vectorization capturing semantic patterns
- 300+ text features from email content
- Identifies common spam words and patterns

**2. Threat Intelligence Features (Dense Numerical)**
- URL count - number of hyperlinks (phishing indicator)
- HTML tag count - HTML elements (formatting attacks)
- Uppercase ratio - aggressive messaging patterns
- Special character count - obfuscation attempts
- Spam keyword count - known malicious terminology
- Exclamation count - urgency signals

**3. Feature Normalization**
- StandardScaler applied to numerical features
- Prevents large-valued features from dominating
- Improves optimization stability during training

This hybrid approach combines semantic understanding (from NLP) with security indicators (from engineered features), creating a robust detection system used in production spam detection and email security systems.

### Model Selection Process

Multiple classification algorithms were evaluated using the hybrid feature engineering approach:

| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | 98.18% | 100.00% | 94.35% | 97.10% |
| Naive Bayes | 98.61% | 99.72% | 95.97% | 97.81% |
| Decision Tree | 92.96% | 90.76% | 87.10% | 88.89% |
| Random Forest | 97.13% | 100.00% | 91.13% | 95.36% |
| XGBoost | 97.13% | 98.57% | 92.47% | 95.42% |
| Logistic Regression (Tuned) | 97.57% | 99.14% | 93.28% | 96.12% |
| Random Forest (Tuned) | 97.91% | 99.43% | 94.09% | 96.69% |
| **XGBoost (Tuned)** | **98.61%** | **98.37%** | **97.31%** | **97.84%** |

**Selection Justification:**

XGBoost with tuned hyperparameters was selected as the production model due to:
- **Highest accuracy** - 98.61% correct classifications on test set
- **Excellent precision** - 98.37% of spam predictions are correct (minimal false alarms)
- **Outstanding recall** - 97.31% of actual spam emails are detected (minimal missed spam)
- **Balanced F1 score** - 97.84% (best overall metric balancing precision and recall)
- **Robust to hybrid features** - Gradient boosting handles both sparse NLP and dense numerical features effectively
- **Production stability** - Battle-tested algorithm widely used in industry
- **Fast inference** - Sub-100ms prediction latency suitable for real-time usage

### Production Model: XGBoost with Hybrid Features

**File:** `models/advanced_xgboost_model.pkl`

**Architecture:**

- **Algorithm:** Gradient Boosting (XGBoost)
- **Input Features:** 300+ TF-IDF features (sparse NLP) + 6 engineered numerical features (dense), StandardScaler normalized
- **Training Dataset:** Combined spam and ham email corpus with comprehensive preprocessing pipeline
- **Serialization:** joblib (fast, Python-native)
- **Artifact Dependencies:**
  - `tfidf_vectorizer.pkl` - Converts new emails to TF-IDF vectors
  - `standard_scaler.pkl` - Normalizes numerical threat signals

---

## 📊 Performance Metrics

### Model Performance (Test Set)

```
XGBoost with Hybrid Features Results:
──────────────────────────────────────
Accuracy:   98.61%
Precision:  98.37%
Recall:     97.31%
F1 Score:   97.84%
```

**What these metrics mean:**

- **Accuracy:** 98.61% of predictions are correct
- **Precision:** 98.37% of emails predicted as spam are actually spam (low false positives - fewer legitimate emails blocked)
- **Recall:** 97.31% of actual spam emails are detected (low false negatives - fewer dangerous emails slip through)
- **F1 Score:** 97.84% balanced performance across precision and recall

**Real-world implications:**
- Out of 1000 spam emails, ~973 are detected
- Out of 100 predicted spam emails, ~98 are actually spam
- False positive rate: ~1.63% (legitimate emails incorrectly marked as spam)
- False negative rate: ~2.69% (spam emails incorrectly marked as legitimate)

### Inference Performance

Optimized for low latency production inference.

---

## 🚀 Deployment

### Frontend Deployment (Streamlit Cloud)

**Platform:** Streamlit Cloud  
**URL:** https://email-threat-intelligence-platform-ai.streamlit.app/  
**Deployment:** Automatic on GitHub push  

**Steps:**

1. Push code to GitHub
2. Connect repo to Streamlit Cloud
3. Streamlit auto-deploys on push

### Backend Deployment (Railway)

**Platform:** Railway  
**URL:** https://email-threat-intelligence-platform-production.up.railway.app/  
**Runtime:** Python 3.11 Development Environment  

Railway deployment runtime configured for cloud compatibility.

**Configuration Files:**

**Procfile** (startup command):
```
web: python -m uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```

**requirements.txt** (dependencies):
```
fastapi==0.104.1
uvicorn==0.24.0
pydantic==2.4.2
scikit-learn==1.3.2
xgboost==2.0.0
pandas==2.1.1
joblib==1.3.2
whylogs==1.1.14
python-dotenv==1.0.0
```

**Deployment Steps:**

1. Create Railway account
2. Connect GitHub repository
3. Railway auto-deploys on push
4. View logs in Railway dashboard

### Environment Variables (Production)

Set in Railway dashboard:

```env
SPAM_THRESHOLD=0.5
LOG_LEVEL=INFO
```

---

## 📈 Monitoring & Logging

### Monitoring Stack

- **WhyLogs Local Profile Monitoring** - Data profiling and logging of predictions
- **UptimeRobot** - API availability monitoring
- **Python Structured Logging** - Application-level logging

### WhyLogs Integration

**Purpose:** Track prediction data and generate local profiles

**Implementation:**

- Logs prediction features and results
- Generates statistical profiles
- Stores profiles locally in `monitoring/logs/profiles/`
- No cloud dependency - fully local operation

**Files:**

- `monitoring/whylogs_logger.py` - Profile generation
- `monitoring/monitoring_service.py` - Integration point

### Structured Logging

All services use Python's built-in logging:

```python
import logging

LOGGER = logging.getLogger(__name__)

LOGGER.info("Email predicted as spam")
LOGGER.warning("Low confidence prediction")
LOGGER.error("Model loading failed")
```

### UptimeRobot Monitoring

Monitors API health endpoint:

```
GET /health
```

Tracks:
- API availability
- Response times
- Downtime alerts

---

## 🎯 Engineering Highlights

Production engineering decisions:

- **Hybrid Feature Engineering** - Combined sparse NLP (TF-IDF) with dense numerical threat signals for robust detection
- **Modular Backend Architecture** - Separated services for preprocessing, vectorization, feature engineering, inference, and monitoring
- **Model Artifact Versioning** - Multiple trained models stored for comparison and rollback capability
- **Railway Deployment Automation** - Git push triggers automatic build and deployment pipeline
- **Streamlit Frontend Deployment** - Separate frontend deployment on Streamlit Cloud with independent scaling
- **API Health Monitoring** - Health check endpoints with UptimeRobot integration for 24/7 uptime tracking
- **Local Prediction Observability** - WhyLogs for monitoring predictions without external cloud dependencies
- **Feature Normalization** - StandardScaler applied to numerical features to prevent feature dominance
- **Structured Logging System** - Consistent logging across services for debugging and observability
- **Production Inference Pipeline** - Separate, optimized inference path for latency-critical operations

---

## 🧪 Testing

### Run Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run all tests
pytest

# Run with coverage report
pytest --cov=backend --cov=frontend

# Run specific test file
pytest tests/test_inference.py -v
```

### Test Structure

```
tests/
├── test_preprocessing.py      # Text cleaning tests
├── test_inference.py          # Prediction pipeline tests
├── test_api.py                # API endpoint tests
└── conftest.py                # Test fixtures
```

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 👨‍💻 Author

**Prasanna Kumar**  
Machine Learning Engineer | Data Scientist

**Links:**
- 🔗 GitHub: https://github.com/prasanna-vaddeman
- 📧 Email: [your-email@example.com]
- 💼 LinkedIn: [your-linkedin-url]

---

## 🙏 Acknowledgments

- XGBoost team for the powerful gradient boosting library
- FastAPI for the modern web framework
- Streamlit for rapid ML application development
- Railway for seamless cloud deployment
- WhyLogs for monitoring and profiling capabilities

---

## 📞 Support

Having issues? Please:

1. Check [Existing Issues](https://github.com/prasanna-vaddeman/email-threat-intelligence-platform/issues)
2. Review API Documentation at `/docs`
3. Check server logs on Railway dashboard
4. Create new GitHub Issue with details

---

**Last Updated:** May 2026  
**Status:** Production Live ✅  
**Maintained By:** Prasanna Kumar