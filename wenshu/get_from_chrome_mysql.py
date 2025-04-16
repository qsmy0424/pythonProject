import random
import time
import mysql.connector
import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from urllib.parse import quote_plus

# 连接到 MySQL 数据库
db = mysql.connector.connect(
    host="192.168.4.214",  # 数据库主机
    user="root",  # 用户名
    port="13306",
    password="top123",  # 密码
    database="crawler_doc",  # 数据库名称
)

# 创建游标对象
cursor = db.cursor()


def get_from_chrome():
    # 设置 Chrome 选项
    chrome_options = Options()
    chrome_options.add_experimental_option(
        "debuggerAddress", "127.0.0.1:9222"
    )  # 连接到调试端口
    # 启用 Performance Logging
    chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

    # 创建浏览器实例（连接到现有浏览器）
    driver = webdriver.Chrome(options=chrome_options)

    # print(driver.current_url)

    all_window_handles = driver.window_handles
    # print("所有窗口句柄:", all_window_handles)

    # 切换到目标窗口
    driver.switch_to.window(all_window_handles[0])

    # 执行查询操作（例如：查询所有用户）
    cursor.execute("SELECT id, rowkey FROM t_list where status = 0")

    count = 0
    # 获取查询结果
    result = cursor.fetchall()
    for row in result:
        print(f"{time.ctime()}--{row[0]}--{row[1]}")
        driver.get(
            "https://wenshu.court.gov.cn/website/wenshu/181107ANFZ0BXSK4/index.html?docId="
            + row[1]
        )

        # time.sleep(round(random.uniform(2, 5), 2))
        # driver.get("https://wenshu.court.gov.cn/down/one?docId=" + quote_plus(row[1]))

        time.sleep(round(random.uniform(20, 40), 2))
        cursor.execute("UPDATE t_list SET status = 1 WHERE id = %s", (row[0],))
        db.commit()
        count += 1
        if count > 400:
            cursor.close()
            db.close()
            sys.exit(1)

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
        admin_case_button = driver.find_element(
            By.XPATH, "//a[contains(text(), '行政案件')]"
        )

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
