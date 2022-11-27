import pathlib
import datetime
import os
import shutil


def main():

    #Excel creation
    current_date = get_current_date()
    filepath = get_parent_filepath()
    new_folder_directory = create_folder_by_date(current_date, filepath)
    counter, text_dict = get_counter_from_csv(current_date)
    remove_and_add_text_file(text_dict, filepath)
    create_excel_copy("Frysting excel test.xlsx", new_folder_directory, f"{current_date}_V_{counter}.xlsx")

def get_parent_filepath():
    filepath = pathlib.Path(__file__).parent.resolve()
    backslash = "\\"
    return_this = ""
    for char in str(filepath):
        if char == backslash:
            return_this += "/"
        else:
            return_this += char
    return return_this

def get_current_date():
    '''returns the format month(abbreviation)-day(number)-year'''
    return datetime.date.today().strftime("%b-%d-%Y") 

def remove_and_add_text_file(a_dict, path):
    '''Doesn't work at the moment, going to keep it here for the moment'''
    os.remove(f"{path}/counter.csv")
    f= open("counter.csv","w+")
    for key, values in a_dict.items():
        f.write(f"{key},{values}\n")
    
    f.close()

def get_counter_from_csv(date):
    
    a_dict = dict()
    is_more_than_zero = False
    filestream = open_file("counter", ".csv")
    
    for line in filestream:
        stripped_line = line.strip()
        line_list = stripped_line.split(",")
        
        if len(line_list) > 0 and line_list[0] == date:
            current_version = int(line_list[1])
            a_dict[date] = current_version + 1
            is_more_than_zero = True
          
        if len(line_list) > 0 and line_list[0] != date:
            a_dict[line_list[0]] = int(line_list[1])
            
    if is_more_than_zero:
        return current_version + 1, a_dict
    else:
        a_dict[date] = 1
        
        return 1, a_dict

def open_file(name, extension):
    with open(f"{name}{extension}") as filestream:
        return filestream.readlines()

def create_folder_by_date(today, filepath) -> str:
    path = os.path.join(filepath, today)
    try:
        os.mkdir(path)
    except FileExistsError:
        pass
    return path

def create_excel_copy(old_name, new_folder_directory, new_name):
    
    if os.path.isfile(f"{new_folder_directory}/{new_name}"):
        print(f"The file already exists in this directory {new_folder_directory}/{new_name}")
    else:
        shutil.copy(old_name, new_folder_directory)
        os.rename(f"{new_folder_directory}/{old_name}", f"{new_folder_directory}/{new_name}")

if __name__ == "__main__":
    main()