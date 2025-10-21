
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}我的讀書計畫{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <h1>我的讀書計畫</h1>
        <p>新北高中30937 陳新頤</p>
    </header>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>
        &copy; 2025 新北高中30937 陳新頤 — All rights reserved.
    </footer>
</body>
</html>
