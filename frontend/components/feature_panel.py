"""
Feature Metrics
"""

import streamlit as st


def render_feature_panel():

    result = st.session_state.get(

        "prediction",

        {}

    )

    features = result.get(

        "features",

        {}

    )

    st.divider()

    st.subheader(

        "Feature Intelligence"

    )

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(

        "Links Found",

        int(

            features.get(

                "url_count",

                0

            )

        )

    )

    c2.metric(

        "HTML Tags",

        int(

            features.get(

                "html_tag_count",

                0

            )

        )

    )

    c3.metric(

        "Uppercase Ratio",

        round(

            features.get(

                "uppercase_ratio",

                0

            ),

            3

        )

    )

    c4.metric(

        "Exclamation Count",

        int(

            features.get(

                "exclamation_count",

                0

            )

        )

    )