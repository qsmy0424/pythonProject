import cv2
import numpy as np

def preprocess_image(image_path):
    """ 读取并预处理图像 """
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # 读取灰度图
    blurred = cv2.GaussianBlur(image, (5, 5), 0)  # 高斯模糊去噪
    _, binary = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV)  # 反色二值化
    return binary

def find_contours(binary):
    """ 查找答题区域的轮廓 """
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def extract_answers(binary, contours):
    """ 提取填涂的答案 """
    answers = {}
    for i, contour in enumerate(sorted(contours, key=lambda c: cv2.boundingRect(c)[1])):  # 按纵坐标排序
        x, y, w, h = cv2.boundingRect(contour)
        roi = binary[y:y+h, x:x+w]  # 提取答案区域
        filled_option = detect_filled_option(roi)  # 识别填涂的选项
        answers[f"Q{i+1}"] = filled_option
    return answers

def detect_filled_option(roi):
    """ 识别填涂的选项（假设A、B、C、D分别在固定位置） """
    options = ['A', 'B', 'C', 'D']
    columns = np.sum(roi, axis=0)  # 计算列的像素值
    darkest_index = np.argmin(columns)  # 找到填涂最黑的区域
    return options[darkest_index] if darkest_index < len(options) else "Unknown"

# 主程序
image_path = "C:\\Users\\qsmy\\Downloads\\123.png"  # 答题卡图片路径
binary = preprocess_image(image_path)
contours = find_contours(binary)
answers = extract_answers(binary, contours)

# 输出答案
print(answers)
