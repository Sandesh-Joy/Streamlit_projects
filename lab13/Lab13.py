import streamlit as st

st.title("Lab 13: Login / Signup")

if "users" not in st.session_state:
    st.session_state.users = {}

option = st.selectbox("Choose an option", ["Signup", "Login"])

if option == "Signup":
    username = st.text_input("Create username")
    password = st.text_input("Create password", type="password")

    if st.button("Signup"):
        if username and password:
            if username in st.session_state.users:
                st.error("Username already exists")
            else:
                st.session_state.users[username] = password
                st.success("Signup successful! Please log in.")
        else:
            st.warning("Enter both username and password")

else:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in st.session_state.users and st.session_state.users[username] == password:
            st.success(f"Welcome, {username}!")
        else:
            st.error("Invalid username or password")