## Python 常用标准库模块和命令

### shutil 模块
- `shutil.copy(src, dst)`: 复制文件或目录。
- `shutil.move(src, dst)`: 移动文件或目录。
- `shutil.rmtree(path)`: 递归删除目录及其内容。
- `shutil.make_archive(base_name, format[, root_dir])`: 创建压缩文件（如zip、tar）。
- `shutil.unpack_archive(filename[, extract_dir])`: 解压缩文件。

### os 模块
- `os.getcwd()`: 获取当前工作目录。
- `os.listdir(path)`: 列出目录中的文件和子目录。
- `os.mkdir(path)`: 创建目录。
- `os.remove(path)`: 删除文件。
- `os.rename(src, dst)`: 重命名文件或目录。
- `os.path.exists(path)`: 检查文件或目录是否存在。

### sys 模块
- `sys.argv`: 获取命令行参数。
- `sys.exit([status])`: 退出程序，可选地指定退出状态码。

### datetime 模块
- `datetime.datetime.now()`: 获取当前日期和时间。
- `datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)`: 创建时间间隔。

### math 模块
- `math.sqrt(x)`: 计算平方根。
- `math.sin(x)`, `math.cos(x)`, `math.tan(x)`: 计算三角函数值。

### random 模块
- `random.randint(a, b)`: 生成[a, b]之间的随机整数。
- `random.choice(seq)`: 从序列中随机选择一个元素。

### json 模块
- `json.dumps(obj)`: 将Python对象转换为JSON字符串。
- `json.loads(s)`: 将JSON字符串解析为Python对象。

### csv 模块
- 用于读写CSV文件。

### re 模块
- 正则表达式操作，用于字符串匹配和处理。

### urllib 模块
- 用于处理URL操作，包括下载网页内容。

### subprocess 模块
- `subprocess.run(args, stdout=None, stderr=None, shell=False)`: 运行外部命令并获取其输出。

### logging 模块
- 用于记录应用程序的日志信息。

### time 模块
- `time.sleep(seconds)`: 暂停程序执行指定秒数。

### argparse 模块
- 用于解析命令行参数和选项。

### itertools 模块
- 提供了用于创建和操作迭代器的工具函数。

### collections 模块
- 提供了额外的数据结构，如命名元组、有序字典等。

### urllib.parse 模块
- 用于解析和构建URL。

### hashlib 模块
- 用于计算哈希值，如MD5、SHA1等。

### functools 模块
- 提供了一些有用的高阶函数，如 `functools.partial` 和 `functools.reduce`。

### os.path 模块
- 用于处理文件路径，包括 `os.path.join` 和 `os.path.exists` 等函数。

### sqlite3 模块
- 用于操作SQLite数据库。

### email 模块
- 用于发送和接收电子邮件。

### tkinter 模块
- 用于创建图形用户界面（GUI）应用程序。

### xml.etree.ElementTree 模块
- 用于解析和生成XML文档。

### socket 模块
- 用于网络编程，包括创建网络套接字和进行套接字通信。