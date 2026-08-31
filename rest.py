import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Streamlit Snake", layout="centered")

st.title("🐍 스트림릿 스네이크 게임")
st.write("키보드 방향키(⬆️ ⬇️ ⬅️ ➡️)로 조작하세요.")

# 3가지 종목 선택
mode = st.radio(
    "종목(모드)을 선택해:",
    ["클래식 (벽 닿으면 즉사)", "포탈 (벽 뚫고 반대편으로)", "광기 (속도 2배)"],
    horizontal=True
)

# 모드별 세팅값을 JS로 넘겨주기 위한 변수
game_mode = "CLASSIC"
if "포탈" in mode:
    game_mode = "PORTAL"
elif "광기" in mode:
    game_mode = "MADNESS"

# HTML/JS로 부드러운 게임 엔진 구현 (스트림릿 렌더링 한계 극복)
snake_html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    body {{
        display: flex;
        flex-direction: column;
        align-items: center;
        background-color: #0e1117;
        color: white;
        font-family: sans-serif;
        margin: 0;
        padding: 20px;
    }}
    canvas {{
        background-color: #222;
        border: 3px solid #4CAF50;
        box-shadow: 0 0 15px rgba(76, 175, 80, 0.5);
    }}
    #scoreBoard {{
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
        color: #4CAF50;
    }}
</style>
</head>
<body>
    <div id="scoreBoard">점수: <span id="score">0</span></div>
    <canvas id="gameCanvas" width="400" height="400"></canvas>

<script>
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');
    const gridSize = 20;
    const mode = "{game_mode}";
    
    let snake = [{{x: 200, y: 200}}];
    let apple = {{x: 100, y: 100}};
    let dx = gridSize;
    let dy = 0;
    let score = 0;
    
    // 광기 모드면 속도 2배 (인터벌 시간이 짧아짐)
    let speed = mode === "MADNESS" ? 50 : 100; 
    
    function spawnApple() {{
        apple.x = Math.floor(Math.random() * (canvas.width / gridSize)) * gridSize;
        apple.y = Math.floor(Math.random() * (canvas.height / gridSize)) * gridSize;
    }}

    function resetGame() {{
        snake = [{{x: 200, y: 200}}];
        dx = gridSize;
        dy = 0;
        score = 0;
        document.getElementById('score').innerText = score;
        spawnApple();
    }}

    function update() {{
        let head = {{x: snake[0].x + dx, y: snake[0].y + dy}};

        // 모드별 벽 충돌 처리 로직
        if (mode === "PORTAL") {{
            if (head.x < 0) head.x = canvas.width - gridSize;
            else if (head.x >= canvas.width) head.x = 0;
            
            if (head.y < 0) head.y = canvas.height - gridSize;
            else if (head.y >= canvas.height) head.y = 0;
        }} else {{
            // 클래식 & 광기 모드: 벽에 닿으면 죽음
            if (head.x < 0 || head.x >= canvas.width || head.y < 0 || head.y >= canvas.height) {{
                resetGame();
                return;
            }}
        }}

        // 자기 몸에 부딪혔을 때
        for (let i = 0; i < snake.length; i++) {{
            if (head.x === snake[i].x && head.y === snake[i].y) {{
                resetGame();
                return;
            }}
        }}

        snake.unshift(head);

        // 사과 먹었을 때
        if (head.x === apple.x && head.y === apple.y) {{
            score += 10;
            document.getElementById('score').innerText = score;
            spawnApple();
        }} else {{
            snake.pop(); // 안 먹었으면 꼬리 자르기 (이동 효과)
        }}
    }}

    function draw() {{
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // 사과 그리기
        ctx.fillStyle = 'red';
        ctx.fillRect(apple.x, apple.y, gridSize - 2, gridSize - 2);
        
        // 뱀 그리기
        ctx.fillStyle = 'lime';
        snake.forEach(part => {{
            ctx.fillRect(part.x, part.y, gridSize - 2, gridSize - 2);
        }});
    }}

    function gameLoop() {{
        update();
        draw();
    }}

    // 방향키 조작 (기본 스크롤 방지 포함)
    window.addEventListener('keydown', e => {{
        if(["ArrowUp","ArrowDown","ArrowLeft","ArrowRight"].indexOf(e.code) > -1) {{
            e.preventDefault();
        }}
        if (e.key === 'ArrowUp' && dy === 0) {{ dx = 0; dy = -gridSize; }}
        if (e.key === 'ArrowDown' && dy === 0) {{ dx = 0; dy = gridSize; }}
        if (e.key === 'ArrowLeft' && dx === 0) {{ dx = -gridSize; dy = 0; }}
        if (e.key === 'ArrowRight' && dx === 0) {{ dx = gridSize; dy = 0; }}
    }});

    spawnApple();
    setInterval(gameLoop, speed);
</script>
</body>
</html>
"""

# 스트림릿에 HTML 컴포넌트 삽입 (높이를 넉넉하게 줘야 스크롤바가 안 생김)
components.html(snake_html, height=550)
