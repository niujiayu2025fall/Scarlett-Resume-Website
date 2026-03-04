"""
Interactive Resume - Jiayu (Scarlett) Niu
Streamlit app with personalized content, widgets, tables, and charts.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Scarlett Niu | Resume",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for a clean, professional look
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1e3a5f;
        margin-bottom: 0.25rem;
    }
    .subtitle {
        color: #5a6c7d;
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }
    .section-header {
        font-size: 1.35rem;
        color: #1e3a5f;
        border-bottom: 2px solid #4a90d9;
        padding-bottom: 0.35rem;
        margin-top: 2.5rem;
        margin-bottom: 1rem;
    }
    .section-block { margin-bottom: 2rem; }
    table.resume-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.95rem;
    }
    table.resume-table th, table.resume-table td {
        padding: 0.65rem 1rem;
        text-align: left;
        border-bottom: 1px solid #e2e8f0;
        vertical-align: top;
    }
    table.resume-table th {
        font-weight: 600;
        color: #1e3a5f;
        white-space: nowrap;
    }
    table.resume-table th.col-year, table.resume-table td.col-year {
        min-width: 4.5rem;
        white-space: nowrap;
    }
    table.resume-table tr:hover td { background-color: #f8fafc; }
    .highlight-box {
        background: linear-gradient(135deg, #f0f7ff 0%, #e8f4fc 100%);
        padding: 1rem 1.25rem;
        border-radius: 8px;
        border-left: 4px solid #4a90d9;
        margin: 1rem 0;
    }
    div[data-testid="stMetricValue"] { font-size: 1.4rem; }
</style>
""", unsafe_allow_html=True)

# ----- Data (personalized resume content) -----

SKILLS_DATA = pd.DataFrame([
    {"Category": "Programming", "Skill": "Python (Pandas, NumPy, Scikit-learn, PyTorch)", "Proficiency": 5},
    {"Category": "Programming", "Skill": "SQL", "Proficiency": 5},
    {"Category": "Programming", "Skill": "R", "Proficiency": 4},
    {"Category": "Tools", "Skill": "Power BI", "Proficiency": 5},
    {"Category": "Tools", "Skill": "Excel (advanced modeling)", "Proficiency": 5},
    {"Category": "Domain", "Skill": "NLP", "Proficiency": 4},
    {"Category": "Domain", "Skill": "Predictive modeling & feature engineering", "Proficiency": 5},
    {"Category": "Domain", "Skill": "A/B analysis & dashboarding", "Proficiency": 5},
])

EDUCATION_DATA = pd.DataFrame([
    {"Institution": "Rotman School of Management, University of Toronto", "Degree": "Master of Management Analytics", "Year": "2026", "Highlight": "$10,000 Entrance Scholarship, 2025"},
    {"Institution": "University of International Business and Economics, Beijing", "Degree": "Bachelor of Finance (International finance and market)", "Year": "2025", "Highlight": "Merit-based Scholarship; Vice Director, Entrepreneurship Support Club"},
])

EXPERIENCE_DATA = pd.DataFrame([
    {"Company": "Cora Group – Jonas Software", "Role": "Product & Strategy Analytics Intern", "Location": "Toronto, Canada", "Start": "2025-12", "End": "Present", "Duration_months": 4},
    {"Company": "Capgemini", "Role": "Data Analytics Intern", "Location": "Beijing, China", "Start": "2024-09", "End": "2024-12", "Duration_months": 4},
    {"Company": "Schneider Electric Co., Ltd", "Role": "Carbon Neutral Consulting Intern", "Location": "Beijing, China", "Start": "2024-01", "End": "2025-01", "Duration_months": 12},
    {"Company": "CITIC Securities", "Role": "Business Development Intern", "Location": "Beijing, China", "Start": "2023-07", "End": "2023-08", "Duration_months": 2},
])

