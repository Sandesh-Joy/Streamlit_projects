import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Visualization", layout="wide")
st.title("Data Visualization")
rng = np.random.default_rng(42)
df = pd.DataFrame(rng.normal(loc=70, scale=12, size=(20, 3)),
                  columns=["Math", "Science", "English"])
st.subheader("Sample marks data")
st.dataframe(df.round(1), use_container_width=True)
st.subheader("Built-in charts")
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)
st.subheader("Matplotlib histogram")
fig, ax = plt.subplots()
ax.hist(df["Math"], bins=10)
ax.set_title("Math Score Distribution")
ax.set_xlabel("Marks")
ax.set_ylabel("Frequency")
st.pyplot(fig)
st.metric("Average Math Score", f"{df['Math'].mean():.2f}")
st.scatter_chart(df, x="Math", y="Science")
