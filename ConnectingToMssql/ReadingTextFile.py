# this file reads data from test.txt and passes it to sheets.py or WritingToSheets.py


def reading_file(filename):
    filename = 'test'
    with open('/home/da/PycharmProjects/DataSourceToSheets/ConnectingToMssql/'+filename+".txt", "r+") as f:
        file_content = list(f.read())
    return file_content
