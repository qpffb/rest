import streamlit as st
import time

# --- 페이지 설정 ---
st.set_page_config(
    page_title="MZ MBTI 진로 폼 미쳤다 🔥", 
    page_icon="🚀", 
    layout="wide"
)

# --- 🚨 에러 원천 차단 깔끔 다크모드 CSS 🚨 ---
st.markdown("""
<style>
    .stApp {
        background-color: #020617 !important;
        color: #F8FAFC !important;
    }
    .bento-box {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.8), rgba(15, 23, 42, 0.95));
        border: 1px solid #334155;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
    }
    .neon-text {
        color: #84CC16;
        font-weight: 800;
        text-shadow: 0 0 10px rgba(132, 204, 22, 0.5);
    }
    .stRadio label, .stCheckbox label {
        color: #F8FAFC !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 헤더 섹션 ---
st.markdown("<h1 style='text-align: center;'>🔥✨💯 폼 미쳤다! 버튼 조합형 찰떡 직업 🚀💸👑</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #94A3B8;'>😎 SyntaxError 박멸 & 다채로운 GIF 폭탄 버전 💥🤡</h3>", unsafe_allow_html=True)
st.write("---")

# MBTI별 직업 데이터 + 각 성향별로 다채롭고 갓생/도파민 터지는 GIF 매핑
mbti_jobs = {
    "INTJ": {
        "job": "AI 설계자, 스타트업 CEO 🧠💼", 
        "desc": "팩폭 장인인 너! 감정소모 없이 능력으로 압살하는 직업이 딱임 💀💯", 
        "imgs": [
            "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif",
            "https://media.giphy.com/media/L1R1tvI9svkIWwpVYr/giphy.gif",
            "https://media.giphy.com/media/xT5LMPj8P2CDUDOqYg/giphy.gif",
            "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif",
            "https://media.giphy.com/media/26ufdipQqUpi3A9Rc/giphy.gif",
            "https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif",
            "https://media.giphy.com/media/oF5oUYTOX97eqEqFua/giphy.gif",
            "https://media.giphy.com/media/3o85xwxr06YNoFdSbm/giphy.gif",
            "https://media.giphy.com/media/26AHvVwUu9P929Rfy/giphy.gif",
            "https://media.giphy.com/media/3o7qDEq2bMbcbPRQ2c/giphy.gif"
        ]
    },
    "INTP": {
        "job": "데이터 과학자, 화이트해커 💻🕵️‍♂️", 
        "desc": "방구석 아인슈타인 그 잡채 🤓✨ 논리로 우주 정복 가능!", 
        "imgs": [
            "https://media.giphy.com/media/Y4cCRuGpvwjzO/giphy.gif",
            "https://media.giphy.com/media/L1R1tvI9svkIWwpVYr/giphy.gif",
            "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif",
            "https://media.giphy.com/media/xT5LMPj8P2CDUDOqYg/giphy.gif",
            "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif",
            "https://media.giphy.com/media/26ufdipQqUpi3A9Rc/giphy.gif",
            "https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif",
            "https://media.giphy.com/media/oF5oUYTOX97eqEqFua/giphy.gif",
            "https://media.giphy.com/media/3o85xwxr06YNoFdSbm/giphy.gif",
            "https://media.giphy.com/media/3o7qDEq2bMbcbPRQ2c/giphy.gif"
        ]
    },
    "ENTJ": {
        "job": "대기업 임원, 경영 컨설턴트 🚀👑", 
        "desc": "추진력 불도저급 ㄷㄷ 네가 가는 길이 곧 법이다 🔥🔥", 
        "imgs": [
            "https://media.giphy.com/media/Lqji0EE1zMDG8/giphy.gif",
            "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif",
            "https://media.giphy.com/media/xT5LMPj8P2CDUDOqYg/giphy.gif",
            "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif",
            "https://media.giphy.com/media/26ufdipQqUpi3A9Rc/giphy.gif",
            "https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif",
            "https://media.giphy.com/media/oF5oUYTOX97eqEqFua/giphy.gif",
            "https://media.giphy.com/media/3o85xwxr06YNoFdSbm/giphy.gif",
            "https://media.giphy.com/media/26AHvVwUu9P929Rfy/giphy.gif",
            "https://media.giphy.com/media/3o7qDEq2bMbcbPRQ2c/giphy.gif"
        ]
    },
    "ENTP": {
        "job": "크리에이티브 디렉터, 발명가 🤪💡", 
        "desc": "아이디어 뱅크 미쳤고~ 말빨로 세상 다 씹어먹을 상 🤡✨", 
        "imgs": [
            "https://media.giphy.com/media/26ufdipQqUpi3A9Rc/giphy.gif",
            "https://media.giphy.com/media/Lqji0EE1zMDG8/giphy.gif",
            "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif",
            "https://media.giphy.com/media/xT5LMPj8P2CDUDOqYg/giphy.gif",
            "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif",
            "https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif",
            "https://media.giphy.com/media/oF5oUYTOX97eqEqFua/giphy.gif",
            "https://media.giphy.com/media/3o85xwxr06YNoFdSbm/giphy.gif",
            "https://media.giphy.com/media/26AHvVwUu9P929Rfy/giphy.gif",
            "https://media.giphy.com/media/3o7qDEq2bMbcbPRQ2c/giphy.gif"
        ]
    },
    "INFJ": {
        "job": "심리 상담가, 소설가 🥺📚", 
        "desc": "겉바속촉 힐러! 통찰력으로 사람 맘 꿰뚫어보는 능력이 거의 무당급 🔮✨", 
        "imgs": [
            "https://media.giphy.com/media/11sBLVxIRvnMQ8/giphy.gif",
            "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif",
            "https://media.giphy.com/media/xT5LMPj8P2CDUDOqYg/giphy.gif",
            "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif",
            "https://media.giphy.com/media/26ufdipQqUpi3A9Rc/giphy.gif",
            "https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif",
            "https://media.giphy.com/media/oF5oUYTOX97eqEqFua/giphy.gif",
            "https://media.giphy.com/media/3o85xwxr06YNoFdSbm/giphy.gif",
            "https://media.giphy.com/media/26AHvVwUu9P929Rfy/giphy.gif",
            "https://media.giphy.com/media/3o7qDEq2bMbcbPRQ2c/giphy.gif"
        ]
    },
    "INFP": {
        "job": "웹소설 작가, 일러스트레이터 🎨🌸", 
        "desc": "망상력 만렙! 너의 머릿속 판타지를 돈으로 바꿔봐 💸💸🥺", 
        "imgs": [
            "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
            "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif",
            "https://media.giphy.com/media/xT5LMPj8P2CDUDOqYg/giphy.gif",
            "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif",
            "https://media.giphy.com/media/26ufdipQqUpi3A9Rc/giphy.gif",
            "https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif",
            "https://media.giphy.com/media/oF5oUYTOX97eqEqFua/giphy.gif",
            "https://media.giphy.com/media/3o85xwxr06YNoFdSbm/giphy.gif",
            "https://media.giphy.com/media/26AHvVwUu9P929Rfy/giphy.gif",
            "https://media.giphy.com/media/3o7qDEq2bMbcbPRQ2c/giphy.gif"
        ]
    },
    "ENFJ": {
        "job": "라이프 코치, HR 매니저 🥰🤝", 
        "desc": "인간 리트리버? 아니 인간 햇살! 주변 사람들 다 감기는 마성의 매력 ☀️💖", 
        "imgs": [
            "https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif",
            "https://media.giphy.com/media/11sBLVxIRvnMQ8/giphy.gif",
            "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif",
            "https://media.giphy.com/media/xT5LMPj8P2CDUDOqYg/giphy.gif",
            "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif",
            "https://media.giphy.com/media/26ufdipQqUpi3A9Rc/giphy.gif",
            "https://media.giphy.com/media/oF5oUYTOX97eqEqFua/giphy.gif",
            "https://media.giphy.com/media/3o85xwxr06YNoFdSbm/giphy.gif",
            "https://media.giphy.com/media/26AHvVwUu9P929Rfy/giphy.gif",
            "https://media.giphy.com/media/3o7qDEq2bMbcbPRQ2c/giphy.gif"
        ]
    },
    "ENFP": {
        "job": "유튜버, 틱톡커, 파티 플래너 🎉📱", 
        "desc": "인싸 그 잡채! 텐션 감당 불가 ㅋㅋㅋ 너는 무조건 카메라 앞에 서야 함 🤪📸", 
        "imgs": [
            "https://media.giphy.com/media/oF5oUYTOX97eqEqFua/giphy.gif",
            "https://media.giphy.com/media/Lqji0EE1zMDG8/giphy.gif",
            "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif",
            "https://media.giphy.com/media/xT5LMPj8P2CDUDOqYg/giphy.gif",
            "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif",
            "https://media.giphy.com/media/26ufdipQqUpi3A9Rc/giphy.gif",
            "https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif",
            "https://media.giphy.com/media/3o85xwxr06YNoFdSbm/giphy.gif",
            "https://media.giphy.com/media/26AHvVwUu9P929Rfy/giphy.gif",
            "https://media.giphy.com/media/3o7qDEq2bMbcbPRQ2c/giphy.gif"
        ]
    },
    "ISTJ": {
        "job": "공인회계사, 공무원 🧐📊", 
        "desc": "갓생러의 표본! 칼각 맞추는 거 좋아하는 너에겐 안정감이 최고 👍💯", 
        "imgs": [
            "https://media.giphy.com/media/3o85xwxr06YNoFdSbm/giphy.gif",
            "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif",
            "https://media.giphy.com/media/xT5LMPj8P2CDUDOqYg/giphy.gif",
            "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif",
            "https://media.giphy.com/media/26ufdipQqUpi3A9Rc/giphy.gif",
            "https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif",
            "https://media.giphy.com/media/oF5oUYTOX97eqEqFua/giphy.gif",
            "https://media.giphy.com/media/Lqji0EE1zMDG8/giphy.gif",
            "https://media.giphy.com/media/26AHvVwUu9P929Rfy/giphy.gif",
            "https://media.giphy.com/media/3o7qDEq2bMbcbPRQ2c/giphy.gif"
        ]
    },
    "ISFJ": {
        "job": "간호사, 유치원 교사 👼💉", 
        "desc": "천사 강림 ㅠㅠ 기억력도 좋아서 꼼꼼하게 챙겨주는 일에 재능캐임 💖✨", 
        "imgs": [
            "https://media.giphy.com/media/26AHvVwUu9P929Rfy/giphy.gif",
            "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif",
            "https://media.giphy.com/media/xT5LMPj8P2CDUDOqYg/giphy.gif",
            "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif",
            "https://media.giphy.com/media/26ufdipQqUpi3A9Rc/giphy.gif",
            "https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif",
            "https://media.giphy.com/media/oF5oUYTOX97eqEqFua/giphy.gif",
            "https://media.giphy.com/media/3o85xwxr06YNoFdSbm/giphy.gif",
            "https://media.giphy.com/media/Lqji0EE1zMDG8/giphy.gif",
            "https://media.giphy.com/media/3o7qDEq2bMbcbPRQ2c/giphy.gif"
        ]
    },
    "ESTJ": {
        "job": "프로젝트 매니저, 경찰관 👮‍♂️📈", 
        "desc": "리더십 폼 미쳤다! 팩트 폭격기로 일 처리 속도 5G급 🔥🚀", 
        "imgs": [
            "https://media.giphy.com/media/3o7qDEq2bMbcbPRQ2c/giphy.gif",
            "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif",
            "https://media.giphy.com/media/xT5LMPj8P2CDUDOqYg/giphy.gif",
            "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif",
            "https://media.giphy.com/media/26ufdipQqUpi3A9Rc/giphy.gif",
            "https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif",
            "https://media.giphy.com/media/oF5oUYTOX97eqEqFua/giphy.gif",
            "https://media.giphy.com/media/3o85xwxr06YNoFdSbm/giphy.gif",
            "https://media.giphy.com/media/26AHvVwUu9P929Rfy/giphy.gif",
            "https://media.giphy.com/media/Lqji0EE1zMDG8/giphy.gif"
        ]
    },
    "ESFJ": {
        "job": "호텔리어, PR 전문가 🏨🗣️", 
        "desc": "친화력 무엇? 어딜 가도 인싸 그룹 센터 차지할 마당발 🥳👑", 
        "imgs": [
            "https://media.giphy.com/media/3o7TKDk86h4FpBqW6A/giphy.gif",
            "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif",
            "https://media.giphy.com/media/xT5LMPj8P2CDUDOqYg/giphy.gif",
            "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif",
            "https://media.giphy.com/media/26ufdipQqUpi3A9Rc/giphy.gif",
            "https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif",
            "https://media.giphy.com/media/oF5oUYTOX97eqEqFua/giphy.gif",
            "https://media.giphy.com/media/3o85xwxr06YNoFdSbm/giphy.gif",
            "https://media.giphy.com/media/26AHvVwUu9P929Rfy/giphy.gif",
            "https://media.giphy.com/media/3o7qDEq2bMbcbPRQ2c/giphy.gif"
        ]
    },
    "ISTP": {
        "job": "파일럿, 소프트웨어 엔지니어 ✈️🔧", 
        "desc": "만능 재주꾼! 무심한 척하면서 뚝딱뚝딱 다 고쳐내는 츤데레 장인 😎✨", 
        "imgs": [
            "https://media.giphy.com/media/Y4cCRuGpvwjzO/giphy.gif",
            "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif",
            "https://media.giphy.com/media/xT5LMPj8P2CDUDOqYg/giphy.gif",
            "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif",
            "https://media.giphy.com/media/26ufdipQqUpi3A9Rc/giphy.gif",
            "https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif",
            "https://media.giphy.com/media/oF5oUYTOX97eqEqFua/giphy.gif",
            "https://media.giphy.com/media/3o85xwxr06YNoFdSbm/giphy.gif",
            "https://media.giphy.com/media/26AHvVwUu9P929Rfy/giphy.gif",
            "https://media.giphy.com/media/3o7qDEq2bMbcbPRQ2c/giphy.gif"
        ]
    },
    "ISFP": {
        "job": "패션 디자이너, 뮤지션 🎸👗", 
        "desc": "예술혼 불타오르네 🔥 누워있는 거 젤 좋아하지만 필 받으면 장난 아님 🥺✨", 
        "imgs": [
            "https://media.giphy.com/media/XbJX8mE1wD0t2/giphy.gif",
            "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif",
            "https://media.giphy.com/media/xT5LMPj8P2CDUDOqYg/giphy.gif",
            "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif",
            "https://media.giphy.com/media/26ufdipQqUpi3A9Rc/giphy.gif",
            "https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif",
            "https://media.giphy.com/media/oF5oUYTOX97eqEqFua/giphy.gif",
            "https://media.giphy.com/media/3o85xwxr06YNoFdSbm/giphy.gif",
            "https://media.giphy.com/media/26AHvVwUu9P929Rfy/giphy.gif",
            "https://media.giphy.com/media/3o7qDEq2bMbcbPRQ2c/giphy.gif"
        ]
    },
    "ESTP": {
        "job": "사업가, 스포츠 에이전트 💸🏃‍♂️", 
        "desc": "인생은 한 방! 스릴 즐기는 폼이 예사롭지 않음. 실행력 킹정 💯🔥", 
        "imgs": [
            "https://media.giphy.com/media/3o6Zt4HU9uwXmXSAuI/giphy.gif",
            "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif",
            "https://media.giphy.com/media/xT5LMPj8P2CDUDOqYg/giphy.gif",
            "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif",
            "https://media.giphy.com/media/26ufdipQqUpi3A9Rc/giphy.gif",
            "https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif",
            "https://media.giphy.com/media/oF5oUYTOX97eqEqFua/giphy.gif",
            "https://media.giphy.com/media/3o85xwxr06YNoFdSbm/giphy.gif",
            "https://media.giphy.com/media/26AHvVwUu9P929Rfy/giphy.gif",
            "https://media.giphy.com/media/3o7qDEq2bMbcbPRQ2c/giphy.gif"
        ]
    },
    "ESFP": {
        "job": "아이돌, 뮤지컬 배우 🎤🌟", 
        "desc": "무대 체질 ㄷㄷ 스포트라이트 안 받으면 병나는 슈퍼스타 그 잡채 🤩✨", 
        "imgs": [
            "https://media.giphy.com/media/13hxeOYjoTWtK8/giphy.gif",
            "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif",
            "https://media.giphy.com/media/xT5LMPj8P2CDUDOqYg/giphy.gif",
            "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif",
            "https://media.giphy.com/media/26ufdipQqUpi3A9Rc/giphy.gif",
            "https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif",
            "https://media.giphy.com/media/oF5oUYTOX97eqEqFua/giphy.gif",
            "https://media.giphy.com/media/3o85xwxr06YNoFdSbm/giphy.gif",
            "https://media.giphy.com/media/26AHvVwUu9P929Rfy/giphy.gif",
            "https://media.giphy.com/media/3o7qDEq2bMbcbPRQ2c/giphy.gif"
        ]
    }
}

# --- 4가지 지표 버튼 선택 영역 ---
st.markdown("<div class='bento-box'>", unsafe_allow_html=True)
st.markdown("### 👇 버튼으로 쪼개서 골라봐! 너의 성향은? 🧠👇")

col1, col2 = st.columns(2)
with col1:
    ei = st.radio("에너지 방향 (E / I)", ["E (외향)", "I (내향)"], horizontal=True)
    ns = st.radio("인식 기능 (N / S)", ["N (직관)", "S (감각)"], horizontal=True)

with col2:
    tf = st.radio("판단 기능 (T / F)", ["T (사고)", "F (감정)"], horizontal=True)
    pj = st.radio("생활 양식 (P / J)", ["P (인식)", "J (판단)"], horizontal=True)

st.markdown("</div>", unsafe_allow_html=True)

# 선택한 값 조합해서 MBTI 문자열 만들기
selected_mbti = ei[0] + ns[0] + tf[0] + pj[0]

# --- 결과 확인 버튼 ---
if st.button("🚀 내 직업 확인하기! 가보자고! 🔥", use_container_width=True):
    st.success(f"선택완료! 조합된 MBTI: {selected_mbti} 🎉🎉🎉")
    
    with st.spinner("MZ 맞춤형 도파민 수치 계산 중... 🔮✨"):
        time.sleep(1.0)
    st.balloons()
    
    # 벤토 그리드 카드 레이아웃
    st.markdown("<div class='bento-box'>", unsafe_allow_html=True)
    st.markdown(f"## 💖 완성된 너의 MBTI: <span class='neon-text'>{selected_mbti}</span> 💖", unsafe_allow_html=True)
    st.markdown(f"### 🎯 추천 직업: {mbti_jobs[selected_mbti]['job']}")
    st.info(f"👉 {mbti_jobs[selected_mbti]['desc']}")
    st.markdown("🔥 **라디오 버튼 조합형으로 라이트모드 찌꺼기 제로(0)% 달성** 💯")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # 해당 MBTI 전용 다채로운 GIF 폭탄 세례 (3열 그리드)
    st.markdown(f"### 💥 {selected_mbti} 맞춤형 도파민 GIF 폭탄 세례 💥")
    imgs = mbti_jobs[selected_mbti]['imgs']
    for i in range(0, len(imgs), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(imgs):
                with cols[j]:
                    st.image(imgs[i + j], use_container_width=True)
    
    # 마무리 이모지
    st.markdown("<h4 style='text-align: center;'>💸💸💸👑👑👑🤪🤪🤪💀💀💀🔥🔥🔥🚀🚀🚀</h4>", unsafe_allow_html=True)
    st.write("에러도 안 나고 GIF도 꽉 찼지? 완벽 그 잡채니까 빨리 친구들한테 공유 ㄱㄱ 🚀🚀")

# 푸터
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748B;'>© 2026 MZ Career Education Platform. All rights reserved. 🔥</p>", unsafe_allow_html=True)
