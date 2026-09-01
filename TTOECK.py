import streamlit as st
import random
import time

# ============================================================
# 페이지 설정
# ============================================================
st.set_page_config(
    page_title="레전드 떡 키우기",
    page_icon="🍡",
    layout="centered",
)

# ============================================================
# 게임 밸런스 상수
# ============================================================
MAX_LEVEL = 20
STARTING_GOLD = 1_000_000
PROTECTION_UNIT_PRICE = 400_000

PROTECTION_PACKS = [
    {"count": 1, "price": 400_000, "discount": 0},
    {"count": 3, "price": 1_080_000, "discount": 10},
    {"count": 5, "price": 1_700_000, "discount": 15},
]


def get_enhance_cost(level: int) -> int:
    """level -> level+1 로 강화할 때 드는 비용"""
    return int(800 * (1.45 ** level))


def get_sell_price(level: int) -> int:
    """현재 level 떡을 팔았을 때 받는 금액"""
    return int(1500 * (1.75 ** level))


def get_probs(target_level: int):
    """target_level(=강화 시도 후 도달하려는 레벨) 기준 (성공%, 실패%, 파괴%)"""
    if target_level <= 4:
        return (95, 5, 0)
    elif target_level <= 8:
        return (85, 14, 1)
    elif target_level <= 11:
        return (70, 19, 11)
    elif target_level <= 14:
        return (55, 24, 21)
    elif target_level <= 17:
        return (40, 24, 36)
    else:
        return (25, 24, 51)


def get_tier(level: int):
    """레벨에 따른 떡 이름/이모지/색상"""
    if level == 0:
        return ("🍡", "평범한 떡", "#c9a876")
    elif level <= 4:
        return ("🍡", "단단한 떡", "#c98b4a")
    elif level <= 8:
        return ("🍘", "쫄깃한 떡", "#e0a52c")
    elif level <= 11:
        return ("🥮", "특제 떡", "#d97b29")
    elif level <= 14:
        return ("🍡", "명인의 떡", "#b968e0")
    elif level <= 17:
        return ("🍡", "전설의 떡", "#4facfe")
    elif level <= 19:
        return ("🍡", "신화의 떡", "#ff5fa2")
    else:
        return ("👑", "레전드 떡", "#ffd700")


# ============================================================
# 세션 상태 초기화
# ============================================================
def init_state():
    if "gold" not in st.session_state:
        st.session_state.gold = STARTING_GOLD
    if "level" not in st.session_state:
        st.session_state.level = 0
    if "protection" not in st.session_state:
        st.session_state.protection = 0
    if "use_protection" not in st.session_state:
        st.session_state.use_protection = False
    if "last_action" not in st.session_state:
        st.session_state.last_action = None
    if "nonce" not in st.session_state:
        st.session_state.nonce = 0
    if "history" not in st.session_state:
        st.session_state.history = []
    if "max_reached" not in st.session_state:
        st.session_state.max_reached = 0
    if "total_sold" not in st.session_state:
        st.session_state.total_sold = 0


init_state()

