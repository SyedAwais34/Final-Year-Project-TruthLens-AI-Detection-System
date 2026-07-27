import gradio as gr

# ============================================================
# Dummy Functions (Backend Later)
# ============================================================

def analyze_image(image):
    return (
        image,
        "⚠️ Fake",
        "92%",
        "High",
        "The uploaded image appears manipulated based on facial inconsistencies and abnormal lighting patterns.",
        "📄 Report generation will be available after backend integration."
    )


def analyze_video(video):
    return (
        "⚠️ Fake",
        "89%",
        "Medium",
        "Multiple frames contain facial inconsistencies and abnormal lip synchronization.",
        "📄 Report generation will be available after backend integration."
    )


def analyze_audio(audio):
    return (
        "✅ Real",
        "95%",
        "Matched Speaker",
        "The uploaded voice closely matches the reference database with 95% similarity.",
        "📄 Report generation will be available after backend integration."
    )


def analyze_text(text):
    return (
        "⚠️ Misleading",
        "84%",
        "Medium",
        "The text contains emotionally biased language and unsupported claims.",
        "📄 Report generation will be available after backend integration."
    )


# ============================================================
# Custom Theme — "Aurora Violet" Premium Color Scheme
# ============================================================

css = """
/* ======================================================
       TruthLens AI — Aurora Violet Premium Theme
====================================================== */

footer{
display:none!important;
}

body{
background:#071410!important;
margin:0!important;
min-height:100vh!important;
}

html{
background:#071410!important;
overflow-x:hidden!important;
}

body{
overflow-x:hidden!important;
}

gradio-app{
display:block!important;
background:linear-gradient(135deg,#071410,#0a2e22,#0f3d2e)!important;
min-height:100vh!important;
width:100%!important;
}

.gradio-container{
max-width:1600px!important;
width:100%!important;
margin:auto!important;
background:linear-gradient(135deg,#071410,#0a2e22,#0f3d2e)!important;
padding:0 25px 25px 25px!important;
min-height:100vh!important;
box-sizing:border-box!important;
}

/* ================= Cards ================= */

.block{
background:rgba(255,255,255,.05)!important;
backdrop-filter:blur(20px);
border-radius:18px!important;
border:1px solid rgba(110,231,183,.12)!important;
padding:20px!important;
box-shadow:0 15px 35px rgba(0,0,0,.45);
}

/* ================= Text ================= */

h1{
color:white!important;
font-size:42px!important;
text-align:center;
font-weight:700;
}

h2{
color:#6ee7b7!important;
}

h3{
color:white!important;
}

p{
color:#f1f5f9!important;
}

label{
color:white!important;
}

/* Markdown Fix */

.prose{
color:white!important;
}

.prose p{
color:white!important;
}

.prose li{
color:white!important;
}

.prose strong{
color:#fbbf24!important;
}

.gr-markdown{
color:white!important;
}

/* ================= Header ================= */

#tl-header{
position:sticky;
top:0;
z-index:1000;
margin:0 -25px 20px -25px;
padding:16px 30px!important;
background:rgba(13,11,30,.85)!important;
backdrop-filter:blur(16px);
border:none!important;
border-bottom:1px solid rgba(192,132,252,.3)!important;
border-radius:0!important;
box-shadow:0 8px 25px rgba(0,0,0,.4);
}

#tl-header .header-inner{
display:flex;
align-items:center;
justify-content:space-between;
flex-wrap:wrap;
gap:10px;
max-width:1600px;
margin:auto;
}

#tl-header h1{
font-size:26px!important;
text-align:left;
margin:0!important;
white-space:nowrap;
background:linear-gradient(90deg,#a7f3d0,#fbbf24);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
background-clip:text;
}

#tl-header .tagline{
color:#6ee7b7!important;
font-size:14px!important;
margin:0!important;
}

#tl-header .badges{
display:flex;
gap:8px;
flex-wrap:wrap;
justify-content:flex-end;
}

#tl-header .badges span{
background:rgba(52,211,153,.18);
border:1px solid rgba(110,231,183,.4);
color:#a7f3d0!important;
font-size:12px!important;
padding:5px 12px;
border-radius:999px;
white-space:nowrap;
}

/* ================= Hero ================= */

#tl-hero{
text-align:center;
padding:10px 10px 4px 10px!important;
background:transparent!important;
border:none!important;
box-shadow:none!important;
}

#tl-hero p{
font-size:16px!important;
}

/* ================= Tabs ================= */

button[role="tab"]{
background:#113328!important;
color:white!important;
border-radius:10px!important;
padding:10px 20px!important;
margin-right:8px!important;
}

button[role="tab"]:hover{
background:#10b981!important;
}

button[aria-selected="true"]{
background:linear-gradient(90deg,#10b981,#34d399)!important;
}

/* ================= Buttons ================= */

button{
border-radius:12px!important;
font-weight:bold!important;
transition:.3s;
}

button:hover{
transform:translateY(-2px);
}

.gr-button-primary, button.primary{
background:linear-gradient(90deg,#10b981,#059669)!important;
border:none!important;
color:white!important;
}

.gr-button-primary:hover, button.primary:hover{
background:linear-gradient(90deg,#8b5cf6,#2dd4bf)!important;
box-shadow:0 8px 20px rgba(52,211,153,.4);
}

/* ================= Inputs ================= */

textarea,
input{
background:#0d1f1a!important;
color:white!important;
border:1px solid #1e4a3a!important;
}

textarea:focus,
input:focus{
border:1px solid #34d399!important;
box-shadow:0 0 0 2px rgba(52,211,153,.25)!important;
}

/* ================= Upload ================= */

img{
border-radius:15px!important;
}

video{
border-radius:15px!important;
}

/* ================= Table ================= */

table{
background:#0d1f1a!important;
color:white!important;
}

/* ================= Footer ================= */

#tl-footer{
margin:30px -25px 0 -25px;
padding:30px 25px 20px 25px!important;
background:rgba(26,19,50,.6)!important;
border:none!important;
border-top:1px solid rgba(192,132,252,.25)!important;
border-radius:0!important;
box-shadow:none!important;
text-align:center;
}

#tl-footer .footer-links{
display:flex;
justify-content:center;
gap:22px;
flex-wrap:wrap;
margin:10px 0 14px 0;
}

#tl-footer .footer-links span{
color:#6ee7b7!important;
font-size:14px!important;
}

#tl-footer .copyright{
color:#4d7a68!important;
font-size:13px!important;
}

/* ================= Scroll ================= */

::-webkit-scrollbar{
width:8px;
}

::-webkit-scrollbar-thumb{
background:#10b981;
border-radius:20px;
}

/* ================= Responsive ================= */

@media(max-width:1200px){
.gradio-container{
width:98%!important;
padding:0 15px 15px 15px!important;
}
#tl-header{
margin:0 -15px 16px -15px;
padding:14px 18px!important;
}
#tl-footer{
margin:24px -15px 0 -15px;
padding:24px 18px 16px 18px!important;
}
}

@media(max-width:900px){
#tl-header .header-inner{
justify-content:center;
text-align:center;
}
#tl-header h1{
text-align:center;
width:100%;
}
#tl-header .badges{
justify-content:center;
width:100%;
}
}

@media(max-width:768px){
h1{
font-size:26px!important;
}
#tl-header h1{
font-size:20px!important;
}
#tl-hero h1{
font-size:26px!important;
}
button{
width:100%!important;
}
button[role="tab"]{
padding:8px 12px!important;
font-size:13px!important;
margin-right:4px!important;
}
.block{
padding:14px!important;
}
}

@media(max-width:480px){
#tl-header .badges span{
font-size:11px!important;
padding:4px 9px;
}
#tl-footer .footer-links{
gap:12px;
}
}

"""


