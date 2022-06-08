# 负责读取csv 文件中的内容
def get_cvs_data(csv_file):
    with open(csv_file,'r',encoding='utf-8') as f:
        lines = f.readlines()
        print(lines)
    return lines
if __name__ == '__main__':
    get_cvs_data('./login_data.csv')