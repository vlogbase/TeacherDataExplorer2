import os
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

def get_database_url():
    """Get the database URL from environment variables."""
    return os.getenv('DATABASE_URL')

def create_engine_with_retries():
    """Create SQLAlchemy engine with proper settings."""
    return create_engine(
        get_database_url(),
        pool_pre_ping=True,
        pool_recycle=300
    )

def init_db():
    """Initialize the database and create necessary tables."""
    engine = create_engine_with_retries()
    
    try:
        # Create teachers table
        with engine.connect() as conn:
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS teachers (
                    id SERIAL PRIMARY KEY,
                    "Date of Birth" DATE,
                    "Gender" VARCHAR(10),
                    "State of Origin" VARCHAR(50),
                    "LGA" VARCHAR(50),
                    "Employment Type" VARCHAR(50),
                    "Grade Level" VARCHAR(20),
                    "Years in Current School" INTEGER,
                    "Teaching Qualification" VARCHAR(100),
                    "Highest Academic Qualification" VARCHAR(100),
                    "TRCN" VARCHAR(50),
                    "Subjects Taught" TEXT,
                    "Marital Status" VARCHAR(20),
                    "NIN" VARCHAR(50)
                )
            """))
            conn.commit()
    except SQLAlchemyError as e:
        print(f"Error creating tables: {str(e)}")
        raise

def load_csv_to_db(csv_path):
    """Load CSV data into the database."""
    try:
        # Read CSV file
        df = pd.read_csv(csv_path)
        
        # Clean column names
        df.columns = df.columns.str.strip()
        
        # Convert date columns
        df['Date of Birth'] = pd.to_datetime(df['Date of Birth'], errors='coerce')
        
        # Create database connection
        engine = create_engine_with_retries()
        
        # Load data into database
        df.to_sql('teachers', engine, if_exists='replace', index=False)
        
        return True
    except Exception as e:
        print(f"Error loading CSV to database: {str(e)}")
        return False

def get_dataframe():
    """Get all teacher data as a pandas DataFrame."""
    engine = create_engine_with_retries()
    try:
        return pd.read_sql_table('teachers', engine)
    except SQLAlchemyError as e:
        print(f"Error reading from database: {str(e)}")
        return pd.DataFrame()
