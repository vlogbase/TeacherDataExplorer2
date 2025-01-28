import os
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

def get_database_url():
    """Get the database URL from environment variables."""
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        raise ValueError("DATABASE_URL environment variable is not set")
    return db_url

def create_engine_with_retries():
    """Create SQLAlchemy engine with proper settings."""
    db_url = get_database_url()
    print(f"Creating database engine with URL (redacted credentials)...")
    return create_engine(
        db_url,
        pool_pre_ping=True,
        pool_recycle=300
    )

def init_db():
    """Initialize the database and create necessary tables."""
    try:
        engine = create_engine_with_retries()

        # Drop sequence if it exists to avoid the unique constraint violation
        with engine.connect() as conn:
            conn.execute(text("DROP SEQUENCE IF EXISTS teachers_id_seq CASCADE"))
            conn.execute(text("DROP TABLE IF EXISTS teachers CASCADE"))
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
            print("Database initialized successfully")
    except SQLAlchemyError as e:
        print(f"Error initializing database: {str(e)}")
        raise

def load_csv_to_db(data):
    """Load data into the database. Accepts either a DataFrame or a file path."""
    try:
        # Handle both DataFrame and file path inputs
        if isinstance(data, str):
            print(f"Reading CSV file from: {data}")
            df = pd.read_csv(data)
        else:
            print("Using provided DataFrame")
            df = data

        # Clean column names
        df.columns = df.columns.str.strip()

        # Convert date columns
        df['Date of Birth'] = pd.to_datetime(df['Date of Birth'], errors='coerce')

        # Create database connection
        engine = create_engine_with_retries()

        # Load data into database
        print("Loading data into database...")
        df.to_sql('teachers', engine, if_exists='replace', index=False)
        print("Data loaded successfully")

        return True
    except Exception as e:
        print(f"Error loading data to database: {str(e)}")
        return False

def get_dataframe():
    """Get all teacher data as a pandas DataFrame."""
    try:
        engine = create_engine_with_retries()
        print("Retrieving data from database...")
        return pd.read_sql_table('teachers', engine)
    except SQLAlchemyError as e:
        print(f"Error reading from database: {str(e)}")
        return pd.DataFrame()