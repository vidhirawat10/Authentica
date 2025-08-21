import streamlit as st
from transformers import pipeline, AutoModelForImageClassification, AutoFeatureExtractor
import time
from PIL import Image
import torch

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

# Text Models
@st.cache_resource
def get_text_detectors():
    detector1 = pipeline("text-classification", model="roberta-large-openai-detector")
    detector2 = pipeline("text-classification", model="Hello-SimpleAI/chatgpt-detector-roberta")
    return detector1, detector2

# SIMPLIFIED: Load only ONE reliable image model and its feature extractor
@st.cache_resource
def get_image_detector_manual():
    model_name = "umm-maybe/AI-image-detector"
    model = AutoModelForImageClassification.from_pretrained(model_name)
    feature_extractor = AutoFeatureExtractor.from_pretrained(model_name)
    return model, feature_extractor

text_detector1, text_detector2 = get_text_detectors()
image_model, image_feature_extractor = get_image_detector_manual()


# --- Helper Functions ---
def analyze_text(text):
    result1 = text_detector1(text)[0]
    score1_ai = 1 - result1['score'] if result1['label'] == 'LABEL_0' else result1['score']
    
    result2 = text_detector2(text)[0]
    score2_ai = 1 - result2['score'] if result2['label'].lower() == 'human' else result2['score']
    
    final_score_ai = (score1_ai * 0.25) + (score2_ai * 0.75)
    
    explanation = f"""
**Multi-Model Analysis:**
- Primary Detector (ChatGPT Focus) Confidence: **{score2_ai:.2%}**
- Secondary Detector (General Purpose) Confidence: **{score1_ai:.2%}**
"""
    return final_score_ai, explanation

# REWRITTEN FOR DEBUGGING AND SIMPLICITY
def analyze_image(image_file, model, feature_extractor):
    """
    Analyzes an image using a single model with detailed debug output.
    """
    img = Image.open(image_file).convert("RGB")
    inputs = feature_extractor(images=img, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)
    
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)[0]
    
    # Get the model's label mapping from its configuration
    # id2label = {0: 'real', 1: 'artificial'}
    real_score = probabilities[0].item()
    ai_score = probabilities[1].item()

    # The final score is simply the probability of the 'artificial' class
    final_score = ai_score

    # Create a detailed explanation for debugging
    explanation = f"""
**Model Analysis Breakdown:**
This shows the model's confidence for each possible label.

- **`real` Probability:** `{real_score:.2%}`
- **`artificial` Probability:** `{ai_score:.2%}`
    """
    return final_score, explanation

def analyze_file(uploaded_file):
    file_type = uploaded_file.type
    
    if "image" in file_type:
        return analyze_image(uploaded_file, image_model, image_feature_extractor)
    elif "audio" in file_type:
        time.sleep(2)
        return 0.25, "Audio analysis is not yet implemented."
    # ... (rest of the placeholders)
    else:
        return None, "Unsupported file type."

# --- UI Sections (Header and Main App) ---
# Your UI code remains exactly the same, no changes needed here.

# --- UI: Header ---
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
                
                if score is not None:
                    # Let's use a standard 50% threshold for now
                    if score > 0.5:
                        st.error("Result: AI-Generated / Deepfake")
                    else:
                        st.success("Result: Likely Real / Authentic")
                    
                    st.metric(
                        label="AI-Generated Confidence",
                        value=f"{score:.2%}",
                        delta=f"{score - 0.5:.2%}",
                        delta_color="inverse"
                    )
                    st.info(f"**Explanation:** {explanation}")
                else:
                    st.warning(explanation)

# --- Column 2: Text Analysis ---
with col2:
    st.markdown("## ✍️ Text Analysis", unsafe_allow_html=True)
    text_input = st.text_area(
        "Paste the text you want to analyze here...",
        height=200,
        label_visibility="collapsed"
    )

    MIN_TEXT_LENGTH = 50

    if st.button("Analyze Text", key="text_analyze_button"):
        if text_input and len(text_input) >= MIN_TEXT_LENGTH:
            with st.spinner('Analyzing text... Please wait.'):
                score, explanation = analyze_text(text_input)

                if score > 0.5:
                    st.error("Result: AI-Generated")
                else:
                    st.success("Result: Likely Human-Written")

                st.metric(
                    label="AI-Generated Confidence",
                    value=f"{score:.2%}",
                    delta=f"{score - 0.5:.2%}",
                    delta_color="inverse"
                )
                st.info(f"**Explanation:** {explanation}")
        elif text_input:
            st.warning(f"Please enter at least {MIN_TEXT_LENGTH} characters for an accurate analysis.")
        else:
            st.warning("Please paste some text to analyze.")