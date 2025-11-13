import streamlit as st

from src.utilities_input_data import define_stream
from src.utilities_cash import manage_cash

manage_cash()

if st.session_state["data_fu"] is not None:

    st.markdown("**Functional unit is defined as:**")

    st.write(st.session_state["data_fu"])

    # Conventional process
    st.markdown("**Define today's process input**")
    st.markdown("Download the template to see the required format. Specify all inputs required for "
                "today's production of the functional unit.")

    if st.session_state["data_today_input"] is None:
        st.session_state["data_today_input"] = define_stream(
            "template_today_input.csv",
            "Download today's input process template"
        )
    else:
        st.markdown("**Today's process input is defined as:**")
        st.write(st.session_state["data_today_input"])

else:
    st.info("Please define functional unit first")