import streamlit as st

st.set_page_config(page_title="Hello Streamlit", page_icon="👋", layout="wide")
st.title("Hello Streamlit")
st.header("My First App")
st.subheader("Learning Basics")
st.write("Streamlit converts Python scripts into interactive web apps.")
st.markdown("**Bold**, *italic*, and `inline code` work here.")
st.success("App loaded successfully!")
st.info("This is an information message.")
st.warning("This is a warning message.")
st.error("This is an example error message.")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=1, max_value=100, value=18)
st.subheader("Sample Data")
st.table({"Name": ["A", "B"], "Marks": [85, 90]})
if name:
    st.write(f"Hello, {name}! You are {age} years old.")
st.code("def greet(name):\n    return f'Hello, {name}!'")
st.divider()
st.caption("Lab 1 — Basic Streamlit commands")
