import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Google Sheets API 설정
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS = Credentials.from_service_account_file('path_to_your_service_account_key.json', scopes=SCOPE)

# 스프레드시트 접근
client = gspread.authorize(CREDS)
sheet = client.open('오늘의 식단').sheet1  # '오늘의 식단'은 스프레드시트 이름입니다

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

# Google Sheets에 데이터 추가
def add_to_sheet(breakfast, lunch, dinner, snacks):
    sheet.append_row([breakfast, lunch, dinner, snacks])

# 오늘의 식단을 정리하는 메시지
if st.button("오늘의 식단 정리"):
    add_to_sheet(breakfast, lunch, dinner, snacks)
    st.success("오늘의 식단이 Google 스프레드시트에 저장되었습니다!")
