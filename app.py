import streamlit as st

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Python Interactive Lab",
    page_icon="🐍",
    layout="wide"
)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

/* Main Background */
.stApp {
    background-color: #F5F5F5;
}

/* Main Title */
.main-title {
    color: #222222;
    font-size: 55px;
    font-weight: bold;
    letter-spacing: 2px;
    text-align: center;
    width: 100%;
    line-height: 1.2;
}

/* Subtitle */
.subtitle {
    color: #1E2A44;
    font-size: 28px;
    font-weight: 600;
}

/* Author Text */
.author {
    color: #8B0000;   /* Dark Red */
    font-size: 22px; /* Smaller Size */
    font-weight: bold;
}

/* Normal Text */
.normal-text {
    color: #333333;
    font-size: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# MAIN PAGE
# =========================================

st.markdown(
    '<div class="main-title">🐍 Python Interactive Lab</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Welcome to Python Learning Platform</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="author">By Sakda Wongadyarin</p>',
    unsafe_allow_html=True
)

st.markdown("---")

st.markdown(
    '<p class="normal-text">เลือกบทเรียนจาก Sidebar ด้านซ้าย</p>',
    unsafe_allow_html=True
)