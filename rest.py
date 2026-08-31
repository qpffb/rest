import streamlit as st
import random

st.set_page_config(page_title="Streamlit 타자게임", page_icon="⌨️", layout="centered")

# 타자 연습용 제시어 목록
WORDS = [
    "스트림릿", "파이썬", "깃허브", "마인크래프트", "지뢰찾기",
    "인공지능", "데이터분석", "프론트엔드", "백엔드", "키보드워리어",
    "오픈소스", "알고리즘", "버그수정", "무한루프", "개발자"
]

# 세션 상태(Session State) 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.current_word = random.choice(WORDS)
    st.session_state.input_key = 0  # 텍스트 박스 초기화를 위한 키값
    st.session_state.message = "엔터(Enter)를 누르면 입력됩니다. 시작!"

# 입력 처리 함수 (엔터 칠 때마다 실행됨)
def check_typing():
    # 현재 텍스트 박스에 입력된 값 가져오기
    user_text = st.session_state[str(st.session_state.input_key)]

    if user_text == st.session_state.current_word:
        st.session_state.score += 10
        st.session_state.message = f"✅ 나이스! (+10점)"
        st.session_state.current_word = random.choice(WORDS)
    else:
        st.session_state.score -= 5
        st.session_state.message = f"❌ 오타! 다시 똑바로 쳐봐요 (-5점)"

    # 엔터 칠 때마다 텍스트 박스를 비워주기 위해 key 값을 바꿈
    st.session_state.input_key += 1

st.title("⌨️ 심플 타자 게임")

# 점수판
st.metric(label="💯 현재 점수", value=f"{st.session_state.score} 점")
st.divider()

# 제시어 표시 (크게 보이게)
st.markdown(f"<h2 style='text-align: center; color: #4CAF50;'>{st.session_state.current_word}</h2>", unsafe_allow_html=True)

# 텍스트 입력창 (on_change를 써서 엔터 누를 때마다 check_typing 함수 실행)
st.text_input(
    "위 단어를 똑같이 입력하고 엔터를 누르세요:", 
    key=str(st.session_state.input_key), 
    on_change=check_typing
)

# 피드백 메시지
if "✅" in st.session_state.message:
    st.success(st.session_state.message)
elif "❌" in st.session_state.message:
    st.error(st.session_state.message)
else:
    st.info(st.session_state.message)

# 리셋 버튼
st.divider()
if st.button("🔄 게임 리셋하기"):
    st.session_state.clear()
    st.rerun()
