import os
from pathlib import Path
import glob
import boto3
import zipfile

class Upload_Files():

    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.s3 = boto3.client('s3')

    def get_grandpath(self) -> str:
        # get the filepath and return the correct format
        grandpath = os.path.dirname(self.filepath)
        return str(grandpath)

    def get_filelist_in_upload_folder(self):
        grandpath = self.get_grandpath()
        return glob.glob(f"{grandpath}\\Upload\\*.csv")

    def download_files_from_bucket(self, bucket_name, file_key, filepath):
        '''Gets all uploaded files of same sort and downloads them to the computer
            'BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME' 
            '''
        # Download the file
        # file_key is the exact name of the file in the bucket
        # filepath is the designated file location and name
        self.s3.download_file(bucket_name, file_key, filepath)

    def delete_file_in_s3_bucket(self, bucket_name, file_key):
        '''file key is the exact name of the file in the s3 bucket'''
        self.s3.Object(bucket_name, file_key).delete()

    def upload_files_to_bucket(self, filename, bucket_name, file_key):
        '''Filename: The path to the file to be uploaded
            Key: The path or name of the file in the bucket once uploaded'''
        self.s3.upload_file(filename, bucket_name, file_key)

    def merge_files(self):
        pass

    def unzip_files(self, filenames:list):
        pass

    def zip_files(self, filenames:list, designated_file_location:str):
        with zipfile.ZipFile(designated_file_location, mode="w") as archive:
            for filename in filenames:
                arcname = filename.split("\\")[-1]  # Extract the file name from the full path
                archive.write(filename, arcname)
    
    def remove_files(self, file_names:list):
        for file in file_names:
            os.remove(file)