EXPERIENCE_BULLETS = {
    "Cora Group – Jonas Software": [
        "Built the core business logic for a new Customer Health & Churn Intelligence workflow.",
        "Worked cross-functionally with product, engineering, data science, and customer success.",
        "Influenced stakeholder decisions through data-driven storytelling and executive-ready demos.",
    ],
    "Capgemini": [
        "Built components of an AI-enabled review extraction platform; validated NLP outputs and tested Qwen-based keyword extraction.",
        "Designed reproducible data validation workflows, reducing error rates.",
        "Analyzed customer sentiment and patterns in large-scale review datasets.",
    ],
    "Schneider Electric Co., Ltd": [
        "Automated sustainability analytics across 200+ projects with SQL/Excel and Power BI.",
        "Conducted emissions and regulatory alignment analysis for ESG frameworks.",
    ],
    "CITIC Securities": [
        "Built Python-based ETF empowerment framework and automated analytics.",
        "Performed quantitative research; improved institutional client engagement by ~20%.",
    ],
}

PROJECTS = [
    ("EASE Design Challenge – 1st Place (2025)", "Designed strategy for financial institutions to support IPV survivors through safer fraud-response workflows."),
    ("Meta AI Product Case Competition (2026)", "Led analytics and impact marketing workstream using Meta AI; built ROI and measurable-sales frameworks."),
    ("RRMA x Scotiabank Credit Risk Case Competition – 2nd Place (2025)", "Built RCF model with leverage stress tests, liquidity analysis, and covenant evaluation."),
]

# ----- Sidebar: interactive widgets -----
with st.sidebar:
    st.markdown("### ⚙️ Customize view")
    
    view_focus = st.selectbox(
        "**What would you like to see?**",
        ["Full resume", "Experience & skills", "Education & projects", "Charts & metrics only"],
        index=0,
    )
    
    min_proficiency = st.slider(
        "**Minimum skill level to display** (1–5)",
        min_value=1,
        max_value=5,
        value=1,
        help="Filter the skills table and chart by proficiency.",
    )
    
    show_contact = st.checkbox("Show contact details", value=True)
    show_detailed_bullets = st.checkbox("Show detailed experience bullets", value=True)
    highlight_recent = st.checkbox("Highlight experience from last 2 years", value=True)

# ----- Main content -----
st.markdown('<p class="main-header">Jiayu (Scarlett) Niu</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">Master of Management Analytics candidate · ML, NLP, customer analytics & data product development</p>',
    unsafe_allow_html=True,
)

if show_contact:
    st.markdown("📞 (437) 771-5812  ·  ✉️ scarlett.niu@rotman.utoronto.ca  ·  [LinkedIn](https://www.linkedin.com/in/scarlett-niu-929802359/)")

st.markdown("""
<div class="highlight-box">
Hands-on experience in machine learning, NLP, customer analytics, and data product development. 
Experienced in building end-to-end analytical solutions and translating technical outputs into business insights. 
Strong interest in analytics consulting and data-driven transformation.
</div>
""", unsafe_allow_html=True)

# Show/hide sections based on view_focus
show_experience = view_focus in ["Full resume", "Experience & skills"]
show_education = view_focus in ["Full resume", "Education & projects"]
show_projects = view_focus in ["Full resume", "Education & projects"]
show_charts = view_focus in ["Full resume", "Charts & metrics only"] or view_focus == "Charts & metrics only"

# Filter skills by minimum proficiency (widget-driven)
skills_filtered = SKILLS_DATA[SKILLS_DATA["Proficiency"] >= min_proficiency]

# ----- Table 1: Skills -----
if show_experience or view_focus == "Full resume":
    st.markdown('<p class="section-header">📊 Technical skills (filtered by level)</p>', unsafe_allow_html=True)
    st.markdown('<div class="section-block">', unsafe_allow_html=True)
    table_skills = skills_filtered[["Category", "Skill", "Proficiency"]].copy()
    table_skills["Proficiency"] = table_skills["Proficiency"].astype(int)
    st.table(table_skills)
    st.markdown('</div>', unsafe_allow_html=True)