theme = gr.themes.Soft(
    primary_hue="emerald",
    secondary_hue="teal",
)

# ============================================================
# Main App
# ============================================================

with gr.Blocks(
    title="TruthLens AI",
    theme=theme,
    css=css,
) as demo:

    # ============================================================
    # HEADER
    # ============================================================

    gr.HTML(
        """
        <div class="header-inner">
            <div>
                <h1>🛡️ TruthLens AI</h1>
                <p class="tagline">Advanced Fake Content Detection System</p>
            </div>
            <div class="badges">
                <span>🖼 Image</span>
                <span>🎥 Video</span>
                <span>🎤 Audio</span>
                <span>📝 Text</span>
            </div>
        </div>
        """,
        elem_id="tl-header"
    )

    gr.Markdown(
        "Detect fake **Images • Videos • Audio • Text** using AI-powered analysis.",
        elem_id="tl-hero"
    )

    with gr.Tabs():
        # ============================================================
        # IMAGE TAB
        # ============================================================

        with gr.Tab("🖼 Image Detection"):

            gr.Markdown("## Upload an Image")

            with gr.Row():

                with gr.Column(scale=1, min_width=260):

                    image_input = gr.Image(
                        type="filepath",
                        label="Upload Image"
                    )

                    image_btn = gr.Button(
                        "🔍 Analyze Image",
                        variant="primary"
                    )

                with gr.Column(scale=1, min_width=260):

                    image_preview = gr.Image(
                        label="Preview"
                    )

            gr.Markdown("---")

            with gr.Row():

                image_result = gr.Textbox(
                    label="Detection Result"
                )

                image_confidence = gr.Textbox(
                    label="Confidence Score"
                )

                image_risk = gr.Textbox(
                    label="Risk Level"
                )

            image_reason = gr.Textbox(
                lines=5,
                label="AI Explanation"
            )

            image_report = gr.Textbox(
                lines=2,
                label="Report Status"
            )

            image_btn.click(
                analyze_image,
                inputs=image_input,
                outputs=[
                    image_preview,
                    image_result,
                    image_confidence,
                    image_risk,
                    image_reason,
                    image_report
                ]
            )

        # ============================================================
        # VIDEO DETECTION TAB
        # ============================================================

        with gr.Tab("🎥 Video Detection"):

            gr.Markdown("## Upload a Video")

            with gr.Row():

                with gr.Column(scale=1, min_width=260):

                    video_input = gr.Video(
                        label="Upload Video"
                    )

                    video_btn = gr.Button(
                        "🎬 Analyze Video",
                        variant="primary"
                    )

                with gr.Column(scale=1, min_width=260):

                    gr.Markdown("""
### Supported Formats

✅ MP4

✅ AVI

✅ MOV

Maximum Size: 500 MB
""")

            gr.Markdown("---")

            with gr.Row():

                video_result = gr.Textbox(
                    label="Detection Result"
                )

                video_confidence = gr.Textbox(
                    label="Confidence Score"
                )

                video_risk = gr.Textbox(
                    label="Risk Level"
                )

            video_reason = gr.Textbox(
                label="AI Explanation",
                lines=5
            )

            video_report = gr.Textbox(
                label="Report Status",
                lines=2
            )

            video_btn.click(
                analyze_video,
                inputs=video_input,
                outputs=[
                    video_result,
                    video_confidence,
                    video_risk,
                    video_reason,
                    video_report
                ]
            )

        # ============================================================
        # AUDIO DETECTION TAB
        # ============================================================

        with gr.Tab("🎤 Audio Detection"):

            gr.Markdown("## Upload an Audio File")

            with gr.Row():

                with gr.Column(scale=1, min_width=260):

                    audio_input = gr.Audio(
                        type="filepath",
                        label="Upload Audio"
                    )

                    audio_btn = gr.Button(
                        "🎧 Analyze Audio",
                        variant="primary"
                    )

                with gr.Column(scale=1, min_width=260):

                    gr.Markdown("""
### Voice Verification

✔ Speaker Matching

✔ Voice Similarity

✔ Frequency Analysis

✔ Tone Analysis

✔ AI Explanation
""")

            gr.Markdown("---")

            with gr.Row():

                audio_result = gr.Textbox(
                    label="Detection Result"
                )

                audio_confidence = gr.Textbox(
                    label="Confidence Score"
                )

                audio_match = gr.Textbox(
                    label="Matched Voice"
                )

            audio_reason = gr.Textbox(
                label="AI Explanation",
                lines=5
            )

            audio_report = gr.Textbox(
                label="Report Status",
                lines=2
            )

            audio_btn.click(
                analyze_audio,
                inputs=audio_input,
                outputs=[
                    audio_result,
                    audio_confidence,
                    audio_match,
                    audio_reason,
                    audio_report
                ]
            )

        # ============================================================
        # TEXT DETECTION TAB
        # ============================================================

        with gr.Tab("📝 Text Detection"):

            gr.Markdown("## Analyze News Article or Social Media Text")

            text_input = gr.Textbox(
                label="Enter Text",
                placeholder="Paste any news article, social media post, or paragraph here...",
                lines=10
            )

            text_btn = gr.Button(
                "🧠 Analyze Text",
                variant="primary"
            )

            gr.Markdown("---")

            with gr.Row():

                text_result = gr.Textbox(
                    label="Detection Result"
                )

                text_confidence = gr.Textbox(
                    label="Confidence Score"
                )

                text_risk = gr.Textbox(
                    label="Risk Level"
                )

            text_reason = gr.Textbox(
                label="AI Explanation",
                lines=5
            )

            text_report = gr.Textbox(
                label="Report Status",
                lines=2
            )

            text_btn.click(
                analyze_text,
                inputs=text_input,
                outputs=[
                    text_result,
                    text_confidence,
                    text_risk,
                    text_reason,
                    text_report
                ]
            )

        # ============================================================
        # HISTORY TAB
        # ============================================================

        with gr.Tab("📜 History"):

            gr.Markdown("## Previous Analysis History")

            history_table = gr.Dataframe(
                headers=[
                    "Type",
                    "Result",
                    "Confidence",
                    "Date"
                ],
                value=[
                    ["Image", "Fake", "92%", "2026-07-08"],
                    ["Video", "Real", "96%", "2026-07-07"],
                    ["Audio", "Real", "95%", "2026-07-06"],
                    ["Text", "Misleading", "84%", "2026-07-05"],
                ],
                interactive=False
            )

            refresh_btn = gr.Button("🔄 Refresh History")

            refresh_btn.click(
                lambda: history_table.value,
                outputs=history_table
            )

        # ============================================================
        # REPORTS TAB
        # ============================================================

        with gr.Tab("📄 Reports"):

            gr.Markdown("## AI Analysis Report")

            report_text = gr.Markdown("""

### Report Summary

This section will display:

✅ Detection Result

✅ Confidence Score

✅ AI Explanation

✅ Risk Assessment

✅ Voice Matching Details

✅ PDF Report Download

""")

            report_status = gr.Textbox(
                value="Backend integration required for report generation.",
                label="Status"
            )

            download_btn = gr.Button("📥 Download Report")

            download_output = gr.Textbox(label="Message")

            download_btn.click(
                lambda: "PDF generation will be available after backend integration.",
                outputs=download_output
            )

    # ============================================================
    # ABOUT SECTION
    # ============================================================

    gr.Markdown("---")

    gr.Markdown("""
# ℹ️ About TruthLens AI

TruthLens AI is an intelligent fake content detection platform capable of
analyzing Images, Videos, Audio, and Text using Artificial Intelligence.

The system provides:

✅ Fake Content Detection

✅ Confidence Score

✅ AI Explanation

✅ Voice Matching

✅ Report Generation

Designed as a Final Year Project.
""")

    # ============================================================
    # SYSTEM FEATURES
    # ============================================================

    with gr.Row():

        with gr.Column(min_width=260):

            gr.Markdown("""
## 🚀 Features

- Image Deepfake Detection
- Video Deepfake Detection
- Audio Verification
- Text Misinformation Detection
- AI Explainability
- PDF Reports
- Analysis History
""")

        with gr.Column(min_width=260):

            gr.Markdown("""
## 📊 Dashboard Statistics

Total Modules : 4

AI Models : 4

Detection Accuracy : 95%*

Supported Formats:

✔ JPG

✔ PNG

✔ MP4

✔ AVI

✔ MP3

✔ WAV

✔ TXT
""")

    gr.Markdown("""
> **Note:** Accuracy values shown in this frontend are placeholders. They will reflect actual model performance once the AI backend is integrated.
""")

    # ============================================================
    # FOOTER
    # ============================================================

    gr.HTML(
        """
        <div>
            <h3 style="text-align:center;margin:0 0 6px 0;">🛡 TruthLens AI</h3>
            <p style="text-align:center;margin:0 0 14px 0;color:#6ee7b7;">
                Advanced Fake Content Detection System
            </p>
            <div class="footer-links">
                <span>🖼 Image Detection</span>
                <span>🎥 Video Detection</span>
                <span>🎤 Audio Detection</span>
                <span>📝 Text Detection</span>
                <span>📜 History</span>
                <span>📄 Reports</span>
            </div>
            <p class="copyright">Developed as Final Year Project • © 2026 All Rights Reserved</p>
        </div>
        """,
        elem_id="tl-footer"
    )

# ============================================================
# LAUNCH APP
# ============================================================

demo.launch(
    server_name="127.0.0.1",
    server_port=7861,
    share=True
)