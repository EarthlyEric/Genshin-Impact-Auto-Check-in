from colored import fg,attr
from InquirerPy import inquirer

saveFilename=inquirer.filepath(message='hi',vi_mode=True).execute()
