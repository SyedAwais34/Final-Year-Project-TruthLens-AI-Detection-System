# 🛡️ TruthLens AI

**Advanced Fake Content Detection System** — a Gradio-based web app for detecting manipulated Images, Videos, Audio, and Text, with a built-in user authentication system.

> ⚠️ This is a **Final Year Project frontend**. Detection results are currently placeholder/dummy outputs — real AI model integration is pending (see [Roadmap](#-roadmap)).

---

## ✨ Features

- 🔐 **User Authentication** — Signup, Login, and Logout with secure password hashing (PBKDF2-HMAC-SHA256 + per-user salt)
- 🖼️ **Image Deepfake Detection** — upload and analyze images
- 🎥 **Video Deepfake Detection** — upload and analyze videos
- 🎤 **Audio Verification** — voice/speaker matching analysis
- 📝 **Text Misinformation Detection** — detect misleading or biased text
- 📜 **Analysis History** — view past detection results
- 📄 **Reports** — downloadable analysis reports (backend pending)
- 🎨 Custom **Aurora Violet** dark theme UI, fully responsive

---

## 🖥️ Tech Stack

| Layer      | Technology                     |
|------------|---------------------------------|
| UI         | [Gradio](https://gradio.app)    |
| Database   | SQLite3                         |
| Auth       | PBKDF2-HMAC-SHA256 password hashing |
| Language   | Python 3                        |

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/truthlens-ai.git
   cd truthlens-ai
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install gradio
   ```

---

## 🚀 Usage

Run the app:

```bash
python app.py
```

The app will launch locally at `http://127.0.0.1:7861` and also generate a temporary **public share link** (via `share=True`).

### How it works

1. **Signup** — Create an account with a username, email, and password (min. 6 characters).
2. **Login** — Sign in using your username *or* email.
3. Once logged in, the main dashboard unlocks with tabs for **Image, Video, Audio, and Text** detection.
4. **Logout** anytime to return to the login screen.

> The app requires login before any detection tool can be accessed — unauthenticated users only see the Login/Signup screen.

---

## 🗂️ Project Structure

```
truthlens-ai/
├── app.py                  # Main application (UI + auth + logic)
├── truthlens_users.db      # SQLite database (auto-created on first run)
└── README.md
```

---

## 🔒 Security Notes

- Passwords are **never stored in plain text** — each password is hashed with PBKDF2-HMAC-SHA256 (100,000 iterations) using a unique random salt per user.
- Password comparison uses `secrets.compare_digest` to prevent timing attacks.
- `truthlens_users.db` is created automatically on first run — **do not commit this file to GitHub** (see `.gitignore` below).

---

## 🧾 Suggested `.gitignore`

```
truthlens_users.db
__pycache__/
venv/
*.pyc
```

---

## 🛣️ Roadmap

- [ ] Integrate real AI deepfake detection models (image/video)
- [ ] Integrate voice similarity/speaker verification model
- [ ] Integrate NLP-based misinformation detection model
- [ ] Persist analysis history per user in the database
- [ ] Enable real PDF report generation and download
- [ ] Add "Forgot Password" / password reset flow
- [ ] Add email verification on signup

---

## 📊 Dashboard Stats (placeholder)

| Metric              | Value |
|----------------------|-------|
| Total Modules         | 4     |
| AI Models             | 4     |
| Detection Accuracy*   | 95%   |

\* Placeholder value — will reflect actual model performance once the AI backend is integrated.

---

## 📄 License

This project is developed as a **Final Year Project**. Add your preferred license here (e.g. MIT) if you plan to open-source it.

---

## 🙌 Acknowledgements

Built with [Gradio](https://gradio.app) — © 2026 TruthLens AI. All rights reserved.
