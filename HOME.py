import streamlit as st
st.title("내가 좋아하는 스포츠 소개")
st.subheader("축구란 무엇인가")

image_url = "https://cdn.mhnse.com/news/photo/202203/97242_79364_4347.jpg"
st.image(image_url, caption='사진은 현재 프리미어리그 우승후보 아스날이다.', use_column_width=True)

st.write("왠지 자신이 똑똑하고 잘나보이는 사람이 되고싶다면 스포츠 정도는 알아놓는게 좋을거다.")
st.write("오늘은 축구에 대해 알아보겠다.")

st.subheader("1. 경기 시간")
st.write("- 정규 시간은 전후반 각각 45분씩 총 90분입니다.")
st.write("- 전반과 후반 사이에는 15분의 휴식 시간이 있습니다.")
st.write("- 추가 시간 (injury time)이 주어질 수 있습니다.")

st.subheader("2. 경기장")
st.write("- 직사각형 모양의 필드로, 길이는 100\~110미터, 너비는 64\~75미터입니다.")
st.write("- 각 끝에는 골대가 있으며, 골대의 너비는 7.32미터, 높이는 2.44미터입니다.")

st.subheader("4. 골")
st.write("- 공이 완전히 골 라인을 넘으면 득점으로 인정됩니다.")
st.write("- 득점이 많은 팀이 승리합니다")

st.subheader("5. 오프사이드")
st.write("- 공격팀 선수가 패스를 받을 때 상대팀의 두 번째 마지막 수비수보다 골 라인에 더 가까이 있으면 오프사이드로 간주됩니다.")

st.subheader("6. 파울 및 반칙")
st.write("- 직접 프리킥, 간접 프리킥, 페널티킥이 주어질 수 있습니다.")
st.write("- 반칙에는 핸드볼, 태클, 방해 행위 등이 있습니다.")
st.write("- 반칙 시 옐로카드 또는 레드카드를 받을 수 있으며 옐로카드를 두 번 받거나 레드카드를 받으면 퇴장합니다.")

st.subheader("7. 프리킥, 페널티킥, 스로인, 골킥, 코너킥")
st.write("- 직접 프리킥: 직접 슈팅으로 득점 가능.")
st.write("- 간접 프리킥: 다른 선수가 공을 터치해야 득점 인정.")
st.write("- 페널티킥: 페널티 구역 내에서 반칙이 발생할 경우, 11미터 지점에서 페널티킥이 주어집니다.")
st.write("- 스로인: 공이 터치 라인을 넘었을 때 상대팀이 던집니다.")
st.write("- 골킥: 공격팀이 공을 골 라인 넘을 때 수비팀이 킥을 합니다.")
st.write("- 코너킥: 수비팀이 공을 골 라인 넘을 때 공격팀이 코너에서 킥을 합니다.")

st.subheader("아스날에 관하여")
st.write("아스날 FC(Arsenal Football Club)는 영국 런던을 연고지로 하는 프로 축구 클럽으로, 잉글랜드 프리미어리그(EPL)에 속해 있습니다. 1886년에 설립된 아스날은 잉글랜드 축구 역사상 가장 성공적인 클럽 중 하나입니다.")
st.write("잉글랜드 1부 리그 우승 13회, fa컵 우승 14회 등의 많은 우승을 한 팀으로 특히 2003-04시즌에 단 한경기도 패배하지 않고 우승을 차지한 업적이 있습니다.")
st.write("역사적으로 많은 유명 선수들이 아스날에서 뛰었습니다. 대표적인 선수로는 티에리 앙리, 데니스 베르캄프 등이 있습니다.")

image_url = "https://i.namu.wiki/i/_TMYi1-kxIiGfAXPN-NJ52MNdsE7c1pWh4k3HfKaw_GW45jw7R1XXNZwUIXL2mEcp3D-wxvPgp-o48j-XCoVNA.svg"
st.image(image_url, caption='아스날의 로고이다.', use_column_width=True)

#스트림릿 사이트 배포및 작성
#깃 다운로드 깃허브 로그인 깃 원격 레파스토리 깃허브에서 만들기
#내프로젝트 깃이랑 연결해서 원격에 저장시키기
#requirements.txt에 필요한 파이썬 라이브러리 쓰기
#streamlit shared에 들어가서 deploy하기