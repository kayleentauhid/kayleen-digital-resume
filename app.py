import streamlit as st
import base64

st.set_page_config(
    page_title="Kayleen Tauhid | Digital Resume",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
            
html {
    scroll-behavior: smooth;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #0f1117;
    color: #f5f5f7;
}

.block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

.hero {
    text-align: center;
    padding: 100px 30px;
    border-radius: 40px;
    background: linear-gradient(135deg, #ffffff 0%, #e8e8ed 100%);
    color: #111;
    margin-bottom: 80px;
}

.hero h1 {
    font-size: 72px;
    font-weight: 800;
    letter-spacing: -3px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 24px;
    color: #6e6e73;
    margin-bottom: 30px;
}

.button {
    display: inline-block;
    padding: 14px 26px;
    border-radius: 999px;
    background: #0071e3;
    color: white !important;
    text-decoration: none;
    font-weight: 600;
    margin: 8px;
    transition: all 0.25s ease;
}

.button:hover {
    transform: translateY(-3px) scale(1.04);
    box-shadow: 0 12px 30px rgba(0, 113, 227, 0.35);
}

.section-title {
    font-size: 44px;
    font-weight: 800;
    letter-spacing: -1.5px;
    margin-top: 60px;
    margin-bottom: 25px;
}

.card {
    background: #ffffff;
    color: #111;
    padding: 34px;
    border-radius: 30px;
    margin-bottom: 25px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.25);
}

.card h3 {
    font-size: 26px;
    margin-bottom: 10px;
}

.card p {
    color: #555;
    font-size: 16px;
    line-height: 1.7;
}

.skill {
    display: inline-block;
    background: #1c1f2a;
    color: #f5f5f7;
    padding: 12px 18px;
    border-radius: 999px;
    margin: 7px;
    font-size: 15px;
    border: 1px solid #2c2f3a;
}

.timeline {
    border-left: 3px solid #0071e3;
    padding-left: 25px;
}

.small-text {
    color: #6e6e73;
    font-size: 14px;
}

a {
    color: #0071e3;
    text-decoration: none;
    font-weight: 600;
}

.navbar {
    position: sticky;
    top: 0;
    z-index: 999;
    backdrop-filter: blur(18px);
    background: rgba(15, 17, 23, 0.75);
    border-bottom: 1px solid rgba(255,255,255,0.08);
    padding: 16px 28px;
    border-radius: 999px;
    margin-bottom: 40px;
}

.navbar-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.navbar a {
    color: #f5f5f7 !important;
    margin-left: 24px;
    text-decoration: none;
    font-weight: 500;
    transition: 0.2s ease;
}

.navbar a:hover {
    color: #2997ff !important;
}
            
div.stDownloadButton > button {
    display: block;
    margin: 0 auto;
    padding: 14px 26px;
    border-radius: 999px;
    background: #0071e3;
    color: white;
    border: none;
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    transition: all 0.25s ease;
}

div.stDownloadButton > button:hover {
    background: #0071e3;
    color: white;
    border: none;
    transform: translateY(-3px) scale(1.04);
    box-shadow: 0 12px 30px rgba(0, 113, 227, 0.35);
}

div.stDownloadButton > button:active {
    transform: scale(0.98);
}

.carousel {
    position: relative;
    width: 100%;
    overflow: hidden;
    border-radius: 22px;
    margin-bottom: 22px;
}

.carousel img {
    width: 100%;
    height: 230px;
    object-fit: cover;
    border-radius: 22px;
    display: none;
    border: 1px solid #e5e5e5;
}

.carousel img.active {
    display: block;
}

.carousel button {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(0,0,0,0.35);
    color: white;
    border: none;
    border-radius: 999px;
    width: 38px;
    height: 38px;
    cursor: pointer;
    font-size: 22px;
    backdrop-filter: blur(8px);
}

.carousel button:hover {
    background: rgba(0,0,0,0.6);
}

.carousel .prev {
    left: 10px;
}

.carousel .next {
    right: 10px;
}
            
</style>
""", unsafe_allow_html=True)


def image_to_base64(path):
    with open(path, "rb") as file:
        return base64.b64encode(file.read()).decode()


st.markdown("""
<div class="navbar">
    <div class="navbar-content">
        <div><b>Kayleen Tauhid</b></div>
        <div>
            <a href="#about">About</a>
            <a href="#projects">Projects</a>
            <a href="#experience">Experience</a>
            <a href="#contact">Contact</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>Kayleen Natania Tauhid</h1>
    <p>Aspiring Data Analyst | Applied Mathematics & Data Science</p>
    <a class="button" href="#contact">Contact Me</a>
    <a class="button" href="https://github.com/kayleentauhid" target="_blank">GitHub</a>
</div>
""", unsafe_allow_html=True)

with open("Kayleen_Tauhid_Resume.pdf", "rb") as file:
    st.download_button(
        label="Download PDF Version of Resume",
        data=file,
        file_name="Kayleen_Tauhid_Resume.pdf",
        mime="application/pdf"
    )

st.markdown('<div id="about" class="section-title">About</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h3>About Me</h3>
    <p>
        I graduated from the University of Washington with a degree in Applied Mathematics: Data Science and a minor in Data Science. 
        As an aspiring data scientist I like working with data and looking for patterns. I’m curious by nature and love learning new things
        and expanding what I can do.
    </p>
</div>
""", unsafe_allow_html=True)

