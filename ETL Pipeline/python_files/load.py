from sqlalchemy import create_engine, text
import pandas as pd

DATABASE_URL = "postgresql://postgres:string1@localhost:5432/hospital_operations"

def create_tables(engine):
    """Create required tables in the PostgreSQL database."""
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS patients (
                patient_id SERIAL PRIMARY KEY,
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                gender VARCHAR(50),
                dob DATE,
                zip_code VARCHAR(20)
            );
        """))
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS admissions (
                admission_id SERIAL PRIMARY KEY,
                patient_id INT REFERENCES patients(patient_id) ON DELETE CASCADE,
                admission_date TIMESTAMP,
                discharge_date TIMESTAMP,
                length_of_stay INT,
                diagnosis_code VARCHAR(50),
                department VARCHAR(100),
                discharge_type VARCHAR(50),
                bed_occupied BOOLEAN,
                readmission_flag BOOLEAN,
                admission_month DATE
            );
        """))
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS readmissions (
                readmission_id SERIAL PRIMARY KEY,
                patient_id INT REFERENCES patients(patient_id) ON DELETE CASCADE,
                original_admission_id INT REFERENCES admissions(admission_id) ON DELETE CASCADE,
                readmission_date TIMESTAMP,
                readmission_reason TEXT,
                diagnosis_code VARCHAR(50),
                department VARCHAR(100)
            );
        """))
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS hospital_capacity (
                date DATE PRIMARY KEY,
                occupied_beds INT,
                total_beds INT
            );
        """))
        print("✅ Tables created successfully.")

def load_to_postgresql(patients_df, admissions_df, readmissions_df, hospital_capacity_df):
    """Load transformed data into PostgreSQL."""
    engine = create_engine(DATABASE_URL)
    create_tables(engine)

    with engine.begin() as conn:
        patients_df.to_sql('patients', conn, if_exists='append', index=False)
        admissions_df.to_sql('admissions', conn, if_exists='append', index=False)
        readmissions_df.to_sql('readmissions', conn, if_exists='append', index=False)
        hospital_capacity_df.to_sql('hospital_capacity', conn, if_exists='append', index=False)

    print("✅ Data loaded successfully.")
