import pygsheets
import numpy as np
import random

class pygsheetsExt:

    gc = pygsheets.authorize(service_account_file="project/mypython_secret_id.json")
    sh = gc.open('pythonTest')

    def example():
        # Open spreadsheet and then worksheet
        sh = pygsheetsExt.gc.open('pythonTest')
        wks = sh.sheet1

        # Update a cell with value (just to let him know values is updated ;) )
        wks.update_value('A1', "Hey yank this numpy array")
        my_nparray = np.random.randint(10, size=(3, 4))

        # update the sheet with array
        wks.update_values('A2', my_nparray.tolist())

         #share the sheet with your friend
        sh.share("yaroslav.nasarenko@gmail.com")

    def getData(sheetName):
        wks = pygsheetsExt.sh.worksheet_by_title(sheetName)
        col = wks.get_col(1, returnas='matrix', include_tailing_empty=False)
        r = random.randint(0, len(col)-1)
        res = col[r]
        return res

    def set_new_worksheet(name, content):
        wks = pygsheetsExt.sh.add_worksheet(name)
        for i in range(1, len(content), 2):
            wks.update_value(('A' + str(i if i < 2 else i - 1)), content[i].text)
        print('ready')
