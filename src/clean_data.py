import csv

# Define the CSV file paths
file_path = r"C:\Users\025445\Desktop\Tableau Projects\Side Projects\Disability\DHDS_-_Prevalence_of_Disability_Status_and_Types_20240721.csv"
cleaned_file_path = r"C:\Users\025445\Desktop\Tableau Projects\Side Projects\Disability\disability_data_clean.csv"

relevant_columns = [
    "Year",
    "LocationAbbr",
    "LocationDesc",
    "Indicator",
    "Response",
    "Data_Value_Unit",
    "Data_Value_Type",
    "Data_Value",
    "Number",
    "WeightedNumber",
    "Low_Confidence_Limit",
    "High_Confidence_Limit",
    "StratificationCategory1",
    "Stratification1"
]
