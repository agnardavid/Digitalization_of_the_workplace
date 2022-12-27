from convert_data import Data_Conversion

class Is_Sheet_Complete:

    def __init__(self, folder_path:str, filename:str) -> None:
        self.filename = filename
        self.converter = Data_Conversion(folder_path, self.filename)

    def get_answer(self):
        
        
        self.converter.execute_sql_query("")
        


