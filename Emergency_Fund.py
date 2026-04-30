import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="Emergency Fund Calculator", layout="centered")

# แก้ไข Parameter จาก unsafe_allow_key_init เป็น unsafe_allow_html
st.markdown("""
    <style>
    /* 1. เปลี่ยน URL เป็นชื่อฟอนต์ที่เลือก (เช่น Prompt) */
    @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;600&display=swap');

    /* 2. เปลี่ยนชื่อฟอนต์ใน font-family */
    html, body, [class*="st-"], .main-header h1, .main-header p {
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
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }

    .main-header h1 {
        font-size: 2.5rem;
        font-weight: 600;
        margin-bottom: 5px;
        color: white !important;
    }

    .main-header p {
        font-size: 1.1rem;
        font-weight: 300;
        opacity: 0.9;
        color: white !important;
    }

    .result-card {
        background-color: #a7ebd2;
        padding: 25px;
        border-radius: 25px;
        text-align: center;
        margin-top: 20px;
        border: 2px solid #ffffff;
    }

    .result-value {
        color: #2596be;
        font-size: 3rem;
        font-weight: 700;
    }
    </style>
    """, unsafe_allow_html=True)

# ส่วนหัว
st.markdown('<div class="main-header"><h1>Emergency Fund</h1><p>คำนวณเงินสำรองเพื่อความอุ่นใจ</p></div>', unsafe_allow_html=True)

# ส่วนอินพุต (ใช้ข้อมูลฐานเงินเดือน 32,585 บาท)
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
        <p style="margin-bottom: 0; color: #2d3436;">เงินสำรองที่ควรมี</p>
        <div class="result-value">{emergency_fund:,.2f}</div>
        <p style="margin-top: 0; color: #636e72;">บาท</p>
    </div>
    """, unsafe_allow_html=True)

st.info(f"เป้าหมายนี้ช่วยให้คุณมั่นใจในการใช้ชีวิตและการวางแผนท่องเที่ยวในอนาคต")
