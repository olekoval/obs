
```python
# ==========================================
# 1. ІМПОРТИ (Блок з "Flask_Dash_2.json")
# ==========================================
from flask import Flask, render_template_string 
from dash import Dash, html, dcc, callback, Input, Output  # Додано callback, Input, Output

# ==========================================
# 2. ІНІЦІАЛІЗАЦІЯ ДОДАТКІВ
# ==========================================
# Створюємо Flask сервер
server = Flask(__name__)  #

# Ініціалізуємо Dash всередині Flask (виправлено опечатку в "routes_")
app = Dash(
    __name__, 
    server=server, 
    routes_pathname_prefix='/dash/'  #
)

# ==========================================
# 3. МАКЕТ DASH (Layout)
# ==========================================
app.layout = html.Div([  #
    html.H1("Аналітичний дашборд"),
    html.Button("Натисни мене", id="dash-btn"),
    html.Div(id="dash-output"),
    html.Br(),
    html.A("← Повернутися на головну Flask", href="/")
])

# ==========================================
# 4. МАРШРУТИ FLASK (@server.route)
# ==========================================
@server.route('/')  #[cite: 2]
def index():
    return render_template_string('''
        <h1>Головна сторінка Flask проєкту</h1>
        <p>Це звичайна сторінка, яку рендерить Flask.</p>
        <hr>
        <a href="/dash/">📊 Перейти до Dash аналітики</a>
    ''')

# ==========================================
# 5. КОЛБЕКИ DASH (@callback)
# ==========================================
@callback(  #[cite: 2]
    Output("dash-output", "children"),
    Input("dash-btn", "n_clicks"),
    prevent_initial_call=True
)
def update_dash_ui(n_clicks):
    return f"Кнопку всередині Dash натиснуто стільки разів: {n_clicks}"

# ==========================================
# 6. ЗАПУСК СЕРВЕРА
# ==========================================
if __name__ == '__main__':  #[cite: 2]
    server.run(debug=True, port=5000)  #[cite: 2]
```