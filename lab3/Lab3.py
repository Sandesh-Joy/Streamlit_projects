import streamlit as st
import pandas as pd

st.set_page_config(page_title="Layouts Demo", layout="wide")
st.title("Layouts Demo")
st.sidebar.header("Settings")
theme = st.sidebar.selectbox("Theme", ["Light", "Dark"])
font_size = st.sidebar.slider("Font size", 10, 30, 15)
st.sidebar.write(f"Selected theme: {theme}; font size: {font_size}px")

c1, c2, c3 = st.columns([1, 2, 1])
c1.metric("Total Sales", "₹25 lakh")
c2.metric("Customers", "1,200", "+8%")
c3.metric("Orders", "420", "+12%")

overview, analysis, about = st.tabs(["Overview", "Analysis", "About"])
with overview:
    st.write("Overview of the application and its key performance indicators.")
    st.bar_chart(pd.DataFrame({"Sales": [12, 18, 15, 24]}, index=["Q1", "Q2", "Q3", "Q4"]))
with analysis:
    st.write("Quarterly sales analysis.")
    st.line_chart(pd.DataFrame({"Sales": [12, 18, 15, 24]}, index=["Q1", "Q2", "Q3", "Q4"]))
with about:
    st.write("This application demonstrates Streamlit layout components.")
with st.container():
    st.subheader("Grouped Section")
    st.write("Elements can be grouped in a container.")
with st.expander("Details"):
    st.write("This section is hidden until expanded.")

