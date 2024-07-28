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

# Open the original CSV file and the new file where we'll save the cleaned data
with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile, \
     open(cleaned_file_path, mode='w', newline='', encoding='utf-8') as cleaned_csvfile:
    
    # Create a CSV reader and writer
    csv_reader = csv.DictReader(csvfile)
    csv_writer = csv.DictWriter(cleaned_csvfile, fieldnames=relevant_columns)
    
    # Write the header to the cleaned CSV
    csv_writer.writeheader()
