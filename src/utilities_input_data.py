import pandas as pd
import streamlit as st
import pint

def define_stream(template_name:str, button_label:str):
    ureg = pint.UnitRegistry()
    st.download_button(
        label=button_label,
        data=pd.DataFrame(columns=["Commodity_name", "Quantity", "Quantity_unit"],
                          data=[["commodity1", 0, "kg"]]).to_csv(index=False),
        file_name=template_name,
        mime="text/csv",
        icon=":material/download:",
    )

    uploaded_file = st.file_uploader(
        "", key=button_label,
        accept_multiple_files=False, type="csv"
    )

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, header=0)
        df["Quantity_unit"] = df["Quantity_unit"].apply(lambda x: ureg(x))
        st.write(df)
        return df


def define_prices(all_commodities, template_name:str, button_label:str):

    df = pd.DataFrame(columns=["Commodity_name", "Price", "Price_unit"])
    df["Commodity_name"] = all_commodities
    df["Price"] = 0
    df["Price_unit"] = ""

    st.download_button(
        label=button_label,
        data=df.to_csv(index=False),
        file_name=template_name,
        mime="text/csv",
        icon=":material/download:",
    )

    uploaded_file = st.file_uploader(
        "", key=button_label,
        accept_multiple_files=False, type="csv"
    )

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, header=0)
        st.write(df)
        return df
