import pandas as pd
import json
from pydbtools import read_sql_query
import pandasql as psql


def sql_query(query, database, table):
    """
    Run SQL query, either on local dataframe, or in AWS, depending on database config
    """
    with open("database_config.json", "r") as file:
        database_config = json.load(file)

    if (
        database in database_config["local_data"]
        and table in database_config["local_data"][database]
    ):
        df = pd.read_csv(
            f"mock_data/{database}__{table}.csv",
        )
        query = query.replace(f"{database}.{table}", "df")
        return psql.sqldf(query, locals())
    else:
        raise ValueError("Database and Table must be defined in database_config.")
