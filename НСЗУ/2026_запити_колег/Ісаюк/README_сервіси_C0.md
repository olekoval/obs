
1. Запит adhoc_pmg.service_C0_20260701.sql створена таблиця зі всіма записами по сервісу С0% . Шлях на локальному комп C:\Users\oleh.koval\Desktop\my_example_py\2026\Ісаюк\сервіси_C0\sql
```sql
create table adhoc_pmg.service_C0_20260701 as (
WITH emz_list AS (
SELECT patient_id, 
       service_number,
       UNNEST(emz_list) AS emz_id 
  FROM analytics.rds_smd_patient_treatments_2025
 WHERE service_number LIKE 'C0%'
   AND is_correct
),

events AS (
 SELECT edrpou,
        patient_id,
        event_id,
		report_year,
		report_month,
		referral_edrpou
  FROM analytics.rds_pmg_events_analytics
 WHERE report_year = '2025'
   AND packet_number = '9'
   AND is_correct
),

Y2025 AS (
SELECT e.*,
       em.service_number
  FROM events e
       JOIN emz_list em ON e.event_id = em.emz_id AND e.patient_id = em.patient_id
),

emz_list_26 AS (
SELECT patient_id, 
       service_number,
       UNNEST(emz_list) AS emz_id 
  FROM analytics.rds_smd_patient_treatments_2026
 WHERE service_number LIKE 'C0%'
   AND is_correct
),

events_26 AS (
 SELECT edrpou,
        patient_id,
        event_id,
		report_year,
		report_month,
		referral_edrpou
  FROM analytics.rds_pmg_events_analytics
 WHERE report_year = '2026'
   AND packet_number = '9'
   AND is_correct
   AND report_month < 4
),

Y2026 AS (
SELECT e.*,
       em.service_number
  FROM events_26 e
       JOIN emz_list_26 em ON e.event_id = em.emz_id AND e.patient_id = em.patient_id
)

SELECT * FROM Y2025
UNION ALL
SELECT * FROM Y2026
);
```
2. Запит services_c0_monthly_avg_2025_2026.sql для розрахунку показників на базі отриманих даних (крок 1)  Шлях на локальному комп C:\Users\oleh.koval\Desktop\my_example_py\2026\Ісаюк\сервіси_C0\sql
```sql
WITH monthly_totals AS (
    -- Крок 1: Рахуємо загальну кількість ЕМЗ для кожного сервісу в розрізі конкретного року та місяця
    SELECT 
        report_year,
        report_month,
        service_number,
        COUNT(*) AS total_emz_in_month
    FROM adhoc_pmg.service_c0_20260701
    GROUP BY report_year, report_month, service_number
),

yearly_patients_and_referrals AS (
    -- Крок 2: Рахуємо унікальних пацієнтів та розподіл направлень за ВЕСЬ РІК
    SELECT 
        report_year,
        service_number,
        COUNT(DISTINCT patient_id) AS unique_patients_period,
        
        -- Рахуємо кількість внутрішніх направлень (свій заклад)
        SUM(CASE WHEN edrpou = referral_edrpou THEN 1 ELSE 0 END) AS internal_referrals,
        
        -- Рахуємо кількість зовнішніх направлений (інший заклад або без направлення)
        SUM(CASE WHEN edrpou <> referral_edrpou OR referral_edrpou IS NULL THEN 1 ELSE 0 END) AS external_referrals
    FROM adhoc_pmg.service_c0_20260701
    GROUP BY report_year, service_number
)

-- Крок 3: Об'єднуємо всі метрики та вираховуємо відсотки
SELECT 
    m.report_year,
    m.service_number,
    COUNT(DISTINCT m.report_month) AS months_with_data,
    SUM(m.total_emz_in_month) AS total_emz_period,
    p.unique_patients_period,
    ROUND(AVG(m.total_emz_in_month)::numeric, 2) AS avg_services_per_month,
    
    -- % направлень зі свого закладу
    ROUND(
        (p.internal_referrals::numeric / NULLIF(SUM(m.total_emz_in_month), 0)) * 100, 
        2
    ) AS pct_internal_referrals,
    
    -- % направлень з інших закладів
    ROUND(
        (p.external_referrals::numeric / NULLIF(SUM(m.total_emz_in_month), 0)) * 100, 
        2
    ) AS pct_external_referrals
FROM monthly_totals m
JOIN yearly_patients_and_referrals p 
    ON m.report_year = p.report_year 
   AND m.service_number = p.service_number
GROUP BY 
    m.report_year, 
    m.service_number, 
    p.unique_patients_period, 
    p.internal_referrals, 
    p.external_referrals
ORDER BY m.report_year DESC, avg_services_per_month DESC;
```
3. Дані з попереднього скрипта result.csv - C:\Users\oleh.koval\Desktop\my_example_py\2026\Ісаюк\сервіси_C0\raw
4. Конвертування у excel та зміна назв полів etl_csv_to_excel.ipynb шлях C:\Users\oleh.koval\Desktop\my_example_py\2026\Ісаюк\сервіси_C0
5. Фінальний файл service_C0_2025-26.xlsx шлях C:\Users\oleh.koval\Desktop\my_example_py\2026\Ісаюк\сервіси_C0