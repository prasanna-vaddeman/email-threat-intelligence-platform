"""
Sidebar Navigation
"""

import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title(

            "Navigation"

        )

        st.caption(

            "v1.0 Production"

        )

        st.divider()

        st.markdown(

            "🛡️ Threat Dashboard"

        )

        st.markdown(

            "🧠 Model Intelligence"

        )

        st.markdown(

            "⚙️ System Health"

        )

        st.divider()

        st.info(

"""
Supported Inputs

• Email Paste

• TXT Upload

• EML Upload

• Mobile Messages

• Gmail Integration

"""
        )

        st.divider()

        st.caption(

"""
Email Threat Intelligence

ML Powered Detection Platform
"""
        )