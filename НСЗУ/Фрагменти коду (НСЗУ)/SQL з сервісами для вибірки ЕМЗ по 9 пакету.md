```sql
WITH tr AS (
SELECT service_number, 
	   UNNEST(emz_list) AS event_id
  FROM analytics.rds_smd_patient_treatments_2026
 WHERE is_correct 
   AND is_payed
   AND packet_number = '9'
   AND service_number IN ('I0030', 'I0020')
),
p9 AS (
SELECT edrpou, 
       patient_id,
	   event_id,  
	   report_month,
	   ends
  FROM analytics.rds_pmg_events_analytics
 WHERE report_year = 2026 
   AND packet_number = '9' 
   AND is_correct
   AND event_type = 'diagnostic_report'
),
kt AS (
SELECT p9.edrpou,
       p9.patient_id, 
	   CASE
	       WHEN service_number = 'I0020' THEN 'Комп’ютерна томографія з контрастуванням'
		   WHEN service_number = 'I0030' THEN 'Комп’ютерна томографія без контрастуванням'
	   END AS service,	   
	   p9.report_month,
	   p9.ends
  FROM p9
       INNER JOIN tr USING(event_id)
)

SELECT v.residence_area,
       v.kwd_name,
       kt.edrpou,
	   kt.patient_id,
	   kt.service,
	   DATE(kt.ends) AS ends_date
  FROM kt
       LEFT JOIN analytics.dwh_legal_entities_edrpou_view AS v USING(edrpou)
 WHERE DATE(kt.ends) BETWEEN '2026-04-01' AND '2026-09-30'
 ORDER BY residence_area, edrpou, ends

```