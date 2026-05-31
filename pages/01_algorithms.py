import streamlit as st

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Algorithms Lab",
    page_icon="🧠",
    layout="wide"
)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #F5F7FA;
}

/* Main Title */
.main-title {
    color: #111111;
    font-size: 70px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    color: #1E3A5F;
    font-size: 28px;
    text-align: center;
    margin-bottom: 40px;
}

/* Section Header */
.section-header {
    color: #003366;
    font-size: 38px;
    font-weight: bold;
    margin-top: 30px;
}

/* Normal Text */
.normal-text {
    color: #333333;
    font-size: 22px;
    line-height: 1.8;
}

/* Highlight Box */
.highlight-box {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 15px;
    border-left: 8px solid #00BFFF;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    margin-top: 20px;
    margin-bottom: 20px;
}

/* Algorithm Step */
.step-box {
    background-color: #E8F4FF;
    padding: 15px;
    border-radius: 10px;
    font-size: 24px;
    margin-bottom: 10px;
    color: #003366;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# TITLE
# =========================================

st.markdown(
    '<div class="main-title">🧠 Algorithms Lab</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">เรียนรู้การคิดแบบลำดับขั้นตอน</div>',
    unsafe_allow_html=True
)

# =========================================
# THEORY
# =========================================

st.markdown(
    '<div class="section-header">📘 Algorithm คืออะไร ?</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="highlight-box">

<div class="normal-text">

Algorithm คือ “ลำดับขั้นตอน” ในการแก้ปัญหา  
หรือการทำงานอย่างเป็นระบบทีละขั้นตอน

ตัวอย่างเช่น:
- การทำอาหาร
- การล็อกอิน
- การเดินทางไปโรงเรียน

ทุกอย่างสามารถเขียนเป็น Algorithm ได้

</div>

</div>
""", unsafe_allow_html=True)

# =========================================
# EXAMPLE
# =========================================

st.markdown(
    '<div class="section-header">☕ ตัวอย่าง Algorithm</div>',
    unsafe_allow_html=True
)

st.write("### ขั้นตอนการชงกาแฟ")

steps = [
    "1️⃣ เตรียมน้ำ",
    "2️⃣ ต้มน้ำ",
    "3️⃣ ใส่กาแฟ",
    "4️⃣ เทน้ำร้อน",
    "5️⃣ พร้อมดื่ม ☕"
]

for step in steps:
    st.markdown(
        f'<div class="step-box">{step}</div>',
        unsafe_allow_html=True
    )

# =========================================
# FLOW VISUALIZATION
# =========================================

st.markdown(
    '<div class="section-header">🔄 Flow Process</div>',
    unsafe_allow_html=True
)

st.info("INPUT ➜ PROCESS ➜ OUTPUT")

# =========================================
# INTERACTIVE QUIZ
# =========================================

st.markdown(
    '<div class="section-header">🎮 Interactive Quiz</div>',
    unsafe_allow_html=True
)

st.write("### เลือกขั้นตอนแรกของการชงกาแฟ")

answer = st.radio(
    "ข้อใดควรทำก่อน ?",
    [
        "เทน้ำร้อน",
        "ต้มน้ำ",
        "เตรียมน้ำ",
        "ดื่มกาแฟ"
    ]
)

if st.button("✅ ตรวจคำตอบ"):

    if answer == "เตรียมน้ำ":
        st.success("ถูกต้อง! 🎉")
        st.balloons()

    else:
        st.error("ยังไม่ถูก ลองใหม่อีกครั้ง")

# =========================================
# MINI CHALLENGE
# =========================================

st.markdown(
    '<div class="section-header">🏆 Mini Challenge</div>',
    unsafe_allow_html=True
)

st.write("### จงเขียน Algorithm การมาโรงเรียนของคุณ")

user_algo = st.text_area(
    "พิมพ์ลำดับขั้นตอนที่นี่",
    height=200
)

if st.button("📤 ส่งคำตอบ"):

    if user_algo.strip() == "":
        st.warning("กรุณาพิมพ์คำตอบก่อน")

    else:
        st.success("บันทึกคำตอบเรียบร้อย 👍")

# =========================================
# DAILY LIFE ALGORITHM
# =========================================

st.markdown(
    '<div class="section-header">🌍 Algorithm ในชีวิตประจำวัน</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🍳 ทำอาหาร", "Algorithm")

with col2:
    st.metric("📱 Login", "Algorithm")

with col3:
    st.metric("🚗 เดินทาง", "Algorithm")

# =========================================
# FOOTER
# =========================================

st.markdown("---")

st.caption("Python Interactive Lab • Algorithms Chapter")
