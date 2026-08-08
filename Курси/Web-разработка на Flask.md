---
tags:
  - flask
  - Linux
  - курси
---
## Основи Flask
### Віртуальні середовища
1. Встановіть інструмент для створення віртуальних середовищ (якщо ще не встановлено)
```bash
sudo apt update && sudo apt install python3-venv
```
2. Створіть віртуальне середовище у паці проєкту
```bash
python3 -m venv venv
```
3. Активуйте його
```bash
source venv/bin/activate
```
4. Тепер команда pip працюватиме без обмежень усередині середовища
```bash
pip install Flask
```
