import pandas as pd

class Get_Data_From_Template():

    def __init__(self, template_name) -> None:
        '''Template name is the complete path to the template with extension, the template must be an excel file
            '''
        self.template_name = template_name
        self.df = pd.read_excel(template_name)

    def get_total_weight(self):
        '''Returns the total weight'''
        return round(self.df.loc[0]['TOTAL'],2)

    def get_rowsum(self, row:int):
        return round(self.df.loc[row-1]["ROWSUM"],2)

    def get_box_weight(self, row:int, box_number:int):
        return round(self.df.loc[row-1][box_number+7],2)

    def get_owner_name(self):
        '''Returns the name of the owner'''
        return self.df.loc[0]['OWNER']
    
    def get_end_result(self):
        '''Returns a capitalized N or Y
            N means the excel is not complete and therefore not ready to be processed
            -------------------------------------------------------------------------
            Y means the excel is complete and is therefore ready to be processed'''
        return self.df.loc[0]['END (Y/N)'].upper()

    def get_pallet_number(self):
        '''Returns the current pallet number'''
        return self.df.loc[0]['PALLET NUMBER']

    def set_new_owner_name(self, new_owner_name):
        '''Sets a new owner name'''
        self.df.loc[0,'OWNER'] = new_owner_name

    def set_pallet_number(self, new_pallet_number:str):
        '''Sets a new pallet number'''
        self.df.loc[0,'PALLET NUMBER'] = new_pallet_number
    