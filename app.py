import streamlit as st
import requests

# Page Configuration
st.set_page_config(page_title="MindGuard AI", page_icon="🧠", layout="centered")

# --- CINEMATIC PARALLAX & GLASS UI ---
st.markdown("""
    <style>
    /* Parallax Background Gradient */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #1b2735 0%, #090a0f 100%);
        background-attachment: fixed;
        color: #ffffff;
        animation: backgroundShift 20s infinite alternate;
    }

    @keyframes backgroundShift {
        0% { background-position: 0% 0%; }
        100% { background-position: 10% 10%; }
    }

    /* Parallax Slide-In Animation for Content */
    @keyframes slideIn {
        from { opacity: 0; transform: translateY(30px) scale(0.95); }
        to { opacity: 1; transform: translateY(0) scale(1); }
    }

    .parallax-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 40px;
        margin-top: 20px;
        animation: slideIn 0.6s cubic-bezier(0.23, 1, 0.32, 1);
        box-shadow: 0 15px 35px rgba(0,0,0,0.5);
    }

    /* Interactive Title with Glow */
    .project-title {
        font-size: 3.5rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(to right, #ffffff, #a5b4fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        transition: all 0.4s ease;
        margin-bottom: 0px;
    }
    .project-title:hover {
        text-shadow: 0 0 30px rgba(165, 180, 252, 0.8);
        transform: scale(1.05);
    }

    /* Animated Button */
    .stButton > button {
        width: 100%;
        border-radius: 50px;
        height: 3.5em;
        background: linear-gradient(45deg, #4f46e5, #06b6d4);
        color: white;
        font-weight: bold;
        border: none;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    .stButton > button:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 25px rgba(6, 182, 212, 0.5);
    }

    /* Fixed Modern Footer */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background: rgba(9, 10, 15, 0.9);
        backdrop-filter: blur(12px);
        color: #94a3b8;
        text-align: center;
        padding: 15px 0;
        font-size: 0.85rem;
        border-top: 1px solid rgba(255, 255, 255, 0.05);
        z-index: 1000;
    }
    </style>
    """, unsafe_allow_html=True)

# Session State
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'scores' not in st.session_state:
    st.session_state.scores = []

# Header
st.markdown('<h1 class="project-title">MindGuard AI</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #94a3b8; margin-top: -10px;">Advanced Cognitive Stress Analytics</p>', unsafe_allow_html=True)

questions = [
    "Do you feel your heart racing when thinking about the exam?",
    "Have you been feeling restless or unable to sit still?",
    "Are you having trouble falling or staying asleep?",
    "Do you feel a sense of 'impending doom' regarding your results?",
    "Is your appetite significantly lower than usual today?",
    "Do you find it difficult to stop worrying once you start?"
]

# --- APP FLOW ---
if st.session_state.step <= 6:
    # The div class "parallax-card" triggers the slide-in animation on every rerun
    st.markdown('<div class="parallax-card">', unsafe_allow_html=True)
    st.write(f"🌌 **Phase {st.session_state.step} of 6**")
    st.progress(st.session_state.step / 6)
    
    current_q = questions[st.session_state.step - 1]
    st.subheader(current_q)
    choice = st.radio("", ["Not at all", "Sometimes", "Constantly"], index=None, key=f"q{st.session_state.step}")
    
    if st.button("Continue"):
        if choice is None:
            st.error("Select an option to proceed.")
        else:
            score_map = {"Not at all": 0, "Sometimes": 1, "Constantly": 2}
            st.session_state.scores.append(score_map[choice])
            st.session_state.step += 1
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.step == 7:
    st.markdown('<div class="parallax-card">', unsafe_allow_html=True)
    st.subheader("Deep Sentiment Analysis")
    
    total_score = sum(st.session_state.scores)
    hint = "I'm overwhelmed and my mind is racing." if total_score > 6 else "I'm a bit tense but managing."
    
    st.markdown(f"💡 **Suggested Input:** *'{hint}'*")
    user_input = st.text_area("How are you feeling right now?", height=120)

    if st.button("Generate Report"):
        if not user_input.strip():
            st.warning("Please enter your thoughts.")
        else:
            with st.spinner("Neural Processing..."):
                try:
                    response = requests.post("http://127.0.0.1:8000/predict", json={"text": user_input})
                    st.session_state.ai_result = response.json()
                    st.session_state.step = 8
                    st.rerun()
                except:
                    st.error("Backend offline. Run main.py first.")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.step == 8:
    st.markdown('<div class="parallax-card">', unsafe_allow_html=True)
    res = st.session_state.ai_result
    q_total = sum(st.session_state.scores)
    
    st.header("📋 Diagnostic Report")
    
    if q_total >= 8 or "High" in res['status']:
        st.error("### 📉 STATUS: CRITICAL ANXIETY")
        st.write("**Advice:** Practice 4-7-8 breathing. Drink cold water now.")
        st.info("🎭 **Joke:** Why did the BTech student bring a ladder? To get over their low GPA!")
    elif q_total >= 4 or "Moderate" in res['status']:
        st.warning("### ⚠️ STATUS: MODERATE STRESS")
        st.write("Take a 15-minute walk without your phone.")
    else:
        st.success("### 😊 STATUS: OPTIMAL CALM")
        st.write("You are in the zone. Trust your hard work!")

    if st.button("Restart Assessment"):
        st.session_state.step = 1
        st.session_state.scores = []
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown(f"""
    <div class="footer">
        BTech Project Submission | <b>Made By Aditya Saumya</b>
    </div>
    """, unsafe_allow_html=True)