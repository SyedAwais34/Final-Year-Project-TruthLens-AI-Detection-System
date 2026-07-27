# 🛡️ TruthLens AI

> **An AI-Powered Deepfake Detection System for Image, Video, Audio, and Text using Python & Gradio**

TruthLens AI is a Final Year Project (FYP) developed to detect manipulated or AI-generated content across multiple media formats. The system analyzes **Images, Videos, Audio, and Text** using Artificial Intelligence and Machine Learning techniques, then provides a **Real/Fake prediction**, **confidence score**, and **detailed explanation** for every analysis.

---

# 📌 Features

## 🔐 Authentication
- User Login
- User Registration
- Secure Password Storage
- Session Management

---

## 🖼️ Image Deepfake Detection

- Upload JPG, PNG, JPEG images
- Detect manipulated or AI-generated images
- Confidence Score
- AI Explanation
- Image Preview

---

## 🎥 Video Deepfake Detection

- Upload MP4, AVI, MOV videos
- Frame-by-frame analysis
- Facial inconsistency detection
- Confidence Score
- AI-generated explanation

---

## 🎤 Audio Deepfake Detection

- Upload MP3 or WAV files
- Voice feature extraction
- Voice comparison
- Fake voice detection
- Confidence Score
- AI explanation

---

## 📰 Text Fake News Detection

- Analyze articles
- Detect misinformation
- Fake news classification
- AI confidence score
- Reason generation

---

## 📊 Dashboard

- Upload history
- Previous reports
- Statistics
- User profile
- Recent analyses

---

## 📄 Report Generation

Generate downloadable reports containing:

- Prediction
- Confidence Score
- AI Explanation
- Analysis Date
- Uploaded File Information

---

# 🚀 Technology Stack

## Frontend

- Python
- Gradio

## Backend

- Python

## Database

- MongoDB

## AI & Machine Learning

- PyTorch
- OpenCV
- Transformers
- Whisper
- Librosa
- NumPy
- Pandas

---

# 🏗️ System Architecture

```
                   User
                     │
                     ▼
             Gradio Interface
                     │
                     ▼
             Python Backend
                     │
      ┌──────────────┼──────────────┐
      │              │              │
      ▼              ▼              ▼
 Image Model     Audio Model     NLP Model
      │              │              │
      └──────────────┼──────────────┘
                     │
                     ▼
        AI Decision & Explanation
                     │
                     ▼
               MongoDB Database
                     │
                     ▼
             Reports & History
```

---

# 📂 Project Structure

```
TruthLens-AI/
│
├── app.py
├── assets/
├── models/
│   ├── image/
│   ├── video/
│   ├── audio/
│   └── text/
│
├── uploads/
├── reports/
├── database/
├── utils/
├── static/
├── history/
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/TruthLens-AI.git
```

```bash
cd TruthLens-AI
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

Application will start on:

```
http://127.0.0.1:7860
```

---

# 📁 Supported Formats

## Images

- JPG
- JPEG
- PNG

---

## Videos

- MP4
- AVI
- MOV

---

## Audio

- MP3
- WAV

---

## Text

- Plain Text
- News Articles
- Social Media Content

---

# 🔍 Detection Workflow

1. User logs into TruthLens AI.
2. Uploads Image, Video, Audio, or Text.
3. Python backend processes the input.
4. AI model analyzes the content.
5. Prediction is generated.
6. Confidence score is calculated.
7. Explanation is generated.
8. Results are stored in MongoDB.
9. Report is generated.
10. User can download the report.

---

# 💡 Future Improvements

- Live Camera Detection
- Real-time Video Detection
- API Integration
- Mobile Application
- Multi-language Support
- Explainable AI Improvements
- Cloud Deployment
- Batch Processing
- AI Model Optimization

---

# 🛡️ Security

- Password Hashing
- Secure Authentication
- MongoDB Data Storage
- File Validation
- Session Handling

---

# 📈 Project Goals

- Detect AI-generated images.
- Detect manipulated videos.
- Detect cloned voices.
- Detect fake news.
- Improve digital media authenticity.
- Help users identify misinformation.

---

# 👨‍💻 Developed By

**TruthLens AI Team**

Final Year Project

Bachelor of Software Engineering

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Acknowledgements

Special thanks to:

- Python
- Gradio
- MongoDB
- PyTorch
- OpenCV
- Hugging Face Transformers
- Open Source AI Community

---

# 📬 Contact

For questions or suggestions:

📧 your-email@example.com

---

## ⭐ If you like this project, don't forget to Star the repository!
