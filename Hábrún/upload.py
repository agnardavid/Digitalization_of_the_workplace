import create_csv_from_finished_sheets
from create_zip import Zip_File_Creation

def main():
    complete_files = create_csv_from_finished_sheets.create_csv("H")
    create_csv_from_finished_sheets.remove_complete_files(complete_files)
    Zip_File_Creation()


if __name__ == "__main__":
    main()