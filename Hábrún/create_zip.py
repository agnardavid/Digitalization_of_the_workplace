from class_zip_upload_donwload_delete import Upload_Files
from pathlib import Path

class Zip_File_Creation:

    def __init__(self) -> None:   
        filepath = Path(__file__).parent.resolve()
        zip = Upload_Files(filepath)
        grandpath = zip.get_grandpath()
        filenames = zip.get_filelist_in_upload_folder()
        zip.zip_files(filenames, f"{grandpath}\\Upload\\archive_frysting.zip")
        zip.remove_files(filenames)

