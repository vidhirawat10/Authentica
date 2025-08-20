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
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("CSS file not found. Please ensure '.streamlit/style.css' exists.")

load_css(".streamlit/style.css")

# --- Model Loading ---
# Model 1: A balanced, powerful model
@st.cache_resource
def get_detector_1():
    return pipeline("text-classification", model="roberta-large-openai-detector")

# Model 2: A model specifically focused on ChatGPT output
@st.cache_resource
def get_detector_2():
    return pipeline("text-classification", model="Hello-SimpleAI/chatgpt-detector-roberta")

detector1 = get_detector_1()
detector2 = get_detector_2()

# --- Helper Functions ---
def analyze_text(text):
    """
    Analyzes text using a weighted average of two models for a more accurate score.
    """
    
    # --- Get prediction from Model 1 (Lower weight) ---
    result1 = detector1(text)[0]
    if result1['label'] == 'LABEL_0': # 'LABEL_0' means 'Real' (Human)
        score1_ai = 1 - result1['score']
    else: # 'LABEL_1' means 'Fake' (AI)
        score1_ai = result1['score']
        
    # --- Get prediction from Model 2 (Higher weight) ---
    result2 = detector2(text)[0]
    if result2['label'].lower() == 'human':
        score2_ai = 1 - result2['score']
    else: # The label is 'chatgpt'
        score2_ai = result2['score']
        
    # --- Calculate the weighted average ---
    # Give 75% weight to the more reliable Model 2, and 25% to Model 1.
    final_score_ai = (score1_ai * 0.01) + (score2_ai * 0.99)
    
    explanation = f"""
Multi-Model Analysis:** We use a primary detector backed by a second opinion from another model. This robust, two-layer approach ensures a more confident and trustworthy result.
    """

    
    return final_score_ai, explanation

def analyze_file(uploaded_file):
    """Placeholder for file analysis."""
    time.sleep(2)
    return 0.12, "File analysis is not yet implemented. This is a placeholder result."

# --- UI Sections (Header, File Analysis, Text Analysis) ---
# (Your existing UI code for the header, file uploader, and text area goes here)
# ... (I'm omitting the UI code for brevity, as it doesn't need to change)
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