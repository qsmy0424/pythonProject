import openpyxl
from openpyxl.styles import Alignment

df = openpyxl.load_workbook(r'/Users/wwhm/Downloads/work/123.xlsx')
dataSheet = df['桥东 ']
alignment_center = Alignment(horizontal='center', vertical='center')
for row in dataSheet.iter_rows(2, 136, 1, 10):
    newSheet = df.copy_worksheet(df['日志'])
    newSheet['B4'].value = row[3].value
    newSheet['B4'].alignment = alignment_center
    newSheet['D4'].value = row[4].value
    newSheet['D4'].alignment = alignment_center
    newSheet['F4'].value = row[8].value
    newSheet['F4'].alignment = alignment_center
    newSheet[5][1].value = newSheet[5][1].value + row[2].value
    newSheet[5][1].alignment = alignment_center
    newSheet[6][1].value = row[5].value
    newSheet[6][1].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    newSheet.title = row[3].value

df.save('result.xlsx')
