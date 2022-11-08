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
    
    def getColor():
        wks = pygsheetsExt.sh.worksheet_by_title('Карапакс')
        col = wks.get_col(1, returnas='matrix', include_tailing_empty=False)
        r = random.randint(0, len(col)-1)
        res = col[r]
        return res
        