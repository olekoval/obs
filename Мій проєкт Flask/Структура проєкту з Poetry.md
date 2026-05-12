#flask 
[[Flask]]


my_flask_app/
│
├── web_app/                      # Основний пакет додатка
│   ├
│   ├── routes.py          # Логіка маршрутів
│   ├── models.py         # Опис моделей (PostgreSQL/SQLAlchemy)
│   ├── static/               # CSS, JS, Images
│   └── templates/        # Jinja2 шаблони
│
├── tests/                      # Тести (pytest)
│   └── __init__.py
│
├── .env                          # Секретні ключі та посилання на БД
├── .gitignore
├── pyproject.toml        # Конфігурація Poetry (залежності, версії)
├── poetry.lock              # Зафіксовані версії пакетів
└── main.py                      # Основний скрипт для запуску додатка

