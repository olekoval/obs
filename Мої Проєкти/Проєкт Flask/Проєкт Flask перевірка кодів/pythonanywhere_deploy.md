# Deploy Flask-проєкту на PythonAnywhere

## Крок 1 — Генеруємо `requirements.txt` (локально)

Poetry не підтримується на PythonAnywhere, тому експортуємо залежності у стандартний формат pip.

```bash
poetry self add poetry-plugin-export
poetry export -f requirements.txt --output requirements.txt --without-hashes --without-markers
```

> ⚠️ Прапорець `--without-markers` прибирає умови на кшталт `; python_version == '3.12'` — файл стає чистішим.

---

## Крок 2 — Клонуємо репозиторій на PythonAnywhere

Відкриваємо **Consoles → Bash** і виконуємо:

```bash
git clone -b назва-гілки https://github.com/твій-репозиторій.git назва-папки
```

- `-b` — скорочення від `--branch`, вказує яку гілку клонувати. Без нього береться гілка за замовчуванням (`main`).
- `назва-папки` — довільна назва папки яку git створить на сервері.

---

## Крок 3 — Створюємо virtualenv і встановлюємо залежності

```bash
python3.12 -m venv /home/olehkoval/.virtualenvs/назва-env
source /home/olehkoval/.virtualenvs/назва-env/bin/activate
cd ~/назва-папки
pip install -r requirements.txt
```

> ⚠️ `mkvirtualenv` не працює на PythonAnywhere — використовуємо стандартний `python -m venv`.

---

## Крок 4 — Створюємо Web App

**Web → Add a new web app → Manual configuration → Python 3.12**

> ⚠️ Коли питає *"Enter a path for a Python file"* — вводити шлях до існуючого `main.py`.
> PythonAnywhere **перезапише файл** своїм Hello World. Відновлення: `git checkout main.py`

---

## Крок 5 — Налаштовуємо WSGI-файл

Відкриваємо `/var/www/olehkoval_pythonanywhere_com_wsgi.py` і залишаємо тільки:

```python
import sys

project_home = '/home/olehkoval/назва-папки'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

from main import app as application  # noqa
```

> ⚠️ **НЕ додавати** `activate_this.py` — він існує тільки у `virtualenv`, але ми створювали через `venv` (вбудований в Python). У `venv` цього файлу немає.

---

## Крок 6 — Налаштовуємо панель Web App

| Поле | Значення |
|------|----------|
| Source code | `/home/olehkoval/назва-папки` |
| Working directory | `/home/olehkoval/назва-папки` |
| Virtualenv | `/home/olehkoval/.virtualenvs/назва-env` |
| Static URL | `/static/` |
| Static Directory | `/home/olehkoval/назва-папки/web_app/static/` |

---

## Крок 7 — Виправлення у `main.py`

### 7.1 Додати `import os`

Без нього `os.environ.get()` викине `NameError` при старті додатку.

```python
import os  # додати на початку файлу
```

### 7.2 Виправити шлях до CSV — з відносного на абсолютний

Відносний шлях працює локально бо запускаєш з папки проєкту. На сервері робоча директорія інша — потрібен абсолютний шлях через `__file__`.

```python
# Було — не працює на сервері
df = pd.read_csv('web_app/static/all_codes.csv')

# Стало — працює завжди
csv_path = os.path.join(os.path.dirname(__file__), 'web_app/static/all_codes.csv')
df = pd.read_csv(csv_path)
```

### 7.3 Виправити `SECRET_KEY`

Захардкоджений ключ небезпечний для продакшну.

```python
# Було
app.config['SECRET_KEY'] = 'dev-key-314'

# Стало
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(24))
```

---

## Крок 8 — Reload та перевірка

Натискаємо кнопку **Reload** у вкладці **Web**.

Якщо помилка — дивимось логи:

```bash
tail -20 /var/log/olehkoval.pythonanywhere.com.error.log
```

---

## Типові помилки та їх причини

### `FileNotFoundError: activate_this.py`
Додали `activate_this` у WSGI але використовували `python -m venv`.  
**Рішення:** прибрати рядки з `activate_this` з WSGI-файлу.

### `NameError: name 'os' is not defined`
Використали `os.environ` але забули `import os` на початку `main.py`.

### `FileNotFoundError: all_codes.csv`
Pandas читає CSV відносним шляхом. На сервері робоча директорія інша.  
**Рішення:** використати `os.path.join(os.path.dirname(__file__), ...)`.

### `main.py` перезаписаний Hello World
PythonAnywhere перезаписав файл при створенні Web App.  
**Рішення:** `git checkout main.py`
