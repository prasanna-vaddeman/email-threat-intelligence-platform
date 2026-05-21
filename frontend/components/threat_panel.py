"""
Threat Visualization
"""

import streamlit as st

from utils.colors import (

    THREAT_COLORS,

    PREDICTION_COLORS

)


def render_threat_panel():

    result = st.session_state.get(

        "prediction",

        {}

    )

    prediction = result.get(

        "prediction",

        "HAM"

    )

    score = result.get(

        "threat_score",

        0

    )

    spam = result.get(

        "spam_probability",

        0

    )

    level = result.get(

        "threat_level",

        "LOW"

    )

    prediction_color = (

        PREDICTION_COLORS.get(

            prediction.lower(),

            "#2563EB"

        )

    )

    risk_color = (

        THREAT_COLORS.get(

            level,

            "#22C55E"

        )

    )

    st.subheader(

        "Threat Intelligence"

    )

    st.markdown(

f"""
<h1 style="
color:{prediction_color};
font-weight:700;
">

{prediction.upper()}

</h1>
""",

unsafe_allow_html=True

)

    progress = min(

        score,

        100

    )

    st.markdown(

f"""
<div style="
width:100%;
height:14px;
background:#E5E7EB;
border-radius:8px;
overflow:hidden;
margin-top:10px;
margin-bottom:20px;
">

<div style="
width:{progress}%;
height:100%;
background:{risk_color};
transition:0.5s;
">
</div>

</div>
""",

unsafe_allow_html=True

)

    st.metric(

        "Threat Score",

        f"{score}/100"

    )

    st.metric(

        "Spam Probability",

        f"{spam:.2f}%"

    )

    st.markdown(

f"""
<div style="
background:{risk_color};
padding:14px;
border-radius:10px;
color:white;
font-size:22px;
font-weight:700;
text-align:center;
">

{level}

</div>
""",

unsafe_allow_html=True

)