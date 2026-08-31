import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Streamlit Snake", layout="centered")

st.title("🐍 스트림릿 스네이크 게임 (버그 패치완료)")
st.write("키보드 방향키(⬆️ ⬇️ ⬅️ ➡️)로 조작하세요.")

# 3가지 종목 선택
mode = st.radio(
    "종목(모드)을 선택해:",
    ["클래식 (벽 닿으면 사망)", "포탈 (벽 뚫고 반대편으로)", "광기 (속도 2배)"],
    horizontal=True
)

game_mode = "CLASSIC"
if "포탈" in mode:
    game_mode = "PORTAL"
elif "광기" in mode:
    game_mode = "MADNESS"

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
        font-family: 'Malgun Gothic', sans-serif;
        margin: 0;
        padding: 20px;
    }}
    #scoreBoard {{
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
        color: #4CAF50;
    }}
    #gameWrapper {{
        position: relative;
        width: 400px;
        height: 400px;
    }}
    canvas {{
        background-color: #222;
        border: 3px solid #4CAF50;
        box-shadow: 0 0 15px rgba(76, 175, 80, 0.5);
    }}
    #overlay {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.8);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        z-index: 10;
    }}
    #overlayTitle {{
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 10px;
        color: white;
    }}
    #overlayScore {{
        font-size: 20px;
        margin-bottom: 20px;
        display: none;
    }}
    button {{
        padding: 10px 25px;
        font-size: 18px;
        font-weight: bold;
        color: white;
        background-color: #4CAF50;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: 0.2s;
    }}
    button:hover {{
        background-color: #45a049;
        transform: scale(1.05);
    }}
</style>
</head>
<body>
    <div id="scoreBoard">점수: <span id="score">0</span></div>
    
    <div id="gameWrapper">
        <canvas id="gameCanvas" width="400" height="400"></canvas>
        
        <div id="overlay">
            <div id="overlayTitle">스네이크 게임</div>
            <div id="overlayScore">최종 점수: <span id="finalScore">0</span></div>
            <button id="startBtn">게임 시작</button>
        </div>
    </div>

<script>
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');
    const gridSize = 20;
    const mode = "{game_mode}";
    
    const overlay = document.getElementById('overlay');
    const overlayTitle = document.getElementById('overlayTitle');
    const overlayScore = document.getElementById('overlayScore');
    const finalScore = document.getElementById('finalScore');
    const startBtn = document.getElementById('startBtn');
    const scoreDisplay = document.getElementById('score');
    
    let snake = [];
    let apple = {{}};
    let dx = gridSize;
    let dy = 0;
    let nextDx = gridSize; // 연타 방지 및 방향 고정을 위한 변수
    let nextDy = 0;
    let score = 0;
    let gameState = "START";
    let gameInterval;
    
    let speed = mode === "MADNESS" ? 50 : 100; 
    
    function spawnApple() {{
        apple.x = Math.floor(Math.random() * (canvas.width / gridSize)) * gridSize;
        apple.y = Math.floor(Math.random() * (canvas.height / gridSize)) * gridSize;
    }}

    function startGame() {{
        snake = [{{x: 200, y: 200}}];
        dx = gridSize;
        dy = 0;
        nextDx = gridSize;
        nextDy = 0;
        score = 0;
        scoreDisplay.innerText = score;
        gameState = "PLAYING";
        
        overlay.style.display = "none";
        spawnApple();
        
        if(gameInterval) clearInterval(gameInterval);
        gameInterval = setInterval(gameLoop, speed);
    }}

    function gameOver() {{
        gameState = "GAMEOVER";
        clearInterval(gameInterval);
        
        overlay.style.display = "flex";
        overlayTitle.innerText = "💀 사망! 💀";
        overlayTitle.style.color = "#ff4444";
        overlayScore.style.display = "block";
        finalScore.innerText = score;
        startBtn.innerText = "다시 시작하기";
    }}

    function update() {{
        if (gameState !== "PLAYING") return;

        // 키보드 입력을 실제 이동 방향으로 확정
        dx = nextDx;
        dy = nextDy;

        let head = {{x: snake[0].x + dx, y: snake[0].y + dy}};

        if (mode === "PORTAL") {{
            if (head.x < 0) head.x = canvas.width - gridSize;
            else if (head.x >= canvas.width) head.x = 0;
            if (head.y < 0) head.y = canvas.height - gridSize;
            else if (head.y >= canvas.height) head.y = 0;
        }} else {{
            if (head.x < 0 || head.x >= canvas.width || head.y < 0 || head.y >= canvas.height) {{
                gameOver();
                return;
            }}
        }}

        // 자기 몸 충돌 시 사망 (머리가 몸통 좌표랑 겹치는지 확인)
        for (let i = 0; i < snake.length; i++) {{
            if (head.x === snake[i].x && head.y === snake[i].y) {{
                gameOver();
                return;
            }}
        }}

        snake.unshift(head);

        if (head.x === apple.x && head.y === apple.y) {{
            score += 10;
            scoreDisplay.innerText = score;
            spawnApple();
        }} else {{
            snake.pop(); 
        }}
    }}

    function draw() {{
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        if (gameState === "START" || gameState === "GAMEOVER") {{
            return;
        }}

        ctx.fillStyle = 'red';
        ctx.fillRect(apple.x, apple.y, gridSize - 2, gridSize - 2);
        
        ctx.fillStyle = 'lime';
        snake.forEach(part => {{
            ctx.fillRect(part.x, part.y, gridSize - 2, gridSize - 2);
        }});
    }}

    function gameLoop() {{
        update();
        draw();
    }}

    // 방향키 조작 (역주행 및 동시 입력 꼬임 방지 로직 적용)
    window.addEventListener('keydown', e => {{
        if(["ArrowUp","ArrowDown","ArrowLeft","ArrowRight", "Space"].indexOf(e.code) > -1) {{
            e.preventDefault();
        }}
        
        if (gameState !== "PLAYING") return;
        
        // 현재 이동 방향(dx, dy)의 정반대 방향으로는 아예 입력이 안 되도록 제어
        if (e.key === 'ArrowUp' && dy === 0) {{ nextDx = 0; nextDy = -gridSize; }}
        if (e.key === 'ArrowDown' && dy === 0) {{ nextDx = 0; nextDy = gridSize; }}
        if (e.key === 'ArrowLeft' && dx === 0) {{ nextDx = -gridSize; nextDy = 0; }}
        if (e.key === 'ArrowRight' && dx === 0) {{ nextDx = gridSize; nextDy = 0; }}
    }});

    startBtn.addEventListener('click', startGame);
</script>
</body>
</html>
"""

components.html(snake_html, height=550)
