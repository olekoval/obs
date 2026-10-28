```sql
SELECT CONCAT (a.service_number, ' - ', s.name) AS servise
  FROM analytics.rds_pmg_events_analytics a
       LEFT JOIN analytics.ref_pmg_coefficients_services s ON a.service_number = s.service_number
	   AND s.year=2026 AND s.is_current = 'Y'
  WHERE a.report_year = 2026
   AND a.is_correct
   AND a.packet_number = '6'
GROUP BY CONCAT (a.service_number, ' - ', s.name)
```