confusion_img = image_to_base64("images/confusion_matrix.png")
correlation_img = image_to_base64("images/correlation_heatmap.png")
default_img = image_to_base64("images/default_distribution.png")
feature_img = image_to_base64("images/feature_importance.png")
roc_img = image_to_base64("images/ROC_curve.png")

attribute_gif = image_to_base64("images/attribute_relationships.gif")
era_gif = image_to_base64("images/era_comparison.gif")
trend_gif = image_to_base64("images/trend_analysis.gif")


st.markdown('<div id="projects" class="section-title">Featured Projects</div>',
            unsafe_allow_html=True)

col1, col2 = st.columns(2)

credit_images = {
    "Feature Importance": "images/feature_importance.png",
    "ROC Curve": "images/ROC_curve.png",
    "Confusion Matrix": "images/confusion_matrix.png",
    "Default Distribution": "images/default_distribution.png",
    "Correlation Heatmap": "images/correlation_heatmap.png",
}

music_images = {
    "Trend Analysis": "images/trend_analysis.gif",
    "Attribute Relationships": "images/attribute_relationships.gif",
    "Era Comparison": "images/era_comparison.gif",
}

with col1:
    selected_credit = st.selectbox(
        "Credit Default Preview",
        list(credit_images.keys()),
        label_visibility="collapsed"
    )

    st.image(credit_images[selected_credit], use_container_width=True)

    st.markdown("""
<div class="card">
<h3>Credit Default Prediction</h3>
<ul>
<li>Preprocessed and engineered features from a credit default dataset with 30,000 records using Python and Scikit-learn.</li>
<li>Conducted exploratory data analysis (EDA) to understand the key predictors of credit default.</li>
<li>Developed and tuned a Logistic Regression model using feature scaling and hyperparameters, achieving an F1 score of 0.512 and an ROC-AUC of 0.740.</li>
<li>Compared model performance against Random Forest, SVM, and Gradient Boosting.</li>
</ul>
<p><b>Tools:</b> Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn</p>
<a href="https://github.com/kayleentauhid/credit-default-prediction" target="_blank">View GitHub →</a>
</div>
""", unsafe_allow_html=True)

with col2:
    selected_music = st.selectbox(
        "Music Trends Preview",
        list(music_images.keys()),
        label_visibility="collapsed"
    )

    st.image(music_images[selected_music], use_container_width=True)

    st.markdown("""
<div class="card">
<h3>Music Trends Dashboard</h3>
<ul>
<li>Analyzed 10,000+ songs using audio features including tempo, loudness, duration, key, and mode.</li>
<li>Built an interactive dashboard with dynamic filtering, time-series visualizations, and comparative distribution analysis.</li>
<li>Processed and aggregated music data to uncover long-term trends across musical eras.</li>
<li>Collaborated on the design and implementation of interactive visualizations for exploratory data analysis.</li>
</ul>
<p><b>Tools:</b> Python, D3.js, Observable Plot, HTML, Data Visualization</p>
<a href="https://github.com/kayleentauhid/music-trends-dashboard" target="_blank">View GitHub →</a>
</div>
""", unsafe_allow_html=True)

st.markdown('<div id="experience" class="section-title">Experience</div>',
            unsafe_allow_html=True)

st.markdown("""<div class="timeline">
<div class="card">
<h3>PT Industri Jamu dan Farmasi Sido Muncul Tbk</h3>
<p><b>Data Internship | Jakarta, Indonesia</b></p>
<p class="small-text">July 2025 – August 2025</p>
<ul>
    <li>Collaborated with the team to find, clean, and transform structured datasets related to KukuBima advertising campaigns using Python (Pandas, NumPy) and SQL.</li>
    <li>Partnered with domain experts and team members during sprint cycles to define objectives and identify constraints.</li>
    <li>Contributed to exploratory data analysis (EDA) and feature engineering to evaluate advertising performance and identify factors influencing campaign effectiveness.</li>
    <li>Co-developed interactive Power BI dashboards for stakeholders.</li>
</ul>
</div>

<div class="card">
<h3>Whatcom Community College</h3>
<p><b>Executive Vice President of Operations | Bellingham, WA</b></p>
<p class="small-text">January 2023 – March 2023</p>
<ul>
    <li>Represented students in discussions with state legislators on higher education and student services.</li>
    <li>Coordinated executive board operations, including meeting agendas, documentation, and regulatory compliance.</li>
</ul>
</div>
</div>""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Education</div>',
            unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="card">
        <h3>University of Washington</h3>
        <p><b>Applied Mathematics: Data Science</b></p>
        <p>Minor: Data Science</p>
        <p>Dean’s List 2024–2026</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <h3>Whatcom Community College</h3>
        <p><b>Associate of Arts and Sciences</b></p>
        <p>Graduated with Honors</p>
        <p>Dean’s List 2022–2024</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div id="contact" class="section-title">Contact</div>',
            unsafe_allow_html=True)
st.markdown("""
<div class="card">
    <h3>Let's Connect!</h3>
    <p>Email: kayleen.nataniatauhid@gmail.com </p>
    <p>Phone: (206) 226-8512</p>
    <p>LinkedIn: <a href="https://www.linkedin.com/in/kayleen-tauhid-a1553b372" target="_blank">linkedin.com/in/kayleen-tauhid-a1553b372</a></p>
    <p>GitHub: <a href="https://github.com/kayleentauhid" target="_blank">github.com/kayleentauhid</a></p>
</div>
""", unsafe_allow_html=True)
