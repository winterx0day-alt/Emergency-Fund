import streamlit as st

st.set_page_config(page_title="Emergency Fund Calculator", layout="centered")

st.markdown("""
    <style>
    /* 1. ดึงฟอนต์ Prompt จาก Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;600&display=swap');

    /* 2. บังคับใช้ Prompt กับ Input, Label, Subheader และ Button */
    html, body, [class*="st-"], .stMarkdown, h3, label, input, select {
        font-family: 'Prompt', sans-serif !important;
    }

    .stApp {
        background-color: #f4f7f9;
    }

    .main-header {
        background: linear-gradient(135deg, #2596be, #acbaee);
        padding: 50px 20px;
        border-radius: 0 0 40px 40px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }

    /* ปรับแต่งหัวข้อในส่วนระบุข้อมูล */
    .st-emotion-cache-10trblm { 
        font-family: 'Prompt', sans-serif !important;
        font-weight: 600;
    }

    .result-card {
        background-color: #a7ebd2;
        padding: 25px;
        border-radius: 25px;
        text-align: center;
        margin-top: 20px;
    }

    .result-value {
        color: #2596be;
        font-size: 3rem;
        font-weight: 700;
        font-family: 'Prompt', sans-serif !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ส่วนหัว
st.markdown("""
    <div class="main-header">
        <h1>Emergency Fund</h1>
        <p>คำนวณเงินสำรองเพื่อความอุ่นใจ</p>
    </div>
    """, unsafe_allow_html=True)

# ส่วนอินพุต - ตอนนี้จะเป็นฟอนต์ Prompt ทั้งหมด
with st.container():
    st.subheader("ระบุข้อมูลทางการเงิน")
    income = st.number_input("รายได้ต่อเดือน (บาท)", min_value=0, value=32585, step=500)
    expenses = st.number_input("รายจ่ายต่อเดือน (บาท)", min_value=0, value=15000, step=500)
    months = st.selectbox("แผนสำรอง (กี่เดือน?)", [3, 6, 12], index=1)

# คำนวณ
emergency_fund = expenses * months

# แสดงผลลัพธ์
st.markdown(f"""
    <div class="result-card">
        <p style="margin-bottom: 0; color: #2d3436; font-weight: 400;">เงินสำรองที่ควรมี</p>
        <div class="result-value">{emergency_fund:,.2f}</div>
        <p style="margin-top: 0; color: #636e72; font-weight: 400;">บาท</p>
    </div>
    """, unsafe_allow_html=True)
