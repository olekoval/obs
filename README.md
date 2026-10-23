# Newborn

Сутність [ЕСОЗ Composition](https://e-health-ua.atlassian.net/wiki/spaces/ESOZ/pages/18527911952/Composition+ENT-009#%D0%A1%D1%82%D0%B0%D1%82%D1%83%D1%81%D0%BD%D0%B0-%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C-%D0%B4%D0%BB%D1%8F-%D0%9C%D0%92%D0%9D-(NEWBORN))

```sql
SELECT *
FROM core.dim_rpt_composition
WHERE is_current = 'Y' 
  AND type_coding_code = 'NEWBORN'
```  