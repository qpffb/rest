import streamlit as st
import time

# --- 페이지 설정 ---
st.set_page_config(
    page_title="MZ MBTI 진로 폼 미쳤다 🔥", 
    page_icon="🚀", 
    layout="wide"
)

# --- 🚨 화이트 모드 및 100개 미니 GIF 최적화 CSS 🚨 ---
st.markdown("""
<style>
    /* 전체 배경 흰색 및 기본 글자색 어두운 회색으로 변경 */
    .stApp {
        background-color: #FFFFFF !important;
        color: #1E293B !important;
    }
    /* 벤토 박스 스타일 (연한 회색 배경과 깔끔한 테두리) */
    .bento-box {
        background: linear-gradient(135deg, rgba(241, 245, 249, 0.8), rgba(226, 232, 240, 0.95));
        border: 1px solid #CBD5E1;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    /* 네온 텍스트 (화이트 모드에 맞게 선명한 초록/포인트 컬러) */
    .neon-text {
        color: #16A34A;
        font-weight: 800;
        text-shadow: 0 0 10px rgba(22, 163, 74, 0.2);
    }
    /* 서브 텍스트 가독성 개선 */
    h3, h4 {
        color: #334155 !important;
    }
    /* GIF 이미지 컴팩트하게 조절 */
    img {
        border-radius: 12px;
        transition: transform 0.2s ease;
    }
    img:hover {
        transform: scale(1.03);
    }
</style>
""", unsafe_allow_html=True)

# --- 세션 스테이트로 MBTI 선택 값 유지 ---
if 'e_i' not in st.session_state: st.session_state.e_i = 'E'
if 'n_s' not in st.session_state: st.session_state.n_s = 'N'
if 't_f' not in st.session_state: st.session_state.t_f = 'T'
if 'p_j' not in st.session_state: st.session_state.p_j = 'P'

# --- 헤더 섹션 ---
st.markdown("<h1 style='text-align: center; color: #0F172A;'>🔥✨💯 폼 미쳤다! 대형 버튼 조합형 찰떡 직업 🚀💸👑</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #475569;'>😎 100개의 미니 도파민 GIF 폭격 & 대형 클릭 버튼 버전 💥🤡</h3>", unsafe_allow_html=True)
st.write("---")

# MBTI별 직업 데이터
mbti_jobs = {
    "INTJ": {"job": "AI 설계자, 스타트업 CEO 🧠💼", "desc": "팩폭 장인인 너! 감정소모 없이 능력으로 압살하는 직업이 딱임 💀💯"},
    "INTP": {"job": "데이터 과학자, 화이트해커 💻🕵️‍♂️", "desc": "방구석 아인슈타인 그 잡채 🤓✨ 논리로 우주 정복 가능!"},
    "ENTJ": {"job": "대기업 임원, 경영 컨설턴트 🚀👑", "desc": "추진력 불도저급 ㄷㄷ 네가 가는 길이 곧 법이다 🔥🔥"},
    "ENTP": {"job": "크리에이티브 디렉터, 발명가 🤪💡", "desc": "아이디어 뱅크 미쳤고~ 말빨로 세상 다 씹어먹을 상 🤡✨"},
    "INFJ": {"job": "심리 상담가, 소설가 🥺📚", "desc": "겉바속촉 힐러! 통찰력으로 사람 맘 꿰뚫어보는 능력이 거의 무당급 🔮✨"},
    "INFP": {"job": "웹소설 작가, 일러스트레이터 🎨🌸", "desc": "망상력 만렙! 너의 머릿속 판타지를 돈으로 바꿔봐 💸💸🥺"},
    "ENFJ": {"job": "라이프 코치, HR 매니저 🥰🤝", "desc": "인간 리트리버? 아니 인간 햇살! 주변 사람들 다 감기는 마성의 매력 ☀️💖"},
    "ENFP": {"job": "유튜버, 틱톡커, 파티 플래너 🎉📱", "desc": "인싸 그 잡채! 텐션 감당 불가 ㅋㅋㅋ 너는 무조건 카메라 앞에 서야 함 🤪📸"},
    "ISTJ": {"job": "공인회계사, 공무원 🧐📊", "desc": "갓생러의 표본! 칼각 맞추는 거 좋아하는 너에겐 안정감이 최고 👍💯"},
    "ISFJ": {"job": "간호사, 유치원 교사 👼💉", "desc": "천사 강림 ㅠㅠ 기억력도 좋아서 꼼꼼하게 챙겨주는 일에 재능캐임 💖✨"},
    "ESTJ": {"job": "프로젝트 매니저, 경찰관 👮‍♂️📈", "desc": "리더십 폼 미쳤다! 팩트 폭격기로 일 처리 속도 5G급 🔥🚀"},
    "ESFJ": {"job": "호텔리어, PR 전문가 🏨🗣️", "desc": "친화력 무엇? 어딜 가도 인싸 그룹 센터 차지할 마당발 🥳👑"},
    "ISTP": {"job": "파일럿, 소프트웨어 엔지니어 ✈️🔧", "desc": "만능 재주꾼! 무심한 척하면서 뚝딱뚝딱 다 고쳐내는 츤데레 장인 😎✨"},
    "ISFP": {"job": "패션 디자이너, 뮤지션 🎸👗", "desc": "예술혼 불타오르네 🔥 누워있는 거 젤 좋아하지만 필 받으면 장난 아님 🥺✨"},
    "ESTP": {"job": "사업가, 스포츠 에이전트 💸🏃‍♂️", "desc": "인생은 한 방! 스릴 즐기는 폼이 예사롭지 않음. 실행력 킹정 💯🔥"},
    "ESFP": {"job": "아이돌, 뮤지컬 배우 🎤🌟", "desc": "무대 체질 ㄷㄷ 스포트라이트 안 받으면 병나는 슈퍼스타 그 잡채 🤩✨"}
}

