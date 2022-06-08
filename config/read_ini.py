import configparser
import os
# print(os.path.dirname(os.path.dirname(__file__)))
class ReadIni():
    def __init__(self,file_name= None,node=None):
        self.file_name = file_name
        self.node = node
        if file_name == None:
            #  文件名+r 防止自动转义
            self.file_name = os.path.dirname(os.path.dirname(__file__))+ "/config/config.ini"
        if node == None:
            self.node = "config"
        self.cf = self.load_ini(self.file_name)

        #  加载配置文件
    def load_ini(self,file_name):
            # 自动解析配置对象
            cf = configparser.ConfigParser()
            cf.read(file_name,encoding='utf-8')
            return cf
        #  获取配置文件中的内容===>指定key
    def get_value(self,key):
            return self.cf.get(self.node,key)
if __name__ == '__main__':
    aa = ReadIni()
    print(aa.get_value("borwser"))    # 读取config.ini 的 browser 结点的值
    print(os.path.dirname(os.path.dirname(__file__)))