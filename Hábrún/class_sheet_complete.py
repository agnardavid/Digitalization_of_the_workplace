from class_get_data_from_template import Get_Data_From_Template

class Sheet_Complete:

    def __init__(self, filepath:str) -> None:
        '''filepath is complete path to file with extensions'''
        self.dataframe = Get_Data_From_Template(filepath)

    def get_answer(self):
        is_complete = self.dataframe.get_end_result()
        if is_complete == "Y":
            return True
        else:
            return False 