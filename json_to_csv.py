import json
import csv
import gspread
from google.oauth2.service_account import Credentials

# Constants for file paths and Google Sheets
PERMISSIONS_FILE = 'permissions.json'

# Google service account credential
CREDENTIALS_FILE = 'credentials.json'
OUTPUT_CSV_FILE = 'output.csv'
SPREADSHEET_ID = '1dOHHogF4wgu4stGXcl_coS5vQ-FmS4D_6YYrdUXHT3Y' 

# Define permission weights to control the column order
# Ensure the columns are displayed in the same order as in the example
PERMISSION_WEIGHTS = {
    'view_grades': 1,
    'change_grades': 2,
    'add_grades': 3,
    'delete_grades': 4,
    'view_classes': 5,
    'change_classes': 6,
    'add_classes': 7,
    'delete_classes': 8
}
DEFAULT_WEIGHT = max(PERMISSION_WEIGHTS.values()) + 1

def load_permissions_data():
    """Load permissions data from the JSON file."""
    try:
        with open(PERMISSIONS_FILE, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error in 'load_permissions_data': {e}")
        raise

def prepare_data_rows(data):
    """Prepare the header and rows for output based on the permission weights."""
    try:
        # Extract all unique permissions from the data
        all_permissions = set()
        for perms in data.values():
            all_permissions.update(perms)

        # Assign weights to all permissions
        permissions_with_weights = []
        for perm in all_permissions:
            weight = PERMISSION_WEIGHTS.get(perm, DEFAULT_WEIGHT)
            permissions_with_weights.append((weight, perm))

        # Sort permissions based on weights
        permissions_with_weights.sort()

        # Build the ordered permissions list
        permissions_list = []
        for weight_perm_tuple in permissions_with_weights:
            perm = weight_perm_tuple[1]
            permissions_list.append(perm)

        # Prepare header
        header = [''] + permissions_list

        # Prepare data rows
        rows = [header]
        for user, perms in data.items():
            row = [user]
            for perm in permissions_list:
                row.append('1' if perm in perms else '0')
            rows.append(row)
        
        return rows
    except Exception as e:
        print(f"Error in 'prepare_data_rows': {e}")
        raise

def generate_local_csv(rows):
    """Generate a local CSV file from the data rows."""
    try:
        with open(OUTPUT_CSV_FILE, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(rows)
        print(f"Local CSV file '{OUTPUT_CSV_FILE}' has been generated.")
    except Exception as e:
        print(f"Error in 'generate_local_csv': {e}")
        raise

def update_google_sheet(rows):
    """Update the Google Sheet with the prepared data rows."""
    try:
        scope = ['https://www.googleapis.com/auth/spreadsheets']
        creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=scope)
        client = gspread.authorize(creds)
        sheet = client.open_by_key(SPREADSHEET_ID).sheet1
        sheet.update(rows)
        print(f"Google Sheet '{SPREADSHEET_ID}' has been updated.")
    except Exception as e:
        print(f"Error in 'update_google_sheet': {e}")
        raise

def main():
    try:
        # Load permissions data
        data = load_permissions_data()

        # Prepare data rows
        rows = prepare_data_rows(data)

        # Generate local CSV
        generate_local_csv(rows)

        # Update Google Sheet
        update_google_sheet(rows)

        print("All operations success!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
