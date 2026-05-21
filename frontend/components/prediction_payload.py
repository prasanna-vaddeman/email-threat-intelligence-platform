"""
Raw API Response
"""

import streamlit as st

import json


def render_prediction_payload():

    result=st.session_state.get(

        "prediction",

        {}

    )

    if result:

        with st.expander(

            "Prediction Payload"

        ):

            st.code(

                json.dumps(

                    result,

                    indent=2

                ),

                language="json"

            )