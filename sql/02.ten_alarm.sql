SELECT
   description,
   `name`,
   end_date,email  
FROM
  tenant 
WHERE 
  PERIOD_DIFF( date_format( now( ) , '%Y%m' ) , date_format( end_date, '%Y%m' ) ) <1 
  AND PERIOD_DIFF( date_format( now( ) , '%Y%m' ) , date_format( end_date, '%Y%m' ) ) >=-1
  AND TO_DAYS( NOW( ) ) - TO_DAYS( end_date) < 0"
