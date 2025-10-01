import streamlit as st
import pickle
import numpy as np

# Load trained model and encoder
with open("xgb.pkl", "rb") as f:
    model = pickle.load(f)

with open("Encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

st.set_page_config(page_title="Network Anomaly Detection", layout="wide")
st.title("🚀 Network Intrusion Detection (Normal / Anomaly)")

st.write("Enter the values below to check if traffic is **Normal** or **Anomaly**:")

# User Inputs
protocol_type = st.selectbox("Protocol Type", ["tcp", "udp", "icmp"])
duration = st.number_input("Duration (in seconds)", min_value=0, step=1)
src_bytes = st.number_input("Source Bytes", min_value=0, step=1)
dst_bytes = st.number_input("Destination Bytes", min_value=0, step=1)

# Predict button
if st.button("🔍 Predict"):
    # Encode protocol_type
    protocol_encoded = encoder.transform([protocol_type])[0]

    # Prepare input features
    features = np.array([[protocol_encoded, duration, src_bytes, dst_bytes]])

    # Prediction
    pred = model.predict(features)[0]

    # Decode: 0 = Normal, 1 = Anomaly (तूने training में class encode किया था)
    if pred == 0:
        st.success("✅ Prediction: NORMAL Traffic")
    else:
        st.error("⚠️ Prediction: ANOMALY Detected")
