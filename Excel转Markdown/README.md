# Excel转Markdown

**背景**：需要将以汇总的Excel表格转成MarkDown，经查资料，Top建议是将文件上传[tableconvert](https://tableconvert.com/)，在线生成，为避免文件上传导致信息安全违规，故搞了个Demo

**原理**：Python+Pands包

**步骤**：

1.pip install pandas   and   pip install openpyxl 

2.键入代码，并将Python输出结果放入MarkDown即可

```python
import pandas as pd

path='D:/test.xlsx'
def excelToMd(path, sheetName="Sheet1"):
    print(path)
    df = pd.read_excel(path, sheetName)
    title = "|"
    splitLine = "|"
    for i in df.columns.values:
        title = title + i + "|"
        splitLine = splitLine + "--" + "|"
    print(title)
    print(splitLine)
    for i in df.iterrows():
        row = "|"
        for j in df.columns.values:
            row = row + str(i[1][j]) + "|"
        print(row.replace("nan", "-"))

excelToMd("D:/test.xlsx")
```