# ----- Chart 1: Skills proficiency bar chart -----
if show_charts or view_focus == "Full resume" or view_focus == "Experience & skills":
    st.markdown('<p class="section-header">📈 Skills proficiency</p>', unsafe_allow_html=True)
    st.markdown('<div class="section-block">', unsafe_allow_html=True)
    fig_skills = px.bar(
        skills_filtered,
        x="Proficiency",
        y="Skill",
        orientation="h",
        color="Proficiency",
        color_continuous_scale="Blues",
        title="",
    )
    fig_skills.update_layout(
        showlegend=False,
        xaxis_title="Level (1–5)",
        yaxis_title="",
        height=320,
        margin=dict(l=20, r=20, t=20, b=20),
        xaxis=dict(range=[0, 6], dtick=1),
    )
    st.plotly_chart(fig_skills, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----- Table 2: Work history -----
if show_experience:
    st.markdown('<p class="section-header">💼 Professional experience</p>', unsafe_allow_html=True)
    st.markdown('<div class="section-block">', unsafe_allow_html=True)
    work_table = EXPERIENCE_DATA[["Company", "Role", "Location", "Start", "End"]].copy()
    if highlight_recent:
        work_table["Recent"] = EXPERIENCE_DATA["End"].isin(["Present", "2025-01", "2024-12"]).map({True: "✓ Recent", False: ""})
    st.table(work_table)

    if show_detailed_bullets:
        for _, row in EXPERIENCE_DATA.iterrows():
            company = row["Company"]
            if company in EXPERIENCE_BULLETS:
                with st.expander(f"**{company}** — {row['Role']}"):
                    for bullet in EXPERIENCE_BULLETS[company]:
                        st.markdown(f"- {bullet}")
    st.markdown('</div>', unsafe_allow_html=True)

# ----- Table 3: Education (custom HTML for column width & spacing) -----
if show_education:
    st.markdown('<p class="section-header">🎓 Education</p>', unsafe_allow_html=True)
    st.markdown('<div class="section-block">', unsafe_allow_html=True)
    def escape_html(s):
        return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
    rows = []
    for _, row in EDUCATION_DATA.iterrows():
        rows.append(
            f"<tr><td>{escape_html(row['Institution'])}</td>"
            f"<td>{escape_html(row['Degree'])}</td>"
            f"<td class=\"col-year\">{escape_html(row['Year'])}</td>"
            f"<td>{escape_html(row['Highlight'])}</td></tr>"
        )
    table_html = (
        "<table class=\"resume-table\">"
        "<thead><tr><th>Institution</th><th>Degree</th><th class=\"col-year\">Year</th><th>Highlight</th></tr></thead>"
        "<tbody>" + "".join(rows) + "</tbody></table>"
    )
    st.markdown(table_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----- Projects -----
if show_projects:
    st.markdown('<p class="section-header">🏆 Technical projects & competitions</p>', unsafe_allow_html=True)
    st.markdown('<div class="section-block">', unsafe_allow_html=True)
    for title, desc in PROJECTS:
        st.markdown(f"**{title}**  \n{desc}")
    st.markdown('</div>', unsafe_allow_html=True)

# ----- Chart 2: Experience timeline (duration) -----
if (show_charts or view_focus == "Full resume") and len(EXPERIENCE_DATA) > 0:
    st.markdown('<p class="section-header">📅 Experience timeline (duration)</p>', unsafe_allow_html=True)
    st.markdown('<div class="section-block">', unsafe_allow_html=True)
    timeline_df = EXPERIENCE_DATA.copy()
    timeline_df["Label"] = timeline_df["Company"].str.split("–").str[0].str.strip() + " · " + timeline_df["Role"]
    fig_timeline = px.bar(
        timeline_df,
        x="Duration_months",
        y="Label",
        orientation="h",
        color="Duration_months",
        color_continuous_scale="Teal",
        title="",
    )
    fig_timeline.update_layout(
        showlegend=False,
        xaxis_title="Months",
        yaxis_title="",
        height=280,
        margin=dict(l=20, r=20, t=20, b=20),
    )
    st.plotly_chart(fig_timeline, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----- Metrics (optional visual) -----
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Roles (experience)", len(EXPERIENCE_DATA), "")
with col2:
    st.metric("Skills (shown)", len(skills_filtered), f"min level {min_proficiency}")
with col3:
    st.metric("Languages", "English, Mandarin", "")

st.markdown("---")
st.caption("Interactive resume · Jiayu (Scarlett) Niu · Built with Streamlit")
