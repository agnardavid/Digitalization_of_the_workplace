import pandas as pd
import os
import pathlib
import datetime
from docxtpl import DocxTemplate


EXCEL_NAME = "Frysting excel test"
CSV_NAME = "Frysting csv test"

TOTAL = "TOTAL"
ROW = "ROW"
EXCEL_EXT = ".xlsx"
CSV_EXT = ".csv"

def word():
    pass

def main():

    # Excel creation
    
        # Handled with the 'Create excel.py' script, to be executed manually

    # Dictionary creation
    convert_excel_to_csv(EXCEL_NAME, CSV_NAME)
    csv_filestream = open_file(CSV_NAME, CSV_EXT)
    data_dict = process_csv(csv_filestream)
    remove_csv_file()

    # Word creation
    print_data(data_dict) # (Not done yet, just displays the data in the terminal)
    script_filepath = get_filepath()

def get_filepath():
    filepath = pathlib.Path(__file__).parent.resolve()
    return str(filepath).replace('\\', '/')

def get_current_date():
    return datetime.date.today()


def create_word_file():
    pass

def remove_csv_file():
    path = get_filepath()
    
    os.remove(f"{path}/{CSV_NAME}{CSV_EXT}")

def print_data(a_dict:dict) -> None:
    rows = " "
    box1 = "BOX 1"
    box2 = "BOX 2"
    box3 = "BOX 3"
    row_sum = "ROW SUM"

    print(f"{rows:<8} {box1:<6} {box2:<6} {box3:<6} {row_sum:>8}")
    for key, value in sorted(a_dict.items()):
        new_key = f"{key}:"
        if key == TOTAL:
            print(f"{new_key:<8}{value[0]:>30}")
        else:
            print(f"{new_key:<8} {value[0]:<6} {value[1]:<6} {value[2]:<6} {value[3]:>8}")    

def convert_excel_to_csv(excel_filename:str, csv_filename:str) -> None:
    '''Creates a csv file from excel'''

    read_file = pd.read_excel (f"{excel_filename}{EXCEL_EXT}")
    read_file.to_csv (f"{csv_filename}{CSV_EXT}", 
                  index = None,
                  header=True)

def open_file(name, extension):
    with open(f"{name}{extension}") as filestream:
        return filestream.readlines()

def process_csv(filestream) -> dict:
    new_dict = dict()
    counter = 0
    line_counter = 0
    for line in filestream:
        new_line = line.strip()
        if line_counter == 0:
            line_counter += 1
        else:    
            line_list = new_line.split(",")
            for char in line_list:
                if char == "":
                    del line_list[line_list.index(char)]
                elif ROW in char:

                    counter += 1
                    new_dict[f"{counter}.ROW"] = []
                elif line_list[0] in new_dict.keys():
                    new_dict[f"{counter}.ROW"].append(f"{float(char):.2f}")
                elif TOTAL in line_list:
                    new_dict[f"{TOTAL}"] = []
                
                if TOTAL in new_dict.keys():
                    new_dict[f"{TOTAL}"].append(f"{float(char):.2f}")

    return new_dict

if __name__ == "__main__":
    main()