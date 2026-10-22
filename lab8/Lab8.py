from pathlib import Path
import streamlit as st
import joblib
import numpy as np
from sklearn.datasets import load_iris

st.set_page_config(page_title="Iris Flower Prediction")
st.title("Iris Flower Prediction")
model_path = Path(__file__).with_name("iris_model.joblib")
if not model_path.exists():
    st.warning("Model file not found. Run `python train_model.py` in this folder first.")
    st.stop()
model = joblib.load(model_path)
names = load_iris().target_names.tolist()
st.write("Enter flower measurements in centimetres.")
with st.form("prediction_form"):
    sl = st.slider("Sepal length", 4.0, 8.0, 5.1, 0.1)
    sw = st.slider("Sepal width", 2.0, 4.5, 3.5, 0.1)
    pl = st.slider("Petal length", 1.0, 7.0, 1.4, 0.1)
    pw = st.slider("Petal width", 0.1, 2.5, 0.2, 0.1)
    submit = st.form_submit_button("Predict species")
if submit:
    features = np.array([[sl, sw, pl, pw]])
    prediction = int(model.predict(features)[0])
    probabilities = model.predict_proba(features)[0]
    st.success(f"Predicted species: **{names[prediction].title()}**")
    st.metric("Model confidence", f"{probabilities.max() * 100:.1f}%")
    st.bar_chart({names[i].title(): float(probabilities[i]) for i in range(len(names))})
