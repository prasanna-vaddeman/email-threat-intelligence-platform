"""
Top KPI Metrics
"""

import streamlit as st


def render_kpi_cards():

    result = st.session_state.get(

        "prediction",

        {}

    )

    threat_score = result.get(

        "threat_score",

        0

    )

    spam_probability = result.get(

        "spam_probability",

        0

    )

    threat_level = result.get(

        "threat_level",

        "LOW"

    )

    features = result.get(

        "features",

        {}

    )

    links_found = features.get(

        "url_count",

        0

    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(

            "Threat Score",

            threat_score

        )

    with c2:

        st.metric(

            "Spam Probability",

            f"{spam_probability:.2f}%"

        )

    with c3:

        st.metric(

            "Links Found",

            links_found

        )

    with c4:

        st.metric(

            "Risk",

            threat_level

        )