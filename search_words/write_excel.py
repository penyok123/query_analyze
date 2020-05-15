# import xlwt
#
#
# class WritrExcel():
#
#     def set_style(self, name, height, bold=False):
#         style = xlwt.XFStyle()  # 初始化样式
#         font = xlwt.Font()  # 为样式创建字体
#         font.name = name
#         font.bold = bold
#         font.color_index = 4
#         font.height = height
#         style.font = font
#         return style
#
#     # 写入Excel
#     def write_excel(self, path, rows):
#         # 创建工作簿
#         workbook = xlwt.Workbook(encoding='utf-8')
#         # 创建sheet
#         data_sheet = workbook.add_sheet('Sheet1')
#         # 将样式定义在循环之外
#         default = self.set_style('Times New Roman', 220, True)
#         j = k = 0
#         # 循环读取每一行数据并写入Excel
#         for row in rows:
#             for i in range(len(row)):
#                 try:
#                     # 写入
#                     data_sheet.write((j + k), i, row[i], default)
#                 except:
#                     print(i)
#                     raise
#                 # data_sheet.write(1, i, row1[i], self.set_style('Times New Roman', 220, True))
#             k = k + 1
#         workbook.save(path)
#         print("写入文件成功，共" + str(k) + "行数据")
#
#
# if __name__ == '__main__':
#     # 设置路径
#     rows = (
#         ('字段名称', '大致时段', 'CRNTI', 'CELL-ID'),
#         ('测试0', '15:50:33-15:52:14', '22706', '4190202'),
#         ('测试1', '15:50:33-15:52:14', '22706', '4190202'),
#         ('测试2', '15:50:33-15:52:14', '22706', '4190202')
#     )
#     path = 'demo.xls'
#     WritrExcel().write_excel(path, rows)
#     print(u'创建demo.xls文件成功')

from enum import Enum


class CONSULTATION_TABS(Enum):
    """tabs"""
    ALL = (0, '全部')
    CONTOUR_SKELETON = (1, '轮廓骨骼')
    SKIN = (2, '皮肤美容')
    SYS = (3, '眼部整形')
    NOSE = (4, '鼻部整形')
    CHEST = (5, '胸部塑身')
    SLIMMING = (6, '瘦身美体')
    INJECTION = (7, '注射美容')
    TOOTH = (8, '牙齿美容')
    HAIR = (9, '毛发管理')
    VISION = (10, '视力矫正')


ss = []

for key, value in CONSULTATION_TABS.__members__.items():
    if value.value[1] in ['视力矫正', '毛发管理']:
        ss.append(value.value[0])

print(ss)