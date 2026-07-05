https://prodject-rules.onrender.com/

[Render](https://render.com/)

1. Перевірити/Додати щоб у pyprodject.toml були рядки
```
[tool.poetry]
package-mode = false

```
1. Зайти на [Render](https://render.com/) на вкладку Dashboard
2. Кнопка +New -> Web Service
3. Кнопка GitHub
4. На GitHub вибрати репозітарій та зберегти вибір
5. На Render вкладка Environment створити нову variables
```
PYTHON_VERSION 3.12
```
6. Якщо диплой не почався (дивись вкладку Logs) то на Environment натиснути Manual Deploy -> Clear build cache & deploy
### Як налаштувати Render для роботи з Poetry

Під час створення **Web Service** змініть стандартні команди на такі:

1. **Build Command** (Команда збірки) Замість стандартного `pip install -r requirements.txt` вкажіть: 
```bash 
poetry add gunicorn && poetry install
```
2. **Start Command** (Команда запуску) Оскільки ваші залежності (зокрема `gunicorn`) встановлені всередині ізольованого оточення Poetry, запускати додаток потрібно через утиліту `poetry run`:
```bash
poetry run gunicorn app:app
```
_(Де перше `app` — назва вашого файлу `app.py`, а друге — змінна `app = Flask(__name__)`)_.
у моєму випадку 
```bash
poetry run gunicorn main:app
```
