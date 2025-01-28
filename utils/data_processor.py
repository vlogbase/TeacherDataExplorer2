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
        # Load both original and new data
        original_df = pd.read_csv("attached_assets/merged_teachers_data.csv")
        new_df = pd.read_csv("attached_assets/combined_data.csv")

        # Combine the datasets
        combined_df = pd.concat([original_df, new_df], ignore_index=True)

        # Clean gender data
        combined_df['Gender'] = combined_df['Gender'].str.lower()
        combined_df['Gender'] = combined_df['Gender'].apply(
            lambda x: x if x in ['male', 'female'] else None
        )

        # Save combined data to database
        success = load_csv_to_db(combined_df)
        if not success:
            raise Exception("Failed to load combined data into database")
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
    df['Gender'] = df['Gender'].fillna('Not Specified')

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