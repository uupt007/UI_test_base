import os
import yaml
from appium import webdriver
def appium_desired():
    # 1. 获取capanilities信息
    # 2.获取yaml 文件目录
    yaml_dir = os.path.dirname(__file__)
    #  获取yaml文件的完整路径
    yaml_path = os.path.join(yaml_dir,'config.yaml')
    # 打开yaml文件，读取内容
    config_file = open(yaml_path,'r',encoding='uft-8')
    #解析 yaml文件
    data = yaml.load(config_file,Loader = yaml.FullLoader)
    desired_caps = {}
    desired_caps['platformName']= data['platformName']
    desired_caps['platformName'] = data['platformVersion']
    desired_caps['app'] = data['app']
    desired_caps['noReset']='false'
    # 启动 app
    driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
    driver.implicitly_wait(10)
    return driver


# common.py 是appium的一些初始化信息


