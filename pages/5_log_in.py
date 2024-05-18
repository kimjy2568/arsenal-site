import streamlit as st
import os

def login():
    st.title("로그인 화면")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("로그인"):
        if username == "user" and password == "1234":
            st.success("로그인 되었습니다")
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.error("사용자 이름또는 비밀번호가 잘못되었습니다")

def download_excel(excel_path):
    with open(excel_path, "rb") as f:
        excel_bytes = f.read()
    return excel_bytes

def main_page():
    st.title("아스날 리그 순위 엑셀")
    st.write("로그인된 상태입니다")
    
    excel_path = "ranking.xlsx"
    excel_bytes = download_excel(excel_path)
    st.download_button(
        label="Download Excel File",
        data=excel_bytes,
        file_name=os.path.basename(excel_path),
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    
    if st.button("로그아웃"):
        st.session_state.logged_in = False
        st.experimental_rerun()

# 로그인 여부에 따라 페이지 변경
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
else:
    main_page()
