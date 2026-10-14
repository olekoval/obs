```python
import pandas as pd

df = pd.DataFrame({'cod': [['A', 'A', 'B'], ['C', 'D', 'D']]})

# 1. Розгортаємо масив у рядки
df_exploded = df.explode('cod')

# 2. Робимо крос-табуляцію та reset_index()
df_gr = pd.crosstab(df_exploded.index, df_exploded['cod']).reset_index()

# 3. Об'єднуємо (merge) вихідний df з df_gr
# Ліворуч об'єднуємо за індексом (left_index=True),
# праворуч — за колонкою з назвою індексу ('row_0' або 'index')
index_col = df_gr.columns[0]  # Автоматично беремо назву першої колонки ('row_0' або 'index')

df_merged = df.merge(df_gr, left_index=True, right_on=index_col)

# (Опціонально) видаляємо службовий стовпчик індексу після merge
df_merged = df_merged.drop(columns=[index_col])

print(df_merged)
```