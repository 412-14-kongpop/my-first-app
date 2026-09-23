import streamlit as st

st.set_page_config(page_title="PROVINCE_GAME", page_icon="🗺️")

st.title("PROVINCE_GAME (จังหวัดไยหยวอออ)")

# ----------------------------------------------------
# 1. ข้อมูลโจทย์และคำตอบทั้ง 8 ข้อ (ข้อละ 5 คะแนน)
# ----------------------------------------------------
QUESTIONS = [
    {"num": 1, "clue": "มีลิงเยอะ 🐒", "ans": "ลพบุรี"},
    {"num": 2, "clue": "เมืองหลวง 🏛️", "ans": "กรุงเทพ"},
    {"num": 3, "clue": "มีหาดบางแสน 🏖️", "ans": "ชลบุรี"},
    {"num": 4, "clue": "เมืองประตูสู่ภาคอีสาน 🚪", "ans": "นครราชสีมา"},
    {"num": 5, "clue": "เกาะที่ใหญ่ที่สุดในประเทศไทย 🏝️", "ans": "ภูเก็ต"},
    {"num": 6, "clue": "ทางโค้งมากกว่า 1,864 โค้ง 🛣️", "ans": "แม่ฮ่องสอน"},
    {"num": 7, "clue": "จังหวัดที่ตั้งอยู่ทางเหนือสุดของประเทศไทย 🧭", "ans": "เชียงราย"},
    {"num": 8, "clue": "มีภูเขาที่สูงที่สุดในประเทศไทย ⛰️", "ans": "เชียงใหม่"},
]

POINTS_PER_QUESTION = 5
MAX_SCORE = len(QUESTIONS) * POINTS_PER_QUESTION  # 8 * 5 = 40 คะแนน

# ----------------------------------------------------
# 2. กำหนดค่าเริ่มต้นใน session_state
# ----------------------------------------------------
for i in range(1, 9):
    if f"ans{i}_val" not in st.session_state:
        st.session_state[f"ans{i}_val"] = ""


# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    for i in range(1, 9):
        st.session_state[f"ans{i}_val"] = ""  # เคลียร์ค่าช่องป้อนคำตอบ
    st.session_state.is_ended = False  # ปิดหน้าต่างสรุปผล


# ----------------------------------------------------
# 3. ฟังก์ชัน MessageBox แสดงผลลัพธ์ (Dialog)
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(user_answers):
    score = 0

    st.write("### 📝 รายละเอียดการตรวจคำตอบ (ข้อละ 5 คะแนน)")

    for idx, q in enumerate(QUESTIONS):
        u_ans = user_answers[idx].strip().replace(" ", "")
        correct_ans = q["ans"].strip().replace(" ", "")

        # ตรวจสอบคำตอบ (รองรับทั้งแบบมีคำว่า 'กรุงเทพ' หรือ 'กรุงเทพมหานคร')
        is_correct = False
        if q["num"] == 2 and u_ans in ["กรุงเทพ", "กรุงเทพมหานคร", "กทม"]:
            is_correct = True
        elif u_ans == correct_ans:
            is_correct = True

        if is_correct:
            st.success(f"✅ ข้อ {q['num']}: ถูกต้อง (+5 คะแนน) - ตอบ {q['ans']}")
            score += POINTS_PER_QUESTION
        else:
            st.error(
                f"❌ ข้อ {q['num']}: ยังไม่ถูกต้อง (คุณตอบ '{user_answers[idx]}' | เฉลย: {q['ans']})"
            )

    st.divider()
    st.info(f"🏆 ได้คะแนนรวม: {score} / {MAX_SCORE} คะแนน")

    # 📌 ตัดเกรด/ประเมินผลตามเงื่อนไขคะแนน
    if score == 40:
        st.balloons()
        st.success("🎉 เก่งสุดๆ")
    elif score >= 30:
        st.success("👏 เก่งมาก")
    elif score >= 20:
        st.info("👍 เก่ง")
    elif score >= 10:
        st.warning("😅 เก่งน้อย")
    else:
        st.error("💀 กากก")


# ----------------------------------------------------
# 4. ปุ่มเริ่มเล่นใหม่ / รีเซ็ตคำตอบ
# ----------------------------------------------------
st.button("🎮 เริ่มใหม่ / เคลียร์คำตอบ", on_click=reset_game)

st.divider()

# ----------------------------------------------------
# 5. แสดงช่องรับคำตอบข้อ 1 - 8
# ----------------------------------------------------
st.subheader("🧩 ทายชื่อจังหวัดจากคำใบ้ต่อไปนี้ (ข้อละ 5 คะแนน เต็ม 40 คะแนน)")

user_answers = []
for q in QUESTIONS:
    i = q["num"]
    val = st.text_input(
        f"ข้อ {i}: {q['clue']}",
        value=st.session_state[f"ans{i}_val"],
        key=f"input_{i}",
    )
    st.session_state[f"ans{i}_val"] = val
    user_answers.append(val)

# ----------------------------------------------------
# 6. ปุ่มส่งคำตอบ
# ----------------------------------------------------
if st.button("📥 ส่งคำตอบ"):
    st.session_state.is_ended = True

# ----------------------------------------------------
# 7. แสดง Dialog สรุปผล
# ----------------------------------------------------
if st.session_state.get("is_ended", False):
    show_result_dialog(user_answers)

st.divider()
st.write("กลุ่ม 6")
