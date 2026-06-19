-- Bronze-equivalent raw input for dbt.
--
-- This deliberately reads the CSV from a relative path instead of using dbt's
-- seed loader. dbt-duckdb 1.10.1 generates an unescaped COPY path for seeds on
-- Windows, which breaks when the project path contains an apostrophe.
{{ config(materialized='table') }}

select *
from read_csv_auto('seeds/raw_orders.csv', header=true, all_varchar=true)
