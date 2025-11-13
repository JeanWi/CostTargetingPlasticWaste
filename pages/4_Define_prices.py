import streamlit as st
import pandas as pd

from src.utilities_input_data import define_prices
from src.utilities_cash import manage_cash

manage_cash()

if st.session_state["data_fu"] is None:
    st.info("Please todays process first")
elif (st.session_state["data_today_input"] is None):
    st.info("Please define functional unit first")
else:

    st.markdown("**The following inputs and outputs have been defined:**")

    all_commodities = []
    for process_name in st.session_state["alternative_process"]:
        all_commodities = all_commodities + st.session_state["alternative_process"][process_name]["inputs"]["Commodity_name"].to_list()
        all_commodities = all_commodities + st.session_state["alternative_process"][process_name]["outputs"]["Commodity_name"].to_list()

    all_commodities = all_commodities + st.session_state["data_today_input"]["Commodity_name"].to_list()
    all_commodities = all_commodities + st.session_state["data_fu"]["Commodity_name"].to_list()

    all_commodities = list(set(all_commodities))
    st.write(pd.Series(all_commodities))

    # Conventional process
    st.markdown("**Define commodity prices**")
    st.markdown("Download the template with all defined commodities. Specify a price for each commodity.")

    if st.session_state["data_prices"] is None:
        st.session_state["data_prices"] = define_prices(
            all_commodities,
            "template_prices.csv",
            "Download price template"
        )
    else:
        st.markdown("**Pries are defined as::**")
        st.write(st.session_state["data_prices"])