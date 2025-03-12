import pandas as pd

def extract():
    # Load cleaned data
    patients_df = pd.read_csv("data/patients.csv")
    admissions_df = pd.read_csv("data/modified_admissions.csv")
    readmissions_df = pd.read_csv("data/modified_readmissions.csv")
    hospital_capacity_df = pd.read_csv("data/modified_hospital_capacity.csv")

    return patients_df, admissions_df, readmissions_df, hospital_capacity_df
