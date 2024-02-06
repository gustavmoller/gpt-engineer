import pandas as pd
from datetime import datetime

# Define the log entries as a dictionary
log_entries = {
    "etl_run_timestamp": [
        datetime(2023, 1, 2, 9, 0),
        datetime(2023, 2, 2, 9, 0),
        datetime(2023, 3, 2, 9, 0),
        datetime(2023, 4, 2, 9, 0),
    ],
    "log_timestamp": [
        datetime(2023, 1, 2, 10, 0),
        datetime(2023, 2, 2, 10, 0),
        datetime(2023, 3, 2, 10, 0),
        datetime(2023, 4, 2, 10, 0),
    ],
    "table_name": ["tableA", "tableA", "tableA", "tableA"],
    "file_name": ["FileA", "FileB", "FileC", "FileD"],
    "log_type": ["INFO", "INFO", "INFO", "FAIL"],
    "log_details": ["SUCCESS", "SUCCESS", "SUCCESS", "Unexpected File Type"],
}

# Create the DataFrame
logs_df = pd.DataFrame(log_entries)

logs_df.to_csv("db_monitoring/mock_data/staging_database__logs.csv", index=False)
