import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="레전드 떡 키우기 🍡", page_icon="🍡", layout="centered")

# --- 게임 데이터 셋업 ---
MAX_LEVEL = 20
TICKET_PRICE = 15000

# 레벨별 떡 이름
TTEOK_NAMES = {
    0: "물 묻은 밀가루 반죽 💧", 1: "평범한 가래떡 🥢", 2: "조금 쫄깃한 가래떡 🥢", 3: "달콤한 꿀떡 🍯", 
    4: "쫀득쫀득 인절미 콩고물 듬뿍 🥜", 5: "바람떡 (앙금 2배) 🥟", 6: "빛나는 찹쌀떡 ✨", 7: "장인의 수제 찹쌀떡 🧑‍🍳", 
    8: "영롱한 백설기 ☁️", 9: "황금 가래떡 👑", 10: "백년 묵은 호박떡 🎃", 11: "천년 묵은 쑥떡 🌿", 
    12: "정령이 깃든 떡 🧚", 13: "마력을 품은 떡 🔮", 14: "드래곤의 숨결이 닿은 떡 🐉", 
    15: "전설의 무지개떡 🌈", 16: "영웅의 떡 ⚔️", 17: "천상의 백설기 👼", 18: "우주를 담은 떡 🌌", 
    19: "차원을 가르는 떡 🌀", 20: "신(神)의 떡 ⚡"
}

# 레벨별 강화 성공 확률 (%)
PROBS = {
    0: 100, 1: 95, 2: 90, 3: 85, 4: 80, 5: 70, 6: 60, 7: 50, 8: 45, 9: 40,
    10: 35, 11: 30, 12: 25, 13: 20, 14: 15, 15: 10, 16: 7, 17: 5, 18: 3, 19: 1
}

# 레벨별 판매 가격
PRICES = {
    0: 0, 1: 100, 2: 300, 3: 700, 4: 1500, 5: 3500, 6: 7000, 7: 15000, 8: 30000, 9: 50000,
    10: 90000, 11: 150000, 12: 300000, 13: 600000, 14: 1200000, 15: 2500000, 
    16: 5000000, 17: 10000000, 18: 25000000, 19: 60000000, 20: 150000000
}

# --- 세션 상태 초기화 ---
if 'level' not in st.session_state: st.session_state.level = 0
if 'money' not in st.session_state: st.session_state.money = 0
if 'tickets' not in st.session_state: st.session_state.tickets = 0
if 'log' not in st.session_state: st.session_state.log = "게임을 시작합니다! 떡을 쳐서 레벨을 올려보세요."

# --- 기능 함수 ---
def enhance():
    lvl = st.session_state.level
    if lvl >= MAX_LEVEL:
        st.session_state.log = "이미 최고 레벨(신의 떡)에 도달했습니다! 이제 팔아서 떼돈을 버세요."
        return

    success_chance = PROBS[lvl]
    roll = random.randint(1, 100)

    if roll <= success_chance:
        st.session_state.level += 1
        st.session_state.log = f"🎉 강화 성공! [{TTEOK_NAMES[lvl]}] ➡️ [{TTEOK_NAMES[lvl+1]}]"
    else:
        if st.session_state.tickets > 0:
            st.session_state.tickets -= 1
            st.session_state.log = f"🛡️ 강화 실패! 하지만 파괴 방지권이 떡을 지켜냈습니다. (남은 방지권: {st.session_state.tickets}개)"
        else:
            st.session_state.level = 0
            st.session_state.log = f"💥 펑! 떡이 산산조각 났습니다... 밀가루 반죽으로 돌아갑니다."

def sell():
    lvl = st.session_state.level
    if lvl == 0:
        st.session_state.log = "밀가루 반죽은 팔 수 없습니다. 강화를 먼저 하세요!"
        return
    
    earn = PRICES[lvl]
    st.session_state.money += earn
    st.session_state.level = 0
    st.session_state.log = f"💰 [{TTEOK_NAMES[lvl]}]을(를) 팔아 {earn:,}원을 벌었습니다!"

def buy_ticket():
    if st.session_state.money >= TICKET_PRICE:
        st.session_state.money -= TICKET_PRICE
        st.session_state.tickets += 1
        st.session_state.log = f"🎟️ 파괴 방지권을 구매했습니다! (보유: {st.session_state.tickets}개)"
    else:
        st.session_state.log = f"💸 돈이 부족합니다. (방지권 가격: {TICKET_PRICE:,}원)"

# --- UI 레이아웃 ---
st.title("🍡 레전드 떡 키우기 시뮬레이터")
st.markdown("---")

# 상단 상태창
col1, col2, col3 = st.columns(3)
col1.metric("현재 떡 레벨", f"Lv. {st.session_state.level}")
col2.metric("보유 자산", f"{st.session_state.money:,} 원")
col3.metric("파괴 방지권", f"{st.session_state.tickets} 개")

st.markdown("---")

# 현재 떡 정보
current_lvl = st.session_state.level
st.subheader(f"현재 상태: {TTEOK_NAMES[current_lvl]}")

if current_lvl < MAX_LEVEL:
    st.write(f"**다음 레벨 강화 성공 확률:** `{PROBS[current_lvl]}%`")
else:
    st.write("**다음 레벨 강화 성공 확률:** `MAX LEVEL`")
    
st.write(f"**현재 판매 가격:** `{PRICES[current_lvl]:,} 원`")

# 조작 버튼
st.markdown("<br>", unsafe_allow_html=True)
b1, b2, b3 = st.columns(3)

with b1:
    if st.button("🔨 강화하기", use_container_width=True, type="primary"):
        enhance()
with b2:
    if st.button("💰 떡 팔기", use_container_width=True):
        sell()
with b3:
    if st.button(f"🛡️ 방지권 구매 ({TICKET_PRICE:,}원)", use_container_width=True):
        buy_ticket()

# 로그 출력
st.markdown("---")
st.info(st.session_state.log)

# 시세표 토글
with st.expander("📊 레벨별 성공 확률 및 가격표 보기"):
    st.write("레벨이 오를수록 떡의 가치는 기하급수적으로 상승하지만, 성공 확률은 바닥을 칩니다.")
    for i in range(1, MAX_LEVEL + 1):
        chance = PROBS[i-1] if i-1 in PROBS else 0
        st.write(f"**Lv.{i} {TTEOK_NAMES[i]}** | 확률: {chance}% | 가격: {PRICES[i]:,}원")
