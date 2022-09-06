import camelot

pdf_file = "/Users/why/Downloads/why/如祺出行应聘申请表(数据产品经理-吴辉扬).pdf"
# 以stream的模式读取当前目录的foo.pdf文件。
data_tb = camelot.read_pdf(pdf_file)
print(data_tb)
export_file = "/Users/why/Downloads/why/20220407135600.csv"
# 将所有表格数据导出为 foo.csv 文件
data_tb.export(export_file, f='csv', compress=True)
print(data_tb[0])
print(data_tb[0].parsing_report)
data_tb[0].to_csv(export_file)
print(data_tb[0].df)
