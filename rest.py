import random
import streamlit as st

st.set_page_config(page_title="Streamlit Minesweeper", layout="centered")

# 게임 설정 (초급 기준: 9x9, 지뢰 10개)
ROWS, COLS, MINES = 9, 9, 10


def init_game():
    st.session_state.board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    st.session_state.revealed = [
        [False for _ in range(COLS)] for _ in range(ROWS)
    ]
    st.session_state.flagged = [
        [False for _ in range(COLS)] for _ in range(ROWS)
    ]
    st.session_state.game_over = False
    st.session_state.won = False

    # 지뢰 배치
    placed = 0
    while placed < MINES:
        r, c = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
        if st.session_state.board[r][c] != "M":
            st.session_state.board[r][c] = "M"
            placed += 1

    # 숫자 계산
    for r in range(ROWS):
        for c in range(COLS):
            if st.session_state.board[r][c] == "M":
                continue
            count = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and st.session_state.board[nr][nc] == "M"
                    ):
                        count += 1
            st.session_state.board[r][c] = count


if "board" not in st.session_state:
    init_game()

st.title("💣 Streamlit 지뢰찾기")

if st.button("게임 재시작"):
    init_game()
    st.rerun()

# 보드 렌더링 (Streamlit 특성상 버튼 클릭으로 좌/우클릭을 대체)
mode = st.radio("모드 선택", ["좌클릭 (확인)", "우클릭 (깃발)"], horizontal=True)

for r in range(ROWS):
    cols = st.columns(COLS)
    for c in range(COLS):
        with cols[c]:
            label = ""
            disabled = st.session_state.game_over or st.session_state.won

            if st.session_state.revealed[r][c]:
                val = st.session_state.board[r][c]
                label = str(val) if val > 0 else ""
                disabled = True
            elif st.session_state.flagged[r][c]:
                label = "🚩"

            if st.button(
                label if label else "⬜", key=f"cell_{r}_{c}", disabled=disabled
            ):
                if mode == "우클릭 (깃발)":
                    if not st.session_state.revealed[r][c]:
                        st.session_state.flagged[r][c] = not st.session_state.flagged[
                            r
                        ][c]
                else:  # 좌클릭
                    if not st.session_state.flagged[r][c]:
                        if st.session_state.board[r][c] == "M":
                            st.session_state.game_over = True
                            # 전체 지뢰 공개
                            for ro in range(ROWS):
                                for co in range(COLS):
                                    if st.session_state.board[ro][co] == "M":
                                        st.session_state.revealed[ro][co] = (
                                            True
                                        )
                        else:
                            st.session_state.revealed[r][c] = True
                st.rerun()

if st.session_state.game_over:
    st.error("게임 오버! 지뢰를 밟았습니다.")
elif st.session_state.won:
    st.success("승리했습니다!")
