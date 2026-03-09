# MindGuard AI: Student Exam Anxiety Detector

MindGuard AI is a sophisticated wellness tool designed for students to monitor and analyze exam-related stress. It uses a hybrid approach combining a clinical questionnaire with a **BERT-based Natural Language Processing (NLP)** model to provide a comprehensive anxiety assessment.

## 🚀 Features
- **Interactive UI:** Built with Streamlit, featuring Glassmorphism design and Parallax transitions.
- **Hybrid Analysis:** Combines a 6-question diagnostic test with open-ended text sentiment analysis.
- **Deep Learning:** Utilizes the BERT model for high-accuracy emotion detection in text.
- **Real-time Feedback:** Provides instant reports with personalized calming techniques and stress-relief humor.

## 🛠️ Tech Stack
- **Presentation Layer:** Streamlit (Python)
- **Application Layer:** FastAPI (Python)
- **Model:** BERT (Transformers)
- **Styling:** CSS3 (Glassmorphism & Parallax Effects)

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/MindGuard-AI.git](https://github.com/your-username/MindGuard-AI.git)
  For installing dependencies: pip install -r requirements.txt
  Run the Backend (FastAPI):uvicorn main:app --reload --port 8000
  Run the Frontend (Streamlit):streamlit run app.py
  
