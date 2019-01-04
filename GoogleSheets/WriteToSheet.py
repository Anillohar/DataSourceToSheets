from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from ConnectingToMssql import ReadingTextFile

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

# The ID and range of a sample spreadsheet.
spreadsheet_id = "1JoHk73ptz0AgL3CsQXVSEASxYoLpcW2_ig7mGMUlT_0"
range_name = 'A9:B1'

store = file.Storage('token.json')
credentials = store.get()

if not credentials or credentials.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    credentials = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=credentials.authorize(Http()))


value_input_option = 'USER_ENTERED'

data = ReadingTextFile.reading_file('test')

values = [
            data
         ]
body = {
    'values': values
}

sheet = service.spreadsheets()
result = sheet.values().append(spreadsheetId=spreadsheet_id, range=range_name, valueInputOption=value_input_option,
                               body=body).execute()
print('{0} cells updated.' + format(result.get('updatedCells')))
