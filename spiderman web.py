from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Movie Dateee!! 🕷️</title>
    <!-- Google Fonts & Canvas Confetti -->
    <link href="https://fonts.googleapis.com/css2?family=Bangers&family=Outfit:wght@400;600;800&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <style>
        :root {
            --spider-red: #e62429;
            --spider-blue: #007bb6;
            --spider-dark: #0d0f12;
            --card-bg: rgba(22, 27, 34, 0.85);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: var(--spider-dark);
            background-image: 
                radial-gradient(circle at 50% 50%, rgba(230, 36, 41, 0.15) 0%, transparent 70%),
                repeating-radial-gradient(circle at 50% 50%, transparent 0, transparent 25px, rgba(255, 255, 255, 0.03) 26px, rgba(255, 255, 255, 0.03) 27px);
            font-family: 'Outfit', sans-serif;
            color: #ffffff;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            overflow-x: hidden;
        }

        .card {
            background: var(--card-bg);
            border: 2px solid rgba(230, 36, 41, 0.5);
            border-radius: 20px;
            padding: 40px 30px;
            max-width: 480px;
            width: 100%;
            text-align: center;
            box-shadow: 0 0 30px rgba(230, 36, 41, 0.3), inset 0 0 15px rgba(0, 123, 182, 0.2);
            backdrop-filter: blur(10px);
            position: relative;
        }

        .spider-badge {
            font-size: 3.5rem;
            margin-bottom: 10px;
            animation: pulse 2s infinite ease-in-out;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.1); }
        }

        h1 {
            font-family: 'Bangers', cursive;
            font-size: 3.2rem;
            letter-spacing: 2px;
            color: var(--spider-red);
            text-shadow: 3px 3px 0px var(--spider-blue), 0 0 10px rgba(230, 36, 41, 0.6);
            margin-bottom: 25px;
            text-transform: uppercase;
        }

        .details-list {
            background: rgba(0, 0, 0, 0.4);
            border-left: 4px solid var(--spider-blue);
            border-radius: 12px;
            padding: 20px;
            text-align: left;
            margin-bottom: 30px;
        }

        .detail-item {
            display: flex;
            align-items: center;
            margin-bottom: 12px;
            font-size: 1.05rem;
        }

        .detail-item:last-child {
            margin-bottom: 0;
        }

        .detail-item span.icon {
            font-size: 1.3rem;
            margin-right: 12px;
            width: 25px;
            text-align: center;
        }

        .detail-item strong {
            color: var(--spider-red);
            margin-right: 8px;
        }

        .buttons-container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
            min-height: 60px;
            position: relative;
        }

        .btn {
            font-family: 'Bangers', cursive;
            font-size: 1.6rem;
            letter-spacing: 1px;
            padding: 12px 36px;
            border-radius: 50px;
            border: none;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            user-select: none;
        }

        .btn-yes {
            background: linear-gradient(135deg, var(--spider-red), #b30000);
            color: white;
            border: 2px solid #ff4d4d;
        }

        .btn-yes:hover {
            transform: scale(1.1);
            box-shadow: 0 0 25px rgba(230, 36, 41, 0.8);
        }

        .btn-no {
            background: #2a2e37;
            color: #888;
            border: 1px solid #444;
            position: relative;
        }

        #celebration {
            display: none;
            margin-top: 20px;
            animation: fadeIn 0.5s forwards;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .celebration-title {
            font-family: 'Bangers', cursive;
            font-size: 2.5rem;
            color: #4E9F3D;
            text-shadow: 0 0 10px rgba(78, 159, 61, 0.5);
        }

        .celebration-sub {
            font-size: 1.1rem;
            margin-top: 5px;
            color: #ddd;
        }
    </style>
</head>
<body>

    <div class="card">
        <div class="spider-badge">🕷️</div>
        <h1>hellooo gandaaaa!!</h1>

        <div class="details-list">
            <div class="detail-item">
                <span class="icon">📅</span>
                <strong>When:</strong> August 9, 2026 (Monday)
            </div>
            <div class="detail-item">
                <span class="icon">📍</span>
                <strong>Meetup:</strong> SDA Campus
            </div>
            <div class="detail-item">
                <span class="icon">⏰</span>
                <strong>Time:</strong> 12:00 PM
            </div>
            <div class="detail-item">
                <span class="icon">🎬</span>
                <strong>Where:</strong> Greenbelt 3
            </div>
            <div class="detail-item">
                <span class="icon">🍿</span>
                <strong>Movie:</strong> Spider-Man: Brand New Day
            </div>
            <div class="detail-item">
                <span class="icon">🍽️</span>
                <strong>Lunch:</strong> Maison @ Greenbelt
            </div>
        </div>

        <div id="interactive-section">
            <p style="margin-bottom: 15px; font-weight: 600;">Are you coming with me? 🕸️</p>
            <div class="buttons-container" id="btnGroup">
                <button class="btn btn-yes" id="yesBtn">YES!</button>
                <button class="btn btn-no" id="noBtn">No</button>
            </div>
        </div>

        <div id="celebration">
            <div class="celebration-title">Yaaayyyyy! 🎉</div>
            <p class="celebration-sub">Can't wait to see you my Lianaaaa! 🕷️❤️</p>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const yesBtn = document.getElementById('yesBtn');
            const noBtn = document.getElementById('noBtn');
            const interactiveSection = document.getElementById('interactive-section');
            const celebration = document.getElementById('celebration');

            // YES Click Action
            yesBtn.addEventListener('click', () => {
                interactiveSection.style.display = 'none';
                celebration.style.display = 'block';

                if (typeof confetti === 'function') {
                    confetti({
                        particleCount: 120,
                        spread: 70,
                        origin: { y: 0.6 },
                        colors: ['#e62429', '#007bb6', '#ffffff']
                    });
                }
            });

            // NO Runaway Action
            const dodgeNo = () => {
                const maxX = 120;
                const maxY = 50;

                const randomX = (Math.random() - 0.5) * maxX;
                const randomY = (Math.random() - 0.5) * maxY;

                noBtn.style.position = 'absolute';
                noBtn.style.transform = `translate(${randomX}px, ${randomY}px)`;
            };

            noBtn.addEventListener('mouseover', dodgeNo);
            noBtn.addEventListener('click', dodgeNo);
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)