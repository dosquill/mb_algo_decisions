from googleapiclient.discovery import build
from google.oauth2 import service_account
import json


def google_service(spreadsheet_id, sheet_name, cell_range, file_path):
    credential_filepath = "google_sheet\key.json"    
    
    credentials = service_account.Credentials.from_service_account_file(
        credential_filepath, 
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
        )
    
    service = build("sheets", "v4", credentials=credentials)

    request = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=f'{sheet_name}!{cell_range}'
    )

    result = request.execute()    
    values = result.get('values', [])

    # SERIALIZATION
    json_str = json.dumps(values, indent=4)

    with open(file_path, 'w') as json_file:
        json_file.write(json_str)

    print(f"Data saved to {file_path}")




