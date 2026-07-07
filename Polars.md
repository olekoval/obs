---
tags:
  - dash
  - polars
  - python
---
[[Polars_cheat_sheet.pdf]]
[Документація](https://docs.pola.rs/)
[Статя по використанню Polars у Dash](https://plotly.com/blog/polars-to-build-fast-dash-apps-for-large-datasets/)


![[Data-flow-DASH-POLARS-PARQUET.png]]

## Приклад використання
```python
import dash
from dash import Html, Dcc, Input, Output
import plotly.express as px
import polars as pl

# 1. Ініціалізуємо ліниве підключення до партиційованих даних.
# Пам'ять на цьому етапі взагалі не витрачається.
dataset = pl.scan_parquet("data/partitioned_directory/**/*.parquet")

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='category-filter',
        options=[{'label': i, 'value': i} for i in ['Category A', 'Category B', 'Category C']],
        value='Category A'
    ),
    dcc.Graph(id='indicator-graph')
])

@app.callback(
    Output('indicator-graph', 'figure'),
    Input('category-filter', 'value')
)
def update_graph(selected_category):
    # 2. Робимо швидку фільтрацію та агрегацію через Polars
    query = (
        dataset
        .filter(pl.col("category") == selected_category)
        .group_by("date")
        .agg(pl.col("value").sum())
        .sort("date")
    )
    
    # 3. Виконуємо обчислення (.collect()) і перетворюємо ТІЛЬКИ агрегований 
    # маленький результат у Pandas для Plotly (або будуємо графік прямо з Polars)
    df_filtered = query.collect().to_pandas()
    
    # 4. Будуємо графік
    fig = px.line(df_filtered, x="date", y="value", title=f"Trend for {selected_category}")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
```