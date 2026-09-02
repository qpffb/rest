import streamlit as st
import random

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
PROTECTION_PRICE = 400_000


def get_enhance_cost(level: int) -> int:
    """level -> level+1 로 강화할 때 드는 비용"""
    return int(800 * (1.45 ** level))


def get_sell_price(level: int) -> int:
    """현재 level 떡을 팔았을 때 받는 금액"""
    return int(1500 * (1.75 ** level))


def get_success_rate(target_level: int) -> int:
    """target_level(=강화 시도 후 도달하려는 레벨) 기준 성공 확률(%)"""
    if target_level <= 4:
        return 95
    elif target_level <= 8:
        return 85
    elif target_level <= 11:
        return 70
    elif target_level <= 14:
        return 55
    elif target_level <= 17:
        return 40
    else:
        return 25


def particle_burst(emojis, count=24, spread=150):
    """레벨업/파괴 등 이벤트 시 사방으로 튀는 파티클 이펙트 HTML 생성"""
    spans = []
    for _ in range(count):
        e = random.choice(emojis)
        dist = random.uniform(spread * 0.4, spread)
        angle = random.uniform(0, 6.283)
        tx = round(dist * random.uniform(-1, 1))
        ty = round(dist * random.uniform(-1, 1))
        delay = round(random.uniform(0, 0.35), 2)
        size = random.randint(16, 34)
        spans.append(
            f"<span class='particle' style='--tx:{tx}px; --ty:{ty}px; "
            f"animation-delay:{delay}s; font-size:{size}px;'>{e}</span>"
        )
    return "".join(spans)


import streamlit.components.v1 as components

BOX_CSS = """
<style>
    * { box-sizing: border-box; }
    html, body {
        margin: 0; padding: 0; background: transparent;
        font-family: "Source Sans Pro", sans-serif;
        overflow: hidden;
    }
    @keyframes shake {
        0% { transform: translateX(0); }
        15% { transform: translateX(-16px) rotate(-3deg); }
        30% { transform: translateX(14px) rotate(3deg); }
        45% { transform: translateX(-12px) rotate(-2deg); }
        60% { transform: translateX(9px) rotate(2deg); }
        75% { transform: translateX(-5px); }
        100% { transform: translateX(0); }
    }
    @keyframes glowpulse {
        0% { transform: scale(1); filter: drop-shadow(0 0 0px gold); }
        30% { transform: scale(1.3); filter: drop-shadow(0 0 40px gold); }
        60% { transform: scale(1.08); filter: drop-shadow(0 0 22px #fff59d); }
        100% { transform: scale(1); filter: drop-shadow(0 0 6px gold); }
    }
    @keyframes glowblue {
        0% { transform: scale(1); filter: drop-shadow(0 0 0px #63c4ff); }
        30% { transform: scale(1.25); filter: drop-shadow(0 0 35px #63c4ff); }
        60% { transform: scale(1.05); filter: drop-shadow(0 0 18px #bfe8ff); }
        100% { transform: scale(1); filter: drop-shadow(0 0 6px #63c4ff); }
    }
    @keyframes shatter {
        0% { transform: scale(1) rotate(0deg); opacity: 1; filter: brightness(1); }
        20% { transform: scale(1.2) rotate(-8deg); filter: brightness(2) saturate(2); }
        50% { transform: scale(1.5) rotate(15deg); opacity: 0.6; filter: brightness(3) hue-rotate(300deg); }
        100% { transform: scale(0.2) rotate(45deg); opacity: 0; }
    }
    @keyframes burst {
        0% { transform: translate(-50%,-50%) scale(0.3) rotate(0deg); opacity: 1; }
        55% { opacity: 1; }
        100% { transform: translate(calc(-50% + var(--tx)), calc(-50% + var(--ty))) scale(1.4) rotate(380deg); opacity: 0; }
    }
    @keyframes flashgold {
        0% { background: radial-gradient(circle, rgba(255,215,0,0.65), rgba(255,215,0,0.08)); }
        100% { background: radial-gradient(circle at 50% 30%, rgba(255,255,255,0.10), rgba(255,255,255,0.02)); }
    }
    @keyframes flashred {
        0% { background: radial-gradient(circle, rgba(255,0,60,0.7), rgba(255,0,60,0.08)); }
        100% { background: radial-gradient(circle at 50% 30%, rgba(255,255,255,0.10), rgba(255,255,255,0.02)); }
    }
    @keyframes flashblue {
        0% { background: radial-gradient(circle, rgba(80,180,255,0.65), rgba(80,180,255,0.08)); }
        100% { background: radial-gradient(circle at 50% 30%, rgba(255,255,255,0.10), rgba(255,255,255,0.02)); }
    }
    @keyframes bigshake {
        0% { transform: translate(0,0) rotate(0deg); }
        10% { transform: translate(-18px,4px) rotate(-4deg); }
        20% { transform: translate(16px,-6px) rotate(4deg); }
        30% { transform: translate(-14px,6px) rotate(-3deg); }
        40% { transform: translate(12px,-4px) rotate(3deg); }
        50% { transform: translate(-10px,4px) rotate(-2deg); }
        60% { transform: translate(9px,-3px) rotate(2deg); }
        70% { transform: translate(-6px,2px) rotate(-1deg); }
        80% { transform: translate(5px,-2px) rotate(1deg); }
        90% { transform: translate(-2px,1px) rotate(0deg); }
        100% { transform: translate(0,0) rotate(0deg); }
    }
    .box-shake-big { animation: bigshake 0.7s ease-in-out; }
    .box-flash-gold { animation: flashgold 1.3s ease-out; }
    .box-flash-red { animation: flashred 1.3s ease-out; }
    .box-flash-blue { animation: flashblue 1.3s ease-out; }
    .particle {
        position: absolute;
        left: 50%; top: 45%;
        transform: translate(-50%, -50%);
        animation: burst 1.3s ease-out forwards;
        pointer-events: none;
        z-index: 5;
    }
    .rice-cake-box {
        position: relative;
        overflow: visible;
        text-align: center;
        padding: 14px 6px;
        border-radius: 20px;
        background: radial-gradient(circle at 50% 30%, rgba(255,255,255,0.10), rgba(255,255,255,0.02));
        border: 1px solid rgba(255,255,255,0.08);
        height: 340px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .anim-success { animation: glowpulse 0.9s ease-in-out; display:inline-block; }
    .anim-fail { animation: shake 0.6s ease-in-out; display:inline-block; }
    .anim-destroy { animation: shatter 0.9s ease-in; display:inline-block; }
    .anim-protect { animation: glowblue 0.9s ease-in-out; display:inline-block; }
</style>
"""


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
    if "last_action" not in st.session_state:
        st.session_state.last_action = None
    if "history" not in st.session_state:
        st.session_state.history = []
    if "max_reached" not in st.session_state:
        st.session_state.max_reached = 0
    if "total_sold" not in st.session_state:
        st.session_state.total_sold = 0
    if "pending_fail" not in st.session_state:
        st.session_state.pending_fail = None


