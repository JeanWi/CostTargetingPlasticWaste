import streamlit as st

def manage_cash():
    pass

    keys_required = [
        "data_fu",
        "data_today_input",
        "data_prices",
        "alternative_process"
    ]
    for key in keys_required:
        if key not in st.session_state:
            st.session_state[key] = None
            if key == "alternative_process":
                st.session_state["alternative_process"] = {}