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
        background-color: #b3a1ff !important; /* เปลี่ยนเป็นสีม่วงอ่อน (ใกล้เคียงโค้ดเดิมที่คุณให้มา) */
        background-image: none !important;    /* ยกเลิก Gradient เดิม */
        color: #000000 !important;            /* เปลี่ยนสีตัวอักษรเป็นสีดำ */
        padding: 40px 20px;
        border-radius: 0 0 40px 40px;
        text-align: center;
    }

    /* บังคับให้ h1 และ p ภายใน Header เป็นสีดำด้วย */
    .main-header h1, .main-header p {
        color: #000000 !important;
    }
    }

    /* ปรับแต่งหัวข้อในส่วนระบุข้อมูล */
    .st-emotion-cache-10trblm { 
        font-family: 'Prompt', sans-serif !important;
        font-weight: 600;
    }

    .result-card {
        background-color: #b1ebba;
        padding: 25px;
        border-radius: 25px;
        text-align: center;
        margin-top: 20px;
    }

    .result-value {
        color: #0d101a;
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
    income = st.number_input("รายได้ต่อเดือน (บาท)", min_value=0, value=15000, step=500)
    expenses = st.number_input("รายจ่ายต่อเดือน (บาท)", min_value=0, value=8000, step=500)
    months = st.selectbox("แผนสำรอง (กี่เดือน?)", [3, 6, 12], index=1)

# คำนวณ
emergency_fund = expenses * months

# แสดงผลลัพธ์
st.markdown(f"""
    <div class="result-card" style="background-color: #b3a1ff; padding: 20px; border-radius: 10px;">
        <p style="margin-bottom: 0; color: #0d101a; font-weight: 400;">เงินสำรองที่ควรมี</p>
        <div class="result-value">{emergency_fund:,.0f}</div>
        <p style="margin-top: 0; color: #212121; font-weight: 400;">บาท</p>
    </div>
    """, unsafe_allow_html=True)

st.info(f"เป้าหมายนี้ช่วยให้คุณมั่นใจในการใช้ชีวิตและการวางแผนท่องเที่ยวในอนาคต")
