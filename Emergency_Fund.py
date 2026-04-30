import streamlit as st

# การตั้งค่าหน้าเว็บและธีมสีตามที่ระบุ
st.set_page_config(page_title="Emergency Fund Calculator", layout="centered")

# Custom CSS เพื่อปรับแต่ง UI ให้ใกล้เคียงกับรูปภาพและโทนสีที่ต้องการ
st.markdown(f"""
    <style>
    .stApp {{
        background-color: #f4f7f9;
    }}
    .main-header {{
        background: linear-gradient(135deg, #2596be, #acbaee);
        padding: 40px;
        border-radius: 0 0 40px 40px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }}
    .result-card {{
        background-color: #a7ebd2;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        margin-top: 20px;
    }}
    .result-value {{
        color: #2596be;
        font-size: 2.5rem;
        font-weight: bold;
    }}
    </style>
    """, unsafe_allow_key_init=True)

# ส่วนหัวของหน้าเว็บ
st.markdown('<div class="main-header"><h1>Emergency Fund</h1><p>คำนวณเงินสำรองเพื่อความอุ่นใจ</p></div>', unsafe_allow_key_init=True)

# ส่วนอินพุตข้อมูล
with st.container():
    st.subheader("ระบุข้อมูลทางการเงิน")
    
    # ดึงข้อมูลจากฐานรายได้เดิม (32,585 THB) เป็นค่าเริ่มต้น
    income = st.number_input("รายได้ต่อเดือน (บาท)", min_value=0, value=32585, step=500)
    
    # รายจ่ายต่อเดือน
    expenses = st.number_input("รายจ่ายต่อเดือน (บาท)", min_value=0, value=15000, step=500)
    
    # จำนวนเดือนที่ต้องการสำรอง
    months = st.selectbox("แผนสำรอง (กี่เดือน?)", [3, 6, 12], index=1)

# การคำนวณ
# หลักการ: เงินสำรอง = รายจ่ายต่อเดือน x จำนวนเดือนที่ต้องการสำรอง
emergency_fund = expenses * months

# แสดงผลลัพธ์
st.markdown(f"""
    <div class="result-card">
        <p style="margin-bottom: 0; color: #2d3436;">เงินสำรองที่ควรมี</p>
        <div class="result-value">{emergency_fund:,.2f}</div>
        <p style="margin-top: 0; color: #636e72;">บาท</p>
    </div>
    """, unsafe_allow_key_init=True)

# คำแนะนำเพิ่มเติม
st.info(f"""
**สรุปแผนการเงิน:**
* เป้าหมายเงินสำรองนี้คิดเป็นประมาณ **{(emergency_fund/income):.1f} เท่า** ของรายได้ต่อเดือนของคุณ
* แนะนำให้แยกเงินส่วนนี้ไว้ในบัญชีที่สภาพคล่องสูงและดอกเบี้ยดี เช่น **Dime!**
""")