# ============================================================
# CSS
# ============================================================
st.markdown(
    """
    <style>
    @keyframes shake {
        0% { transform: translateX(0); }
        15% { transform: translateX(-14px) rotate(-3deg); }
        30% { transform: translateX(12px) rotate(3deg); }
        45% { transform: translateX(-10px) rotate(-2deg); }
        60% { transform: translateX(8px) rotate(2deg); }
        75% { transform: translateX(-5px); }
        100% { transform: translateX(0); }
    }
    @keyframes glowpulse {
        0% { transform: scale(1); filter: drop-shadow(0 0 0px gold); }
        30% { transform: scale(1.35); filter: drop-shadow(0 0 35px gold); }
        60% { transform: scale(1.1); filter: drop-shadow(0 0 20px #fff59d); }
        100% { transform: scale(1); filter: drop-shadow(0 0 6px gold); }
    }
    @keyframes shatter {
        0% { transform: scale(1) rotate(0deg); opacity: 1; filter: brightness(1); }
        20% { transform: scale(1.2) rotate(-8deg); filter: brightness(2) saturate(2); }
        50% { transform: scale(1.5) rotate(15deg); opacity: 0.6; filter: brightness(3) hue-rotate(300deg); }
        100% { transform: scale(0.2) rotate(45deg); opacity: 0; }
    }
    @keyframes fadein {
        from { opacity: 0; transform: translateY(-8px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .rice-cake-box {
        text-align: center;
        padding: 30px 10px 10px 10px;
        border-radius: 18px;
        background: radial-gradient(circle at 50% 30%, rgba(255,255,255,0.10), rgba(255,255,255,0.02));
        border: 1px solid rgba(255,255,255,0.08);
        margin-bottom: 10px;
    }
    .anim-success { animation: glowpulse 0.9s ease-in-out; display:inline-block; }
    .anim-fail { animation: shake 0.6s ease-in-out; display:inline-block; }
    .anim-destroy { animation: shatter 0.8s ease-in; display:inline-block; }
    .result-banner {
        text-align:center;
        font-size:20px;
        font-weight:700;
        padding:10px;
        border-radius:10px;
        margin: 6px 0 14px 0;
        animation: fadein 0.4s ease-out;
    }
    .banner-success { background: rgba(255,215,0,0.14); color:#ffd700; border:1px solid rgba(255,215,0,0.4);}
    .banner-fail { background: rgba(255,255,255,0.06); color:#dddddd; border:1px solid rgba(255,255,255,0.15);}
    .banner-destroy { background: rgba(255,0,80,0.14); color:#ff5f7e; border:1px solid rgba(255,0,80,0.4);}
    .banner-protect { background: rgba(80,180,255,0.14); color:#63c4ff; border:1px solid rgba(80,180,255,0.4);}
    .gold-display {
        position: fixed;
        bottom: 14px;
        left: 14px;
        background: rgba(20,20,25,0.85);
        color: #ffd700;
        padding: 8px 14px;
        border-radius: 10px;
        font-size: 15px;
        font-weight: 600;
        border: 1px solid rgba(255,215,0,0.35);
        z-index: 9999;
        box-shadow: 0 2px 10px rgba(0,0,0,0.4);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# 사이드바 - 게임 설명 & 기록
# ============================================================
with st.sidebar:
    st.markdown("### 📖 게임 방법")
    st.markdown(
        """
        1. **🔨 강화하기**를 눌러 떡의 레벨을 올려보세요.
        2. 레벨이 높아질수록 **성공 확률은 낮아지고**,
           실패 시 떡이 **파괴될 위험**도 커집니다.
        3. **🛡️ 방지권**을 사용하면 파괴를 막을 수 있어요.
        4. **💰 떡 팔기**로 지금까지 키운 떡을 현금화하세요.
        5. 최대 **Lv.20 레전드 떡**을 완성해보세요!
        """
    )
    st.divider()
    st.markdown("### 📊 내 기록")
    st.write(f"최고 달성 레벨: **Lv.{st.session_state.max_reached}**")
    st.write(f"누적 판매 금액: **{st.session_state.total_sold:,}원**")
    st.divider()
    if st.button("🔄 게임 초기화", use_container_width=True):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()

# ============================================================
# 메인 타이틀
# ============================================================
st.markdown(
    "<h1 style='text-align:center;'>🍡 레전드 떡 키우기 🍡</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align:center; color:gray; margin-top:-10px;'>그 유명한 강화 게임, 이번엔 '떡'으로!</p>",
    unsafe_allow_html=True,
)

level = st.session_state.level
gold = st.session_state.gold
emoji, name, color = get_tier(level)

# ============================================================
# 애니메이션 클래스 결정
# ============================================================
anim_class = ""
banner_html = ""
last = st.session_state.last_action
if last is not None:
    if last["type"] == "success":
        anim_class = "anim-success"
        banner_html = f"<div class='result-banner banner-success'>✨💥 강화 성공! Lv.{last['from']} → Lv.{last['to']} ✨</div>"
    elif last["type"] == "fail":
        anim_class = "anim-fail"
        banner_html = "<div class='result-banner banner-fail'>😅 강화 실패... 떡은 무사히 버텼습니다.</div>"
    elif last["type"] == "destroy":
        anim_class = "anim-destroy"
        banner_html = f"<div class='result-banner banner-destroy'>💥😱 떡이 파괴되었습니다! Lv.{last['from']} → Lv.0</div>"
    elif last["type"] == "protected":
        anim_class = "anim-fail"
        banner_html = "<div class='result-banner banner-protect'>🛡️ 방지권 발동! 파괴 위기를 넘겼습니다.</div>"
    elif last["type"] == "sell":
        banner_html = f"<div class='result-banner banner-success'>💰 떡을 {last['price']:,}원에 판매했습니다!</div>"

# ============================================================
# 떡 표시 박스
# ============================================================
font_size = 70 + level * 4
st.markdown(
    f"""
    <div class="rice-cake-box">
        <div class="{anim_class}" style="font-size:{font_size}px;">{emoji}</div>
        <div style="font-size:22px; font-weight:700; color:{color}; margin-top:6px;">{name}</div>
        <div style="font-size:16px; color:#aaaaaa;">Lv. {level} / {MAX_LEVEL}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

if banner_html:
    st.markdown(banner_html, unsafe_allow_html=True)

st.progress(level / MAX_LEVEL)

# ============================================================
# 강화 정보 패널
# ============================================================
if level >= MAX_LEVEL:
    st.success("🎉 축하합니다! 최고 레벨의 '레전드 떡'을 완성했습니다! 이제 떡을 팔아 대박을 노려보세요!")
    st.balloons()
else:
    target = level + 1
    succ, fail, destroy = get_probs(target)
    cost = get_enhance_cost(level)

    c1, c2, c3 = st.columns(3)
    c1.metric("성공 확률", f"{succ}%")
    c2.metric("실패 확률", f"{fail}%")
    c3.metric("파괴 확률", f"{destroy}%", delta=None)

    st.caption(f"🔨 강화 비용: **{cost:,}원**  ·  다음 목표: **Lv.{target}**")

    if destroy > 0:
        st.session_state.use_protection = st.checkbox(
            f"🛡️ 방지권 사용하기 (보유: {st.session_state.protection}개) — 파괴 방지",
            value=st.session_state.use_protection,
            disabled=(st.session_state.protection <= 0),
        )
    else:
        st.session_state.use_protection = False
        st.caption("이 구간은 파괴 위험이 없습니다. 안심하고 강화하세요!")

    col_enh, col_sell = st.columns(2)

    with col_enh:
        if st.button("🔨 강화하기", use_container_width=True, type="primary"):
            if gold < cost:
                st.toast("💸 골드가 부족합니다!", icon="⚠️")
            else:
                st.session_state.gold -= cost
                roll = random.random() * 100
                st.session_state.nonce += 1

                if roll < succ:
                    st.session_state.level += 1
                    st.session_state.max_reached = max(
                        st.session_state.max_reached, st.session_state.level
                    )
                    st.session_state.last_action = {
                        "type": "success", "from": level, "to": level + 1
                    }
                    st.session_state.history.insert(
                        0, f"✅ Lv.{level} → Lv.{level+1} 강화 성공 (-{cost:,}원)"
                    )
                elif roll < succ + fail:
                    st.session_state.last_action = {"type": "fail"}
                    st.session_state.history.insert(
                        0, f"➖ Lv.{level} 강화 실패 (-{cost:,}원)"
                    )
                else:
                    # 파괴 판정
                    if st.session_state.use_protection and st.session_state.protection > 0:
                        st.session_state.protection -= 1
                        st.session_state.last_action = {"type": "protected"}
                        st.session_state.history.insert(
                            0, f"🛡️ Lv.{level} 파괴 위기 → 방지권으로 방어! (-{cost:,}원)"
                        )
                    else:
                        st.session_state.last_action = {"type": "destroy", "from": level}
                        st.session_state.history.insert(
                            0, f"💥 Lv.{level} → Lv.0 떡 파괴! (-{cost:,}원)"
                        )
                        st.session_state.level = 0

                st.session_state.history = st.session_state.history[:8]
                st.rerun()

    with col_sell:
        sell_price = get_sell_price(level)
        if st.button(f"💰 떡 팔기 ({sell_price:,}원)", use_container_width=True):
            st.session_state.gold += sell_price
            st.session_state.total_sold += sell_price
            st.session_state.last_action = {"type": "sell", "price": sell_price}
            st.session_state.history.insert(
                0, f"💰 Lv.{level} 떡 판매 (+{sell_price:,}원)"
            )
            st.session_state.history = st.session_state.history[:8]
            st.session_state.level = 0
            st.rerun()

if level >= MAX_LEVEL:
    sell_price = get_sell_price(level)
    if st.button(f"💰 레전드 떡 팔기 ({sell_price:,}원)", use_container_width=True, type="primary"):
        st.session_state.gold += sell_price
        st.session_state.total_sold += sell_price
        st.session_state.last_action = {"type": "sell", "price": sell_price}
        st.session_state.history.insert(0, f"💰 Lv.{level} 떡 판매 (+{sell_price:,}원)")
        st.session_state.history = st.session_state.history[:8]
        st.session_state.level = 0
        st.rerun()

st.divider()

# ============================================================
# 방지권 상점
# ============================================================
st.markdown("### 🏪 방지권 상점")
st.caption(f"방지권 1개당 기본가 {PROTECTION_UNIT_PRICE:,}원 · 많이 살수록 할인!")

shop_cols = st.columns(3)
for idx, pack in enumerate(PROTECTION_PACKS):
    with shop_cols[idx]:
        st.markdown(f"**{pack['count']}개 구매**")
        if pack["discount"] > 0:
            st.caption(f"{pack['discount']}% 할인가")
        st.markdown(f"### {pack['price']:,}원")
        if st.button("구매하기", key=f"buy_{pack['count']}", use_container_width=True):
            if st.session_state.gold < pack["price"]:
                st.toast("💸 골드가 부족합니다!", icon="⚠️")
            else:
                st.session_state.gold -= pack["price"]
                st.session_state.protection += pack["count"]
                st.toast(f"🛡️ 방지권 {pack['count']}개 구매 완료!", icon="✅")
                st.rerun()

st.caption(f"현재 보유 방지권: **🛡️ {st.session_state.protection}개**")

# ============================================================
# 강화 기록
# ============================================================
if st.session_state.history:
    with st.expander("📜 최근 기록 보기"):
        for h in st.session_state.history:
            st.write(h)

# ============================================================
# 좌측 하단 골드 표시 (고정)
# ============================================================
st.markdown(
    f"<div class='gold-display'>💰 {st.session_state.gold:,}원</div>",
    unsafe_allow_html=True,
)
