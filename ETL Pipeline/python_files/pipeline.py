from python_files.extract import extract
from python_files.transform import transform
from python_files.load import load_to_postgresql
from python_files.drop_tables import drop_all_tables
import pandas as pd

def run_etl_pipeline():
    """Run the full ETL process."""
    print("🚀 Starting ETL pipeline...")

    # Drop existing tables before loading new data
    drop_all_tables()

    # Extract data
    patients_df, admissions_df, readmissions_df, hospital_capacity_df = extract()
    print("📥 Data extracted.")

    # Transform data
    patients_df, admissions_df, readmissions_df, hospital_capacity_df = transform(
        patients_df, admissions_df, readmissions_df, hospital_capacity_df
    )
    print("🔧 Data transformed.")

    # Load data into database
    load_to_postgresql(patients_df, admissions_df, readmissions_df, hospital_capacity_df)
    print("✅ ETL pipeline completed successfully!")

if __name__ == "__main__":
    run_etl_pipeline()
