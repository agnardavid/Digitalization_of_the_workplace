import pyodbc
import pathlib
import csv

''' 
    -------------------- INSTRUCTIONS! -------------------------------------

    - Get the filepath using path = get_filepath()
    - Connect to excel file using connect_to_excel_file(path/filename and extension)
    - Print the results using print_results
    - Make a sql query and use execute_sql_query(sql_query:string) to make the magic happen
    
    - ALWAYS CLOSE THE CONNECTION WHEN IT IS DONE using close_connection()
'''
## Still need to find a way to name the csv files
## edit the csv files
## do the csv files include the headers?

class Excel_To_SQL:

    def __init__(self) -> None:
        pass
    
    def connect_to_excel_file(self, path):
        '''needs a filepath of the excel to function, don't forget the extension'''
        # Connect to the Excel file
        self.conn = pyodbc.connect(f'Driver={{Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)}};DBQ={path}')
        self.cursor = self.conn.cursor()
        return self.cursor
    
    def get_filepath(self):
        filepath = pathlib.Path(__file__).parent.resolve()
        return str(filepath).replace('\\', '/')

    def execute_sql_query(self, sql_query:str):

        # Execute a SQL query
        self.cursor.execute(sql_query)
    
    def print_results(self):

        # Print the results
        print(self.cursor.fetchall())

    def results_to_csv(self):

        # Write the results to a CSV file
        with open('results.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(self.cursor.fetchall())
    
    def close_connection(self):
        # Close the connection
        self.conn.close()
    