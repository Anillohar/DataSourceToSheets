from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID is present in URL of your spreadsheet and range of a sample spreadsheet is range which you want to read.
SAMPLE_SPREADSHEET_ID = '1JoHk73ptz0AgL3CsQXVSEASxYoLpcW2_ig7mGMUlT_0'
SAMPLE_RANGE_NAME = 'A9:B1'


def main():

    # The file token.json stores the user's access it's automatically created
    # when authorization flow compeletes first time
    store = file.Storage('token.json')
    credentials = store.get()

    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)

    service = build('sheets', 'v4', http=credentials.authorize(Http()))

    # Calling the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('Nothing in the spreadsheet, check if the data exists in given Range.')
    else:
        print('Name, Major:')
        for i in values:
            print('%s' %i)


if __name__ == '__main__':
    main()

