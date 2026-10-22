import streamlit as st
import pandas as pd
from io import StringIO

st.set_page_config(page_title="CSV Analyzer", layout="wide")
st.title("Upload CSV and Analyze")
sample = pd.DataFrame({
    "name": ["Ravi", "Priya", "Arjun", "Sneha"],
    "math": [85, 92, 70, 88],
    "science": [78, 88, 65, 91],
    "english": [90, 95, 72, 85],
})
st.download_button("Download sample CSV", sample.to_csv(index=False).encode("utf-8"),
                   "students.csv", "text/csv")
uploaded = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded:
    try:
        df = pd.read_csv(uploaded)
    except Exception as exc:
        st.error(f"Could not read CSV: {exc}")
        st.stop()
else:
    st.info("Showing sample data until you upload a CSV.")
    df = sample.copy()

st.subheader("Data Preview")
st.dataframe(df, use_container_width=True)
st.subheader("Statistics")
st.dataframe(df.describe(include="all").transpose(), use_container_width=True)
st.subheader("Missing values")
st.write(df.isna().sum())
missing_action = st.radio("Handle missing values", ["Keep", "Drop rows with missing values", "Fill numeric missing values with 0"])
if missing_action == "Drop rows with missing values":
    df = df.dropna()
elif missing_action == "Fill numeric missing values with 0":
    numeric = df.select_dtypes(include="number").columns
    df[numeric] = df[numeric].fillna(0)

st.subheader("Filter")
col = st.selectbox("Choose a column to filter", list(df.columns))
value = st.text_input("Contains (leave blank to show all)")
filtered = df[df[col].astype(str).str.contains(value, case=False, na=False)] if value else df
st.dataframe(filtered, use_container_width=True)
sort_col = st.selectbox("Sort by", list(df.columns), key="sort_column")
st.subheader("Sorted data")
st.dataframe(df.sort_values(sort_col, kind="stable"), use_container_width=True)
numeric_cols = df.select_dtypes(include="number").columns.tolist()
if numeric_cols:
    group_col = st.selectbox("Group averages by", list(df.columns))
    st.subheader("Group averages")
    st.dataframe(df.groupby(group_col, dropna=False)[numeric_cols].mean(numeric_only=True))
st.download_button("Download processed CSV", df.to_csv(index=False).encode("utf-8"),
                   "processed.csv", "text/csv")
