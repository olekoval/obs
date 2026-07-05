# Інструкція: Оновлення реєстру кодів ЕСОЗ та деплой на PythonAnywhere

Цей документ описує покроковий процес перенесення оновленого файлу `all_codes.csv` з локального комп'ютера на сервер [olehkoval.pythonanywhere.com](https://olehkoval.pythonanywhere.com/) через GitHub.

---

## Схема процесу оновлення

```
[Локальний ПК] (export_codes.py) 
       │
       ▼ (git commit & push)
[Репозиторій GitHub] (flask_searching_codes)
       │
       ▼ (git pull)
[Сервер PythonAnywhere] (~/kod-checker) ──> (Reload Web App)
```

---

## Крок 1. Дії на локальному комп'ютері (Push)

Виконується після того, як скрипт `export_codes.py` успішно відпрацював і у консолі з'явилося повідомлення:  
`"Виявлено зміни в кодах. Оновлюємо кодифікатор..."`

1. Відкрийте термінал у папці проєкту (`C:\Users\oleh.koval\Desktop\my_flask`).
2. Перевірте, що Git бачить зміни у файлі:
   ```bash
   git status
   ```
   *(У виводі файл `web_app/static/all_codes.csv` має бути підсвічений червоним коліром у секції "Changes not staged for commit").*

3. Додайте оновлений файл до індексу Git:
   ```bash
   git add web_app/static/all_codes.csv
   ```

4. Створіть комміт із описом оновлення (бажано вказати дату або суть):
   ```bash
   git commit -m "Update all_codes.csv: synced with DWH registry"
   ```

5. Відправте зміни до вашого репозиторію на GitHub:
   ```bash
   git push origin main
   ```

---

## Крок 2. Дії на сервері PythonAnywhere (Pull)

1. Увійдіть у свій акаунт на **PythonAnywhere**.
2. Перейдіть у вкладку **Consoles** та відкрийте вашу робочу **Bash**-консоль.
3. Перейдіть у кореневу папку вашого веб-застосунку:
   ```bash
   cd ~/kod-checker
   ```
4. Стягніть оновлений файл із GitHub:
   ```bash
   git pull origin main
   ```
   *(Git має вивести повідомлення про успішне оновлення файлу `web_app/static/all_codes.csv` через `Fast-forward`).*

---

## Крок 3. Перезапуск веб-застосунку (Reload)

Оскільки Flask читає файл `all_codes.csv` в оперативну пам'ять **лише один раз під час старту**, застосунок на сервері не дізнається про нові коди до перезапуску воркера.

1. На панелі керування PythonAnywhere перейдіть у вкладку **Web** (меню зверху праворуч).
2. Знайдіть ваш застосунок `olehkoval.pythonanywhere.com`.
3. Натисніть велику зелену кнопку **Reload olehkoval.pythonanywhere.com**.

---
**Готово!** Нові коди успішно завантажені та доступні для перевірки користувачами.
