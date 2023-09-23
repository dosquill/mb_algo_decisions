from googleapiclient.discovery import build
from google.oauth2 import service_account
import json

# mb-algorithm@form-endpoint.iam.gserviceaccount.com


folder_path = "db/google_sheet"
key_file_path = "key.json"

def google_service(spreadsheet_id, sheet_name, cell_range, file_path=None, return_values=False):
    credential_filepath = f"{folder_path}/{key_file_path}"    
    
    
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

    if return_values:
        return values

    # SERIALIZATION
    json_str = json.dumps(values, indent=4)

    with open(file_path, 'w') as json_file:
        json_file.write(json_str)

    print(f"Data saved to {file_path}")




