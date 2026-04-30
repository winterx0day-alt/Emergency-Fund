import streamlit as st

st.set_page_config(page_title="Emergency Fund Calculator", layout="centered")

st.markdown("""
    <style>
    /* 1. ดึงฟอนต์ Prompt จาก Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;600&display=swap');

    /* 2. บังคับใช้ Prompt กับทุกส่วน */
    html, body, [class*="st-"], .stMarkdown, h3, label, input, select {
        font-family: 'Prompt', sans-serif !important;
    }

    .stApp {
        background-color: #f4f7f9;
    }

    .main-header {
        background-color: #b3a1ff !important;
        background-image: none !important;
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
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }

    .plan-card {
        background-color: #a7ebd2;
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        margin-top: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }

    .result-value {
        color: #0d101a;
        font-size: 2.8rem;
        font-weight: 700;
        line-height: 1.2;
    }

    .plan-value {
        color: #2596be;
        font-size: 2.2rem;
        font-weight: 700;
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

# ส่วนอินพุตข้อมูลพื้นฐาน
with st.container():
    st.subheader("ระบุข้อมูลทางการเงิน")
    # ปรับค่าเริ่มต้นตามฐานเงินเดือนจริงของคุณ
    income = st.number_input("รายได้ต่อเดือน (บาท)", min_value=0, value=32585, step=500)
    expenses = st.number_input("รายจ่ายต่อเดือน (บาท)", min_value=0, value=15000, step=500)
    months = st.selectbox("แผนสำรอง (กี่เดือน?)", [3, 6, 12], index=1)

# ส่วนอินพุตแผนการออม (เพิ่มใหม่)
st.markdown("---")
st.subheader("แผนการเก็บเงิน")
target_period = st.slider("ต้องการเก็บให้ครบภายในกี่เดือน?", min_value=1, max_value=48, value=12)

# คำนวณเงินสำรองและเงินที่ต้องเก็บต่อเดือน
emergency_fund = expenses * months
monthly_saving_target = emergency_fund / target_period

# แสดงผลลัพธ์: เงินสำรองที่ควรมี
st.markdown(f"""
    <div class="result-card">
        <p style="margin-bottom: 0; color: #0d101a; font-weight: 400;">เงินสำรองรวมที่ต้องมี</p>
        <div class="result-value">{emergency_fund:,.0f}</div>
        <p style="margin-top: 0; color: #212121; font-weight: 400;">บาท</p>
    </div>
    """, unsafe_allow_html=True)

# แสดงผลลัพธ์: ยอดที่ต้องเก็บต่อเดือน (เพิ่มใหม่)
st.markdown(f"""
    <div class="plan-card">
        <p style="margin-bottom: 0; color: #0d101a; font-weight: 400;">ต้องออมเงินเดือนละ</p>
        <div class="plan-value">{monthly_saving_target:,.2f}</div>
        <p style="margin-top: 0; color: #212121; font-weight: 400;">บาท / เดือน (เป็นเวลา {target_period} เดือน)</p>
    </div>
    """, unsafe_allow_html=True)

# แจ้งเตือนสถานะความยากง่ายในการออม
saving_ratio = (monthly_saving_target / income) * 100
if saving_ratio > 30:
    st.warning(f"ยอดออมต่อเดือนสูงถึง {saving_ratio:.1f}% ของรายได้ อาจจะตึงเกินไป ลองขยายเวลาเก็บเงินดูครับ")
else:
    st.success(f"ยอดออมต่อเดือนคิดเป็น {saving_ratio:.1f}% ของรายได้ เป็นแผนที่ทำได้จริง สู้ๆ ครับ!")

st.info("เป้าหมายนี้ช่วยให้คุณมั่นใจในการใช้ชีวิตและการวางแผนท่องเที่ยวในอนาคต")
