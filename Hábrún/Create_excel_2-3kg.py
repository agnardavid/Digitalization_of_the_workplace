### This needs to be changed and updated so that each file it creates takes a look at the number and type of fish
### Instead of using counters stored in csv

import pathlib
import os
import shutil
from Data_conversion import CSV_Data_Conversion
from tempfile import NamedTemporaryFile

def main():

    # folderpath and grandpath of the script
    filepath, grandpath = get_filepath()
    
    show_file(grandpath)
    
    script_data_folder = f"{grandpath}/Script_data"

    # Path to the counter file from the script location
    counter_file = f"{grandpath}/Script_data/counter.csv"

    # Path to the templates from the script location
    template_path = f"{grandpath}/Templates"

    # Template name
    template_name = "2-3kg_Hábrún"
    
    # Template name without special characters
    template_name_without_special_characters = "2-3kg_Habrun"

    # Where is the template name going to be in the dataframe? top line is index 0
    front_row_number = "2"

    # The pallet number that the excel is going to have
    pallet_number, pallet_number_dict = get_pallet_number(template_name_without_special_characters, counter_file)

    create_excel_copy(f"{template_path}", filepath, f"{template_name}_H{pallet_number}.xlsx", template_name)

    update_csv(pallet_number_dict, script_data_folder, counter_file)
    
    hide_file(grandpath)

def hide_file(grandpath:str):
    # Needs to be placed in a path without spaces to work
    os.system(f"attrib +h {grandpath}/Script_data/counter.csv")
    os.system(f"attrib +h {grandpath}/Script_data")

def show_file(grandpath:str):
    # Needs to be placed in a path without spaces to work
    os.system(f"attrib +h {grandpath}/Script_data")
    os.system(f"attrib +h {grandpath}/Script_data/counter.csv")

def get_filepath() -> tuple[str,str]:
    # get the filepath and return the correct format
    filepath = pathlib.Path(__file__).parent.resolve()
    grandpath = os.path.dirname(filepath)
    return str(filepath).replace('\\', '/'), str(grandpath).replace('\\', '/')

def get_pallet_number(dict_key, path_to_counter_csv) -> str:

    # check the existing filename in the path to see the pallet number, we could also automatically change the pallet number
    # within the copy to match the filename
    # we also need to check the folder and see if all excels are finished or not, if all are finished, then we need to automatically
    # create the next one.

    pallet_number_dict = {}
    filestream = open_file(path_to_counter_csv)

    for line in filestream:
        stripped_line = line.strip()
        line_list = stripped_line.split(",")
        

        if line_list[0] == dict_key:
            current_version = int(line_list[1])
            pallet_number_dict[dict_key] = current_version + 1
          
        if line_list[0] != dict_key:
            pallet_number_dict[line_list[0]] = line_list[1]
        
    return pallet_number_dict[dict_key], pallet_number_dict

def update_csv(dict_to_write_csv:dict, script_data_folder:str, csv_path:str):
    CSV_Data_Conversion(csv_path).update_csv(dict_to_write_csv, script_data_folder)
    
def open_file(name):
    with open(name, encoding="utf8") as filestream:
        return filestream.readlines()

def create_excel_copy(template_path, new_folder_directory, new_name, old_name):
    
    if os.path.isfile(f"{new_folder_directory}/{new_name}"):
        print(f"The file already exists in this directory {new_folder_directory}/{new_name}")
    else:
        shutil.copy(f"{template_path}/{old_name}.xlsx", new_folder_directory)
        os.rename(f"{new_folder_directory}/{old_name}.xlsx", f"{new_folder_directory}/{new_name}")

if __name__ == "__main__":
    main()