import streamlit as st

st.set_page_config(page_title="Forms and Session State")
st.title("Forms + Session State")
if "count" not in st.session_state:
    st.session_state.count = 0
if "todos" not in st.session_state:
    st.session_state.todos = []
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

left, mid, right = st.columns(3)
if left.button("Increment"):
    st.session_state.count += 1
if mid.button("Add 5"):
    st.session_state.count += 5
if right.button("Reset"):
    st.session_state.count = 0
st.metric("Counter", st.session_state.count)

with st.form("login_form"):
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")
if submitted:
    if username == "admin" and password == "1234":
        st.session_state.logged_in = True
        st.success("Login successful!")
    else:
        st.error("Invalid credentials. admin / 1234")
if st.session_state.logged_in:
    st.info("Welcome, admin! You are now logged in.")

with st.form("todo_form", clear_on_submit=True):
    task = st.text_input("New to-do task")
    add_task = st.form_submit_button("Add Task")
if add_task and task.strip():
    st.session_state.todos.append(task.strip())
st.subheader("Your Tasks")
if st.session_state.todos:
    for i, item in enumerate(st.session_state.todos, 1):
        st.write(f"{i}. {item}")
else:
    st.caption("No tasks yet.")
if st.button("Clear All Tasks"):
    st.session_state.todos = []
    st.rerun()
