import streamlit as st

# 앱 제목
st.title("오늘의 식단 정리")

# 아침 식단 입력
st.header("아침")
breakfast = st.text_input("아침 식단을 입력하세요", "예: 밥, 김치, 달걀")

# 점심 식단 입력
st.header("점심")
lunch = st.text_input("점심 식단을 입력하세요", "예: 비빔밥, 된장국")

# 저녁 식단 입력
st.header("저녁")
dinner = st.text_input("저녁 식단을 입력하세요", "예: 스테이크, 샐러드")

# 스낵 또는 기타 입력
st.header("스낵/기타")
snacks = st.text_input("스낵 또는 기타 간식 입력", "예: 과일, 요거트")

# 입력된 식단 출력
st.subheader("오늘의 식단")
st.write("**아침:**", breakfast)
st.write("**점심:**", lunch)
st.write("**저녁:**", dinner)
st.write("**스낵/기타:**", snacks)

# 오늘의 식단을 정리하는 메시지
if st.button("오늘의 식단 정리"):
    st.success("오늘의 식단이 정리되었습니다!")
