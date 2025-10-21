
import os
from flask import Flask, render_template

# -------------------------------
# Flask App 初始化設定
# -------------------------------
app = Flask(__name__)

# -------------------------------
# 路由設定區（網站各頁面）
# -------------------------------

@app.route('/')
def index():
    """首頁"""
    return render_template('index.html')


@app.route('/competition')
def competition():
    """競賽頁面"""
    return render_template('competition.html')


@app.route('/activities')
def activities():
    """活動頁面"""
    return render_template('activities.html')


@app.route('/leadership')
def leadership():
    """領導力頁面"""
    return render_template('leadership.html')


@app.route('/club')
def club():
    """社團頁面"""
    return render_template('club.html')


@app.route('/electives')
def electives():
    """選修課頁面"""
    return render_template('electives.html')


@app.route('/ai')
def ai():
    """人工智慧頁面"""
    return render_template('ai.html')


# -------------------------------
# 主程式進入點
# -------------------------------
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(
        host='0.0.0.0',   # 可從外部訪問（例如在部署環境）
        port=port,
        debug=True        # 啟用除錯模式，方便開發階段
    )