init_state()

# ============================================================
# CSS
# ============================================================
st.markdown(
    """
    <style>
    header[data-testid="stHeader"] {
        background: rgba(14,17,23,0.95);
    }
    .block-container {
        padding-top: 3.5rem !important;
        padding-bottom: 1rem !important;
        max-width: 760px;
    }
    div[data-testid="stVerticalBlock"] {
        gap: 0.45rem;
    }
    @keyframes shake {
        0% { transform: translateX(0); }
        15% { transform: translateX(-16px) rotate(-3deg); }
        30% { transform: translateX(14px) rotate(3deg); }
        45% { transform: translateX(-12px) rotate(-2deg); }
        60% { transform: translateX(9px) rotate(2deg); }
        75% { transform: translateX(-5px); }
        100% { transform: translateX(0); }
    }
    @keyframes glowpulse {
        0% { transform: scale(1); filter: drop-shadow(0 0 0px gold); }
        30% { transform: scale(1.3); filter: drop-shadow(0 0 40px gold); }
        60% { transform: scale(1.08); filter: drop-shadow(0 0 22px #fff59d); }
        100% { transform: scale(1); filter: drop-shadow(0 0 6px gold); }
    }
    @keyframes glowblue {
        0% { transform: scale(1); filter: drop-shadow(0 0 0px #63c4ff); }
        30% { transform: scale(1.25); filter: drop-shadow(0 0 35px #63c4ff); }
        60% { transform: scale(1.05); filter: drop-shadow(0 0 18px #bfe8ff); }
        100% { transform: scale(1); filter: drop-shadow(0 0 6px #63c4ff); }
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
    @keyframes burst {
        0% { transform: translate(-50%,-50%) scale(0.3) rotate(0deg); opacity: 1; }
        55% { opacity: 1; }
        100% { transform: translate(calc(-50% + var(--tx)), calc(-50% + var(--ty))) scale(1.4) rotate(380deg); opacity: 0; }
    }
    @keyframes flashgold {
        0% { background: radial-gradient(circle, rgba(255,215,0,0.65), rgba(255,215,0,0.08)); }
        100% { background: radial-gradient(circle at 50% 30%, rgba(255,255,255,0.10), rgba(255,255,255,0.02)); }
    }
    @keyframes flashred {
        0% { background: radial-gradient(circle, rgba(255,0,60,0.7), rgba(255,0,60,0.08)); }
        100% { background: radial-gradient(circle at 50% 30%, rgba(255,255,255,0.10), rgba(255,255,255,0.02)); }
    }
    @keyframes flashblue {
        0% { background: radial-gradient(circle, rgba(80,180,255,0.65), rgba(80,180,255,0.08)); }
        100% { background: radial-gradient(circle at 50% 30%, rgba(255,255,255,0.10), rgba(255,255,255,0.02)); }
    }
    @keyframes bigshake {
        0% { transform: translate(0,0) rotate(0deg); }
        10% { transform: translate(-18px,4px) rotate(-4deg); }
        20% { transform: translate(16px,-6px) rotate(4deg); }
        30% { transform: translate(-14px,6px) rotate(-3deg); }
        40% { transform: translate(12px,-4px) rotate(3deg); }
        50% { transform: translate(-10px,4px) rotate(-2deg); }
        60% { transform: translate(9px,-3px) rotate(2deg); }
        70% { transform: translate(-6px,2px) rotate(-1deg); }
        80% { transform: translate(5px,-2px) rotate(1deg); }
        90% { transform: translate(-2px,1px) rotate(0deg); }
        100% { transform: translate(0,0) rotate(0deg); }
    }
    @keyframes rainbowtext {
        0% { color: #ff5f7e; }
        25% { color: #ffd700; }
        50% { color: #7cff6b; }
        75% { color: #63c4ff; }
        100% { color: #ff5f7e; }
    }
    .box-shake-big { animation: bigshake 0.7s ease-in-out; }
    .box-flash-gold { animation: flashgold 1.3s ease-out; }
    .box-flash-red { animation: flashred 1.3s ease-out; }
    .box-flash-blue { animation: flashblue 1.3s ease-out; }
    .particle {
        position: absolute;
        left: 50%; top: 45%;
        transform: translate(-50%, -50%);
        animation: burst 1.3s ease-out forwards;
        pointer-events: none;
        z-index: 5;
    }
    .banner-rainbow { animation: fadein 0.4s ease-out, rainbowtext 1.2s linear infinite !important; }
    .rice-cake-box {
        position: relative;
        overflow: visible;
        text-align: center;
        padding: 14px 6px;
        border-radius: 20px;
        background: radial-gradient(circle at 50% 30%, rgba(255,255,255,0.10), rgba(255,255,255,0.02));
        border: 1px solid rgba(255,255,255,0.08);
        min-height: 340px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .anim-success { animation: glowpulse 0.9s ease-in-out; display:inline-block; }
    .anim-fail { animation: shake 0.6s ease-in-out; display:inline-block; }
    .anim-destroy { animation: shatter 0.9s ease-in; display:inline-block; }
    .anim-protect { animation: glowblue 0.9s ease-in-out; display:inline-block; }
    .result-banner {
        text-align:center;
        font-size:16px;
        font-weight:700;
        padding:6px;
        border-radius:8px;
        margin: 2px 0 6px 0;
        animation: fadein 0.4s ease-out;
    }
    .banner-success { background: rgba(255,215,0,0.14); color:#ffd700; border:1px solid rgba(255,215,0,0.4);}
    .banner-fail { background: rgba(255,255,255,0.06); color:#dddddd; border:1px solid rgba(255,255,255,0.15);}
    .banner-destroy { background: rgba(255,0,80,0.14); color:#ff5f7e; border:1px solid rgba(255,0,80,0.4);}
    .banner-protect { background: rgba(80,180,255,0.14); color:#63c4ff; border:1px solid rgba(80,180,255,0.4);}
    .gold-display {
        background: rgba(20,20,25,0.9);
        color: #ffd700;
        padding: 10px 14px;
        border-radius: 10px;
        font-size: 16px;
        font-weight: 700;
        border: 1px solid rgba(255,215,0,0.35);
        box-shadow: 0 2px 10px rgba(0,0,0,0.4);
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# 사이드바 - 소유 골드 표시 & 게임 설명 & 기록
# ============================================================
with st.sidebar:
    st.markdown(
        f"<div class='gold-display'>💰 보유 골드<br>{st.session_state.gold:,}원</div>",
        unsafe_allow_html=True,
    )
    st.markdown("### 📖 게임 방법")
    st.markdown(
        """
        1. **🔨 강화하기**를 눌러 떡의 레벨을 올려보세요.
        2. 레벨이 높아질수록 **성공 확률이 낮아집니다.**
        3. 강화에 **실패하면 떡이 Lv.0으로 초기화**돼요.
           그 순간 **방지권(40만원)**으로 지킬 수 있어요!
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
# (실패 처리는 강화 버튼이 있던 자리에 바로 인라인으로 표시됩니다)
# ============================================================

# ============================================================
# 메인 타이틀
# ============================================================
st.markdown(
    "<h3 style='text-align:center; margin:0 0 4px 0;'>🍡 레전드 떡 키우기 🍡"
    "<span style='font-size:13px; color:gray; font-weight:400;'> · 그 유명한 강화 게임을 떡으로!</span></h3>",
    unsafe_allow_html=True,
)

level = st.session_state.level
gold = st.session_state.gold
emoji, name, color = get_tier(level)

# ============================================================
# 애니메이션 & 배너 & 파티클 결정 (일부러 과하게!)
# ============================================================
# ============================================================
# 애니메이션 & 배너 & 파티클 결정
# (파티클/화면 플래시 이펙트는 Lv.10부터 등장하며, 레벨이 높을수록 커집니다)
# ============================================================
def get_effect_scale(effect_level: int):
    """10레벨 미만이면 None(이펙트 없음), 이상이면 (count, spread)를 레벨에 비례해 반환"""
    if effect_level < 10:
        return None
    t = min(max((effect_level - 10) / 10, 0), 1)  # Lv10=0.0 ~ Lv20=1.0
    count = int(8 + t * 30)      # 8개 ~ 38개
    spread = int(80 + t * 150)   # 80px ~ 230px
    return count, spread


anim_class = ""
box_extra_class = ""
banner_html = ""
particles_html = ""
last = st.session_state.last_action
if last is not None:
    if last["type"] == "success":
        anim_class = "anim-success"
        eff = get_effect_scale(last.get("level", 0))
        if eff:
            count, spread = eff
            box_extra_class = "box-flash-gold"
            particles_html = particle_burst(
                ["✨", "⭐", "🌟", "💥", "🎉", "🎆", "💫", "🔥"], count=count, spread=spread
            )
        banner_html = (
            "<div class='result-banner banner-success banner-rainbow'>"
            "🎉✨💥 강화 성공! 💥✨🎉<br>"
            f"<span style='font-size:14px;'>Lv.{last['from']} → Lv.{last['to']} 달성!</span></div>"
        )
    elif last["type"] == "destroy":
        anim_class = "anim-destroy"
        eff = get_effect_scale(last.get("level", 0))
        if eff:
            count, spread = eff
            box_extra_class = "box-flash-red box-shake-big"
            particles_html = particle_burst(
                ["💥", "🔥", "💢", "😱", "🍡", "💔", "⚡"], count=count, spread=spread
            )
        banner_html = (
            "<div class='result-banner banner-destroy'>"
            "💥😱 떡이 파괴되었습니다! 😱💥<br>"
            f"<span style='font-size:14px;'>Lv.{last['from']} → Lv.0</span></div>"
        )
    elif last["type"] == "protected":
        anim_class = "anim-protect"
        eff = get_effect_scale(last.get("level", 0))
        if eff:
            count, spread = eff
            box_extra_class = "box-flash-blue"
            particles_html = particle_burst(
                ["🛡️", "✨", "💠", "🔷"], count=min(count, 22), spread=spread
            )
        banner_html = "<div class='result-banner banner-protect'>🛡️✨ 방지권 발동! 떡을 무사히 지켰습니다! ✨🛡️</div>"
    elif last["type"] == "sell":
        banner_html = f"<div class='result-banner banner-success'>💰 떡을 {last['price']:,}원에 판매했습니다!</div>"

if banner_html:
    st.markdown(banner_html, unsafe_allow_html=True)

# ============================================================
# 메인 레이아웃: 왼쪽 = 조작 패널 / 오른쪽 = 초대형 떡
# ============================================================
col_left, col_right = st.columns([1, 1.3])

with col_right:
    font_size = min(90 + level * 6, 220)
    box_html = (
        f'<div class="rice-cake-box {box_extra_class}">'
        f'{particles_html}'
        f'<div class="{anim_class}" style="font-size:{font_size}px; line-height:1;">{emoji}</div>'
        f'<div style="font-size:22px; font-weight:700; color:{color}; margin-top:8px;">{name}</div>'
        f'<div style="font-size:15px; color:#aaaaaa;">Lv. {level} / {MAX_LEVEL}</div>'
        f'</div>'
    )
    st.markdown(box_html, unsafe_allow_html=True)

with col_left:
    st.markdown(
        f"<div class='gold-display' style='font-size:14px; padding:6px 10px; margin-bottom:8px;'>"
        f"💰 {st.session_state.gold:,}원</div>",
        unsafe_allow_html=True,
    )
    st.progress(level / MAX_LEVEL)

    if level >= MAX_LEVEL:
        st.success("🎉 레전드 떡 완성!\n이제 팔아서 대박 나세요!")
        sell_price = get_sell_price(level)
        if st.button(f"💰 떡 팔기 ({sell_price:,}원)", use_container_width=True, type="primary"):
            st.session_state.gold += sell_price
            st.session_state.total_sold += sell_price
            st.session_state.last_action = {"type": "sell", "price": sell_price}
            st.session_state.history.insert(0, f"💰 Lv.{level} 떡 판매 (+{sell_price:,}원)")
            st.session_state.history = st.session_state.history[:8]
            st.session_state.level = 0
            st.rerun()
    elif st.session_state.pending_fail is not None:
        lvl = st.session_state.pending_fail["level"]
        st.markdown(
            f"<div class='result-banner banner-destroy' style='margin-top:0;'>"
            f"💥 강화 실패 ㅠㅠ<br><span style='font-weight:400; font-size:14px;'>"
            f"Lv.{lvl} 떡이 와장창 흔들려요! 방지권을 쓰면 그대로 유지, "
            f"안 쓰면 Lv.0으로 초기화됩니다.</span></div>",
            unsafe_allow_html=True,
        )
        can_afford = gold >= PROTECTION_PRICE
        if st.button("😭 포기하고 파괴 인정", use_container_width=True, type="primary"):
            st.session_state.level = 0
            st.session_state.last_action = {"type": "destroy", "from": lvl, "level": lvl}
            st.session_state.history.insert(0, f"💥 Lv.{lvl} → Lv.0 떡 파괴!")
            st.session_state.history = st.session_state.history[:8]
            st.session_state.pending_fail = None
            st.rerun()
        if st.button(
            f"🛡️ 방지권 사용 (-{PROTECTION_PRICE:,}원)",
            use_container_width=True,
            disabled=not can_afford,
        ):
            st.session_state.gold -= PROTECTION_PRICE
            st.session_state.last_action = {"type": "protected", "level": lvl}
            st.session_state.history.insert(
                0, f"🛡️ Lv.{lvl} 파괴 위기 → 방지권 사용 (-{PROTECTION_PRICE:,}원)"
            )
            st.session_state.history = st.session_state.history[:8]
            st.session_state.pending_fail = None
            st.rerun()
        if not can_afford:
            st.caption("😢 골드가 부족해서 방지권을 살 수 없어요.")
    else:
        target = level + 1
        succ = get_success_rate(target)
        fail = 100 - succ
        cost = get_enhance_cost(level)

        st.markdown(
            f"<div style='font-size:15px;'>✅ 성공 <b>{succ}%</b> &nbsp;·&nbsp; 💥 실패 <b>{fail}%</b></div>",
            unsafe_allow_html=True,
        )
        st.caption(f"🔨 강화 비용: **{cost:,}원**  ·  다음 목표: **Lv.{target}**")

        if st.button("🔨 강화하기", use_container_width=True, type="primary"):
            if gold < cost:
                st.toast("💸 골드가 부족합니다!", icon="⚠️")
            else:
                st.session_state.gold -= cost
                roll = random.random() * 100
                if roll < succ:
                    st.session_state.level += 1
                    st.session_state.max_reached = max(
                        st.session_state.max_reached, st.session_state.level
                    )
                    st.session_state.last_action = {
                        "type": "success", "from": level, "to": level + 1, "level": level + 1
                    }
                    st.session_state.history.insert(
                        0, f"✅ Lv.{level} → Lv.{level+1} 강화 성공 (-{cost:,}원)"
                    )
                    st.session_state.history = st.session_state.history[:8]
                else:
                    st.session_state.pending_fail = {"level": level}
                st.rerun()

        sell_price = get_sell_price(level)
        if level > 0:
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
        else:
            st.caption("💡 강화하지 않은 떡은 팔 수 없어요. 레벨을 올려보세요!")

    if st.session_state.history:
        with st.expander("📜 최근 기록"):
            for h in st.session_state.history:
                st.write(h)
