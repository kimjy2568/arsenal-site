import streamlit as st

# Streamlit 앱 제목 설정
st.title("아스날의 현재 리그 순위")

# 로컬 이미지 불러오기
image = "league.png"

# 이미지 표시
st.image(image, caption='아스날의 리그 순위이다.', use_column_width=True)