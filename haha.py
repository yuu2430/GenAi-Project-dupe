import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import shapiro
import plotly.express as px
from docx import Document
import os

# =====================================================
# GLOBAL COLOR THEME ( emphasize academic blue palette)
# =====================================================
THEME_COLORS = {
    "primary": "#5b9bd5",
    "secondary": "#9dc3e6",
    "accent1": "#bdd7ee",
    "accent2": "#ddebf7",
    "accent3": "#2f75b5",
    "neutral": "#f4f8fc"
}

BAR_COLORS = ["#5b9bd5", "#9dc3e6", "#bdd7ee", "#2f75b5"]
PIE_COLORS = ["#5b9bd5", "#9dc3e6", "#bdd7ee", "#ddebf7"]

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="GenAI Impact Study – MSc Statistics",
    layout="wide"
)

# =========================================================
# GLOBAL CSS — CLEAN & ACADEMIC UI
# =========================================================
st.markdown("""
<style>
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

section[data-testid="stSidebar"] {
    background-color: #f4f8fc;
}

.card {
    background-color: white;
    padding: 18px 22px;
    border-radius: 14px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
    margin-bottom: 16px;
}

.soft-card {
    background-color: #ddebf7;
    padding: 16px 20px;
    border-radius: 12px;
    margin-bottom: 14px;
}

.plot-box {
    background-color: white;
    padding: 16px;
    border-radius: 14px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.06);
    margin-bottom: 20px;
}

div[data-testid="metric-container"] {
    background-color: white;
    padding: 14px;
    border-radius: 12px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.markdown("""
<div class="card">
<h3>📊 GenAI Project</h3>
<p style="font-size:14px;">
MSc Statistics – Research Dashboard
</p>
</div>
""", unsafe_allow_html=True)

tabs = [
    "📘 Overview",
    "🎯 Objectives",
    "🧪 Pilot Survey",
    "📐 Sampling & Sample Size",
    "📝 Questionnaire",
    "📋 Dataset Overview",
    "📊 Data Visualization",
    "📑 Inference",
    "📌 Conclusion"
]

active_tab = st.sidebar.radio("Navigation", tabs)

# =========================================================
# OVERVIEW
# =========================================================
if active_tab == "📘 Overview":

    st.markdown(f"""
    <div class="card" style="
        background: linear-gradient(90deg,{THEME_COLORS['primary']},{THEME_COLORS['secondary']});
    ">
        <h2>
        Cognitive & Educational Impacts of Generative AI Usage<br>
        Among University Students
        </h2>
        <p>MSc Statistics · Research Dashboard</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="soft-card">
    <b>Programme:</b> MSc Statistics (Team 4)<br>
    <b>Institution:</b> The Maharaja Sayajirao University of Baroda<br>
    <b>Students:</b> Rohan Shukla • Vaishali Sharma • Raiwant Kumar • Ashish Vaghela<br>
    <b>Mentor:</b> Prof. Murlidharan Kunnumal
    </div>
    """, unsafe_allow_html=True)

    st.header("Project Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
        <h4>Introduction</h4>
        <p>
        Generative Artificial Intelligence (GenAI) tools such as ChatGPT, Gemini, and Copilot
        have become integral to university learning environments. These tools assist students
        in content creation, coding, idea generation, and exam preparation.<br><br>
        As GenAI becomes embedded in academic workflows, it is important to understand its
        influence on cognitive engagement, learning depth, motivation, and independent thinking.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h4>Why This Project?</h4>
        <p>
        Existing research on GenAI largely focuses on usability and performance.
        The deeper <b>cognitive and educational impacts</b> remain under-explored.<br><br>
        This study addresses this gap through a structured <b>statistical analysis</b>
        of AI usage patterns, learning behaviour, and academic outcomes.
        </p>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("Aim of the Study")

    st.markdown("""
    <div class="soft-card">
    To examine the cognitive and educational impacts of Generative AI usage among
    university students, with emphasis on learning behaviour, academic performance,
    and critical thinking abilities.
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# OBJECTIVES
# =========================================================
elif active_tab == "🎯 Objectives":

    st.header("Objectives of the Study")
    st.caption("Research goals guiding the analysis")

    objectives = [
        "To find out how often students use AI tools and for what purpose, and see how this differs by their education level or gender.",
        "To understand how students’ views on AI dependence differ across different age groups, genders, and study programs.",
        "To check if depending on AI for thinking (cognitive offloading) affects the link between AI usage and students’ learning performance (CGPA).",
        "To study how AI tool usage is related to students’ critical thinking and engagement in learning, using self-reported ratings.",
        "To explore how using AI tools influences students’ academic skills, such as creativity and independent learning.",
        "To create a model that predicts factors leading to positive or negative effects of AI tool usage on students’ academic outcomes."
    ]

    for i, obj in enumerate(objectives, start=1):
        st.markdown(f"""
        <div class="soft-card">
        <b>Objective {i}.</b> {obj}
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# SAMPLING & SAMPLE SIZE
# =========================================================
elif active_tab == "📐 Sampling & Sample Size":

    st.header("Sampling Design and Sample Size Determination")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Sampling Method", "Probability Proportional to Size (PPS) sampling")
        st.metric("Population", "MSU Students")
        st.metric("Final Sample Size", "221")
    with col2:
        st.metric("Confidence Level", "95%")
        st.metric("Significance Level (α)", "0.05")
        st.metric("Data Type", "Primary")

    st.subheader("Faculty-wise, Gender-wise and Programme-wise Sample Distribution")

    sampling_data = pd.DataFrame({
        "Faculty": [
            "Arts", "Commerce", "Education & Psychology", "Family & Community Sciences",
            "Fine Arts", "Journalism & Communication", "Law", "Management Studies",
            "Performing Arts", "Pharmacy", "Science", "Social Work", "Technology & Engineering"
        ],
        "Total": [25, 120, 5, 7, 4, 1, 8, 2, 2, 2, 23, 3, 19],
        "Female UG": [13, 58, 3, 5, 2, 1, 4, 1, 1, 1, 9, 1, 3],
        "Female PG": [3, 8, 1, 1, 1, 0, 0, 0, 0, 0, 4, 1, 2],
        "Male UG": [8, 50, 1, 1, 1, 0, 4, 1, 1, 1, 8, 1, 12],
        "Male PG": [1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2]
    })

    st.dataframe(sampling_data, use_container_width=True)

    with st.expander("Sample Size Formula (Single Proportion)"):
        st.latex(r"n = \frac{z_{\alpha/2}^2 \, p \, q}{E^2}")

# =========================================================
# PILOT SURVEY
# =========================================================
elif active_tab == "🧪 Pilot Survey":

    st.header("Pilot Survey Analysis")
    st.success("Pilot survey conducted prior to full-scale data collection.")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Population (N)", "37,095")
        st.metric("Sampling Method", "Simple Random Sampling")
    with col2:
        st.metric("Pilot Sample Size (n)", "58")
        st.metric("Pilot Question", "Single Perception Item")

    st.info("“Has Generative AI impacted your education?”")

    col3, col4 = st.columns(2)
    with col3:
        st.metric("Yes", "48")
    with col4:
        st.metric("No", "10")

# =========================================================
# QUESTIONNAIRE
# =========================================================
elif active_tab == "📝 Questionnaire":

    st.header("Research Questionnaire")
    st.caption("Survey Instrument Used for Data Collection")

    QUESTIONNAIRE_FILE = "Questionnaire.docx"

    if not os.path.exists(QUESTIONNAIRE_FILE):
        st.error("Questionnaire file not found in GitHub repository.")
    else:
        doc = Document(QUESTIONNAIRE_FILE)
        for para in doc.paragraphs:
            if para.text.strip():
                st.write(para.text)

# =========================================================
# DATASET OVERVIEW
# =========================================================
elif active_tab == "📋 Dataset Overview":

    st.header("Dataset Overview")
    FILE_NAME = "FINAL DATA OF PROJECT (1).xlsx"

    df = pd.read_excel(FILE_NAME)
    df = df.drop(columns=["Timestamp"], errors="ignore")

    col1, col2, col3 = st.columns(3)
    col1.metric("Number of Responses", df.shape[0])
    col2.metric("Number of Variables", df.shape[1])
    col3.metric("Total Missing Values", int(df.isnull().sum().sum()))

    st.dataframe(df, use_container_width=True)

# =========================================================
# DATA VISUALIZATION
# =========================================================
elif active_tab == "📊 Data Visualization":

    st.header("Objective 1: To find out how often students use AI tools and for what purpose, and see how this differs by their education level, or gender.")

    viz_type = st.radio(
        "Select Analysis View",
        [
            "Multiple Bar Chart – AI Tools vs Academic Purpose",
            "AI Usage Distribution (Programme & Gender)",
            "AI Tools Used for Academic Purposes"
        ],
        horizontal=True
    )

    if viz_type == "Multiple Bar Chart – AI Tools vs Academic Purpose":

        df = pd.read_excel("FINAL DATA OF PROJECT (1).xlsx", sheet_name="Sheet3")
        df.columns = df.columns.astype(str).str.strip()
        df = df.rename(columns={df.columns[0]: "Label"})

        purposes = [
            "Project / Assignment",
            "Concept Learning",
            "Writing / Summarizing",
            "Exam Preparation",
            "Research / Idea Generation",
            "Programming / Coding"
        ]

        ai_tools = ["ChatGPT", "Gemini", "Copilot", "Perplexity"]
        df["Purpose"] = df["Label"].where(df["Label"].isin(purposes)).ffill()
        df = df[~df["Label"].isin(purposes)]

        records = []
        for purpose in purposes:
            subset = df[df["Purpose"] == purpose]
            for tool in ai_tools:
                records.append({
                    "Academic Purpose": purpose,
                    "AI Tool": tool,
                    "Number of Students": int(subset[tool].sum())
                })

        final_df = pd.DataFrame(records)

        fig = px.bar(
            final_df,
            x="Academic Purpose",
            y="Number of Students",
            color="AI Tool",
            barmode="group",
            text_auto=True,
            template="plotly_white",
            color_discrete_sequence=BAR_COLORS
        )

        st.markdown('<div class="plot-box">', unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# CONCLUSION
# =========================================================
elif active_tab == "📌 Conclusion":

    st.header("Conclusion")
    st.caption("Integrated Summary of Findings")

    st.markdown("""
    <div class="soft-card">
    This study concludes that Generative AI tools have become an integral part of
    students’ academic workflows at The Maharaja Sayajirao University of Baroda.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        "<div style='text-align:center; font-size:42px;'><b>Thank you! :)</b></div>",
        unsafe_allow_html=True
    )

# =========================================================
# FOOTER
# =========================================================
st.caption("Team 4 - MSc Statistics - Final Year")
