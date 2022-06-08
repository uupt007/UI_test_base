import csv
from _csv import reader


def get_csv_data(csv_file,line):
    jk_csv_file =open(csv_file,'r',encoding='utf-8')
    reader = csv.reader(jk_csv_file)
    #  参数2 ：决定了下表位置开始计数方式
    for index, row in enumerate(reader,1):
        if index ==line:
            print(row)
            return row
if __name__ == '__main__':
    get_csv_data("./xuanke.csv",1)
    get_csv_data("./xuanke.csv",2)
    get_csv_data("./xuanke.csv",3)
