# 安装PyMuPDF
# pip install PyMuPDF

# 导入库
import fitz

import os

# 查看PyMuPDF版本
def getVersion():
    return fitz.__doc__

# 方法调用
print(getVersion())

# 获取当前执行所在目录
print(os.getcwd())

# 获取代码文件所有目录
pyfile_path = os.path.dirname(__file__)
print(pyfile_path)

pdffile_path = os.path.join(pyfile_path, 'test.pdf')
print(pdffile_path)

# 打开PDF文件
doc = fitz.open(pdffile_path)
print(doc)

# 获得PDF文件页数
doc_page_count = doc.page_count
print(doc_page_count)

# 获取PDF文件元数据
doc_metadata = doc.metadata
print(doc_metadata)

# 获取PDF目标大纲
doc_toc = doc.get_toc()
print(doc_toc)

# 读取PDF某一页面
doc_page = doc.load_page(14)
print(doc_page)

# 循环读取页面
for page in doc:
    print(page)

    # 获取PDF页面的链接，返回字典列表
    # 方式一
    links = page.get_links()
    print(links)

    # 方式二
    for link in page.links():
        print(link)

    # 获取PDF页面的注释
    for annot in page.annots():
        print(annot)

    # 获取PDF页面的表单字段
    for field in page.widgets():
        print(field)

# 获取PDF页面的文本：默认）带换行符的纯文本。无格式、无文字位置详细信息、无图像
text = doc_page.get_text('text')
print(text)

# 提取内容：生成文本块（段落）的列表
blocks = doc_page.get_text('blocks')
print(blocks)

# 提取内容：生成单词列表（不包含空格的字符串）
words = doc_page.get_text('words')
print(words)

# 提取内容：创建页面的完整视觉版本，包括任何图像。这可以通过internet浏览器显示
html = doc_page.get_text('html')
print(html)

# "dict"/"json"：与HTML相同的信息级别，但作为Python字典或resp.JSON字符串。
dict = doc_page.get_text('dict')
print(dict)

json = doc_page.get_text('json')
print(json)

# "rawdict"/"rawjson"："dict"/"json"的超级集合。它还提供诸如XML之类的字符详细信息。
rawdict = doc_page.get_text('rawdict')
print(rawdict)

rawjson = doc_page.get_text('rawjson')
print(rawjson)

# "xhtml"：文本信息级别与文本版本相同，但包含图像。
xhtml = doc_page.get_text('xhtml')
print(xhtml)

# "xml"：不包含图像，但包含每个文本字符的完整位置和字体信息。使用XML模块进行解释。
xml = doc_page.get_text('xml')
print(xml)

# 搜索文本，返回确切位置，提供矩形列表
search = doc_page.search_for('thought')
print(search)

# 复制页面
doc.copy_page()
doc.fullcopy_page()
doc.move_page()
# 插入页面
doc.insert_page()
doc.new_page()
# 删除页面
# doc.delete_page(1)
# doc.delete_pages()

# 连接2个PDF文件
doc1.insert_pdf(doc2)

# doc1后面连接doc2的前10页
doc1.insert_pdf(doc2, to_page=9)

# doc1后面连接doc2的后10页
doc1.insert_pdf(doc2, from_page=len(doc2)-10)

# doc保存
new_pdffile = ''
doc.save(new_pdffile)

# doc关闭
doc.close()