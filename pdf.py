from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from pdfminer.converter import TextConverter
from openpyxl import Workbook
import io

def pdf_to_text(pdf_file_path):
    resource_manager = PDFResourceManager()
    result = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(resource_manager, result, laparams=laparams)
    fp = open(pdf_file_path, 'rb')
    interpreter = PDFPageInterpreter(resource_manager, device)
    password = ""
    maxpages = 0
    caching = True
    page_numbers = set()

    for page in PDFPage.get_pages(fp, page_numbers, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = result.getvalue()
    fp.close()
    device.close()
    result.close()

    return text

def text_to_excel(text_data, sheet_name, output_file_path):
    lines = text_data.split('\n')
    wb = Workbook()
    ws = wb.active
    ws.title = sheet_name

    for idx, line in enumerate(lines):
        line_tuple = (line,)
        ws.append(line_tuple)

    wb.save(output_file_path)

if __name__ == '__main__':
    pdf_file_path = '/Users/wwhm/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/1020439b0e527a7a333d52537db9196e/Message/MessageTemp/43a2b7680f2cbe9925b6434d48a9cc98/File/六合-南京双线特大桥 宁淮施桥-11-2-副本_140.pdf'
    output_file_path = 'example.xlsx'
    sheet_name = 'Sheet1'
    text_data = pdf_to_text(pdf_file_path)
    text_to_excel(text_data, sheet_name, output_file_path)