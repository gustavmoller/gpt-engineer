import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def random_date_in_year_month(year, month=None):
    """Generate a random date within a specified year and month."""
    start_date = datetime(year, month if month else 1, 1)
    if month:
        end_date = datetime(year, month % 12 + 1, 1) - timedelta(days=1)
    else:
        end_date = datetime(year, 12, 31)
    random_days = np.random.randint(0, (end_date - start_date).days + 1)
    return start_date + timedelta(days=random_days)


def date_before_given_date(given_date, max_days_before=28):
    """Generate a date 1 to max_days_before days before the given date."""
    days_before = np.random.randint(1, max_days_before + 1)
    return given_date - timedelta(days=days_before)


def update_row(row):
    """Randomly update 1 to 3 columns in a row with new data."""
    updates = np.random.choice(
        ["data_column1", "data_column2", "data_column3"],
        np.random.randint(1, 4),
        replace=False,
    )
    if "data_column1" in updates:
        row["data_column1"] = np.random.choice(["A", "B", "C"])
    if "data_column2" in updates:
        row["data_column2"] = np.random.randint(1, 101)
    if "data_column3" in updates:
        row["data_column3"] = date_before_given_date(row["update_date"])
    return row


def produce_data(num_rows, pkey_start, file_name, year, month):
    """Create a DataFrame with specified characteristics."""
    df = pd.DataFrame(
        {
            "primary_key": range(pkey_start + 1, pkey_start + num_rows + 1),
            "source_file": [file_name] * num_rows,
            "update_date": [
                random_date_in_year_month(year, month) for _ in range(num_rows)
            ],
            "update_type": ["INSERT"] * num_rows,
            "snapshot_date": (
                datetime(year, month + 1, 1) - timedelta(days=1)
                if month
                else datetime(year, 12, 31)
            ),
            "data_column1": np.random.choice(["A", "B", "C"], num_rows),
            "data_column2": np.random.randint(1, 101, num_rows),
            "data_column3": [
                date_before_given_date(random_date_in_year_month(year, month))
                for _ in range(num_rows)
            ],
        }
    )
    return df


def produce_delta(df, file_name, year, month):
    """Generate a delta DataFrame based on random updates to a subset of rows and new rows."""
    # Select 10 random rows and create updates
    delta_indices = np.random.choice(df.index, 10, replace=False)
    df_delta = df.loc[delta_indices].copy()

    df_delta["source_file"] = file_name
    df_delta["update_date"] = [
        random_date_in_year_month(year, month) for _ in range(10)
    ]
    df_delta["update_type"] = "UPDATE"
    df_delta["snapshot_date"] = datetime(year, month + 1, 1) - timedelta(days=1)
    df_delta = df_delta.apply(update_row, axis=1)

    # Generate 10 new rows
    new_rows = produce_data(10, df["primary_key"].max(), file_name, year, month)
    df_delta = pd.concat([df_delta, new_rows], ignore_index=True)

    return df_delta


def merge_delta(df, df_delta):
    """Merge the original DataFrame with updates and new rows from the delta DataFrame."""
    df_combined = pd.concat([df, df_delta]).drop_duplicates("primary_key", keep="last")
    df_combined["data_column2"] = df_combined["data_column2"].astype(int)
    return df_combined.sort_values("primary_key").reset_index(drop=True)


# Example usage
df_a = produce_data(50, 0, "FileA", 2023, None)
df_delta_b = produce_delta(df_a, "FileB", 2024, 1)
df_snapshot_b = merge_delta(df_a, df_delta_b)

df_delta_c = produce_delta(df_snapshot_b, "FileC", 2024, 2)
df_snapshot_c = merge_delta(df_snapshot_b, df_delta_c)

print(df_a)
print(df_delta_b)
print(df_snapshot_b)

# To produce our simple staging database, we union df_a, with df_delta_b, and df_delta_c
staging_database = pd.concat([df_a, df_delta_b, df_delta_c], ignore_index=True)

# We add etl_run_timestamp columns, which are one more than the snapshot date
staging_database["etl_run_timestamp"] = staging_database["snapshot_date"] + timedelta(
    days=2, hours=9
)

print(staging_database)

staging_database.to_csv(
    "db_monitoring/mock_data/staging_database__table.csv", index=False
)
