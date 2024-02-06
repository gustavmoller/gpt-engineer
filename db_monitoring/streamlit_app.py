import streamlit as st
import json
import pandas as pd
from metrics.counts import *
from metrics.checks import *
from metrics.tables import *
from metrics.plots import *

# Load database configuration and mock data for local development
with open("database_config.json") as config_file:
    config = json.load(config_file)
    database_tables = config["local_data"]

# Streamlit UI components
st.title("Athena Database Monitoring Dashboard")

# Database selection dropdown
selected_database = st.selectbox("Select a database:", list(database_tables.keys()))

# Table selection dropdown
tables = list(database_tables[selected_database].keys())
selected_table = st.selectbox("Select a table:", tables)

# Select metrics
table_metrics = database_tables[selected_database][selected_table]

# Display metrics based on the selected database configuration
if "checks" in table_metrics:
    st.header("Checks")
    checks_dict = {}
    for check in table_metrics["checks"]:
        function = globals()[check]
        result = function(selected_database, selected_table)
        checks_dict[check] = "✅" if result else "❌"
    # Convert the dictionary to a DataFrame
    checks_table = pd.DataFrame.from_dict(checks_dict, orient="index").reset_index()
    checks_table.columns = ["Check", "Result"]
    st.dataframe(checks_table)

if "counts" in table_metrics:
    st.header("Counts")
    counts_dict = {}
    for count in table_metrics["counts"]:
        function = globals()[count]
        counts_dict[count] = function(selected_database, selected_table)
    # Convert the dictionary to a DataFrame
    counts_table = pd.DataFrame.from_dict(counts_dict, orient="index").reset_index()
    counts_table.columns = ["Count", "Value"]
    st.dataframe(counts_table)

if "tables" in table_metrics:
    st.header("Tables")
    for table in table_metrics["tables"]:
        function = globals()[table]
        st.subheader(table)
        st.dataframe(function(selected_database, selected_table))

if "plots" in table_metrics:
    st.header("Plots")
    for plot in table_metrics["plots"]:
        function = globals()[plot]
        fig = function(selected_database, selected_table)
        st.plotly_chart(fig)
