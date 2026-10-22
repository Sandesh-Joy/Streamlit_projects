import streamlit as st
from datetime import date

st.set_page_config(page_title="Widgets Playground", page_icon="🎛️")
st.title("Widgets Playground")
name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=100, value=20)
marks = st.slider("Marks", 0, 100, 75)
city = st.selectbox("City", ["Chennai", "Mumbai", "Delhi"])
skills = st.multiselect("Skills", ["Python", "Machine Learning", "SQL", "Streamlit"])
gender = st.radio("Gender", ["Male", "Female", "Other"])
agree = st.checkbox("I agree to the terms")
dob = st.date_input("Date of Birth", date(2000, 1, 1))
uploaded = st.file_uploader("Upload a file")
color = st.color_picker("Pick a color", "#00AAFF")
mark_range = st.select_slider("Select a marks range", options=list(range(0, 101)), value=(40, 80))
if st.button("Submit"):
    st.subheader("Submitted values")
    st.write({"Name": name, "Age": age, "Marks": marks, "City": city,
              "Skills": skills, "Gender": gender, "Agreed": agree,
              "Date of birth": str(dob), "Colour": color, "Marks range": mark_range})
    st.write("Uploaded file:", uploaded.name if uploaded else "No file uploaded")
    st.write("Widget value types:", {"name": str(type(name)), "age": str(type(age)),
             "marks": str(type(marks)), "skills": str(type(skills)), "agreed": str(type(agree))})
