import pandas as pd
import numpy as np
from utils.db import get_dataframe, init_db, load_csv_to_db

def load_and_process_data(file_path):
    """Load and process the teachers dataset from database."""
    # Initialize database if needed
    init_db()

    # Check if we need to load CSV data
    df = get_dataframe()
    if df.empty:
        # Load CSV data into database if it's empty
        success = load_csv_to_db(file_path)
        if not success:
            raise Exception("Failed to load CSV data into database")
        df = get_dataframe()

    # Clean column names
    df.columns = df.columns.str.strip()

    # Convert date columns to datetime
    date_columns = ['Date of Birth']
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

    # Handle missing values
    df['NIN'] = df['NIN'].fillna('Not Provided')
    df['TRCN'] = df['TRCN'].fillna('Not Provided')
    df['Teaching Qualification'] = df['Teaching Qualification'].fillna('None')

    return df

def calculate_age(date_of_birth):
    """Calculate age from date of birth."""
    today = pd.Timestamp.now()
    return today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

def get_summary_stats(df, column):
    """Get summary statistics for a column."""
    return {
        'count': df[column].value_counts(),
        'percentage': df[column].value_counts(normalize=True) * 100
    }

def filter_dataframe(df, filters):
    """Apply filters to dataframe."""
    filtered_df = df.copy()
    for column, value in filters.items():
        if value:
            filtered_df = filtered_df[filtered_df[column] == value]
    return filtered_df