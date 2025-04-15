import pytesseract
import cv2

# 读取图片并预处理
img = cv2.imread("C:\\Users\\qsmy\\Desktop\\123.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# 识别文字
text = pytesseract.image_to_string(thresh, config="--psm 6")  # PSM 6适合单行文本
print(text.strip())