# --- 100개 구성용 도파민 폭탄 소스 풀 (자동 반복 확장) ---
base_gifs = [
    "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif",
    "https://media.giphy.com/media/L1R1tvI9svkIWwpVYr/giphy.gif",
    "https://media.giphy.com/media/xT5LMPj8P2CDUDOqYg/giphy.gif",
    "https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif",
    "https://media.giphy.com/media/26ufdipQqUpi3A9Rc/giphy.gif",
    "https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif",
    "https://media.giphy.com/media/oF5oUYTOX97eqEqFua/giphy.gif",
    "https://media.giphy.com/media/3o85xwxr06YNoFdSbm/giphy.gif",
    "https://media.giphy.com/media/26AHvVwUu9P929Rfy/giphy.gif",
    "https://media.giphy.com/media/3o7qDEq2bMbcbPRQ2c/giphy.gif",
    "https://media.giphy.com/media/Y4cCRuGpvwjzO/giphy.gif",
    "https://media.giphy.com/media/Lqji0EE1zMDG8/giphy.gif",
    "https://media.giphy.com/media/11sBLVxIRvnMQ8/giphy.gif",
    "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
    "https://media.giphy.com/media/3o7TKDk86h4FpBqW6A/giphy.gif",
    "https://media.giphy.com/media/XbJX8mE1wD0t2/giphy.gif",
    "https://media.giphy.com/media/3o6Zt4HU9uwXmXSAuI/giphy.gif",
    "https://media.giphy.com/media/13hxeOYjoTWtK8/giphy.gif",
    "https://media.giphy.com/media/12HxX1b4E3hVle/giphy.gif",
    "https://media.giphy.com/media/5wWf7GMbT1ZUGTDdTqM/giphy.gif"
]
# 정확히 100개로 뻥튀기 생성
hundred_gifs = (base_gifs * 5)[:100]

# --- 대형 줄바꿈 버튼 인터페이스 구현 ---
st.markdown("<div class='bento-box'>", unsafe_allow_html=True)
st.markdown("### 👇 큼직한 버튼으로 줄바꿈 딱딱 맞춰서 골라봐! 🧠👇")

# 1행: E / I 선택
st.markdown("#### 1단계: 에너지 방향 (E vs I)")
col_e, col_i = st.columns(2)
with col_e:
    if st.button("🚀 E (외향형)", use_container_width=True, type="primary" if st.session_state.e_i == 'E' else "secondary"):
        st.session_state.e_i = 'E'
