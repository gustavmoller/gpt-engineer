import pandas as pd
from functions.sql_query import sql_query


def check_primary_key_uniqueness(database: str, table: str) -> bool:
    """
    Check the uniqueness of new primary keys in the specified table.
    """
    query = f"""
    SELECT COUNT(*) as total_count, COUNT(DISTINCT primary_key) as unique_count
    FROM {database}.{table}
    """
    df = sql_query(query, database, table)
    return df["total_count"][0] == df["unique_count"][0]
