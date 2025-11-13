import streamlit as st

from src.utilities_input_data import define_stream
from src.utilities_cash import manage_cash

manage_cash()

#FU
st.markdown("**Define functional unit**")
st.markdown("Download the template to see the required format. Specify all products of your "
            "included in the functional unit, including their quantity, "
            "and the market_price of the respective product. The unit column needs to be filled "
            "to check for unit consistency in the calculation process (e.g. kg, t,...).")

if st.session_state["data_fu"] is None:
    st.session_state["data_fu"] = define_stream(
        "template_fu.csv",
        "Download FU template"
    )
else:
    st.markdown("**Functional unit is defined as:**")
    st.write(st.session_state["data_fu"])

