import pandas as pd
from functions.sql_query import sql_query


def get_new_primary_keys_count(database: str, table: str) -> int:
    """
    Get the count of new primary keys added to the specified table.
    """
    query = f"""
    SELECT COUNT(DISTINCT primary_key) as new_keys_count
    FROM {database}.{table}
    WHERE etl_run_timestamp = (SELECT MAX(etl_run_timestamp) FROM {database}.{table})
    """
    df = sql_query(query, database, table)
    return df["new_keys_count"][0]
