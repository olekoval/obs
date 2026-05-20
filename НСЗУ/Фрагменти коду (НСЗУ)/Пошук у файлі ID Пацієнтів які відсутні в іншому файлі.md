Пошук у файлі 'packet_3_4.xlsx' 'ID_пацієнта' які відсутні у файлі "ІД всіх пацієнтів за 5 років (20 пакет).xlsx"
```python
import pandas as pd

df_34 = pd.read_excel('packet_3_4.xlsx')
df_20year5 = pd.read_excel("ІД всіх пацієнтів за 5 років (20 пакет).xlsx")

# Створюємо список унікальних ID з пакета 20 для швидкого пошуку
p20_ids = df_20year5['patient_id'].unique()

df_34['Примітка'] = (df_34['ID_пацієнта']
                     .isin(p20_ids)
                     .map({True: 'Є в packet_20year5',
                           False: 'Відсутній у packet_20year5'}))

# Збереження результату
df_34.to_excel('packet34_marked_year5.xlsx', index=False)

print(f"Файл збеоежено - {len(df_34)} рядків")
```
