import streamlit as st
import time

# --- 페이지 설정 ---
st.set_page_config(
    page_title="MZ MBTI 진로 폼 미쳤다 🔥", 
    page_icon="🚀", 
    layout="wide"
)

# --- 🚨 라이트모드 찌꺼기 원천 차단 강력 CSS & JS 핵 🚨 ---
st.markdown("""
<style>
    /* 전체 배경 및 폰트 */
    .stApp {
        background-color: #020617 !importantimport streamlit as str_lib
import time

# --- 페이지 설정 ---
str_lib.set_page_config(
    page_title="MZ MBTI 진로 폼 미쳤다 🔥", 
    page_icon="🚀", 
    layout="wide"
)

# --- 🚨 깔끔하고 확실한 다크모드 전용 CSS (셀렉박스 스트레스 없음!) 🚨 ---
str_lib.markdown("""
<style>
    /* 전체 배경 및 기본 폰트 */
    .stApp {
        background-color: #020617 !important;
        color: #F8FAFC !important;
    }
    
    /* 벤토 박스 */
    .bento-box {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.8), rgba(15, 23, 42, 0.95));
        border: 1px solid #334155;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
    }
    
    /* 네온 포인트 글자 */
    .neon-text {
        color: #84CC16;
        font-weight: 800;
        text-shadow: 0 0 10px rgba(132, 204, 22, 0.5);
    }
    
    /* 라디오 버튼 / 세그먼트 스타일 텍스트 보호 */
    .stRadio label, .stCheckbox label {
        color: #F8FAFC !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 헤더 섹션 ---
str_lib.markdown("<h1 style='text-align: center;'>🔥✨💯 폼 미쳤다! 버튼으로 쪼개서 찾는 찰떡 직업 🚀💸👑</h1>", unsafe_allow_html=True)
str_lib.markdown("<h3 style='text-align: center; color: #94A3B8;'>😎 라이트모드 찌꺼기 원천 차단! 버튼 조합형 MBTI 👈💀👉</h3>", unsafe_allow_html=True)
str_lib.write("---")

# MBTI별 직업 데이터 (16가지 전체 완벽 대응)
mbti_jobs = {
    "INTJ": {
        "job": "AI 설계자, 스타트업 CEO 🧠💼", 
        "desc": "팩폭 장인인 너! 감정소모 없이 능력으로 압살하는 직업이 딱임 💀💯", 
    },
    "INTP": {
        "job": "데이터 과학자, 화이트해커 💻🕵️‍♂️", 
        "desc": "방구석 아인슈타인 그 잡채 🤓✨ 논리로 우주 정복 가능!", 
    },
    "ENTJ": {
        "job": "대기업 임원, 경영 컨설턴트 🚀👑", 
        "desc": "추진력 불도저급 ㄷㄷ 네가 가는 길이 곧 법이다 🔥🔥", 
    },
    "ENTP": {
        "job": "크리에이티브 디렉터, 발명가 🤪💡", 
        "desc": "아이디어 뱅크 미쳤고~ 말빨로 세상 다 씹어먹을 상 🤡✨", 
    },
    "INFJ": {
        "job": "심리 상담가, 소설가 🥺📚", 
        "desc": "겉바속촉 힐러! 통찰력으로 사람 맘 꿰뚫어보는 능력이 거의 무당급 🔮✨", 
    },
    "INFP": {
        "job": "웹소설 작가, 일러스트레이터 🎨🌸", 
        "desc": "망상력 만렙! 너의 머릿속 판타지를 돈으로 바꿔봐 💸💸🥺", 
    },
    "ENFJ": {
        "job": "라이프 코치, HR 매니저 🥰🤝", 
        "desc": "인간 리트리버? 아니 인간 햇살! 주변 사람들 다 감기는 마성의 매력 ☀️💖", 
    },
    "ENFP": {
        "job": "유튜버, 틱톡커, 파티 플래너 🎉📱", 
        "desc": "인싸 그 잡채! 텐션 감당 불가 ㅋㅋㅋ 너는 무조건 카메라 앞에 서야 함 🤪📸", 
    },
    "ISTJ": {
        "job": "공인회계사, 공무원 🧐📊", 
        "desc": "갓생러의 표본! 칼각 맞추는 거 좋아하는 너에겐 안정감이 최고 👍💯", 
    },
    "ISFJ": {
        "job": "간호사, 유치원 교사 👼💉", 
        "desc": "천사 강림 ㅠㅠ 기억력도 좋아서 꼼꼼하게 챙겨주는 일에 재능캐임 💖✨", 
    },
    "ESTJ": {
        "job": "프로젝트 매니저, 경찰관 👮‍♂️📈", 
        "desc": "리더십 폼 미쳤다! 팩트 폭격기로 일 처리 속도 5G급 🔥🚀", 
    },
    "ESFJ": {
        "job": "호텔리어, PR 전문가 🏨🗣️", 
        "desc": "친화력 무엇? 어딜 가도 인싸 그룹 센터 차지할 마당발 🥳👑", 
    },
    "ISTP": {
        "job": "파일럿, 소프트웨어 엔지니어 ✈️🔧", 
        "desc": "만능 재주꾼! 무심한 척하면서 뚝딱뚝딱 다 고쳐내는 츤데레 장인 😎✨", 
    },
    "ISFP": {
        "job": "패션 디자이너, 뮤지션 🎸👗", 
        "desc": "예술혼 불타오르네 🔥 누워있는 거 젤 좋아하지만 필 받으면 장난 아님 🥺✨", 
    },
    "ESTP": {
        "job": "사업가, 스포츠 에이전트 💸🏃‍♂️", 
        "desc": "인생은 한 방! 스릴 즐기는 폼이 예사롭지 않음. 실행력 킹정 💯🔥", 
    },
    "ESFP": {
        "job": "아이돌, 뮤지컬 배우 🎤🌟", 
        "desc": "무대 체질 ㄷㄷ 스포트라이트 안 받으면 병나는 슈퍼스타 그 잡채 🤩✨", 
    }
}

# 공통 GIF 리스트 (도파민 폭탄용)
default_imgs = [
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

# --- 4가지 지표를 버튼(radio horizontal)으로 쪼개서 선택하게 구현 ---
str_lib.markdown("<div class='bento-box'>", unsafe_allow_html=True)
str_lib.markdown("### 👇 쪼개서 골라봐! 너의 성향은? 🧠👇")

col1, col2 = str_lib.columns(2)
with col1:
    ei = str_lib.radio("에너지 방향 (E / I)", ["E (외향)", "I (내향)"], horizontal=True)
    ns = str_lib.radio("인식 기능 (N / S)", ["N (직관)", "S (감각)"], horizontal=True)

with col2:
    tf = str_lib.radio("판단 기능 (T / F)", ["T (사고)", "F (감정)"], horizontal=True)
    pj = str_lib.radio("생활 양식 (P / J)", ["P (인식)", "J (판단)"], horizontal=True)

str_lib.markdown("</div>", unsafe_allow_html=True)

# 선택한 값 조합해서 MBTI 문자열 만들기
selected_mbti = ei[0] + ns[0] + tf[0] + pj[0]

# --- 결과 확인 버튼 ---
if str_lib.button("🚀 내 직업 확인하기! 가보자고! 🔥", use_container_width=True):
    str_lib.success(f"선택완료! 조합된 MBTI: {selected_mbti} 🎉🎉🎉")
    
    with str_lib.spinner("MZ 맞춤형 도파민 수치 계산 중... 🔮✨"):
        time.sleep(1.0)
    str_lib.balloons()
    
    # 벤토 그리드 카드 레이아웃
    str_lib.markdown("<div class='bento-box'>", unsafe_allow_html=True)
    str_lib.markdown(f"## 💖 완성된 너의 MBTI: <span class='neon-text'>{selected_mbti}</span> 💖", unsafe_allow_html=True)
    str_lib.markdown(f"### 🎯 추천 직업: {mbti_jobs[selected_mbti]['job']}")
    str_lib.info(f"👉 {mbti_jobs[selected_mbti]['desc']}")
    str_lib.markdown("🔥 **라디오 버튼 조합형으로 라이트모드 찌꺼기 제로(0)% 달성** 💯")
    str_lib.markdown("</div>", unsafe_allow_html=True)
    
    # GIF 폭탄 세례
    str_lib.markdown("### 💥 뿌슝빠슝 도파민 GIF 폭탄 세례 💥")
    for i in range(0, len(default_imgs), 3):
        cols = str_lib.columns(3)
        for j in range(3):
            if i + j < len(default_imgs):
                with cols[j]:
                    str_lib.image(default_imgs[i + j], use_container_width=True)
    
    # 마무리 이모지
    str_lib.markdown("<h4 style='text-align: center;'>💸💸💸👑👑👑🤪🤪🤪💀💀💀🔥🔥🔥🚀🚀🚀</h4>", unsafe_allow_html=True)
    str_lib.write("어때, 셀렉박스 스트레스 안 받고 깔끔하지? 완벽 그 잡채니까 빨리 친구들한테 공유 ㄱㄱ 🚀🚀")

# 푸터
str_lib.markdown("---")
str_lib.markdown("<p style='text-align: center; color: #64748B;'>© 2026 MZ Career Education Platform. All rights reserved. 🔥</p>", unsafe_allow_html=True)
        color: #F8FAFC !important;
    }
    
    /* 벤토 박스 */
    .bento-box {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.8), rgba(15, 23, 42, 0.95));
        border: 1px solid #334155;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
    }
    
    /* 네온 포인트 */
    .neon-text {
        color: #84CC16;
        font-weight: 800;
        text-shadow: 0 0 10px rgba(132, 204, 22, 0.5);
    }

    /* 💥 스트림릿 셀렉박스(Selectbox) 라이트모드 찌꺼기 완전 섬멸 💥 */
    /* 메인 셀렉박스 입력 필드 */
    div[data-baseweb="select"] > div,
    div[data-baseweb="select"] div {
        background-color: #0f172a !important;
        color: #F8FAFC !important;
        border-color: #334155 !important;
    }
    
    /* 셀렉박스 내부 글자 및 아이콘 */
    div[data-baseweb="select"] span, 
    div[data-baseweb="select"] svg {
        color: #F8FAFC !important;
        fill: #F8FAFC !important;
    }

    /* 드롭다운 펼쳐졌을 때 뜨는 메뉴 리스트 박스 */
    div[data-baseweb="popover"],
    div[data-baseweb="menu"],
    ul[role="listbox"] {
        background-color: #0f172a !important;
        color: #F8FAFC !important;
        border: 1px solid #334155 !important;
    }

    /* 드롭다운 개별 옵션 항목 */
    li[role="option"] {
        background-color: #0f172a !important;
        color: #F8FAFC !important;
    }
    
    /* 마우스 올렸을 때(Hover) 항목 색상 */
    li[role="option"]:hover {
        background-color: #334155 !important;
        color: #84CC16 !important;
    }
    
    /* 선택된 태그나 라벨 배경 */
    span[data-baseweb="tag"] {
        background-color: #334155 !important;
        color: #F8FAFC !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 헤더 섹션 ---
st.markdown("<h1 style='text-align: center;'>🔥✨💯 폼 미쳤다! 내 MBTI에 딱 맞는 찰떡 직업 찾기 🚀💸👑</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #94A3B8;'>😎 MZ력 10000% 충전! 라이트모드 찌꺼기 박멸 버전 💀🤡🤪</h3>", unsafe_allow_html=True)
st.write("---")

# MBTI별 직업 데이터 (GIF 10개 이상 도배)
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
            "https://media.giphy.com/media/L1R1tvI9svkIWwpVYr/giphy.gif",
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
            "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif",
            "https://media.giphy.com/media/xT5LMPj8P2CDUDOqYg/giphy.gif",
            "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif",
            "https://media.giphy.com/media/Lqji0EE1zMDG8/giphy.gif",
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
            "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif",
            "https://media.giphy.com/media/xT5LMPj8P2CDUDOqYg/giphy.gif",
            "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif",
            "https://media.giphy.com/media/26ufdipQqUpi3A9Rc/giphy.gif",
            "https://media.giphy.com/media/11sBLVxIRvnMQ8/giphy.gif",
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
            "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif",
            "https://media.giphy.com/media/xT5LMPj8P2CDUDOqYg/giphy.gif",
            "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif",
            "https://media.giphy.com/media/26ufdipQqUpi3A9Rc/giphy.gif",
            "https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif",
            "https://media.giphy.com/media/Lqji0EE1zMDG8/giphy.gif",
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

# --- 메인 입력 레이아웃 ---
st.markdown("<div class='bento-box'>", unsafe_allow_html=True)
st.markdown("### 👇 현기증 나니까 빨리 골라라 😵‍💫👇")
mbti_options = ["선택안함 🙄"] + list(mbti_jobs.keys())
selected_mbti = st.selectbox("너의 MBTI는?", mbti_options)
st.markdown("</div>", unsafe_allow_html=True)

# --- 결과 확인 버튼 ---
if st.button("🚀 내 직업 확인하기! 가보자고! 🔥", use_container_width=True):
    if selected_mbti == "선택안함 🙄":
        st.error("아니 MBTI를 골라야지 뭐하는거야 💀💀💀 장난 똥때리냐구 🤡🤡")
    else:
        st.success("폼 미쳤다!!! 결과 떴다!!! 🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
        
        with st.spinner("다크모드 100% 강제 적용 중... 🔮✨"):
            time.sleep(1.2)
        st.balloons()
        
        # 벤토 그리드 카드 레이아웃
        st.markdown("<div class='bento-box'>", unsafe_allow_html=True)
        st.markdown(f"## 💖 너의 MBTI: <span class='neon-text'>{selected_mbti}</span> 💖", unsafe_allow_html=True)
        st.markdown(f"### 🎯 추천 직업: {mbti_jobs[selected_mbti]['job']}")
        st.info(f"👉 {mbti_jobs[selected_mbti]['desc']}")
        st.markdown("🔥 **라이트모드 찌꺼기 1도 없는 완벽한 다크 디자인 발급 완료** 💯")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # GIF 10개 이상 연달아 폭격
        st.markdown("### 💥 뿌슝빠슝 도파민 GIF 폭탄 세례 💥")
        imgs = mbti_jobs[selected_mbti]['imgs']
        
        for i in range(0, len(imgs), 3):
            cols = st.columns(3)
            for j in range(3):
                if i + j < len(imgs):
                    with cols[j]:
                        st.image(imgs[i + j], use_container_width=True)
        
        # 마무리 이모지
        st.markdown("<h4 style='text-align: center;'>💸💸💸👑👑👑🤪🤪🤪💀💀💀🔥🔥🔥🚀🚀🚀</h4>", unsafe_allow_html=True)
        st.write("이제 하얀색 찌꺼기 안 보이지? 완벽 그 잡채니까 빨리 링크 공유 ㄱㄱ 🚀🚀")

# 푸터
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748B;'>© 2026 MZ Career Education Platform. All rights reserved. 🔥</p>", unsafe_allow_html=True)
