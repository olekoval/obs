---
tags:
  - polars
  - pandas
---
## Перетворювати датафрейми Pandas на Polars

З Pandas до Polars
```python
animals_pl = pl.DataFrame(animals_pd)
```

З  Polars до Pandas
```python
animals_pd = animals_pl.to_pandas()
```
## Порівняння деяких операцій

| Дія                                | Pandas                                                           | Polars                                                              |
| ---------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------- |
| Видалення дублікатів               | animals_pd.drop_duplicates(subset="class")                       | animals_pl.unique(subset="class")                                   |
| Видалення пропущених значень       | animals_pd.dropna(subset="weight")                               | animals_pl.drop_nulls(subset="weight")                              |
| Сортування рядків                  | animals_pd.sort_values("weight", ascending=False)                | animals_pl.sort("weight", descending=True)                          |
| Приведення типів існуючих стовпців | animals_pd.assign(lifespan=animals_pd["lifespan"].astype(float)) | animals_pl.with_columns(pl.col("lifespan").cast(pl.Float64))        |
| Агрегація даних                    | animals_pd.groupby(["class", "status"])[["weight"]].mean()       | animals_pl.group_by("class", "status").agg(pl.col("weight").mean()) |
