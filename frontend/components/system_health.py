"""
Backend Health Check
"""

import streamlit as st

import requests

import os


API=os.getenv(

    "BACKEND_URL",

    "http://127.0.0.1:8000"

)


def render_system_health():

    st.divider()

    st.subheader(

        "System Health"

    )

    try:

        response=requests.get(

            f"{API}/health",

            timeout=3

        )

        if response.ok:

            st.success(

                "Backend Online"

            )

        else:

            st.warning(

                "Backend Unhealthy"

            )


    except Exception:

        st.error(

            "Backend Offline"

        )