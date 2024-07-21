import FreeSimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("Black")
 
label1 = sg.Text("Select archive:")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")
 
label2 = sg.Text("Select destination directory:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")
 
extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")
 
col1 = sg.Column([[label1], [label2]])
col2 = sg.Column([[input1], [input2]])
col3 = sg.Column([[choose_button1], [choose_button2]])
 
window = sg.Window("Archive Extractor",
                   layout=[[col1, col2, col3], [extract_button]])

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    
    archive_path = values["file"]
    file_dest = values['folder']
    extract_archive(archive_path, file_dest)
    window["output"].update("Extraction Completed!")    
window.close()