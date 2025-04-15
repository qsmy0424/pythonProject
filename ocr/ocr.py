from paddleocr import PaddleOCR
import re

# 初始化OCR
ocr = PaddleOCR(use_angle_cls=True, lang="en")  # 英文模式

# 识别图片
img_path = "C:\\Users\\qsmy\\Desktop\\123.jpg"
result = ocr.ocr(img_path, cls=True)

# 提取文本内容
print(result)
print(result[0])
