---
tags:
  - render
---
[Документація по deploy на render](https://render.com/docs/deploys)
[ Документація First Render Deploy](https://render.com/docs/your-first-deploy)


[Розгортання нового проєкту](https://dashboard.render.com/)

## Основні пункти форми для deploy
- Build Command: 
```bash
$ poetry add gunicorn && poetry install
```
- Start Command:
```bash
$ poetry run gunicorn main:app
```
Де main це назва файла python у проєкті в котрому запускається весь додаток app