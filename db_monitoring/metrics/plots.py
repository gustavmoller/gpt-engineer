import pandas as pd
from functions.sql_query import sql_query
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def display_bar_chart(database: str, table: str, column: str):
    query = f"""
    SELECT {column}, count(*) as count
    FROM {database}.{table}
    GROUP BY {column}
    ORDER BY {column}
    """
    df = sql_query(query, database, table)

    # Create a bar chart using matplotlib
    fig, ax = plt.subplots()
    ax.bar(df[column], df["count"])
    ax.set_xlabel(column)
    ax.set_ylabel("Count")
    ax.set_title(f"Counts per {column}")

    return fig


def display_bar_chart_data_column1(database: str, table: str):
    """
    Create bar chart of counts per data_colum1
    """
    return display_bar_chart(database, table, "data_column1")


def display_bar_chart_data_snapshot(database: str, table: str):
    """
    Create bar chart of counts per snapshot
    """
    return display_bar_chart(database, table, "snapshot_date")


def display_scatter_plot(
    database: str, table: str, column1: str, column2: str, column3: str
):
    # Assuming sql_query is a function that returns a DataFrame based on a SQL query
    df = sql_query(
        f"SELECT {column1}, {column2}, {column3} FROM {database}.{table}",
        database,
        table,
    )

    # Ensure column3 is a datetime type
    df[column3] = pd.to_datetime(df[column3])

    # Sort DataFrame by the date to ensure the legend matches the color gradient
    df.sort_values(by=column3, inplace=True)

    # Convert dates to numbers for coloring
    date_num = mdates.date2num(df[column3])

    # Normalize the date_num array for color mapping
    norm = plt.Normalize(date_num.min(), date_num.max())

    # Create a scatter plot using matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))  # Larger figure size
    scatter = ax.scatter(
        df[column1], df[column2], c=date_num, cmap="viridis", norm=norm
    )

    # Create colorbar as legend, manually handling date formatting
    cbar = fig.colorbar(scatter, ax=ax)
    cbar.ax.yaxis.set_major_locator(mdates.AutoDateLocator())
    cbar.ax.yaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    # Set labels with improved font sizes
    ax.set_xlabel(column1, fontsize=12)
    ax.set_ylabel(column2, fontsize=12)
    ax.set_title(f"{column1} vs {column2} stratified by {column3}", fontsize=14)

    # Set grid
    ax.grid(True, which="both", linestyle="--", linewidth=0.5)

    # Improve tick marks
    ax.tick_params(axis="both", which="major", labelsize=10)

    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to prevent overlap

    return fig


def display_scatter_plot_example(database: str, table: str):
    return display_scatter_plot(
        database, table, "data_column2", "data_column3", "snapshot_date"
    )
