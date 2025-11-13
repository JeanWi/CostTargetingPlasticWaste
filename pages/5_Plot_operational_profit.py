import streamlit as st
import pandas as pd
from pint import UnitRegistry
import altair as alt

from src.utilities_input_data import define_prices
from src.utilities_cash import manage_cash

manage_cash()

operational_profit = pd.DataFrame()

for process_name in st.session_state["alternative_process"]:
    prices = st.session_state["data_prices"]
    inputs = st.session_state["alternative_process"][process_name]["inputs"].merge(prices, on="Commodity_name")
    outputs = st.session_state["alternative_process"][process_name]["outputs"].merge(prices, on="Commodity_name")
    fu = st.session_state["data_fu"].merge(prices, on="Commodity_name")

    # st.write(fu)
    # st.write(inputs)
    # st.write(outputs)
    savings = (fu["Quantity"]* fu["Price"]).sum()
    feedstock_costs = (inputs["Quantity"]* inputs["Price"]).sum()
    additional_production_cost = 0

    for product_fu in fu["Commodity_name"]:
        conventional_production = fu[fu["Commodity_name"] == product_fu]["Quantity"].values[0]
        price = fu[fu["Commodity_name"] == product_fu]["Price"].values[0]
        if product_fu in outputs["Commodity_name"].to_list():
            process_production = outputs[outputs["Commodity_name"] == product_fu]["Quantity"].values[0]
        else:
            process_production = 0

        delta_production = conventional_production - process_production
        additional_production_cost = additional_production_cost + delta_production * price

    operational_profit.loc[process_name, "Total operational profit"] = savings - feedstock_costs - additional_production_cost

if len(operational_profit) > 0:

    chart = (
        alt.Chart(operational_profit.reset_index())
        .mark_bar(color="steelblue")
        .encode(
            y=alt.Y("index:N",
                    title=None,
                    sort="-x",
                    axis=alt.Axis(labelLimit=600)
                    ),
            x=alt.X("Total operational profit:Q", title="Total operational profit"),
        )
        .properties(
            width=400,
            height=300,
            title="Total operational profit by process"
        )
    )

    st.altair_chart(chart, width='stretch')

