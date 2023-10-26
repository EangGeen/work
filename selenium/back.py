from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
import webdriver_manager.microsoft
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import re
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import os
import schedule
# 配置日志记录器
logging.basicConfig(filename='E:\\log\\py_cf_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# 自动下载并设置webdriver路径
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
# 窗口最大化
driver.maximize_window()
# 打开一个网页
driver.get('https://cf.qq.com/cp/a20230904rlr/lr/')

#以下是官方页面的页面结构：---------------------------------------------
# 定位搜索按钮并点击
# search_button = driver.find_element(By.ID, 'dologin')
# search_button.click()

# 切换到iframe,QQ登陆框是一个iframe
# iframe = driver.find_element(By.ID, 'loginIframe')
# driver.switch_to.frame(iframe)
#------------------------------------------------------------------
# 登录
iframe = driver.find_element(By.CLASS_NAME, "qqLoginFrame")
driver.switch_to.frame(iframe)


# 定位图片元素
image_element = driver.find_element(By.XPATH, "//*[@id='img_2050087820']")

# 使用 ActionChains 模拟鼠标操作
actions = ActionChains(driver)
actions.move_to_element(image_element).click().perform()

# 切回主页面
driver.switch_to.default_content()

# 定位包含特定文本的元素
element = driver.find_element(By.XPATH, "//*[text()='需60团队召集币']")

# 滚动到指定位置
element = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div[1]/div[6]/ul/li[2]/a")
actions = ActionChains(driver)
actions.move_to_element(element).perform()

# 设置等待时间
wait = WebDriverWait(driver, 10)

# 使用循环等待元素并尝试点击
while True:
    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div[1]/div[6]/ul/li[2]/a")))
        button_text = element.text  # 获取按钮文本内容
        element.click()
        break  # 如果成功点击，退出循环
    except:
        pass
        # print("开始第二轮查找")

# 多方法命中----------------------------------------------------------
max_attempts = 10  # 设置最大尝试次数
attempt = 0
while attempt < max_attempts:
    # 获取当前时间
    current_time = datetime.now()

    # 格式化时间戳为'%Y-%m-%d %H:%M:%S'
    timestamp_formatted = current_time.strftime('%Y-%m-%d %H:%M:%S')

    # 检查元素是否变得可见
    modal = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "amsdialog_modal")))

    # 获取模态框文本内容
    modal_text = modal.text

    # 使用正则表达式过滤文本内容
    filtered_text = re.sub(r'(×|系统消息|确认)', '', modal_text)
    filtered_text = filtered_text.replace('\n', ' ')

    # 打印模态框文本内容
    # print(timestamp_formatted+filtered_text)
    logging.info(filtered_text)
    try:
        # 使用CSS选择器定位确认按钮并点击
        confirm_button = driver.find_element(By.CSS_SELECTOR, ".amsdialog_modal .amsdialog_bconfirm")
        confirm_button.click()

        # print("使用CSS选择器找到并点击确认按钮")
        break

    except NoSuchElementException:
        print("使用CSS选择器未找到确认按钮")

    try:
        # 使用XPath定位确认按钮并点击
        confirm_button = driver.find_element(By.XPATH, "//div[@class='amsdialog_modal']//a[contains(@class, 'amsdialog_bconfirm')]")
        confirm_button.click()
        print("使用XPath找到并点击确认按钮")
        break

    except NoSuchElementException:
        print("使用XPath未找到确认按钮")

    try:
        # 使用class属性定位确认按钮并点击
        confirm_button = driver.find_element(By.CLASS_NAME, "amsdialog_bconfirm")
        confirm_button.click()
        print("使用class属性找到并点击确认按钮")
        break

    except NoSuchElementException:
        print("使用class属性未找到确认按钮")

    try:
        # 使用ID属性定位确认按钮并点击
        confirm_button = driver.find_element(By.ID, "amsopenFrame_1698205278968")
        confirm_button.click()
        print("使用ID属性找到并点击确认按钮")
        break

    except NoSuchElementException:
        print("使用ID属性未找到确认按钮")

    # 如果未找到确认按钮，等待一段时间后再次尝试
    time.sleep(1)  # 等待1秒
    attempt += 1

# 多方法命中结束-------------------------------------------------------

# while True:
#     pass
# 关闭浏览器
driver.quit()