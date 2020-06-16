import os
import shutil
from threading import Timer

folder_to_track = r"C:\Users\RON\Downloads"
textfile_folder_destination = r"D:\move_file\text_file"
exefile_folder_destination = r"D:\move_file\exe_File"
picfile_folder_destination = r"D:\move_file\pic_File"
xlsfile_folder_destination = r"D:\move_file\xls_File"
docfile_folder_destination = r"D:\move_file\doc_File"

os.chdir(folder_to_track)

def move_files():
    for filename in os.listdir(folder_to_track):
        if os.path.isfile(filename):
            
            if filename.endswith('.txt'):
                shutil.move(filename, textfile_folder_destination)

            elif filename.endswith('.msi') | filename.endswith('.exe'):
                shutil.move(filename, exefile_folder_destination)

            elif filename.endswith('.png' ) | filename.endswith('.jpg'):
                shutil.move(filename, picfile_folder_destination)

            elif filename.endswith('.xlsx'):
                shutil.move(filename, xlsfile_folder_destination)

            elif filename.endswith('.docx'):
                shutil.move(filename, docfile_folder_destination)

            else:
                pass
    
    Timer(2, move_files).start()

if __name__ == "__main__":
    try:
        move_files()
    except:
        pass