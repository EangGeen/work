import os
import cv2
import json
import numpy as np

# 自定义目录
base_directory = "D:/PyProj/yolov8/datasets/train/"

# 处理13个目录
for batch_num in range(1, 14):
    # 拼接目录路径
    image_batch_directory = os.path.join(base_directory, "images", f"batch_{batch_num}")
    label_batch_directory = os.path.join(base_directory, "labels", f"batch_{batch_num}")

    # 读取标注文件
    label_files = os.listdir(label_batch_directory)

    # 处理每个图像
    for label_file_name in label_files:
        # 构造标注文件的完整路径
        label_file = os.path.join(label_batch_directory, label_file_name)

        # 构造图像文件的完整路径，将.txt替换为.jpg
        image_file = os.path.join(image_batch_directory, label_file_name.replace(".txt", ".jpg"))

        # 检查图像文件是否存在
        if os.path.exists(image_file):
            image = cv2.imread(image_file)

            # 读取标注文件并逐行解析
            with open(label_file, "r") as txt_file:
                lines = txt_file.readlines()

            # 处理每行标注数据
            for line in lines:
                try:
                    segmentation = json.loads(line.strip())
                except json.JSONDecodeError as e:
                    print(f"JSONDecodeError: {e}")
                    continue

                # 处理每个分割区域
                for points in segmentation:
                    points = np.array(points).reshape((-1, 2))
                    points = points.astype(int)
                    cv2.polylines(image, [points], isClosed=True, color=(0, 255, 0), thickness=2)

            # 保存带有分割区域的图像
            output_image_file = os.path.join(image_batch_directory, "annotated_" + os.path.basename(image_file))
            cv2.imwrite(output_image_file, image)

print("标注完成。")
