import pandas as pd
from class_sheet_complete import Sheet_Complete
import glob
import os
import pathlib
from class_get_data_from_template import Get_Data_From_Template

def get_filepath() -> tuple[str,str]:
    # get the filepath and return the correct format
    filepath = pathlib.Path(__file__).parent.resolve()
    grandpath = os.path.dirname(filepath)
    return str(filepath), str(grandpath)

def create_csv(letter):
    # Get a list of all excels in the folder
    filepath, grandpath = get_filepath()
    file_list = glob.glob(f"{filepath}/*.xlsx")
    numbers = []
    files = []
    complete_files = []
    for filename in file_list:
        # Trigger the is_sheet_complete script for each of the excel
        is_sheet_complete = Sheet_Complete(filename)
        template_data = Get_Data_From_Template(filename)
        if is_sheet_complete.get_answer():
            complete_files.append(filename)
            pallet_number = template_data.get_pallet_number()
            numbers.append(int(pallet_number[pallet_number.rfind(letter)+1:]))
            df = template_data.ready_template()
            files.append(df)
    frame = pd.concat(files, axis=0)
    if len(numbers) != 0 and max(numbers) != min(numbers):
        max_number = max(numbers)
        min_number = min(numbers)
        frame.to_csv(f"{grandpath}\\Upload\\{letter}{min_number}_{letter}{max_number}.csv",float_format = "%.2f")
    elif len(numbers) == 1:
        frame.to_csv(f"{grandpath}\\Upload\\{letter}{numbers[0]}.csv",float_format = "%.2f")
    #print(frame.loc[0]['OWNER'])
    # if an excel is complete, then add it to the list of the sheets that shall be converted to csv
    print(frame)
    # Remember to uncomment this -----------------------------------------------------------------------
    
    return complete_files



def remove_complete_files(file_names:list):
    for file in file_names:
        os.remove(file)


