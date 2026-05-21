"""
Main Streamlit Dashboard
"""

import streamlit as st

from components.header import render_header
from components.sidebar import render_sidebar
from components.kpi_cards import render_kpi_cards
from components.input_panel import render_input_panel
from components.threat_panel import render_threat_panel
from components.feature_panel import render_feature_panel
from components.prediction_payload import render_prediction_payload
from components.system_health import render_system_health
from components.model_metrics import render_model_metrics


st.set_page_config(

    page_title="Email Threat Intelligence",

    page_icon="🛡️",

    layout="wide",

    initial_sidebar_state="expanded"

)


if "prediction" not in st.session_state:

    st.session_state["prediction"] = {}


render_sidebar()

render_header()


# KPI BACK TO TOP
render_kpi_cards()


left, right = st.columns(2)

with left:

    render_input_panel()

with right:

    render_threat_panel()


render_feature_panel()

render_prediction_payload()

render_model_metrics()

render_system_health()