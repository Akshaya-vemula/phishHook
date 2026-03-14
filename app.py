import streamlit as st
import pickle
import time
import pandas as pd

# Suspicious keywords
suspicious_keywords = [
    "verify",
    "password",
    "urgent",
    "suspend",
    "account",
    "login",
    "click",
    "bank",
    "update",
    "security"
]

# Load ML model
model = pickle.load(open("model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

# Page configuration
st.set_page_config(page_title="PhishHook", page_icon="🛡️", layout="wide")

# Custom styling
st.markdown("""
<style>
.big-title {
    font-size:50px;
    font-weight:bold;
    color:#00c8ff;
}
.subtitle {
    font-size:20px;
    color:gray;
}
.feature-card {
    padding:20px;
    border-radius:10px;
    background-color:#0e1117;
    border:1px solid #00c8ff;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="big-title">🛡️ PhishHook</p>', unsafe_allow_html=True)

st.warning("⚠ Phishing attacks account for over 80% of cyber incidents worldwide.")

# Animated intro
intro_text = "AI-Powered Phishing Detection System"
placeholder = st.empty()
display = ""

for char in intro_text:
    display += char
    placeholder.markdown(f'<p class="subtitle">{display}</p>', unsafe_allow_html=True)
    time.sleep(0.03)

st.write("Protect your organization from phishing emails and malicious links.")

# Dashboard metrics
col1, col2, col3 = st.columns(3)
col1.metric("Emails Scanned Today", "1,284")
col2.metric("Phishing Detected", "312")
col3.metric("Threat Level", "Medium ⚠")

st.divider()

# Feature cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="feature-card">📧 Email Content Analysis</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="feature-card">🔗 Suspicious URL Detection</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="feature-card">⚡ Real-Time Risk Scoring</div>', unsafe_allow_html=True)

# Chart
st.subheader("📊 Weekly Phishing Activity")

data = pd.DataFrame({
    "Day": ["Mon","Tue","Wed","Thu","Fri"],
    "Attacks": [12,18,25,20,30]
})

st.line_chart(data.set_index("Day"))

st.divider()

# Email input
st.subheader("📩 Email Analysis")

email_text = st.text_area("Paste Email Content")

if st.button("Load Example Phishing Email"):
    email_text = "Your bank account will be suspended. Click here to verify immediately."

url = st.text_input("Enter URL (optional)")

analyze = st.button("🔍 Analyze Email")

# Prediction
if analyze:

    with st.spinner("🔎 Running Security Scan..."):
        progress_bar = st.progress(0)

        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)

    email_vector = vectorizer.transform([email_text])
    # ML prediction
    prediction = model.predict(email_vector)[0]
    prob = model.predict_proba(email_vector)

    risk_score = int(prob.max() * 100)

    # Detect suspicious keywords
    found_keywords = []

    for word in suspicious_keywords:
        if word in email_text.lower():
            found_keywords.append(word)

    st.divider()
    st.subheader("📊 Detection Result")

    st.metric("Risk Score", f"{risk_score}%")

    if prediction == "phishing":
        st.error("⚠ High Phishing Risk Detected")
    else:
        st.success("✅ Email appears safe")

    # Show detected keywords
    if found_keywords:
        st.subheader("⚠ Suspicious Keywords Detected")

        for word in found_keywords:
            st.write(f"• {word}")

    st.write("### Possible Reasons")

    st.write("• Suspicious keywords detected")
    st.write("• Unknown sender domain")
    st.write("• Suspicious URL pattern")

    st.info("Recommendation: Avoid clicking unknown links and verify the sender before taking action.")

st.divider()

st.markdown("🔐 Built by **Team CyberGuardians** | Hackathon Prototype")