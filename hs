import streamlit as st
from datetime import datetime

# 애플리케이션 제목
st.title("학생 결석 사유 입력")

# 학생 이름 입력
student_name = st.text_input("학생 이름을 입력하세요:")

# 학번 입력
student_id = st.text_input("학번을 입력하세요:")

# 결석 종류 선택
absence_type = st.selectbox(
    "결석 종류를 선택하세요:",
    ["질병결석", "인정결석", "기타결석"]
)

# 결석 날짜 선택
absence_date = st.date_input(
    "결석 날짜를 선택하세요:",
    value=datetime.today()
)

# 결석 사유 입력
reason = st.text_area("결석 사유를 서술하세요:")

# 메모리에 저장된 결석 데이터 리스트
if "absences" not in st.session_state:
    st.session_state.absences = []

# 제출 버튼
if st.button("제출"):
    if not student_name.strip():
        st.error("학생 이름을 입력해 주세요.")
    elif not student_id.strip():
        st.error("학번을 입력해 주세요.")
    elif not reason.strip():
        st.error("결석 사유를 입력해 주세요.")
    elif absence_date > datetime.today().date():
        st.error("미래 날짜는 선택할 수 없습니다.")
    else:
        # 제출된 정보 저장
        st.session_state.absences.append({
            "학생 이름": student_name,
            "학번": student_id,
            "결석 종류": absence_type,
            "결석 날짜": absence_date.strftime('%Y-%m-%d'),
            "사유": reason
        })
        st.success("결석 사유가 성공적으로 제출되었습니다.")

# 기존 제출된 정보 보기
st.sidebar.title("기존 제출된 정보 보기")
if st.session_state.absences:
    for idx, absence in enumerate(st.session_state.absences):
        st.sidebar.write(f"### 제출된 정보 {idx + 1}")
        st.sidebar.write(f"- **학생 이름**: {absence['학생 이름']}")
        st.sidebar.write(f"- **학번**: {absence['학번']}")
        st.sidebar.write(f"- **결석 종류**: {absence['결석 종류']}")
        st.sidebar.write(f"- **결석 날짜**: {absence['결석 날짜']}")
        st.sidebar.write(f"- **사유**: {absence['사유']}")
else:
    st.sidebar.info("현재 저장된 데이터가 없습니다.")
