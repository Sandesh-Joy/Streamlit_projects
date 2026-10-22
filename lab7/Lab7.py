import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("Interactive Sales Dashboard")
rng = np.random.default_rng(7)
df = pd.DataFrame({
    "Year": rng.choice([2022, 2023, 2024], 200),
    "Region": rng.choice(["North", "South", "East", "West"], 200),
    "Product": rng.choice(["A", "B", "C"], 200),
    "Sales": rng.integers(1000, 10000, 200),
})
st.sidebar.header("Filters")
years = st.sidebar.multiselect("Year", sorted(df["Year"].unique()), default=sorted(df["Year"].unique()))
regions = st.sidebar.multiselect("Region", sorted(df["Region"].unique()), default=sorted(df["Region"].unique()))
products = st.sidebar.multiselect("Product", sorted(df["Product"].unique()), default=sorted(df["Product"].unique()))
filtered = df[df["Year"].isin(years) & df["Region"].isin(regions) & df["Product"].isin(products)]
a, b, c = st.columns(3)
a.metric("Total Sales", f"₹{filtered['Sales'].sum():,}")
b.metric("Average Sale", f"₹{filtered['Sales'].mean():,.0f}" if len(filtered) else "₹0")
c.metric("Records", len(filtered))
if filtered.empty:
    st.warning("No records match these filters. Select at least one option in each filter.")
else:
    left, right = st.columns(2)
    with left:
        st.subheader("Sales by Region")
        st.bar_chart(filtered.groupby("Region")["Sales"].sum())
    with right:
        st.subheader("Sales by Year")
        st.line_chart(filtered.groupby("Year")["Sales"].sum())
    st.subheader("Sales share by Product")
    st.bar_chart(filtered.groupby("Product")["Sales"].sum())
st.dataframe(filtered, use_container_width=True)
st.download_button("Download Filtered CSV", filtered.to_csv(index=False).encode("utf-8"),
                   "filtered_sales.csv", "text/csv")
