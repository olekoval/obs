- Щоб видалити всі файли та папки у поточній директорії: 
```
rm -rf *
```
- Щоб видалити також і приховані файли (наприклад, конфігурації `.config` чи `.local`):
```
rm -rf .* *
```
- Якщо ви хочете видалити також свої віртуальні середовища (virtualenvs)
```
rm -rf ~/.virtualenvs/*
```
- Перевірте вміст директорії
```
ls -la
```
- Клонування з GitHub
```
git clone -b add-decoding https://github.com/olekoval/flask_searching_codes.git kod-checker
```
- Після внесення змін у локальному проєкті
```
git add .
git commit -m "опис змін"
git push origin add-decoding
```
**На PythonAnywhere** у консолі Bash:
```
cd ~/kod-checker
git pull
```


## Таги
створити локально
```
git tag -a v1.0 -m "опис тегу"
```
Запушити на GitHub:
```
git push origin v1.0
```
Переглянути деталі тегу:
```
git show v1.0
```
