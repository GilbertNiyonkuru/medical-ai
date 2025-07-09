import streamlit as st
import pandas as pd
from analyzer import analyze_results
from recommender import generate_recommendations

st.title("🧠 Medical AI Assistant")

uploaded_file = st.file_uploader("Upload patient results (CSV)", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.subheader("📊 Uploaded Data")
    st.dataframe(data)

    if st.button("Analyze and Recommend"):
        analysis = analyze_results(data)
        recommendations = generate_recommendations(analysis)

        st.subheader("🩺 Analysis Summary")
        st.write(analysis)

        st.subheader("💊 Recommendations & Treatments")
        st.write(recommendations)
