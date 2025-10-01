import streamlit as st
import pickle
import base64
import numpy as np


st.set_page_config(page_title="Network Anomaly Detection", layout="wide")
# Function to set local image as background

def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
    }}
    .overlay-box {{
        background-color: rgba(0,0,0,0.6);
        padding: 20px;
        border-radius: 15px;
        max-width: 450px;
        margin: auto;
        color: white;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Load model & encoder
with open("xgb.pkl", "rb") as f:
    model = pickle.load(f)
with open("Encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

set_bg("network-intrusion-detection-system-768x384.jpg")

# Overlay form
st.markdown('<div class="overlay-box">', unsafe_allow_html=True)

st.title("🚀 Network Anomaly Detection")
st.write("Fill details below to check if traffic is Normal or Anomaly:")

# Inputs
protocol_type = st.selectbox("Protocol Type", ["tcp", "udp", "icmp"])
duration = st.number_input("Duration (seconds)", min_value=0, step=1)
src_bytes = st.number_input("Source Bytes", min_value=0, step=1)
dst_bytes = st.number_input("Destination Bytes", min_value=0, step=1)

# Predict
if st.button("🔍 Predict"):
    protocol_encoded = encoder.transform([protocol_type])[0]
    features = np.array([[protocol_encoded, duration, src_bytes, dst_bytes]])
    pred = model.predict(features)[0]

    if pred == 0:
        st.success("✅ Prediction: NORMAL Traffic")
    else:
        st.error("⚠️ Prediction: ANOMALY Detected")

st.markdown('</div>', unsafe_allow_html=True)
