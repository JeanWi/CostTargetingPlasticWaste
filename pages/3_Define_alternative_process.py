import streamlit as st
import pandas as pd

from src.utilities_input_data import define_stream
from src.utilities_cash import manage_cash

manage_cash()

if st.session_state["data_fu"] is None:
    st.info("Please todays process first")
elif (st.session_state["data_today_input"] is None):
    st.info("Please define functional unit first")
else:

    process_name = st.text_input("Process name:")
    # if process_name in st.session_state["alternative_process"]:
    #     st.error(f"{process_name} already exists")
    #     if st.button(f"Delete process?"):
    #         del st.session_state["alternative_process"][process_name]
    # else:

    st.markdown("**Define process outputs**")
    st.markdown("Download the template to see the required format. Specify all outputs that are "
                "produced by the process.")

    outputs = define_stream(
        "template_alternative_process_outputs.csv",
        "Download output template"
    )

    inputs = define_stream(
        "template_alternative_process_inputs.csv",
        "Download input template"
    )

    if st.button(f"Create process"):
        # st.session_state["alternative_process"] = {}
        st.session_state["alternative_process"][process_name] = {}
        st.session_state["alternative_process"][process_name]["outputs"] = None
        st.session_state["alternative_process"][process_name]["inputs"] = None

        # Alternative process

        if st.session_state["alternative_process"][process_name]["outputs"] is None:
            st.session_state["alternative_process"][process_name]["outputs"] = outputs
        if st.session_state["alternative_process"][process_name]["inputs"] is None:
            st.session_state["alternative_process"][process_name]["inputs"] = inputs