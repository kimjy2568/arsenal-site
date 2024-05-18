import streamlit as st
import random

# 정해진 글과 사진의 쌍들
content_pairs = [
    {"text": "카이 하베르츠-스트라이커", "image_url": "https://i.namu.wiki/i/gVtWsTyFpHddhoWSmk3ILHdEtiXdPxTmayl75rJb_uiH7yfUfOGGHzXlv856GWbD79wZbTB9Nv4aK7P7r7WZAr0Y2pkArOyis-D6iLrYPFOHmm8MUpvaASg9Ncqi2cm2ymGSd6uepa2o9Y-iUlaaWQ.webp"},
    {"text": "데클란 라이스-중앙 미드필더", "image_url": "https://i.namu.wiki/i/g1QlS_-y3ea6XekYSBjEVkUcu5FJNsDUE8APV60SJs9JhHVh4O9gMxR_Iqm3us-LqUfPatgS_7Imdk7D_2TDyTOoRnawfyoygeWFVunXRVu92YPYQPVu4E0pKMWMGVmokUeErpSd4goPkiipr8ZLpA.webp"},
    {"text": "부카요 사카-윙어", "image_url": "https://i.namu.wiki/i/ZPHH4uOy5PMskpgyiNjCpdQVvJENqx_QjysM126zdMijVf8NCNALd3MgBJIdch5W-55Uy-sD3BWh__F-kXUR_69HuImbnwqLIHLgohCNRMowdMX3ShI7ml73n0CYSyzsQcRjVuyjbjDzR6DzgUty1g.webp"},
    {"text": "가브리엘 마갈량이스-센터백", "image_url": "https://i.namu.wiki/i/FY-sTvp2gei_Nky8QnExjpsrOEIDGuGXXxkMBa49SNQF2pldiEe0fUZODYtYWdBEwsx79PFlbmdSFaDPkB1q79-rTS_rldvEDG7TBj7l2BVjdM4I9yGE66DELn-ISywWmnwrto9GJS6Gdy2a_mINSg.webp"},
    {"text": "윌리엄 살리바-센터백", "image_url": "https://i.namu.wiki/i/Bs4P1QHchxLgFDxomWrljq4ezcQotxKsRJSZ5J88rnIGEsiMREJxrsy2FxI9jWGyle2vuYlzwhb8JKb39TTy4DLkk6yt67u8t9nHR1hJWuqMOhU3ZsXzxWFZdXRX_ANAmQ5v5h5m3lFdaEC19qu7wg.webp"}
]

# 버튼을 누르면 랜덤한 글과 사진을 출력하는 함수
def display_random_content():
    pair = random.choice(content_pairs)
    st.write(pair["text"])
    st.image(pair["image_url"], use_column_width=True)

# Streamlit 앱 제목 설정
st.title('오늘의 선수')

# 'Generate Random Content' 버튼 생성
if st.button('버튼을 누르세요'):
    display_random_content()