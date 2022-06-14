from time import sleep

from config.driver import get_chrome_driver
from config.findelement import FindElement
from config.read_ini import ReadIni


def jk_xuanke(username, password,kechenghao):
    jk = ReadIni()
    driver = get_chrome_driver()
    #  jk2 专门查找元素
    jk2 = FindElement(driver)
    try:
    #     登录
    #     jk2.get_element(node="login",key="user_login").click()
        jk2.get_element(node="login",key="user_name").send_keys(username)
        jk2.get_element(node="login",key="user_password").send_keys(password)
        jk2.get_element(node="login",key="login_button").click()
        sleep(2)
        jk2.get_element(node='xuanke',key='xuankezhongxin').click()
        sleep(3)
        jk2.get_element(node='xuanke',key='jiagepaixu').click()
        sleep(3)
        kecheng_xpath = "//*[@id='__layout']/div/div[2]/div/div[2]/div[2]/div[" + str(kechenghao) + "]/div[3]/button"
     # 选择的课程xpath
        driver.find_element_by_xpath(kecheng_xpath).click()
        sleep(2)
     # 点击开始学习()
        jk2.get_element(node='xuanke',key='kaishixuexi').click()
        sleep(2)
    #    点击开始学习
        jk2.get_element(node='xuanke',key='kaishixuexi').click()
        # 验证是否有评价信息
        sleep(2)
        result  = jk2.get_element(node='jwxuanke',key='yanzheng')
        sleep(2)
        print("找回是否有评价的结果是",result)
        if result ==None:
            return False
        else:
            return True
    except Exception as e:
        print('jk',e)
        print("流程异常，认为选课失败")
        return False
    finally:
        driver.quit()


if __name__=="__main__":

    jk_xuanke("19999999999","a123456",3)