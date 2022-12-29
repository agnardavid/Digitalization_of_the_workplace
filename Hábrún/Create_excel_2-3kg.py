### This needs to be changed and updated so that each file it creates takes a look at the number and type of fish
### Instead of using counters stored in csv

import pathlib
import os
import shutil
from csv import DictReader, DictWriter, unix_dialect
from tempfile import NamedTemporaryFile

def main():

    filepath, grandpath = get_filepath()
    #Excel creation
    show_file(grandpath)
    # current_date = get_current_date()
    script_data_folder = f"{grandpath}/Script_data"
    template_path = f"{grandpath}/Templates"
    template_name = "2-3kg_Hábrún"
    pallet_number = get_pallet_number(template_name, script_data_folder)
    update_file({template_name:pallet_number}, script_data_folder, template_name)
    
    create_excel_copy(f"{template_path}", filepath, f"{template_name}_H{pallet_number}.xlsx", template_name)
    hide_file(grandpath)

def hide_file(grandpath:str):
    os.system(f"attrib +h {grandpath}/Script_data")
    os.system(f"attrib +h {grandpath}/Script_data/counter.csv")

def show_file(grandpath:str):
    os.system(f"attrib +h {grandpath}/Script_data")
    os.system(f"attrib +h {grandpath}/Script_data/counter.csv")

def get_filepath():
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
        line_list = line.split(",")

        if line_list[0] == dict_key:
            current_version = int(line_list[1])
            pallet_number_dict[dict_key] = current_version + 1
          
        if line_list[0] != dict_key:
            pallet_number_dict[line_list[0]] = int(line_list[1])
        
    return int(pallet_number_dict[dict_key])

def update_file(updated_data: dict, filepath, dict_key) -> None:
    """Updates data in a row whose ID column matches the id in the passed dict.
       Adds the data no row with the same ID exists already.
    Args:
        updated_data (dict): A dictionary with data to update or write.
                             Keys in the dict must match values in counter.csv
    """
    
    tempfile = NamedTemporaryFile("w+t", newline="", delete=False, encoding="utf-8")
    
    with open(filepath, mode="r+", newline="", encoding="utf-8") as csv_file, tempfile:
        reader = DictReader(csv_file, unix_dialect)
        writer = DictWriter(tempfile, unix_dialect)
        writer.writeheader()
        for row in reader:
            if row[0] == dict_key:
                row = updated_data
                
            writer.writerow(row)
        csv_file.flush()
        tempfile.flush()
    shutil.move(tempfile.name, filepath)
    
def open_file(name):
    with open(name) as filestream:
        return filestream.readlines()

def create_excel_copy(template_path, new_folder_directory, new_name, old_name):
    
    if os.path.isfile(f"{new_folder_directory}/{new_name}"):
        print(f"The file already exists in this directory {new_folder_directory}/{new_name}")
    else:
        shutil.copy(template_path, new_folder_directory)
        os.rename(f"{new_folder_directory}/{old_name}", f"{new_folder_directory}/{new_name}")

if __name__ == "__main__":
    main()