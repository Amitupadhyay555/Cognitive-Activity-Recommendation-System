import sys
import os

# Ensure backend directory is in the sys.path (this is required if you're running preprocess.py from the root)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'backend')))

import pandas as pd
import re
import json
import logging

from database import get_session, Activity  # Now import using just 'database' and 'Activity'

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Get the base directory (project root)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Use relative paths based on the base directory
file_path = os.path.join(base_dir, "../data/Dataset.xlsx")
processed_data_path = os.path.join(base_dir, "../data/processed_data.json")

# Load dataset
df = pd.read_excel(file_path, sheet_name="Sheet1")

# Standardize column names
df.rename(columns={
    "Activity name": "name",
    "Activity description": "description",
    "Zone": "zone",
    "Time": "time_required",
    "Age": "age_range"
}, inplace=True)

# Handle missing values
df["time_required"] = df["time_required"].fillna(0)
df["zone"] = df["zone"].fillna("Unknown")
df["age_range"] = df["age_range"].fillna("Unknown")

# Convert time to numeric format
def extract_time(time_str):
    match = re.findall(r'\d+', str(time_str))
    if match:
        times = list(map(int, match))
        return sum(times) // len(times)
    return None

df["time_required"] = df["time_required"].apply(extract_time)

# Extract cognitive category
def get_category(row):
    if "Memory" in row and row["Memory"] == "Yes":
        return "Memory"
    elif "Reasoning" in row and row["Reasoning"] == "Yes":
        return "Reasoning"
    elif "Association" in row and row["Association"] == "Yes":
        return "Association"
    elif "Visualization" in row and row["Visualization"] == "Yes":
        return "Visualization"
    return "General"

df["category"] = df.apply(get_category, axis=1)

# Save processed data
df.to_json(processed_data_path, orient="records", indent=4)
logging.info(f"Processed data saved to {processed_data_path}")

# Insert processed data into database
session = get_session()
for _, row in df.iterrows():
    activity = Activity(
        name=row["name"],
        description=row["description"],
        zone=row["zone"],
        time_required=row["time_required"],
        age_range=row["age_range"],
        category=row["category"]
    )
    session.add(activity)

session.commit()
session.close()
logging.info("Data successfully inserted into the database")
