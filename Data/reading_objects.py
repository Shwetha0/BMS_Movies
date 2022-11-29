import xlrd
from Library.config import Config

def read_locators():
    workbook= xlrd.open_workbook(Config.Data_Path)
    worksheet = workbook.sheet_by_name("Moviespage")
    rows = worksheet.nrows
    # print(rows) #will print no of rows
    d={}
    for i in range(1,rows): #to start from row[1]
        row= worksheet.row_values(i) #to get the values of the row
        # print(row)
        d[row[0]] = (row[1],row[2])
    return d
print(read_locators())



