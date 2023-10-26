cuda、cudnn、驱动

0.CUDA、cuDNN或GPU驱动存在冲突或未正确安装，即使在Conda环境中安装了PyTorch和TorchVision，模型也无法正常在GPU上运行，所以只要之前的环境可以跑gpu，那么说明至少CUDA、cuDNN或GPU驱动（nvidia-smi、dxdiag）是没有问题的。【cuda、cudnn、驱动】和conda虚拟环境的不匹配也有可能能用

1.如何查看代码（模型）是否支持gpu，也就是是否安装成功？

```python
import torch
import os
print(torch.cuda.is_available())
print(os.environ.get('CUDA_VISIBLE_DEVICES'))
print(torch.cuda.device_count())
print(torch.__version__)
print(torch.zeros(1).cuda())
```

```
显示如下就是正常：
True
None
1
2.0.1+cu118
tensor([0.], device='cuda:0')
```

2.如果是cpu版本怎么办？

2.1不要从pytorch安装，conda和pip都不行，也不要使用清华源，不要后面加-C，从https://download.pytorch.org/whl/cu118里面搜cuda配套的torch和torchvision版本，查看配套的版本：pip debug，比如cp310-cp310-win_amd64 ，然后使用cmd，pip install 包名，安装。

2.2删除torch和torchvision:虚拟环境中安装的，找到该虚拟环境的lib->site-packages（envs表示根目录，里面有你所有的虚拟环境），例如我的是`D:\anaconda\envs\yolov8.6\Lib\site-packages`，删除所有torch开头的文件。

2.3安装顺序：

1. NVIDIA-smi 
2. cudn (https://developer.nvidia.com/rdp/cudnn-download)
3. pytorch、torchvision、torchaudio （https://download.pytorch.org/whl/cu118）
4. cmd --> pip install 包名、配置环境变量

2.4常用命令：

1. 豆瓣源安装：pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio===0.9.0 -f https://download.pytorch.org/whl/torch_stable.html -i https://pypi.douban.com/simple

2. pip和conda安装卸载：conda install torchvision、conda uninstall torchvision、pip install torchvision、pip uninstall torchvision

3. conda源

   ```
   conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/pkgs/main/
   conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/pkgs/free/
   conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/pkgs/r
   conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/pkgs/msys2
   conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/cloud/pytorch/
   conda config --add channels https://mirrors.bfsu.edu.cn/anaconda/cloud/conda-forge
   conda config --set show_channel_urls yes
   ```

   

4. conda新建环境 conda create --name TACO python=3.10、conda activate TACO

5. 【简版指令】yolov8测试：

   ```
   yolo task=detect mode=predict model=yolov8n.pt source='D:/PyProj/yolov8/ultralytics/ultralytics/assets' show=True
   ```

   【简版指令】yolov8训练自定义数据集

   ```
   yolo task=segment mode=train data=D:/PyProj/yolov8/ultralytics/ultralytics/cfg/datasets/taco-seg.yaml model=D:/PyProj/yolov8/ultralytics/ultralytics/cfg/models/v8/yolov8-seg-taco.yaml epochs=100 batch=16 imgsz=640 device=0 name=taco-seg
   ```

   【详版指令】正确的命令格式示例：

   ```
   yolo TASK MODE ARGS
   ```

   其中：

   - `TASK` 是可选的，可以是 ('detect', 'segment', 'classify', 'pose') 中的一个。
   - `MODE` 是必需的，可以是 ('train', 'val', 'predict', 'export', 'track', 'benchmark') 中的一个。
   - `ARGS` 是可选的，用于覆盖默认设置的自定义 'arg=value' 对，比如 'imgsz=320'。

   在您的命令中，您混合了 `yolo`、`task`、`mode` 和参数，但格式不正确。您应该按照正确的格式编写命令，例如：

   ```
   yolo detect predict source='D:/PyProj/yolov8/ultralytics/ultralytics/assets/bus
   ```

   yolov5图片: 

   ```
   python detect.py --source video_path_or_url
   ```

6. "NotImplementedError:无法使用来自“CUDA”后端的参数运行“torchvision：：nms原因：版本不匹配。

yolo mode=train model=yolov8x.pt data=ultralytics/ultralytics/cfg/datasets/taco.yaml model=ultralytics/ultralytics/cfg/models/v8/yolov8taco.yaml epochs=100 batch=6 imgsz=640 device=0 name=taco

参考文献：

https://blog.csdn.net/aaatomaaa/article/details/125326107

https://blog.csdn.net/qq_36521174/article/details/123654700