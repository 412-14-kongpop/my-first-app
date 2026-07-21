import streamlit as st
st.title("เเอพพลิเคชั่นเเปลงปี พ.ศ. เป็นปี ค.ศ." )

bh_year=st.number_input("กรองปีพ.ศ. ที่ต้องการเเปลง",value=2569)
ce_year=bh_year-543
st.header(f"ปี ค.ศ. คือ : {ce_year}")
