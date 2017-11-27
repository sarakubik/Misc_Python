# Youtube tutorial https://www.youtube.com/watch?v=-0NwrcZOKhQ
# Github files https://github.com/codebasics/py/blob/master/pandas/4_read_write_to_excel
# I had to install xlrd because I was getting errors from just
#having pandas installed
# so I did a 'pip install xlrd' (Thanks Stack Overflow!)

#to get help, Google pandas read_csv

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

#a function to replace na with my name in the column called people

def convert_people_column(cell):
    if cell == 'n.a.':
        return 'Sara Kubik'
    return cell

#a function to replace na with none in the eps price

def convert_eps_column(cell):
    if cell == 'not available':
        return 'none'
    return cell
        
    

# to read and write to an excel file


df = pd.read_excel('sample_data.xlsx', sheet_name='Sheet1', converters = {
    'people': convert_people_column,
    'eps': convert_eps_column
    })
print(df)



# to write back to an excel file
# for help https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_excel.html

df.to_excel('new.xlsx', sheet_name='stocks', index=False)
