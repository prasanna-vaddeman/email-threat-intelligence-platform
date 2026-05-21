"""
Input Component
"""

import streamlit as st

from utils.file_parser import (
    parse_uploaded_file
)

from services.api_client import (
    predict_email
)


def render_input_panel():

    st.subheader(

        "Input Source"

    )

    option = st.radio(

        "Select Input",

        [

            "Paste Email",

            "Upload File",

            "Upload Message"

        ],

        key="input_option"

    )

    input_text = ""


    if option == "Paste Email":

        input_text = st.text_area(

            "Email Content",

            height=250,

            key="email_input"

        )


    elif option == "Upload File":

        file = st.file_uploader(

            "TXT or EML",

            [

                "txt",

                "eml"

            ],

            key="email_file"

        )

        input_text = parse_uploaded_file(

            file

        )


    else:

        input_text = st.text_area(

            "Message Content",

            height=250,

            key="message_input"

        )


    if st.button(

        "Analyze Threat",

        use_container_width=True

    ):

        if not input_text.strip():

            st.warning(

                "Input Required"

            )

            return


        with st.spinner(

            "Analyzing..."

        ):

            result = predict_email(

                input_text

            )


        # SINGLE SOURCE OF TRUTH

        st.session_state[

            "prediction"

        ] = result


        # FORCE UI REFRESH

        st.rerun()