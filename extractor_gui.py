import FreeSimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("Black")

layout = [[sg.Text("Select Archive:"), sg.InputText(key="file_input"), sg.FileBrowse("Choose", key="file")],
          [sg.Text("Select Directory:"), sg.InputText(key="file_dest"), sg.FolderBrowse("Choose", key="folder")],
          [sg.Button("Extract"), sg.Button("Exit"), sg.Text(key="output", text_color="Green")]]

window = sg.Window("Archive Extractor", layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    
    archive_path = values["file"]
    file_dest = values['folder']
    extract_archive(archive_path, file_dest)
    window["output"].update("Extraction Completed!")    
window.close()
