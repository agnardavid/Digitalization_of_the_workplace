
import pathlib
import csv
import pandas as pd
import sqlalchemy

## Still need to find a way to name the csv files
## edit the csv files
## do the csv files include the headers?

class Excel_Data_Conversion:
    ''' 
    -------------------- INSTRUCTIONS! -------------------------------------

    - Get the filepath using path = get_filepath()
    - 
    - 
    - Make a sql query and use execute_sql_query(sql_query:string) to make the magic happen
    
    - 
    '''
    def __init__(self, path_to_folder:str, filename:str, extension:str="xlsx", sheet_name:str='Sheet1') -> None:
        self.filepath = f"{path_to_folder}/{filename}.{extension}"
        self.dataframe = pd.read_excel(self.filepath, sheet_name)
        self.csv_file = self.dataframe.to_csv(self.filepath, float_format='%.2f', index=False)


## these are not entirely done
    def execute_sql_query(self, sql_query:str, engine):
        '''returns a dataframe with the query executed'''
        return pd.read_sql_query(sql_query, engine)
        # Execute a SQL query

    def connect_to_sql_database(self, user:str, password:str, server_name:str, database_name:str):
        '''Creates a connection and returns an engine, 
            accessed with self.engine which is used to convert dataframe to sql table'''
        # Create a connection string
        conn_str = f'mysql+pymysql://{user}:{password}@{server_name}/{database_name}'
        

        # Connect to the database
        self.engine = sqlalchemy.create_engine(conn_str)

    def dataframe_to_sql_table(self, table_name:str):
        # Write the dataframe to a table
        self.dataframe.to_sql(table_name, self.engine, index=False)

class CSV_Data_Conversion:

    def __init__(self, csv_path:str) -> None:
        self.csv_name = csv_path
        self.df = pd.read_csv(csv_path)

    def update_csv(self, front_row_value, column_value, new_value):
        # updating the column value/data
        self.df.loc[front_row_value, column_value] = new_value

        # writing into the file
        self.df.to_csv(self.csv_name, index=False)
