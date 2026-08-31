import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Streamlit Snake", layout="centered")

st.title("🐍 스트림릿 스네이크 게임 (완전판)")
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

# HTML/JS - 시작 버튼과 사망창(Overlay) 추가
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
    /* 시작/사망 오버레이 창 설정 */
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
        border: 3px solid transparent;
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
        
        <!-- 게임 오버레이 (시작창 / 사망창) -->
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
    
    // UI 요소 가져오기
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
    let score = 0;
    let gameState = "START"; // 상태: START, PLAYING, GAMEOVER
    let gameInterval;
    
    let speed = mode === "MADNESS" ? 50 : 100; 
    
    function spawnApple() {{
        apple.x = Math.floor(Math.random() * (canvas.width / gridSize)) * gridSize;
        apple.y = Math.floor(Math.random() * (canvas.height / gridSize)) * gridSize;
    }}

    function startGame() {{
        // 변수 초기화
        snake = [{{x: 200, y: 200}}];
        dx = gridSize;
        dy = 0;
        score = 0;
        scoreDisplay.innerText = score;
        gameState = "PLAYING";
        
        // 오버레이 숨기기
        overlay.style.display = "none";
        
        spawnApple();
        
        // 기존 인터벌 지우고 새로 시작
        if(gameInterval) clearInterval(gameInterval);
        gameInterval = setInterval(gameLoop, speed);
    }}

    function gameOver() {{
        gameState = "GAMEOVER";
        clearInterval(gameInterval);
        
        // 오버레이 띄우기 (사망창 세팅)
        overlay.style.display = "flex";
        overlayTitle.innerText = "💀 사망! 💀";
        overlayTitle.style.color = "#ff4444";
        overlayScore.style.display = "block";
        finalScore.innerText = score;
        startBtn.innerText = "다시 시작하기";
    }}

    function update() {{
        if (gameState !== "PLAYING") return;

        let head = {{x: snake[0].x + dx, y: snake[0].y + dy}};

        if (mode === "PORTAL") {{
            if (head.x < 0) head.x = canvas.width - gridSize;
            else if (head.x >= canvas.width) head.x = 0;
            if (head.y < 0) head.y = canvas.height - gridSize;
            else if (head.y >= canvas.height) head.y = 0;
        }} else {{
            // 벽 충돌 시 사망
            if (head.x < 0 || head.x >= canvas.width || head.y < 0 || head.y >= canvas.height) {{
                gameOver();
                return;
            }}
        }}

        // 자기 몸 충돌 시 사망
        for (let i = 0; i < snake.length; i++) {{
            if (head.x === snake[i].x && head.y === snake[i].y) {{
                gameOver();
                return;
            }}
        }}

        snake.unshift(head);

        // 사과 먹었을 때
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
            // 시작 전이거나 죽었을 때는 배경만 어둡게 냅둠
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

    // 방향키 조작
    window.addEventListener('keydown', e => {{
        if(["ArrowUp","ArrowDown","ArrowLeft","ArrowRight", "Space"].indexOf(e.code) > -1) {{
            e.preventDefault(); // 스크롤 방지
        }}
        
        if (gameState !== "PLAYING") return;
        
        if (e.key === 'ArrowUp' && dy === 0) {{ dx = 0; dy = -gridSize; }}
        if (e.key === 'ArrowDown' && dy === 0) {{ dx = 0; dy = gridSize; }}
        if (e.key === 'ArrowLeft' && dx === 0) {{ dx = -gridSize; dy = 0; }}
        if (e.key === 'ArrowRight' && dx === 0) {{ dx = gridSize; dy = 0; }}
    }});

    // 시작 버튼 클릭 이벤트
    startBtn.addEventListener('click', startGame);
</script>
</body>
</html>
"""

components.html(snake_html, height=550)
