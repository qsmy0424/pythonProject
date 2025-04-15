import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def get_from_chrome():
    # 设置 Chrome 选项
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")  # 连接到调试端口
    # 启用 Performance Logging
    chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

    # 创建浏览器实例（连接到现有浏览器）
    driver = webdriver.Chrome(options=chrome_options)

    # print(driver.current_url)

    all_window_handles = driver.window_handles
    # print("所有窗口句柄:", all_window_handles)

    # 切换到目标窗口
    driver.switch_to.window(all_window_handles[0])

    # 获取窗口标题和 URL
    title = driver.title
    url = driver.current_url
    print("窗口标题:", title)
    print("窗口 URL:", url)

    for i in range(1, 40):
        # 定位所有 <h4> 标签下的 <a> 标签
        a_tags = driver.find_elements(By.XPATH, "//h4//a")
        href_list = [ a_tag.get_attribute("href") for a_tag in a_tags]
        print(href_list)
        # 遍历 <a> 标签并获取 href 属性
        for href in href_list:
            if href:
                print("href:", href)
                time.sleep(round(random.uniform(40, 60), 2))
                # 在新选项卡中打开页面
                driver.execute_script(f"window.open('{href}');")
                print("已打开新页面")
                driver.switch_to.window(all_window_handles[0])
                print("已切换回第一个窗口")

        time.sleep(round(random.uniform(5, 10), 2))
        close_tab_exclude_last_tab(driver)
        driver.switch_to.window(all_window_handles[0])
        go_to_next_page(driver)

    # forward_category(driver)

    # 继续操作
    # driver.get("https://www.google.com")
    # print("新页面标题:", driver.title)

    # 关闭浏览器（可选）
    # driver.quit()

def go_to_next_page(driver):
    admin_case_button = driver.find_element(By.XPATH, "//a[contains(text(), '下一页')]")
    admin_case_button.click()
    print("已点击下一页按钮")

def close_tab_exclude_last_tab(driver):
    print("关闭除第一个窗口以外的所有窗口")
    all_window_handles = driver.window_handles
    # 关闭除第一个窗口以外的所有窗口
    for handle in all_window_handles[1:]:
        driver.switch_to.window(handle)
        driver.close()

def forward_category(driver):
    try:
        all_window_handles = driver.window_handles
        # 等待“行政案件”按钮加载完成
        admin_case_button = driver.find_element(By.XPATH, "//a[contains(text(), '行政案件')]")

        # 点击“行政案件”按钮
        admin_case_button.click()
        print("已点击行政案件按钮")
        driver.switch_to.window(all_window_handles[0])
        driver.close()
        time.sleep(round(random.uniform(4, 6), 2))

        # 等待新页面加载完成
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        # print("新页面已加载")

    except Exception as e:
        print("操作失败:", e)

if __name__ == "__main__":
    get_from_chrome()