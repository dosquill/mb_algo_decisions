from googleapiclient.discovery import build
from google.oauth2 import service_account
import os
import json


# google_json = os.environ.get('google_credentials')
# INPUT
spreadsheet_id = "1Fl8tSpBjKQt4yn2CFlC-i-Lg948PbtCksaRNQW4r9rw"
credential_filepath = "service\key.json"
# mb-algorithm@form-endpoint.iam.gserviceaccount.com
sheet_name = "risposte_form"
cell_range = "A:Z"


def main():
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

    with open('service/risposte_form.json', 'w') as json_file:
        json_file.write(json_str)

    print(f"Data saved to sheet_data.json")


    #for row in values:
    #    print(row)



if __name__ == '__main__':
    main()