import pathlib
from is_sheet_complete import Is_Sheet_Complete
from convert_data import Data_Conversion

def main():
    filepath = get_filepath()
    filename = "2-3kg"
    test_data = Is_Sheet_Complete(filepath, filename)
    print(test_data.converter.csv_file)



def get_filepath():
    # get the filepath and return the correct format
    filepath = pathlib.Path(__file__).parent.resolve()
    return str(filepath).replace('\\', '/')

def get_filename():
    pass


if __name__ == "__main__":
    main()