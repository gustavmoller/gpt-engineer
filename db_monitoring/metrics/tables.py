import pandas as pd
from functions.sql_query import sql_query


def display_recent_failures(database: str, table: str):
    """
    Select all failures from the logs.
    """
    query = f"""
    SELECT *
    FROM {database}.{table}
    WHERE log_type = 'FAIL'
    ORDER BY etl_run_timestamp DESC
    """
    df = sql_query(query, database, table)
    return df
