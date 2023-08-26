import cv2
import os

def batch_extract_frames(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    video_extensions = ['.mp4', '.avi', '.mov']
    
    for filename in os.listdir(input_directory):
        if any(filename.lower().endswith(ext) for ext in video_extensions):
            video_path = os.path.join(input_directory, filename)
            capture = cv2.VideoCapture(video_path)
            
            frame_count = 0
            while True:
                ret, frame = capture.read()
                if not ret:
                    break
                
                frame_filename = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_{frame_count:04d}.jpg")
                cv2.imwrite(frame_filename, frame)
                
                frame_count += 1

            capture.release()
            print(f"视频 {filename} 解帧完成，共保存 {frame_count} 帧图片。")

if __name__ == "__main__":
    input_dir = input("请输入包含视频文件的文件夹路径：")
    output_dir = input("请输入保存解帧图片的文件夹路径：")
    
    batch_extract_frames(input_dir, output_dir)
