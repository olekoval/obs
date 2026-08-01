- створити файл python_profile.py
```python
try:
    from rich import pretty, inspect
    from rich import print as rprint
    
    pretty.install()
    print("✨ Rich успішно інтегровано в REPL!")
except ImportError:
    pass
```
- У консолі windows ввести команду
```shell
setx PYTHONSTARTUP "C:\Users\oleh.koval\Desktop\my_example_py\python_profile.py"
```
Де шлях це шлях до збереженого файлу python_profile.py

Консольна справка:

```shall
python -m rich
```