with col_i:
    if st.button("🛋️ I (내향형)", use_container_width=True, type="primary" if st.session_state.e_i == 'I' else "secondary"):
        st.session_state.e_i = 'I'

st.write("")

# 2행: N / S 선택
st.markdown("#### 2단계: 인식 기능 (N vs S)")
col_n, col_s = st.columns(2)
with col_n:
    if st.button("🔮 N (직관형)", use_container_width=True, type="primary" if st.session_state.n_s == 'N' else "secondary"):
        st.session_state.n_s = 'N'
with col_s:
    if st.button("📏 S (감각형)", use_container_width=True, type="primary" if st.session_state.n_s == 'S' else "secondary"):
        st.session_state.n_s = 'S'

st.write("")

# 3행: T / F 선택
st.markdown("#### 3단계: 판단 기능 (T vs F)")
col_t, col_f = st.columns(2)
with col_t:
    if st.button("🧠 T (사고형)", use_container_width=True, type="primary" if st.session_state.t_f == 'T' else "secondary"):
        st.session_state.t_f = 'T'
with col_f:
    if st.button("💖 F (감정형)", use_container_width=True, type="primary" if st.session_state.t_f == 'F' else "secondary"):
        st.session_state.t_f = 'F'

st.write("")

# 4행: P / J 선택
st.markdown("#### 4단계: 생활 양식 (P vs J)")
col_p, col_j = st.columns(2)
with col_p:
    if st.button("🎨 P (인식형)", use_container_width=True, type="primary" if st.session_state.p_j == 'P' else "secondary"):
        st.session_state.p_j = 'P'
with col_j:
    if st.button("📋 J (판단형)", use_container_width=True, type="primary" if st.session_state.p_j == 'J' else "secondary"):
        st.session_state.p_j = 'J'

st.markdown("</div>", unsafe_allow_html=True)

# 실시간 조합된 MBTI
selected_mbti = st.session_state.e_i + st.session_state.n_s + st.session_state.t_f + st.session_state.p_j

# --- 결과 확인 버튼 ---
if st.button(f"🔥 [{selected_mbti}] 내 직업 확인하기! 가보자고! 🚀", use_container_width=True):
    st.success(f"선택완료! 조합된 MBTI: {selected_mbti} 🎉🎉🎉")
    
    with st.spinner("100개 미니 도파민 GIF 패키지 장전 중... 🔮✨"):
        time.sleep(1.0)
    st.balloons()
    
    # 결과 벤토 박스
    st.markdown("<div class='bento-box'>", unsafe_allow_html=True)
    st.markdown(f"## 💖 완성된 너의 MBTI: <span class='neon-text'>{selected_mbti}</span> 💖", unsafe_allow_html=True)
    st.markdown(f"### 🎯 추천 직업: {mbti_jobs[selected_mbti]['job']}")
    st.info(f"👉 {mbti_jobs[selected_mbti]['desc']}")
    st.markdown("🔥 **대형 줄바꿈 버튼 & 미니 GIF 100개 도배 버전 발급 완료** 💯")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # 100개 미니 GIF 폭격 (5열 컴팩트 그리드 구조)
    st.markdown(f"### 💥 {selected_mbti} 맞춤형 미니 GIF 100개 폭탄 세례 💥")
    
    for i in range(0, len(hundred_gifs), 5):
        cols = st.columns(5)
        for j in range(5):
            if i + j < len(hundred_gifs):
                with cols[j]:
                    st.image(hundred_gifs[i + j], use_container_width=True)
    
    # 마무리
    st.markdown("<h4 style='text-align: center;'>💸💸💸👑👑👑🤪🤪🤪💀💀💀🔥🔥🔥🚀🚀🚀</h4>", unsafe_allow_html=True)
    st.write("버튼 큼직하고 줄바꿈 깔끔하지? GIF 100개도 작고 앙증맞게 꽉 채웠다 완벽 그 잡채니까 빨리 공유 ㄱㄱ 🚀🚀")

# 푸터
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748B;'>© 2026 MZ Career Education Platform. All rights reserved. 🔥</p>", unsafe_allow_html=True)
