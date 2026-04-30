import streamlit as st
import math

st.set_page_config(page_title="Emergency Fund Calculator", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;600&display=swap');

    html, body, [class*="st-"], .stMarkdown, h3, label, input, select {
        font-family: 'Prompt', sans-serif !important;
    }

    .stApp {
        background-color: #f4f7f9;
    }

    .main-header {
        background-color: #b3a1ff !important;
        color: #000000 !important;
        padding: 40px 20px;
        border-radius: 40px 40px 40px 40px;
        text-align: center;
        margin-bottom: 20px;
    }

    .main-header h1, .main-header p {
        color: #000000 !important;
    }

    .result-card {
        background-color: #b3a1ff;
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        margin-top: 20px;
    }

    .plan-card {
        background-color: #a7ebd2;
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        margin-top: 15px;
    }

    .result-value {
        color: #0d101a;
        font-size: 2.8rem;
        font-weight: 700;
    }

    .plan-value {
        color: #2596be;
        font-size: 2.2rem;
        font-weight: 700;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="main-header">
        <h1>Emergency Fund</h1>
        <p>คำนวณระยะเวลาการออมเพื่อเป้าหมาย</p>
    </div>
    """, unsafe_allow_html=True)

with st.container():
    st.subheader("ระบุข้อมูลทางการเงิน")
    income = st.number_input("รายได้ต่อเดือน (บาท)", min_value=0, value=32585, step=500) #
    expenses = st.number_input("รายจ่ายต่อเดือน (บาท)", min_value=0, value=15000, step=500)
    months_multiplier = st.selectbox("เป้าหมายเงินสำรอง (กี่เดือนของรายจ่าย?)", [3, 6, 12], index=1)

st.markdown("---")
st.subheader("ความสามารถในการออม")
monthly_savings = st.number_input("จำนวนเงินที่ต้องการออมต่อเดือน (บาท)", min_value=1, value=5000, step=500)

# คำนวณ
emergency_fund_goal = expenses * months_multiplier
if monthly_savings > 0:
    months_to_reach = math.ceil(emergency_fund_goal / monthly_savings)
    # คิดเป็นกี่ % ของรายได้ต่อเดือน
    percent_of_income = (monthly_savings / income) * 100
else:
    months_to_reach = 0
    percent_of_income = 0

# แสดงผลเป้าหมายรวม
st.markdown(f"""
    <div class="result-card">
        <p style="margin-bottom: 0; color: #0d101a; font-weight: 400;">เป้าหมายเงินสำรองทั้งหมด</p>
        <div class="result-value">{emergency_fund_goal:,.0f}</div>
        <p style="margin-top: 0; color: #212121; font-weight: 400;">บาท</p>
    </div>
    """, unsafe_allow_html=True)

# แสดงผลระยะเวลาที่ต้องใช้
st.markdown(f"""
    <div class="plan-card">
        <p style="margin-bottom: 0; color: #0d101a; font-weight: 400;">ต้องใช้เวลาออมทั้งหมด</p>
        <div class="plan-value">{months_to_reach} เดือน</div>
        <p style="margin-top: 0; color: #212121; font-weight: 400;">ด้วยเงินออม {percent_of_income:.1f}% ของรายได้ต่อเดือน</p>
    </div>
    """, unsafe_allow_html=True)

# ส่วนวิเคราะห์เพิ่มเติม
if percent_of_income > 40:
    st.warning(f"ยอดออม {percent_of_income:.1f}% อาจจะตึงเกินไปสำหรับการจัดการค่าใช้จ่ายส่วนอื่น")
elif percent_of_income > 0:
    st.success(f"การออมเดือนละ {monthly_savings:,.0f} บาท เป็นจุดเริ่มต้นที่ดีสู่ความมั่นคงทางการเงิน")

st.info("การออมอย่างสม่ำเสมอในบัญชีดอกเบี้ยสูง เช่น Dime! จะช่วยให้ถึงเป้าหมายได้เร็วขึ้น")
