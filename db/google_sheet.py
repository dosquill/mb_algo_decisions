from googleapiclient.discovery import build
from google.oauth2 import service_account
import json


# mb-algorithm@form-endpoint.iam.gserviceaccount.com


# INPUT
spreadsheet_id = "1Fl8tSpBjKQt4yn2CFlC-i-Lg948PbtCksaRNQW4r9rw"
sheet_name = "risposte_form"
cell_range = "A:Z"



def google_sheet_service(spreadsheet_id, sheet_name, cell_range):
    credential_filepath = "db\google_sheets\key.json"    
    
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

    with open('./db/google_sheets/risposte_form.json', 'w') as json_file:
        json_file.write(json_str)

    print(f"Data saved to sheet_data.json")





if __name__ == '__main__':
    google_sheet_service(spreadsheet_id, sheet_name, cell_range)