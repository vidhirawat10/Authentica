import streamlit as st
from transformers import pipeline
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="Authentica | Deepfake Detector",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS ---
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Call this function to load the CSS file from the .streamlit folder
load_css(".streamlit/style.css")


# --- Model Loading ---
# Using st.cache_resource to load the model only once
@st.cache_resource
def get_text_detector():
    return pipeline("text-classification", model="roberta-base-openai-detector")

text_detector = get_text_detector()

# --- Helper Functions ---
def analyze_text(text):
    """Analyzes text using a real Hugging Face model."""
    result = text_detector(text)
    score_real = result[0]['score']
    
    if result[0]['label'] == 'Real':
        score_ai = 1 - score_real
        explanation = f"The model is {score_real:.1%} confident that this text is human-written."
    else:
        score_ai = score_real
        explanation = f"The model is {score_ai:.1%} confident that this text is AI-generated, based on its linguistic patterns."
        
    return score_ai, explanation

def analyze_file(uploaded_file):
    """Placeholder for file analysis."""
    time.sleep(2) # Simulate model running
    # This is a placeholder
    return 0.12, "File analysis is not yet implemented. This is a placeholder result."

# --- UI: Header Section ---
with st.container():
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    st.title("Authentica: Multi-Modal Deepfake Detector")
    st.markdown("<h3>Detect AI-generated content across text, images, audio, and video with confidence.</h3>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("---")


# --- UI: Main Application ---
col1, col2 = st.columns(2, gap="large")

# --- Column 1: File Analysis ---
with col1:
    st.markdown("## 📁 File Analysis", unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Upload a document, image, audio, or video file",
        type=['txt', 'pdf', 'png', 'jpg', 'jpeg', 'mp3', 'wav', 'mp4', 'mov'],
        label_visibility="collapsed"
    )

    if uploaded_file is not None:
        if st.button("Analyze File", key="file_analyze_button"):
            with st.spinner('Analyzing file... Please wait.'):
                score, explanation = analyze_file(uploaded_file)
                
                if score > 0.5:
                    st.error("Result: AI-Generated / Deepfake")
                else:
                    st.success("Result: Likely Real / Authentic")
                
                # Display result with st.metric for a nicer look
                st.metric(
                    label="AI-Generated Confidence",
                    value=f"{score:.2%}",
                    delta=f"{score - 0.5:.2%}",
                    delta_color="inverse"
                )
                st.info(f"**Explanation:** {explanation}")

# --- Column 2: Text Analysis ---
with col2:
    st.markdown("## ✍️ Text Analysis", unsafe_allow_html=True)
    text_input = st.text_area(
        "Paste the text you want to analyze here...",
        height=200,
        label_visibility="collapsed"
    )

    if st.button("Analyze Text", key="text_analyze_button"):
        if text_input:
            with st.spinner('Analyzing text... Please wait.'):
                score, explanation = analyze_text(text_input)

                if score > 0.5:
                    st.error("Result: AI-Generated")
                else:
                    st.success("Result: Likely Human-Written")

                st.metric(
                    label="AI-Generated Confidence",
                    value=f"{score:.2%}",
                    delta=f"{score - 0.5:.2%}", # Shows deviation from the 50% threshold
                    delta_color="inverse" # Red for positive delta, Green for negative
                )
                st.info(f"**Explanation:** {explanation}")
        else:
            st.warning("Please paste some text to analyze.")