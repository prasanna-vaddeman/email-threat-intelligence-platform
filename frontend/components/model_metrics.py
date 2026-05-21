"""
Model Performance Metrics
"""

import streamlit as st


def render_model_metrics():

    st.divider()

    st.subheader(

        "Model Intelligence"

    )

    c1,c2,c3,c4 = (

        st.columns(4)

    )

    c1.metric(

        "Precision",

        "98.2%"

    )

    c2.metric(

        "Recall",

        "97.4%"

    )

    c3.metric(

        "F1 Score",

        "97.8%"

    )

    c4.metric(

        "ROC AUC",

        "99.1%"

    )

    st.caption(

"""
Evaluation Metrics

Precision → False Positive Control

Recall → Spam Detection Coverage

F1 → Overall Balance

ROC AUC → Ranking Performance

"""
    )