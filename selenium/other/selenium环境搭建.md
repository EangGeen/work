## 前言

- **webdriver_manager是什么？** 

**webdriver_manager** 是 Python 中的一个库，用于管理 Web 驱动程序。它的作用是自动下载和设置不同浏览器（如 Chrome、Firefox、Edge 等）的 Web 驱动程序，以便在自动化测试中使用这些浏览器。

在进行 Selenium 测试时，需要一个与浏览器相匹配的 Web 驱动程序，以便控制和操作浏览器。webdriver_manager 为您提供了一种简便的方式，可以自动检测所需浏览器的版本并下载相应的 Web 驱动程序。这样，您就不需要手动下载和设置 Web 驱动程序，可以减轻您的负担，提高测试的可靠性和可维护性。

## 一、导入模块

```python
pip install webdriver_manager
pip install Selenium
```

## 二、Chrome用法

```python
# Selenium4.0以下版本使用该方法
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# 使用 ChromeDriverManager 安装 ChromeDriver，并返回驱动程序的路径
driver_path = ChromeDriverManager().install()
# 打印驱动程序路径
print(driver_path)

# 创建 Chrome WebDriver，并指定驱动路径
driver = webdriver.Chrome(executable_path=driver_path)
# 打开百度网页
driver.get("https://www.baidu.com")

# Selenium4.0以上版本使用该方法
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 使用 ChromeDriverManager 安装 ChromeDriver，并返回驱动程序的路径
driver_path = ChromeDriverManager().install()
# 打印驱动程序的路径
print(driver_path)

# 创建 ChromeDriver 服务，并指定驱动程序的路径
service = Service(driver_path)
# 创建 Chrome WebDriver，并指定服务
driver = webdriver.Chrome(service=service)
# 打开百度网页
driver.get("https://www.baidu.com")

```

- **下载驱动到指定目录中**

```python
# Selenium4.0以上版本使用该方法
import os
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 指定驱动目标位置
folder_path = r'C:\Users\admin\Desktop\run'
# 路径拼接
file_path = os.path.join(folder_path, 'chromedriver.exe')

# 使用ChromeDriverManager安装ChromeDriver，并获取驱动程序的路径
download_driver_path = ChromeDriverManager().install()
# 复制文件到目标位置
shutil.copy(download_driver_path, folder_path)

# 创建Chrome WebDriver，并指定驱动路径
driver = webdriver.Chrome(service=Service(file_path))
# 打开百度网页
driver.get("https://www.baidu.com")

```

- **以下代码是判断谷歌浏览器版本和谷歌驱动版本是否一致，不一致则重新下载**

```python
# Selenium4.0以上版本使用该方法
import os
import shutil
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def determine_google_drive():
    """判断谷歌驱动版本是否和谷歌浏览器版本一致"""
    # 谷歌浏览器可执行文件的完整路径
    chrome_path = r'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'

    # 指定谷歌驱动目标位置
    folder_path = r'C:\Users\admin\Desktop\run'
    # 驱动名称
    file_name = 'chromedriver.exe'
    # 路径拼接
    file_path = os.path.join(folder_path, file_name)

    if os.path.exists(file_path):
        # 获取chromedriver.exe版本(谷歌浏览器驱动)
        result = subprocess.run([file_path, '--version'], capture_output=True, text=True)
        driverversion = '.'.join(result.stdout.strip().split(' ')[1].split('.')[:-1])

        # 获取chrome.exe版本(谷歌浏览器)
        command = f'wmic datafile where name="{chrome_path}" get Version /value'
        result_a = subprocess.run(command, capture_output=True, text=True, shell=True)
        output = result_a.stdout.strip()
        chromeversion = '.'.join(output.split('=')[1].split('.')[0:3])

        # 判断版本是否一致，不一致就重新下载
        if driverversion != chromeversion:
            # 使用ChromeDriverManager安装ChromeDriver，并获取驱动程序的路径
            download_driver_path = ChromeDriverManager().install()
            # 复制文件到目标位置
            shutil.copy(download_driver_path, folder_path)
        else:
            print("版本一致，无需重新下载！")

    else:
        download_driver_path = ChromeDriverManager().install()
        shutil.copy(download_driver_path, folder_path)

    return file_path


if __name__ == '__main__':
    # 创建Chrome WebDriver，并指定驱动路径
    driver = webdriver.Chrome(service=Service(determine_google_drive()))
    # 打开百度网页
    driver.get("https://www.baidu.com")
```

## 三、Edge用法

```python
# Selenium4.0以下版本使用该方法
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
driver.get("https://www.baidu.com")



# Selenium4.0以上版本使用该方法






from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
# 自动下载并设置webdriver路径
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

# 打开一个网页
driver.get('https://www.baidu.com')
# 设置隐式等待时间为10秒
driver.implicitly_wait(10)

# 定位搜索框并输入搜索内容
search_box = driver.find_element(By.ID, 'kw')
search_box.send_keys('Selenium')

# 定位搜索按钮并点击
search_button = driver.find_element(By.ID, 'su')
search_button.click()
while True:
    pass

# 关闭浏览器
# driver.quit()
```

## 四、Firefox用法

```python
# Selenium4.0以下版本使用该方法
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://www.baidu.com")

# Selenium4.0以上版本使用该方法
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.get("https://www.baidu.com")
```

