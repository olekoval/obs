**eHealth/LOINC/observation_codes** - коди спостережень
**eHealth/ICD10_AM/condition_codes** - коди діагнозів


коди інтервенцій зберігаються у таблиці - **core.dim_rpt_services**

```bash
SELECT 
        v.code, 
        v.description, 
        d.kwd_name
    FROM core.dim_rpt_dictionary_values AS v
    INNER JOIN core.dim_rpt_dictionaries AS d ON v.dictionary_id = d.id
    WHERE v.is_current = 'Y' 
      AND d.is_current = 'Y'
      AND d.kwd_name IN ('eHealth/LOINC/observation_codes', 'eHealth/ICD10_AM/condition_codes')
```