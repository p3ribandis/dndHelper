import pygsheets as pyg

class keyboard_creator:
    
    def get_sheets_names():
        gc = pyg.authorize(service_account_file="project/mypython_secret_id.json")
        sh = gc.open('pythonTest')
        wks = sh.worksheets()
        names = []
        for w in wks:
            names.append(w.title)
        return names

