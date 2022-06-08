# 思路
# 1. 获取capabilities信息
# 2. 启动app(包含安装过程)
# 3. 点击“取消”按钮
# 4.点击”跳过“按钮
# 5. 输入用户名和密码
# 6. 点击“登录按钮”
# 7. 验证是否登录成功

from time import sleep

from config.common import appium_desired


def login_test(username1,password1):
    #  1.获取capabiliies信息
    # 2. 启动app（包含安装过程）
    driver = appium_desired()

    #  3. 点击“取消按钮”
    sleep(3)
    cancel_btn = driver.find_element_by_id("android:id/button2")
    cancel_btn.click()
    # 4. 点击“跳过”按钮
    sleep(3)
    skip_btn = driver.find_element_by_id("com.tal.kaoyan:id/tv_skip")
    skip_btn.click()
    sleep(3)

    #  5. 输入用户名和密码
    username = driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext')
    username.send_keys(username1)
    password = driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext')
    password.send_keys(password1)
    sleep(3)
    # 6. 点击“登录”按钮
    login_btn = driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn')
    login_btn.click()

    # 7.验证是否登录成功
    # 帐号下线提示
    try:
        element1 = driver.find_element_by_id("com.tal.kaoyan:id/tip_commit")
    except:
        print("没有账号下线提示")
    else:
        element1.click()

    # 增加新的广告处理
    try:
        element3 = driver.find_element_by_id("com.tal.kaoyan:id/view_wemedia_cacel")
    except:
        print("没有弹出广告提示２")
    else:
        element3.click()

    # 检测是否有我知道了按钮
    try:
        element2 = driver.find_element_by_id("com.tal.kaoyan:id/task_no_task")
    except:
        print("没有弹出广告提示")
    else:
        element2.click()

    # 根据界面是否有‘我’判断登录是否成功
    try:
        # 寻找下方 4个tab中的‘我’
        driver.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl")
    except:
        print("登录失败")
        return False
    else:
        print("登录成功")
        return True


# 自测
if __name__ == '__main__':
    login_test(18143994089,1234567890)



