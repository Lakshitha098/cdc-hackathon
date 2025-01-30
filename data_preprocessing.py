import pandas as pd
import openpyxl  # Import openpyxl for more robust sheet handling
import re

file_path = 'C:/Users/laksh/OneDrive/Documents/IPCC-AR6-SYR-SPM4-Panel(a)-LR-F3-3-Panel(a)(linear-graph).xlsx'

try:

    workbook = openpyxl.load_workbook(file_path)
    sheet_names = workbook.sheetnames
    print(f"Available sheet names (from openpyxl): {sheet_names}")

    metadata = pd.read_excel(file_path, sheet_name='Metadata', nrows=20)

    note_column = None
    for col in metadata.columns:
        if metadata[col].dtype == 'object' and any(re.search(r"The sheet.*contains.*observed", str(x).lower()) for x in metadata[col].dropna()):  # More general regex
            note_column = col
            break

    if note_column is None:

        raise ValueError(f"Could not find the column containing the data sheet note in metadata. Available columns: {list(metadata.columns)}")

    note = metadata[note_column].iloc[0]

    # 4. Extract the data sheet name:
    if isinstance(note, str) and "The sheet" in note.lower() and "contains" in note.lower():  # Check for "contains"
        start = note.find('"') + 1
        end = note.find('"', start)
        data_sheet_name = note[start:end]
        print(f"Identified data sheet: {data_sheet_name}")
    else:
        raise ValueError("Could not find data sheet name in metadata.")

    # 5. Read the data sheet:
    data = pd.read_excel(file_path, sheet_name=data_sheet_name)

    print(data.head())
    print(data.info())



    print(data.head())

    

except FileNotFoundError:
    print(f"Error: File not found at path: {file_path}")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit()