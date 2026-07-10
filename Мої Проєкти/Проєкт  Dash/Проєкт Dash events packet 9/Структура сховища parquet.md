my_dash_app/
┃
└── data/
    └── healthcare_events/              <-- Головна директорія датасету
	        ├── year=2025/
	        │   ├── month=11/
	        │   │   └── data_0.parquet
	        │   └── month=12/
	        │       └── data_0.parquet
	        └── year=2026/
	            ├── month=01/
	            │   └── data_0.parquet
	            └── month=02/
	                └── data_0.parquet



```sql
SELECT event_id, metric, year, month FROM 'data/healthcare_events/**/*.parquet' WHERE year = 2026 AND month = '01';
```
```python
query = """
SELECT edrpou, COUNT(*)
  FROM './data/events/**/*.parquet'
 WHERE month IN ('01', '02') 
 GROUP BY edrpou 
"""
df_count = duckdb.query(query).to_df()

```