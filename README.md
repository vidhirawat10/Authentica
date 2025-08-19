# 🛡️ Authentica
**Unmasking the Fake and Generating Authenticity in Every Pixel, Word, and Voice.**

---

<p align="center">
  <img src="https://img.shields.io/badge/AI-Deepfake%20Detection-blueviolet?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-Under%20Development-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" />
</p>

---

## 📌 Overview
Authentica is an **AI/ML-powered multi-modal deepfake detection system** that verifies whether a given **text, image, audio, or video** is **real or AI-generated (deepfake)**.  
It aims to provide **trust, transparency, and explainability** in an era where generative AI can create hyper-realistic synthetic content.  

---

## ✨ Features
- 📝 **Text Detection** – Identify AI-generated or human-written text.  
- 🖼️ **Image Detection** – Spot GAN-generated/manipulated images with heatmap highlights.  
- 🎙️ **Audio Detection** – Detect voice cloning and synthetic speech.  
- 🎥 **Video Detection** – Flag manipulated faces, lip-sync mismatches, and frame-level artifacts.  
- 🔎 **Explainability** – Grad-CAM for images/videos, highlighted text sections, and spectrogram regions for audio.  
- 🌐 **Web App + API** – Upload or provide a link, and get instant authenticity results with confidence scores.  

---

## 🏗️ System Architecture

[Input: Text / Image / Audio / Video] <br>
          │<br>
   ┌──────┴────────┐<br>
   │   Type Router │<br>
   └──────┬────────┘<br>
          │<br>
 ┌────────┼─────────┬─────────┬─────────┐<br>
 │        │         │         │         │<br>
Text  Image     Audio     Video    (Future: Docs)<br>
 │        │         │         │<br>
 └────────┴─────────┴─────────┴─────────┘<br>
          │<br>
   [Fusion + Calibrator]<br>
          │<br>
   [Decision + Explanation]<br>

   
---

## ⚙️ Tech Stack
- **Frameworks**: PyTorch, HuggingFace Transformers, TorchAudio, Streamlit, FastAPI  
- **Text**: RoBERTa/DeBERTa + stylometry features  
- **Image**: EfficientNet / Vision Transformers + FFT/DCT analysis  
- **Audio**: ResNet + Mel-Spectrogram + CQCC features  
- **Video**: Frame-level CNN + Temporal model (LSTM / TimeSformer)  
- **Backend**: FastAPI  
- **Frontend**: Streamlit (demo UI)  
- **Storage**: MinIO / S3 for uploads, PostgreSQL for metadata  

---

## 📊 Datasets Used
- **Text**: [HC3](https://arxiv.org/abs/2301.07597), GPT-generated corpora  
- **Image**: [FaceForensics++](https://github.com/ondyari/FaceForensics), StyleGAN/ProGAN, DeeperForensics  
- **Audio**: [ASVspoof](https://datashare.ed.ac.uk/handle/10283/3336), WaveFake, Fake or Real Speech  
- **Video**: Celeb-DF v2, DFDC, FaceForensics++  

---

## 🚀 Roadmap
- ✅ Phase 1: Text & Image deepfake detection  
- 🔄 Phase 2: Add Audio & Video modules  
- 🔮 Phase 3: Multi-modal fusion + explainability dashboard  
- 🌍 Phase 4: Real-world deployment with API & UI  

---

## 📈 Evaluation Metrics
- **Text**: AUC, F1, Perplexity-robustness  
- **Image/Video**: AUC, EER, Grad-CAM visualization  
- **Audio**: t-DCF, EER, channel robustness tests  
- **Cross-dataset generalization** for real-world performance  

---

## 🧪 Example Output (Demo Ideas)
- ✅ Upload an **image** → Result: *Fake, 92% confidence* → Heatmap highlighting manipulated regions.  
- ✅ Upload **text** → Result: *AI-Generated, 87% confidence* → Highlighted unnatural phrasing.  
- ✅ Upload **audio** → Result: *Cloned Voice, 95% confidence* → Spectrogram marking anomalies.  
- ✅ Upload **video** → Result: *Deepfake, 90% confidence* → Marked frames with artifacts.  

---

## ⚠️ Ethical Disclaimer
Authentica is a **probabilistic system**. Predictions should **not** be considered absolute proof.  
It is designed to **assist in detecting synthetic content**, not to make final judgments.  

---

## 👩‍💻 Contributors
- **Vidhi Rawat** – Data Science & Machine Learning Enthusiast ✨  
- (Add collaborators here)  

---

## 🌟 Future Vision
Authentica will evolve into a **trust layer for the internet**, enabling:  
- Safer social media & journalism  
- Fraud prevention in finance & politics  
- Protection against misinformation  

---

## 📜 License
Distributed under the [MIT License](LICENSE).  
You are free to use and modify for research and educational purposes.  

---

<p align="center">  
  Made with ❤️ by Vidhi Rawat  
</p>

