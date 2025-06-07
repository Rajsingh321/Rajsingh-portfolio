import streamlit as st

st.set_page_config(page_title="Raj | Data Analyst Portfolio", page_icon="📊", layout="wide")

st.markdown("""
    <style>
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #0f172a;
        }
        ::-webkit-scrollbar-thumb {
            background: #6366f1;
            border-radius: 10px;
        }

        html, body, [class*="css"] {
            background-color: #0f172a;
            color: #e0f2fe;
            font-family: 'Segoe UI', sans-serif;
        }

        .centered {
            text-align: center;
            margin-top: 4rem;
        }

        .title-text {
            font-size: 58px;
            font-weight: 800;
            background: linear-gradient(to right, #a855f7, #6366f1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            white-space: nowrap;
            overflow: hidden;
            border-right: 2px solid #6366f1;
            width: 0;
            margin: auto;
            animation: typing 4s steps(35, end) forwards, blink 0.8s step-end infinite;
        }

        @keyframes typing {
            from { width: 0 }
            to { width: 18ch }
        }

        @keyframes blink {
            50% { border-color: transparent }
        }

        .subtitle {
            font-size: 20px;
            color: #60a5fa;
            margin-top: 1rem;
            text-align: center;
        }

        .intro {
            font-size: 16px;
            color: #94a3b8;
            text-align: center;
            margin-bottom: 2rem;
        }

        .section-header {
            font-size: 32px;
            margin-top: 3rem;
            margin-bottom: 1rem;
            font-weight: bold;
            color: #7dd3fc;
        }

        .project-card {
            background: #1e293b;
            padding: 1.5rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            box-shadow: 0 0 15px rgba(99, 102, 241, 0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .project-card:hover {
            transform: scale(1.03);
            box-shadow: 0 0 25px rgba(99, 102, 241, 0.35);
        }

        .project-card h3 {
            font-size: 24px;
            color: #c084fc;
        }

        .project-card p {
            font-size: 16px;
            color: #cbd5e1;
        }

        .live-button {
            background-color: #ffffff;
            color: #2563eb;
            padding: 0.4rem 1rem;
            border-radius: 8px;
            font-weight: bold;
            text-decoration: none;
            display: inline-block;
            margin-top: 1rem;
            transition: background-color 0.3s ease, color 0.3s ease;
            border: 2px solid #2563eb;
        }

        .live-button:hover {
            background-color: #f0f9ff;
            color: #1d4ed8;
        }
    </style>
""", unsafe_allow_html=True)


# --- Landing Page ---
st.markdown("""
    <div class="centered">
        <div class="title-text">Hey, I'm RajSingh</div>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="subtitle">Futuristic Data Analyst turning data into insight using AI + Python + Power BI</div>', unsafe_allow_html=True)
st.markdown('<div class="intro">Welcome to my personal portfolio. I transform raw data into smart dashboards, powerful insights, and intelligent visualizations.</div>', unsafe_allow_html=True)



# --- About Me ---
st.markdown('<div class="section-header">💻 About Me</div>', unsafe_allow_html=True)
st.markdown("""
i am a Data Analyst with a strong grasp of Python, Pandas, NumPy, SQL, Excel, and Power BI.
Currently studying Data Science and applying skills to real datasets and business problems.
Experienced in transforming raw data into clear dashboards and reports.
Capable of finding patterns, spotting trends, and delivering actionable insights.
Efficient in handling complex data tasks with a structured, analytical approach.
Driven to support smart decision-making through clean, reliable data analysis.""")

# --- Education ---
st.markdown('<div class="section-header">🎓 Education</div>', unsafe_allow_html=True)
st.markdown("""
**Bachelor’s Degree in Data Science** — 2023 – Present

👉**From** - Sushila Devi Bansal College Of Engineering 
RGPV University  
✔ Year of completion 2027 
 
 """)

st.markdown("""
**High Secondary Edution** — 2021 – 2023

👉**From** - Saraswati Shishu Mandir

📕MP Board  

 
 """)

# --- Projects ---
st.markdown('<div class="section-header">📁 Projects</div>', unsafe_allow_html=True)

projects = [
    {
        "title": "Data.AI – AI Insight Chatbot",
        "description": "An AI-powered chatbot (Streamlit + Gemini) that answers questions and finds insights from CSV files.",
        "link": "https://dataaiassistant-vfapgbshrakyundpafvrwq.streamlit.app/"
    },
    {
        "title": "Flipkart Product Data Analysis",
        "description": "Analyzed Flipkart e-commerce data and visualized pricing, ratings, and trends by category.",
        "link": "https://flipkart-data-analysis-9hsyuaazui9edyhzfpb95s.streamlit.app/"
    },
    {
        "title": "Pizza Sales Analysis Dashboard",
        "description": "Uncovered top-selling pizzas, peak order times, and monthly revenue using Pandas & Power BI.",
        "link": "https://pizza-s-sales-analysis-xtzjck9dnmwsnaruthexuc.streamlit.app/"
    }
]

for project in projects:
    st.markdown(f"""
        <div class="project-card">
            <h3>{project['title']}</h3>
            <p>{project['description']}</p>
            <a href="{project['link']}" target="_blank" class="live-button">🚀 It's Live</a>
        </div>
    """, unsafe_allow_html=True)

# --- Skills Section ---
st.markdown('<div class="section-header">🧰 Skills</div>', unsafe_allow_html=True)
st.markdown("""
- 📌 Python, SQL, Streamlit, Pandas, NumPy  
- 📊 Power BI, Excel
- 🧠 Gemini AI, Prompt Engineering 
- 📈 Data visualization, problem solving, storytelling
""")

# --- Resume / CV ---
st.markdown('<div class="section-header">📄 Resume</div>', unsafe_allow_html=True)
try:
    with open("Raj_Singh_Resume.pdf", "rb") as file:
        st.download_button(
            label="📄 Download My Resume",
            data=file,
            file_name="Raj_Singh_Resume.pdf",
            mime="application/pdf",
        )
except FileNotFoundError:
    st.info("Resume file not found. Please make sure it's named 'Raj_Singh_Resume.pdf'")

# --- Contact (No form) ---
st.markdown('<div class="section-header">📬 Contact</div>', unsafe_allow_html=True)
st.markdown("""
- 📧 Email: rajbgi377@gmail.com
- 💼 [LinkedIn](https://www.linkedin.com/in/rajsingh-sendhav-860259307?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)  
- 🐱 [GitHub](https://github.com/Rajsingh321)  
""")
