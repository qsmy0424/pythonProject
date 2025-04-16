# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
from urllib.parse import urlencode
from urllib.parse import quote
from urllib.parse import quote_plus


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f"Hi, {name}")  # 按 Ctrl+F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == "__main__":
    print_hi("PyCharm")
    str = "V3D3+2vF8WLw0MfY9jiFSdsbYcrlfNVEVOZWH+wNPuiOCAgaV8bAa5/dgBYosE2g+gTrpdyC9FJ8JZ4JS13SRTqpezGD3tElkbunpoPgLphhyom5onBG8MAr8FVlXGaY"
    print(str)
    print(
        "V3D3%2B2vF8WLw0MfY9jiFSdsbYcrlfNVEVOZWH%2BwNPuiOCAgaV8bAa5%2FdgBYosE2g%2BgTrpdyC9FJ8JZ4JS13SRTqpezGD3tElkbunpoPgLphhyom5onBG8MAr8FVlXGaY"
    )
    print(quote_plus(str))
    print(quote(str))

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
