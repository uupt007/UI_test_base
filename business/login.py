from time import sleep

from config.driver import get_chrome_driver
from config.findelement import FindElement
from config.read_ini import ReadIni


def jk_login(username, password,kechenghao):
    jk = ReadIni()
    driver = get_chrome_driver()
    #  jk2 专门查找元素
    jk2 = FindElement(driver)
    try:
    #     登录
        jk2.get_element(node="login",key="user_login").click()
        jk2.get_element(node="login",key="user_name").send_keys(username)
        jk2.get_element(node="login",key="user_password").send_keys(password)
        jk2.get_element(node="login",key="login_button").click()
        sleep(2)
        jk2.get_element(node='xuanke',key='xuankezhongxin').click()
        sleep(3)
        jk2.get_element(node='xuanke',key='jiagepaixu').click()
        sleep(3)
    except Exception as e:
        print('jk', e)
        print("流程异常，认为选课失败")
        return False
    finally:
        driver.quit()
if __name__ == '__main__':
    jk_login("18143994089","test123",1)




