import subprocess
import os
import shutil

def extract_and_copy(source_folder, output_name):
    output_folder = f"{output_name}"
    command = f".\\repkg extract -o .\\{output_folder} C:\\Users\\Acer\\Desktop\\repkg"

    has_video_files = any(file.lower().endswith(('.mp4', '.flv')) for file in os.listdir(source_folder))

    if has_video_files:
        os.rename(source_folder, f"{source_folder}(Video)")
        print(f"路径 {source_folder} 中存在视频文件，重命名为 {source_folder}(Video)")
    else:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)

        if result.returncode == 0:
            print(f"路径 {source_folder} 的命令执行成功")
            source_dir = os.path.join(os.getcwd(), output_folder)
            destination_dir = os.path.join(os.getcwd(), "output_img")

            os.makedirs(destination_dir, exist_ok=True)

            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                        source_file_path = os.path.join(root, file)
                        shutil.copy(source_file_path, destination_dir)
            print("图片文件已复制到output_img文件夹下")
        else:
            print(f"路径 {source_folder} 的命令执行失败")
            print(result.stderr)

directories = [entry.name for entry in os.scandir('.') if entry.is_dir() and entry.name.isdigit()]

for i, directory in enumerate(directories):
    print(f"处理第 {i + 1} 个目录：{directory}")
    extract_and_copy(directory, f"{directory}_output")
