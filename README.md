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
      <br>│<br>
 ┌────────┼─────────┬─────────┬─────────┐<br>
 │        │         │         │         │<br>
Text  Image     Audio     Video    (Future: Docs)<br>
 │        │         │         │<br>
 └────────┴─────────┴─────────┴─────────┘<br>
      <br>│<br>
   [Fusion + Calibrator]<br>
      <br>│<br>
   [Decision + Explanation]<br>
