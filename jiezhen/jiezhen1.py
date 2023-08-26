import cv2
import os

def main():
    video_path = input("请输入视频文件路径：")
    output_directory = input("请输入保存解帧图片的目录路径：")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    capture = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        ret, frame = capture.read()
        if not ret:
            break
        
        frame_filename = os.path.join(output_directory, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        
        frame_count += 1

    capture.release()
    print(f"解帧完成，共保存 {frame_count} 帧图片。")

if __name__ == "__main__":
    main()
