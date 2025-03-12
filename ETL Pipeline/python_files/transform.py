import pandas as pd
import numpy as np

def transform(patients_df, admissions_df, readmissions_df, hospital_capacity_df):
    # Handling Missing Values
    patients_df.fillna({"gender": "Unknown", "zip_code": "00000"}, inplace=True)
    admissions_df.fillna({"discharge_date": np.nan, "length_of_stay": 0, "department": "Unknown"}, inplace=True)
    readmissions_df.fillna({"readmission_reason": "Unknown", "department": "Unknown"}, inplace=True)
    hospital_capacity_df.fillna({"occupied_beds": 0, "total_beds": np.nan}, inplace=True)
    
    # Fix Data Types
    patients_df["dob"] = pd.to_datetime(patients_df["dob"], errors='coerce')
    admissions_df["admission_date"] = pd.to_datetime(admissions_df["admission_date"], errors='coerce')
    admissions_df["discharge_date"] = pd.to_datetime(admissions_df["discharge_date"], errors='coerce')
    readmissions_df["readmission_date"] = pd.to_datetime(readmissions_df["readmission_date"], errors='coerce')
    hospital_capacity_df["date"] = pd.to_datetime(hospital_capacity_df["date"], errors='coerce')
    
    # Remove Duplicates
    patients_df.drop_duplicates(inplace=True)
    admissions_df.drop_duplicates(inplace=True)
    readmissions_df.drop_duplicates(inplace=True)
    hospital_capacity_df.drop_duplicates(inplace=True)
    
    # Correct Invalid Data
    admissions_df.loc[admissions_df["length_of_stay"] < 0, "length_of_stay"] = np.nan
    hospital_capacity_df.loc[hospital_capacity_df["occupied_beds"] < 0, "occupied_beds"] = np.nan
    hospital_capacity_df.loc[hospital_capacity_df["total_beds"] < 0, "total_beds"] = np.nan
    
    # Remove ER Visits as it is not in the new CSV files
    # er_visits_df is no longer used since you removed ER Visits from the dataset
    
    return patients_df, admissions_df, readmissions_df, hospital_capacity_df
