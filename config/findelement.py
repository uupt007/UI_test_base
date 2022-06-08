import os
from time import sleep
from config.driver import  get_chrome_driver
from config.read_ini import ReadIni

class FindElement():
    def __init__(self,driver):
        self.driver = driver
    # 获取元素
    def get_element(self,file=None,node = None,key=None):
        if file == None:
            file = os.path.dirname(os.path.dirname(__file__)) +"/business/LocalElement.ini"
        if node ==None:
            node = "login"
        read_ini = ReadIni(file,node)
        data = read_ini.get_value(key)
        # 得出定位方式，文件中是以 > 方式切割
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by =='id':
                return self.driver.find_element_by_id(value)
            elif by =='name':
                return self.driver.find_element_by_name(value)
            elif by =='className':
                return self.driver.find_element_by_class_name(value)
            elif by =='link_text':
                return self.driver.find_element_by_link_text(value)
            elif by =='xpath':
                return self.driver.find_element_by_xpath(value)
            elif by == 'tagName':
                return  self.driver.fnd_element_by_tagName(value)
        except:
            return None
    def to_bottom(self):
        self.driver.set_window_size(600,600)
        sleep(2)
        jk01 = "window.scrollTo(0,600);"
        self.driver.execute_script(jk01)
if __name__ == '__main__':
    parent_path = os.path.dirname(os.path.dirname(__file__))
    driver = get_chrome_driver()
    aa = FindElement
    print(aa.get_element(parent_path +"/business/LocalElement.ini","login","user_login"))



