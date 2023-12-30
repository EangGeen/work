import os
import tkinter as tk
from tkinter import filedialog
import pyperclip

button_height = 2  # 按钮高度等于输入框高度
def generate_key(version_str, a_data, b_data, c_data):
    a_key = a_data.get(version_str[:3], "")
    b_key = b_data.get(version_str[3:5], "")
    c_key = c_data.get(version_str[5:], "")

    return a_key[1:-1] + b_key[1:-1] + c_key[1:-1]


def read_file(file_path):
    result = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            key, value = line.strip().split()
            result[key] = value
    return result


def main():
    # 配置文件名
    file1 = "E:/A.txt"
    file2 = "E:/B.txt"
    file3 = "E:/C.txt"

    # 读取文件数据
    global a_data, b_data, c_data
    a_data = read_file(file1)
    b_data = read_file(file2)
    c_data = read_file(file3)

    def on_select_path():
        folder_path = filedialog.askdirectory()
        if folder_path:
            entry_path.delete(0, tk.END)
            entry_path.insert(0, folder_path)

    def on_generate_result():
        version_str = entry_version.get()
        if len(version_str) == 8:
            result = generate_key(version_str, a_data, b_data, c_data)
            entry_result.delete(0, tk.END)
            entry_result.insert(0, result)
        else:
            entry_result.delete(0, tk.END)
            entry_result.insert(0, "请输入8位版本号")

    def on_copy_result():
        result_text = entry_result.get()
        if result_text:
            pyperclip.copy(result_text)

    # 创建GUI窗口
    window = tk.Tk()
    window.title("版本解密工具")

    # 创建GUI组件
    entry_width = 20  # 输入框长度减掉三分之一
    entry_height = 2
    button_width = 12  # 按钮长度减掉五分之一

    tk.Label(window, text="根目录:").grid(row=0, column=0, pady=5, padx=5, sticky='e')
    entry_path = tk.Entry(window, width=entry_width, font=("Helvetica", 12))
    entry_path.grid(row=0, column=1, pady=5, padx=5, columnspan=2)
    entry_path.insert(0, "E:/svn/trunk")  # 设置默认值
    btn_select_path = tk.Button(window, text="选择路径", command=on_select_path, width=button_width,
                                height=button_height)
    btn_select_path.grid(row=0, column=3, pady=5, padx=5)

    tk.Label(window, text="版本号:").grid(row=1, column=0, pady=5, padx=5, sticky='e')
    entry_version = tk.Entry(window, width=entry_width, font=("Helvetica", 12))
    entry_version.grid(row=1, column=1, pady=5, padx=5, columnspan=2)

    btn_generate = tk.Button(window, text="生成结果", command=on_generate_result, width=button_width,
                             height=button_height)
    btn_generate.grid(row=1, column=3, pady=5, padx=5)

    tk.Label(window, text="解密后:").grid(row=2, column=0, pady=5, padx=5, sticky='e')
    entry_result = tk.Entry(window, width=entry_width, font=("Helvetica", 12))
    entry_result.grid(row=2, column=1, pady=5, padx=5, columnspan=2)

    btn_copy = tk.Button(window, text="复制结果", command=on_copy_result, width=button_width, height=button_height)
    btn_copy.grid(row=2, column=3, pady=5, padx=5)

    # 运行GUI窗口
    window.mainloop()


if __name__ == "__main__":
    # 运行GUI
    main()