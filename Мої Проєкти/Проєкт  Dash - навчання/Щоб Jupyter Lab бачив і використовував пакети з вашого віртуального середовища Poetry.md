[[Використання Jupyter Notebook для запуска  додатків Dash]]
## Встановлення ядра для jupyter
- Крок 1: Додайте `ipykernel` до вашого проєкту 

```shall
poetry add ipykernel
```
  - Крок 2: Зареєструйте ядро в Jupyter. Виконайте у терміналі (перебуваючи в папці проєкту):
  ```shall
  poetry run python -m ipykernel install --user --name=dash_project_env --display-   name="Python (Poetry: Dash)"
  ```
	--name=dash_project_env — це внутрішня назва ядра для системи (краще писати латиницею без пробілів).
	    
	--display-name="Python (Poetry: Dash)" — це красиве ім'я, яке ви будете бачити безпосередньо в інтерфейсі Jupyter Lab.
	
3. Крок 3: Запуск та вибір ядра в Jupyter Lab
		**В інтерфейсі Jupyter Lab:**	
	        Відкрийте ваш ноутбук (`.ipynb` файл).
		    У правому верхньому кутку натисніть на поточну назву ядра (зазвичай там написано _Python 3 (ipykernel)_).
		    У випадаючому списку виберіть створене вами ядро: **`Python (Poetry: Dash)`**.
		    атисніть **Select**.
## Корисна порада на майбутнє (якщо захочеться видалити ядро)

Якщо цей проєкт колись стане неактуальним і ви захочете прибрати це ядро зі списку доступних в Jupyter, просто виконайте команду:
```shall
jupyter kernelspec uninstall dash_project_env
```
де dash_project_env - це --name=dash_project_env

## Щоб перевірити список усіх зареєстрованих ядер у Jupyter і дізнатися їхні точні внутрішні назви (ідентифікатори для системи), скористайтеся консольною командою у вашому терміналі.

```shall
jupyter kernelspec list
```
текст перед шляхом є назва ядра