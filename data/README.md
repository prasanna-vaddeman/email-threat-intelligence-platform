# Dataset Information

## Data Source

Raw email dataset collected from:

SpamAssassin Public Corpus

https://spamassassin.apache.org/old/publiccorpus/

The corpus contains real-world email samples organized into categories such as:

- Easy Ham (Legitimate emails)
- Spam (Unwanted or suspicious emails)

The dataset was used to build an end-to-end Email Threat Intelligence pipeline for spam detection and email threat analysis.

---

## Data Pipeline

Raw email files undergo a structured machine learning processing workflow:

```text
Raw Emails
   ↓
Email Parsing
   ↓
Text Preprocessing
   ↓
Feature Engineering
   ↓
Processed Dataset Creation
   ↓
TF-IDF Vectorization
   ↓
Model Training
   ↓
Inference Pipeline
```

---

## Folder Structure

data/

├── raw/

│   Original email corpus files

│

├── interim/

│   Parsed and cleaned intermediate outputs

│

├── processed/

│   Final structured dataset used for modeling

│

└── feature_engineered/

    Additional handcrafted features used for ML training

---

## Feature Engineering Examples

Generated features include:

- URL Count
- Exclamation Count
- Uppercase Ratio
- HTML Tag Count
- Special Character Count
- Spam Keyword Count

---

## Objective

Build a production-oriented Email Threat Intelligence Platform capable of:

- Spam email detection
- Threat severity estimation
- Explainable feature-based predictions
- End-to-end ML deployment architecture