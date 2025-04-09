import pychrome

browser = pychrome.Browser(url="http://localhost:9222")

# 获取所有打开的标签页
all_tabs = browser.list_tab()

for tab in all_tabs:
    print(tab.Page)
