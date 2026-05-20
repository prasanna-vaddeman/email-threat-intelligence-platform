# Email Threat Intelligence Platform

Machine Learning powered spam email detection system with NLP preprocessing, feature engineering, XGBoost inference pipeline, FastAPI backend deployment, and explainable threat intelligence scoring.

---

## Project Overview

This platform analyzes incoming emails and predicts:

- Spam / Ham classification
- Spam probability score
- Threat severity level
- Explainable engineered features

Built using:

- NLP preprocessing
- TF-IDF vectorization
- Manual feature engineering
- XGBoost classification
- FastAPI backend
- Production inference pipeline

---

## Features

### NLP Processing

- Lowercasing
- URL removal
- Email cleanup
- HTML cleanup
- Stopword removal
- Stemming

### Feature Engineering

Manual engineered features:

- URL count
- Exclamation count
- Uppercase ratio
- HTML tag count
- Special character count
- Spam keyword count

### Machine Learning

Models evaluated:

- Naive Bayes
- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

Advanced hybrid pipeline:

TF-IDF + Manual Features + XGBoost

Final model:

Advanced XGBoost

---

## Architecture

```text
Email Input

↓

Preprocessing

↓

Feature Engineering

↓

TF-IDF Vectorization

↓

Manual Features

↓

Feature Combination

↓

XGBoost Model

↓

Threat Intelligence Output
```

---

## Backend Architecture

```text
backend/

├── api/
│   └── routes.py

├── schemas/
│   └── email_schema.py

├── services/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── vectorization.py
│   └── inference.py

└── main.py
```

---

## API Endpoints

### Health Check

```http
GET /email/health
```

Response:

```json
{
 "status":"healthy"
}
```

### Predict Email Threat

```http
POST /email/predict
```

Request:

```json
{
 "email_text":"FREE MONEY CLICK NOW"
}
```

Response:

```json
{
 "prediction":"spam",

 "spam_probability":0.998,

 "threat_level":"HIGH",

 "features":{

   "url_count":1,

   "spam_keyword_count":2

 }
}
```

---

## Local Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Run backend:

```bash
uvicorn backend.main:app --reload
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

## Model Performance

| Model | F1 Score |
|--------|-----------|
| Naive Bayes | 0.978 |
| Logistic Regression | 0.971 |
| Random Forest | 0.954 |
| Advanced Random Forest | 0.967 |
| Advanced XGBoost | 0.978 |

Final selected model:

Advanced XGBoost

---

## Future Improvements

- Monitoring integration
- WhyLabs monitoring
- Drift detection
- Docker deployment
- CI/CD pipeline
- Frontend dashboard

---

## Author

Prasanna Kumar

Machine Learning Engineer / Data Science