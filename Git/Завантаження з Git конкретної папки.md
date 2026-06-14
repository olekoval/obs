
# 1. Створюємо нову порожню папку для проєкту і переходимо в неї
mkdir my_project
cd my_project

# 2. Ініціалізуємо порожній Git-репозиторій
git init

# 3. Додаємо віддалений репозиторій (remote) з увімкненим фільтром на відсутність об'єктів (blob:none)
git remote add -f origin https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash.git

# 4. Вмикаємо режим sparse-checkout
git sparse-checkout init --cone

# 5. Вказуємо конкретну папку, яку хочемо завантажити
git sparse-checkout set data

# 6. Стягуємо дані (буде завантажено лише папку data)
git pull origin master