
[[Щоб Jupyter Lab бачив і використовував пакети з вашого віртуального середовища Poetry]]

## Застарілий варіант:
```shell
from jupyter_dash import JupyterDash
app = JupyterDash(__name__)
```
Также вы можете указать желаемую ширину и высоту приложения, как по-
казано ниже:

```shell
app.run_server(mode='inline', height=600, width='80%')
```
## Поточний варіант - імпорт бібліотек як у звичайному файлі python