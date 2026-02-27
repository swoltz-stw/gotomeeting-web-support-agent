import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="GoToMeeting Support Agent",
    page_icon="🤝",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default chrome for a clean embed
st.markdown("""
    <style>
        #MainMenu, header, footer { visibility: hidden; }
        .block-container { padding: 0 !important; max-width: 100% !important; }
        .stApp { background: #0A1628; }
    </style>
""", unsafe_allow_html=True)

# Securely load API key from Streamlit secrets
try:
    api_key = st.secrets["ANTHROPIC_API_KEY"]
except KeyError:
    st.error("⚠️ Anthropic API key not found. Please add ANTHROPIC_API_KEY to your Streamlit secrets.")
    st.stop()

# Load the HTML widget file
html_file_path = os.path.join(os.path.dirname(__file__), "gotomeeting_agent.html")

try:
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Securely inject the API key into the HTML at runtime
    # The placeholder __ANTHROPIC_API_KEY__ is never stored with a real value in the file
    html_content = html_content.replace("__ANTHROPIC_API_KEY__", api_key)

    components.html(html_content, height=780, scrolling=False)

except FileNotFoundError:
    st.error("❌ Widget file not found. Make sure `gotomeeting_agent.html` is in the same folder as `app.py`.")
