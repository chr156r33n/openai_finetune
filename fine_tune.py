import streamlit as st
import csv
import json
import pandas as pd
import io

def csv_to_jsonl(csv_data):
    json_lines = []
    reader = csv.DictReader(io.StringIO(csv_data))
    for row in reader:
        json_line = {
            "messages": [
                {"role": "system", "content": row['system']},  # Use the system prompt from the CSV
                {"role": "user", "content": row['user']},
                {"role": "assistant", "content": row['assistant']}
            ]
        }
        json_lines.append(json.dumps(json_line))
    return "\n".join(json_lines)

# Streamlit app
st.title("CSV to JSONL Converter")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file
    csv_data = uploaded_file.getvalue().decode("utf-8")
    
    # Convert CSV to JSONL
    jsonl_output = csv_to_jsonl(csv_data)
    
    # Create a download link for the JSONL file
    st.download_button(
        label="Download JSONL",
        data=jsonl_output,
        file_name="output.jsonl",
        mime="application/json"
    )
